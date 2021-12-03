from fastapi import APIRouter

from apis.v1 import route_jobs, route_login, route_user

api_router = APIRouter()

api_router.include_router(route_user.router, prefix='/users', tags=['users'])
api_router.include_router(route_jobs.router, prefix='/jobs', tags=['jobs'])
api_router.include_router(route_login.router, prefix='/login', tags=['login'])
