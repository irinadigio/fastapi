from fastapi import APIRouter

from apis.version1 import route_users
from apis.version1 import routes_jobs
from apis.version1 import route_login

api_router = APIRouter()

api_router.include_router( route_users.router, prefix="/users", tags=["users"] )
api_router.include_router( routes_jobs.router, prefix="/job", tags=["Jobs"] )
api_router.include_router( route_login.router, prefix="/login", tags=["login"] )