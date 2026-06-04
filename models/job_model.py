from pydantic import BaseModel
from datetime import datetime

class job(BaseModel):
    company_name:str
    role:str
    status:str
    priority:str
    notes:str = ""
    application_link:str = ""
    created_at:str = datetime.now().strftime("%Y-%m-%d")