from fastapi import FastAPI
from .routers import get
import pandas as pd

app = FastAPI()

#/CORS STUFF HERE
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
