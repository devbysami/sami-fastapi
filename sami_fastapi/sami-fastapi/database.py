from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from pymongo import MongoClient

# PSQL Database
PSQL_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/tododb"
                              
engine = create_async_engine(PSQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

async def get_db_psql():
    async with SessionLocal() as session:
        yield session
        
# Mongodb

server_config = {
    "username" : "samuamir555",
    "password" : "bmw740il",
    "ip" : "ac-5zdakwq-shard-00-00.eevx2ao.mongodb.net",
    "port" : "27017",
    "db" : "sample_mflix"
}

MONGO_CONNECTION_STRING = f"mongodb+srv://{server_config['username']}:{server_config['password']}@{server_config['ip']}"

mongo_client = MongoClient(MONGO_CONNECTION_STRING)
db = mongo_client[server_config["db"]]

def get_db_mongo():
    yield db
