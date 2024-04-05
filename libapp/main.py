"""
This is the main module of the library application.

It sets up the FastAPI application and includes the router for the students API.
"""

from fastapi import FastAPI

from api.v1.students import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter)
