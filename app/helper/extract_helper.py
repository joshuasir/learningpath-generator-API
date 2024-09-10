from langchain.chains import LLMChain,ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
import json

model_id = "mistral.mistral-7b-instruct-v0:2"

def extract_info(texts):
    json_object = json.dumps({'job': texts, 'steps':[]}, indent=4)

    with open(f'job-{1}.json', "w") as outfile:
        outfile.write(json_object)

    template = """You are an expert at professional field and education, given a list of possible technical skill below:

    Language :
    JavaScript, HTML/CSS, SQL, Python, TypeScript, Java, C#, C++, PHP, C, Go, Rust, Kotlin, Ruby, Dart, Lua, Swift, Visual Basic (.Net), 

    Database :
    PostgreSQL, MySQL, SQLite, MongoDB, Microsoft SQL Server, Redis, MariaDB, Elasticsearch, Oracle, DynamoDB, Firebase Realtime Database, Cloud Firestore, BigQuery, Microsoft Access, H2, Cosmos DB, Supabase, InfluxDB, Cassandra, Snowflake, Neo4J

    Cloud Provider :
    Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Firebase, Cloudflare, Digital Ocean, Heroku, Vercel, Netlify, VMware,

    Framework :
    React, Node.js, jQuery, Angular, Express, ASP.NET Core, Vue.js, Next.js, ASP.NET, Spring Boot, WordPress, Flask, Django, Laravel, AngularJS, FastAPI, Ruby on Rails, Svelte, NestJS, Blazor, Nuxt.js, Symfony, Gatsby, Phoenix, Fastify, Deno, CodeIgniter

    Other tools :
    Docker, npm, Pip, Homebrew, Yarn, Webpack, Make, Kubernetes, NuGet, Maven (build tool), Gradle, Vite, Visual Studio Solution, CMake, Cargo, GNU GCC, Terraform

    Based on the previous given list of technicall skill pick 1 in each category which corespond to the job post given : {question}
    
    you can only answer based on the category, do not say anything else other than category
    
    Do not invent new category, do not repeat yourself."""
    
    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm = VertexAI(model_name="gemini-pro")
    qaa = LLMChain(prompt=prompt, llm=llm)
    result = qaa.run(str(texts))

    return str(result)
