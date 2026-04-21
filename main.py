from fastapi import FastAPI

app = FastAPI(title="My Laba3 API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Привет, мир! CI/CD работает!", "author": "Ваше Имя"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"project": "Лабораторная работа 3", "server": "VPS"}
