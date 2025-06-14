# app/main.py
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from mako.lookup import TemplateLookup

# Templates setup
templates = TemplateLookup(directories=["app/templates"], input_encoding="utf-8")

# Routers
from app.routers.auth import router as auth_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth_router)