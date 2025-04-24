from config import supabase_url, supabase_key
from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from supabase import create_client


router = APIRouter()

sb = create_client(supabase_url, supabase_key)


class User(BaseModel):
    email: str
    password: str


@router.post("/sign_up")
async def sign_up(request: User):
    return await run_in_threadpool(sb.auth.sign_up, request.model_dump())


@router.post("/sign_in")
async def sign_in(request: User):
    return await run_in_threadpool(sb.auth.sign_in_with_password, request.model_dump())


@router.get("/sign_out")
async def sign_out():
    return await run_in_threadpool(sb.auth.sign_out)
