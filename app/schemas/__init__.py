patient_schema_post = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string",
                  "format": "email",
                  "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"},
        "password": {"type": "string",
                     "minLength": 8,
                     "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"}
    },
    "required": ["age", "name", "email", "password"],
    "additionalProperties": True
}

patient_schema_put = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string",
                 "minLength": 1,
                 "pattern": "^[^\\s]"
                 },
        "age": {"type": "integer",
                "minimum": 0,
                "pattern": "^[^\\s]"}
    },
    "additionalProperties": True
}

medics_schema_login = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "email": {"type": "string",
                  "format": "email",
                  "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"},
        "password": {"type": "string",
                     "minLength": 8,
                     "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"}
    },
    "required": ["email", "password"]
}
medics_schema_add = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "pattern": "^[\\S]"},
        "crm": {"type": "string", "minLength": 4, "pattern": "\\d{4}"},
        "specialty": {"type": "string", "pattern": "^[^\\s]"},
        "email": {"type": "string",
                  "format": "email",
                  "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"},
        "password": {"type": "string",
                     "minLength": 8,
                     "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"},
        "roles": {"type": "array",
                  "minItems": 1,
                  "items": {"type": "string", "minLength": 1},
                  "default": ["medic"]}
    },
    "required": ["name", "crm", "specialty", "email", "password", "roles"],
    "additionalProperties": True
}

medics_schema_put = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string", "pattern": "^[\\S]"},
        "crm": {"type": "string", "minLength": 4},
        "specialty": {"type": "string", "pattern": "^[^\\s]"}
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
            "description": "notes about consultation (optional)",
            "pattern": "^[^\\s]"
        },
        "medic_id": {
            "type": "integer",
            "description": "medic associated at consult"
        }
    },
    "required": [],
    "additionalProperties": False
}
