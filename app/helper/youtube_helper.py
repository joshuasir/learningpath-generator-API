from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from fastapi import HTTPException
# import torch


#Mean Pooling - Take attention mask into account for correct averaging
# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0] #First element of model_output contains all token embeddings
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{BASE_DIR}/../.env')
API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY environment variable is not set")

youtube = build("youtube", "v3", developerKey=API_KEY)


def fetch_youtube(query):
    try:
        search_response = youtube.search().list(
            q=query,
            type="video",
            part="id",
            relevanceLanguage='en',
            maxResults=10
        ).execute()

        video_ids = [search_result["id"]["videoId"] for search_result in search_response.get("items", [])]

        videos_response = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(video_ids)
        ).execute()

        videos = []
        for video_result in videos_response.get("items", []):
            video = {
                "title": video_result["snippet"]["title"],
                "description": video_result["snippet"]["description"],  # This will be the full description
                "thumbnail": video_result["snippet"]["thumbnails"]["default"]["url"],
                "video_id": video_result["id"],
                "duration": video_result["contentDetails"]["duration"],
                "view_count": video_result["statistics"]["viewCount"],
                "like_count": video_result["statistics"].get("likeCount", "N/A"),
                "comment_count": video_result["statistics"].get("commentCount", "N/A"),
                "published_at": video_result["snippet"]["publishedAt"]
            }
            videos.append(video)

        return {"videos": videos}
    except HttpError as e:
        raise HTTPException(status_code=e.resp.status, detail=str(e))
