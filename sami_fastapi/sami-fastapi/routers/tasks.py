from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from curd import create_task
from schemas import tasks as schemasTasks
from fastapi.responses import JSONResponse
from auth import get_current_user

router = APIRouter()

@router.post("/tasks/", response_model=schemasTasks.Task)
async def create_task(task: schemasTasks.TaskCreate, db: AsyncSession = Depends(get_db), user: schemasTasks.User = Depends(get_current_user)):
    return await create_task(db, task, user.id)