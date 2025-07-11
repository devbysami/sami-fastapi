from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    is_complete: bool

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True