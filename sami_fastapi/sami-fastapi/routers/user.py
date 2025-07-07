from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db_psql, get_db_mongo
from schemas import tasks as schemasTasks
from schemas import user as schemasUser
from fastapi.responses import JSONResponse
from auth import get_current_user, create_access_token, verify_password, get_password_hash
from curd import get_user_by_email, create_user, get_user_by_email_mongo, create_user_mongo
from database import db

router = APIRouter()

@router.post("/user/signup")
async def signup(user: schemasTasks.UserCreate, db: AsyncSession = Depends(get_db_psql)):
    
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user.password = get_password_hash(user.password)
    created_user = await create_user(db, user)
    
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "User created successfully",
            "data": {
                "id": created_user.id,
                "email": created_user.email,
            }
        }
    )
    
@router.post("/user/login")
async def login(user: schemasUser.UserLogin, db: AsyncSession = Depends(get_db_psql)):
    
    db_user = await get_user_by_email(db, user.email)
    
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(db_user.id)})
    
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer"
        }
    )

@router.post("/user/signup/v2/")
async def signup(user: schemasTasks.UserCreate):
    
    db_user = await get_user_by_email_mongo(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user.password = get_password_hash(user.password)
    created_user = await create_user_mongo(db, user)
    
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "User created successfully",
            "data": {
                "id": str(created_user["id"]),
                "email": created_user["email"],
            }
        }
    )
    
@router.post("/user/login/v2/")
async def login(user: schemasUser.UserLogin):
    
    db_user = await get_user_by_email_mongo(db, user.email)
    
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(db_user["id"])})
    
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer"
        }
    )

