from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API m00-projeto funcionando perfeitamente 🚀"}
