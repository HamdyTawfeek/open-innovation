from fastapi import FastAPI
from app.db import engine
from app.frames import adjust_and_store_frames
from sqlalchemy import text


def start_application():
    app = FastAPI()
    adjust_and_store_frames()
    return app

app = start_application()


@app.get("/frames/")
def read_item(depth_min: float = 9000.1, depth_max: float = 9546.0):
    conn = engine.connect()
    output = conn.execute(
        text(f"SELECT * FROM data WHERE depth BETWEEN {depth_min} AND {depth_max}")
    )
    results = output.mappings().fetchall()
    conn.close()
    return {"image_frames": results}

@app.get("/")
def home():
    return {"msg":"This is a simple API to filter and color image frames."}
