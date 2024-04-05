"""
This is the main module of the library application.

It sets up the FastAPI application and includes the router for the students API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api.v1.students import router as StudentRouter

app = FastAPI()

# CORS middleware
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(StudentRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
