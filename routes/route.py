from fastapi import APIRouter, HTTPException
from models.issues import Issue
from config.database import collection_name
from schema.schemas import list_serial

router = APIRouter()

# Get Request Method
@router.get("/")
async def get_issues():
    return list_serial(collection_name.find())


# Post Request Method
@router.post("/")
async def post(issue: Issue):
    result = collection_name.insert_one(dict(issue))
    return {
        "id": str(result.inserted_id),
        "issue_number": issue.issue_number,
        "reason": issue.reason,
    }


# Delete Request Method
@router.delete("/{issue_number}")
async def delete_issue(issue_number: int):
    result = collection_name.find_one_and_delete({"issue_number": issue_number})
    if not result:
        raise HTTPException(status_code=404, detail="Issue not found")
    return {"message": "Issue deleted successfully"}


