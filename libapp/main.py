"""
This is the main module of the library application.

It sets up the FastAPI application and includes the router for the students API.
"""

from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware

from api.v1.students import router as StudentRouter

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(StudentRouter)
