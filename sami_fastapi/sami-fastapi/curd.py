from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from models import tasks as modelTasks
from schemas import tasks as schemaTasks

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(modelTasks.User).where(modelTasks.User.email == email))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user: schemaTasks.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = modelTasks.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def create_task(db: AsyncSession, task: schemaTasks.TaskCreate, user_id: int):
    db_task = modelTasks.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task