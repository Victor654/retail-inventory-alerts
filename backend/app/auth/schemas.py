from pydantic import BaseModel, Field

class RequestCodeSchema(BaseModel):
    phone_number: str = Field(..., example="+573001234567")
