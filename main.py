"""Naralabs task: Managing samples.
    Manuel Frias Leon
"""

from fastapi import FastAPI
from routers import samples

app = FastAPI()

#Routers
app.include_router(samples.router)

@app.get("/")
async def root():
    return "Hello Naralabs"