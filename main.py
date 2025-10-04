from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test_CICD():
    return {"Hello": "test success"}
