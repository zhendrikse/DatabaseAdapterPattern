from fastapi import FastAPI
import uvicorn

from endpoint import app, router

app.include_router(router)
uvicorn.run(app,host="0.0.0.0",port=8080)
