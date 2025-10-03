from pydantic import BaseModel

class Issue(BaseModel):
    issue_number: int
    reason: str 

