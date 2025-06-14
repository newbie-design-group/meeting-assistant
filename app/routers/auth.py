# app/routers/auth.py
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import EmailStr
from app.main import templates
from app.core.database import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

# Setup service
db = SessionLocal()
service = UserService(UserRepository(db))
router = APIRouter()

@router.get("/signup", response_class=HTMLResponse)
async def signup_get(request: Request):
    tmpl = templates.get_template("signup.mako")
    return HTMLResponse(tmpl.render(request=request, page_title="Sign Up"))

@router.post("/signup", response_class=HTMLResponse)
async def signup_post(
    request: Request,
    username: str = Form(...),
    email: EmailStr = Form(...),
    password: str = Form(...),
    confirm: str = Form(...),
):
    error = None
    if password != confirm:
        error = "Passwords do not match."
    elif len(password) < 8:
        error = "Password must be at least 8 characters."
    elif service.get_by_username(username):
        error = "Username already taken."
    elif service.get_by_email(email):
        error = "Email already registered."

    if error:
        tmpl = templates.get_template("signup.mako")
        return HTMLResponse(tmpl.render(request=request, page_title="Sign Up", error=error))

    service.create_user(username, email, password)
    return RedirectResponse(url="/welcome", status_code=303)