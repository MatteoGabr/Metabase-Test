from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

# Configura cartella templates
templates = Jinja2Templates(directory="templates")

@app.get("/",)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
async def submit(username: str = Form(...), password: str = Form(...)):
    # Fai un redirect verso /name con il parametro nella query string
    return RedirectResponse(url=f"/name?username={username}&password={password}", status_code=303)

@app.get("/name")
async def name(request: Request, username: str = "", password: str = ""):
    return templates.TemplateResponse(
        "dati_user.html", 
        {"request": request, "name": username, "password": password}
    )