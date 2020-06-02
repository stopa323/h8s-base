from pydantic import BaseModel, Field


class PancakeType(BaseModel):
    name: str = Field(...,
                      title="Juicy Pancake type")
    description: str = Field("No description so far...",
                             title="Catchy description",
                             max_length=500)

    class Config:
        schema_extra = {
            "description": "Object represents Pancake type",
            "example": {
                "name": "BananaPancake",
                "description": "World-class, 5-star, Gordon Ramsay-approved, "
                               "Banana pancake."}}
