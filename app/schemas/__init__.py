patient_schema_post = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["age", "name"],
    "additionalProperties": False
}

patient_schema_put = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "additionalProperties": False
}

medics_schema_post = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "crm": {"type": "string", "minLength": 4},
        "specialty": {"type": "string"}
    },
    "required": ["name", "crm", "specialty"],
    "additionalProperties": False
}

medics_schema_put = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "crm": {"type": "string", "minLength": 4},
        "specialty": {"type": "string"}
    },
    "additionalProperties": False
}

consultation_schema_post = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "consult_time": {
            "type": "string",
            "pattern": "^([01]?\\d|2[0-3]):([0-5]\\d)$",
            "description": "hour of consult in HH:MM"
        },
        "consult_date": {
            "type": "string",
            "pattern": "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\\d{4})$",
            "description": "date of consult in DD/MM/YYYY"
        },
        "notes": {
            "type": "string",
            "maxLength": 500,
            "description": "notes about consult (optional)"
        }
    },
    "required": ["consult_time", "consult_date"],
    "additionalProperties": False
}

consultation_schema_put = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "consultation_time": {
            "type": "string",
            "pattern": "^([01]?\\d|2[0-3]):([0-5]\\d)$",
            "description": "time of consultation in HH:MM format"
        },
        "consultation_date": {
            "type": "string",
            "pattern": "^(0[1-9]|[12]?\\d|3[0-1])/(0[1-9]|1[0-2])/(\\d{4})$",
            "description": "date of consultation in DD/MM/YYYY format"
        },
        "notes": {
            "type": "string",
            "maxLength": 500,
            "description": "notes about consultation (optional)"
        }
    },
    "required": [],
    "additionalProperties": False
}
