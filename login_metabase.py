from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Mostra il form di login
@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("metabase_form.html", {"request": request})

# Riceve i dati, chiede sessione a Metabase e fa redirect
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:3000/api/session",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:
            session_id = response.json()["id"]
            # Fai redirect verso Metabase con cookie di sessione
            redirect = RedirectResponse(url="http://localhost:3000/", status_code=303)
            redirect.set_cookie(key="metabase.SESSION", value=session_id)
            return redirect
        else:
            return {"error": "Login a Metabase fallito, controlla credenziali"}
