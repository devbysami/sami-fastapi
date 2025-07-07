from fastapi import FastAPI
from routers import user, tasks

app = FastAPI()

app.include_router(user.router)
app.include_router(tasks.router)