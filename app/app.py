import os
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from helper.youtube_helper import fetch_youtube
from helper.udemy_helper import fetch_udemy
from helper.oreilly_helper import fetch_oreilly
from helper.embed_helper import generate_learning_path,store_and_embed
from helper.extract_helper import extract_info

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


app = FastAPI(
        # openapi_prefix='/py'
    )

load_dotenv()
security = HTTPBasic()
prefix_router = APIRouter(prefix="/api/v1")

# Add the paths to the router instead

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class SearchRequest(BaseModel):
    query: str

class GeneratePathRequest(BaseModel):
    topic: str
    description: str
    pathid: str

@prefix_router.post("/search_youtube")
def search_youtube(request: SearchRequest):
    return fetch_youtube(request.query)


@prefix_router.post("/embed_youtube")
def embed_youtube(request: SearchRequest):
    res = fetch_youtube(request.query)
    dict_ = {}
    for r in res["videos"]:
        video_id = r["video_id"]
        dict_[f'https://www.youtube.com/watch?v={video_id}'] = r["title"] + ' ' + r['description']
    return store_and_embed(dict_)

@prefix_router.post("/path")
def search_db_embedding(request: GeneratePathRequest):
    learning_path = generate_learning_path(request.topic,request.description,request.pathid)
    return learning_path

@prefix_router.post("/search_udemy")
def search_udemy(request: SearchRequest):
    return fetch_udemy(request.query)


@prefix_router.post("/extract")
def extract_requirement(request: SearchRequest):
    return extract_info(request.query)

@prefix_router.post("/search_oreilly")
def search_oreilly(request: SearchRequest):
    return fetch_oreilly(request.query)

@prefix_router.get("/")
def init():
    return os.getenv("PASSWORD")


def isAuth(username, password):
    return ((os.getenv("FASTAPI_USERNAME")==username) and (os.getenv("FASTAPI_PASSWORD")==password))


app.include_router(prefix_router)