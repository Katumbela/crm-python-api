
from facebook_scraper import get_posts
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id }




@app.get("/get_fb_posts/{query}")
def read_item(query: str):
    posts = []
    for post in get_posts(query, pages=1):
        posts.append(post['text'][:50])
        

    return {"query": query, "posts": posts}


