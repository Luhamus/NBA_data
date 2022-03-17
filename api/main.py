from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import get

app = FastAPI()

# To make it reachable from anywhere on web
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get.router)

@app.get("/", tags=["Index"])
def getIndex():
    return {"Message": "Hello! add /docs for documentation"}
