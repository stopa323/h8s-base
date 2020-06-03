from fastapi import APIRouter
from typing import List

from base.provider import pancake as provider
from base.schema import pancake as api


router = APIRouter()


@router.get("/types",
            name="List Pancake types",
            description="Fetch list of all available pancake types",
            response_model=List[api.PancakeType],
            tags=["Pancakes"])
async def list_pancakes():
    objects = provider.list_pancakes()
    return objects


@router.post("/types",
             name="Create Pancake type",
             description="Create brand new pancake type",
             response_model=api.PancakeType,
             tags=["Pancakes"])
async def create_pancake_type(pancake_type: api.PancakeType):
    object = provider.create_pancake_type(pancake_type)
    return object
