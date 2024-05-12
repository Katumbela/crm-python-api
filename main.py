from typing import Union
from facebook_scraper import get_posts
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




@app.get("/get_fb_posts/{query}")
def read_item(query: str, q: Union[str, None] = None):
    posts = []
    for post in get_posts(query, pages=1):
        posts.append(post['text'][:50])
        print(post['text'])

    return {"query": query, "posts": posts}


