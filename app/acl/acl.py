def has_access(user_id: str, query: str) -> bool:
    acl = {
        "user123": ["finance", "aml"],
        "user456": ["tax"],
    }
    for keyword in acl.get(user_id, []):
        if keyword in query.lower():
            return True
    return False