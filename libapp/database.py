import os

from motor.motor_asyncio import AsyncIOMotorClient

from settings import config

def get_database():
    username = config.get('DATABASE', 'DB_USERNAME')
    password =  config.get('DATABASE', 'DB_PASSWORD')
    client = AsyncIOMotorClient(
        f"mongodb+srv://{username}:{password}@libmgr.xvmgc08.mongodb.net/?retryWrites=true&w=majority&appName=libMgr"
    )
    return client.libMgr
