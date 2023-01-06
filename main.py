from web_automation import automaton

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def base_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post("/testrun")
async def test_run(url: str):
    title = await automaton.go_to_web_and_fetch_title(url)
    return {"title": title}

@app.post("/find")
async def find_images_on_google(request: Request, prompt: str = Form()):
    result = await automaton.find_images_on_google(prompt)
    return templates.TemplateResponse('result.html', {'request': request, 'prompt': prompt, 'images': result})