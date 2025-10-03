def individual_serial(issue) -> dict:
    return {
        "id": str(issue["_id"]),
        "issue_number": issue["issue_number"],
        "reason": issue["reason"]
    }

def list_serial(issues) -> list:
    return [individual_serial(issue) for issue in issues]

