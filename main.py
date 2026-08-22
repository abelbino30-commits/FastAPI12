from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from my AI app on Vercel!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
