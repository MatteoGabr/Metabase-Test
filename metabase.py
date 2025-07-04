from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DOGS = [{"name": "Milo", "type": "Golden"}, {"name": "Jax", "type": "German Sheperd"}]

@app.get('/')
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "home", "dogs": DOGS})