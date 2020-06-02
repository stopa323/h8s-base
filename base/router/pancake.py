from fastapi import APIRouter
from typing import List

from base.schema import pancake


router = APIRouter()


@router.get("/types",
            name="List Pancake types",
            description="Fetch list of all available pancake types",
            response_model=List[pancake.PancakeType],
            tags=["Pancakes"])
async def list_pancakes():
    return {"pancakes": ["ChocolatePancake", "BananaPancake"]}
