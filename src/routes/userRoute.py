from fastapi import APIRouter

from src.dtos.productSchema import UserResponse
from src.utils.utils import get_all_users
from typing import List
userRoute=APIRouter()


@userRoute.get("/", response_model=List[UserResponse])
def get_users():
    data=get_all_users()
    return data