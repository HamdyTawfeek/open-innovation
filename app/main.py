from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"msg":"This is a simple API to filter and color image frames."}
