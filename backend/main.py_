from fastapi import FastAPI
from api import auth
app.include_router(auth.router)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Backend Online 🚀"}
