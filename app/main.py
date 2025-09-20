from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from CI/CD pipeline demo!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
