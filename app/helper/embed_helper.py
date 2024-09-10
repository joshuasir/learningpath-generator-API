from langchain.chains import ConversationalRetrievalChain
from langchain_core.messages import HumanMessage, AIMessage
from langchain.vectorstores import DeepLake
from langchain.chains import ConversationalRetrievalChain
from langchain_google_vertexai import VertexAIEmbeddings,VertexAI


import json
import os

dataset_path = 'hub://josuasirustara/education5'
# embedding_id = "sentence-transformers/all-MiniLM-L6-v2"
# repo_id = "HuggingFaceTB/SmolLM-135M"
# model_id = "mistral.mistral-7b-instruct-v0:2"

QA = None
#Mean Pooling - Take attention mask into account for correct averaging
# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0] #First element of model_output contains all token embeddings
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# tokenizer = AutoTokenizer.from_pretrained(embedding_id)
# model = AutoModel.from_pretrained(embedding_id)


# def embedding_function(texts):
#     if isinstance(texts, str):
#         texts = [texts]
#     encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

#     with torch.no_grad():
#         model_output = model(**encoded_input)

#     sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

#     sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
#     return sentence_embeddings


def store_and_embed(contents, chunk_size=1000):
    # Initialize DeepLake vector store
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    vector_store = DeepLake(dataset_path=dataset_path, embedding_function=embeddings)

    for s, t in contents.items():
        chunked_text = [t[i:i+chunk_size] for i in range(0, len(t), chunk_size)]
        
        # Add documents to the vector store
        vector_store.add_texts(
            texts=chunked_text,
            metadatas=[{"source": s} for _ in range(len(chunked_text))]
        )

    return {
        'message': 'success',
        'status': 200
    }

def search_db():
    global QA

    if QA is None:
        embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
        db = DeepLake(dataset_path=dataset_path, read_only=True, embedding=embeddings)
        retriever = db.as_retriever()
        retriever.search_kwargs['distance_metric'] = 'cos'
        retriever.search_kwargs['fetch_k'] = 50
        retriever.search_kwargs['k'] = 10

       
        llm = VertexAI(model_name="gemini-pro")
     
        QA = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, return_source_documents=True)
    return QA

def generate_learning_path(topic,description,pathid):
    file_path = f'job-{pathid}.json'
    requirement = {}
    if os.path.exists(f'job-{pathid}.json'):
        # Open and read the JSON file
        with open(f'job-{pathid}.json', "r") as json_file:
            requirement = json.load(json_file)

    job = requirement['job']
    chat_history = [
        HumanMessage(content=f"Based on this job post, decide which topic should i learn :{job}"), 
        ]
    for s in requirement['steps']:
        chat_history.append(AIMessage('You should learn the topic :'+s['topic']))
        chat_history.append(HumanMessage('What i have learned :'+s['learned']))

    chat_history.append(AIMessage(topic))
    chat_history.append(HumanMessage(description))
    print(chat_history,job)
    qa = search_db()
    result = qa({'question': 
                 """Decide three option on what should i learn next based on previous learned, expand on previously learned description from the history chat, do not repeat on learned topic, do not move on from a certain topic to quick, makesure align with the objective for applying job requirement of :
                  
                    {job}

                 Please answer in list only with format [Topic]: [Description] - [Resources, do not make up resource]
                 
                 Maximum 3-5 items, do not repeat yourself.
                 """,
                "chat_history": chat_history})

    source_documents = result['source_documents']
    ans = str(result['answer'])

    print(ans)
    print('=============================')

    sd = []
    for i in range(len(source_documents)):
        sd.append(dict(source_documents[i]))

    json_dictionary = {'source_documents': sd, 'topics':str(ans)}
    requirement['steps'].append({
        'topic':topic,
        'learned':description,
    })
    json_object = json.dumps(requirement, indent=4)

    with open(file_path, "w") as outfile:
        outfile.write(json_object)

    return json_dictionary