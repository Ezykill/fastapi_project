from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from wiki_random import get_wiki_random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/wiki")
async def wikipedia():
    title,url = get_wiki_random()

    return {"title": title,"url": url}

@app.get("/wikiredirect")
async def wiki_redirect():
    title,url = get_wiki_random()

    return RedirectResponse(url)