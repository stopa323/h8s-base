from fastapi import APIRouter


router = APIRouter()


@router.get("/types",
            name="List Pancake types",
            description="Fetch list of all available pancake types",
            tags=["Pancakes"])
async def list_pancakes():
    return {"pancakes": ["ChocolatePancake", "BananaPancake"]}
