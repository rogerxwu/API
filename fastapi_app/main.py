"""
Author: Xian Wu xianwuusa@gmail.com
Date: 2024-08-17 10:24:03
LastEditors: Xian Wu xianwuusa@gmail.com
LastEditTime: 2024-08-17 10:24:08
FilePath: /Code/API/fastapi_app/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""

# app/main.py

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Initialize monitoring
Instrumentator().instrument(app).expose(app)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
