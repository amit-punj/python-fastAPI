from bson import ObjectId

def serialize_doc(doc: dict) -> dict:
    """Convert a MongoDB document to a JSON-serializable dict"""
    for key, value in doc.items():
        if isinstance(value, ObjectId):   # convert ObjectId
            doc[key] = str(value)
        elif isinstance(value, list):     # handle nested lists
            doc[key] = [serialize_doc(item) if isinstance(item, dict) else item for item in value]
        elif isinstance(value, dict):     # handle nested dicts
            doc[key] = serialize_doc(value)
    return doc

def serialize_docs(docs: list) -> list:
    """Convert a list of MongoDB documents"""
    return [serialize_doc(doc) for doc in docs]
