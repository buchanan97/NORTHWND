from pydantic import BaseModel

class CustomerOut(BaseModel):
    id: str
    company_name: str
    contact_name: str
    city: str

    class Config:
        orm_mode = True