patient_schema_post = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["age", "name"],
    "additionalProperties": False
}

medics_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "crm": {"type": "string"}
    }
}

consultation_schema = {}
