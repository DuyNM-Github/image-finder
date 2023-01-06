from web_automation import automaton

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def base_page():
    return {"message": "Hello"}

@app.post("/goto")
async def test_run(url: str):
    title = await automaton.go_to(url)
    return {"title": title}