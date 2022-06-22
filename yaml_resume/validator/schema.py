DOB_REGEX = r"(([0-2][0-9])|[1-9]|(3[0-1]))/((1[0-2])|(0?[1-9]))/[0-9]{4}"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
PHONE_NUMBER_REGEX = (
    r"((?:\+|00)[17](?: |\-)?"
    + r"|(?:\+|00)[1-9]\d{0,2}(?: |\-)?"
    + r"|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)"
    + r"|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})"
    + r"|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))"
)
URL_REGEX = (
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]"
    + r"|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

experience = {
    "company": {"type": "string"},
    "position": {"type": "string"},
    "start_date": {"type": "string"},
    "end_date": {"type": "string", "required": False},
    "summary": {"type": "string"},
    "tags": {"type": "list", "schema": {"type": "string"}},
    "website": {"type": "string", "regex": URL_REGEX, "required": False},
}

degree = {
    "institution": {"type": "string"},
    "program": {"type": "string"},
    "degree": {"type": "string"},
    "start_date": {"type": "string"},
    "end_date": {"type": "string", "required": False},
    "location": {"type": "string", "required": False},
    "website": {"type": "string", "regex": URL_REGEX, "required": False},
    "courses": {"type": "list", "schema": {"type": "string"}},
}

skill = {"name": {"type": "string"}, "level": {"type": "integer", "min": 0, "max": 100}}

hobby = {"name": {"type": "string"}, "details": {"type": "string", "required": False}}

project = {
    "name": {"type": "string"},
    "description": {"type": "string"},
    "website": {"type": "string", "regex": URL_REGEX, "required": False},
}

language = {"name": {"type": "string"}, "level": {"type": "string"}}

profile = {"network": {"type": "string"}, "website": {"type": "string", "regex": URL_REGEX}}

contact = {
    "name": {"type": "string"},
    "summary": {"required": False, "type": "string"},
    "email": {"type": "string", "regex": EMAIL_REGEX},
    "phone": {"type": "string", "regex": PHONE_NUMBER_REGEX},
    "location": {"type": "string"},
}

award = {
    "name": {"type": "string"},
    "year": {"type": "integer"},
    "description": {"type": "string"},
    "website": {"type": "string", "regex":URL_REGEX, "required": False},
}

resume = {
    "contact": {
        "type": "dict",
        "required": True,
        "require_all": True,
        "schema": contact,
    },
    "summary": {
        "type": "string",
        "required": False
    },
    "profiles": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": profile},
    },
    "experiences": {
        "type": "list",
        "required": True,
        "require_all": True,
        "schema": {"type": "dict", "schema": experience},
    },
    "education": {
        "type": "list",
        "required": True,
        "require_all": True,
        "schema": {"type": "dict", "schema": degree},
    },
    "skills": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": skill},
    },
    "languages": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": language},
    },
    "projects": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": project},
    },
    "hobbies": {
        "type": "list",
        "required": False,
        "require_all": False,
        "schema": {"type": "dict", "schema": hobby},
    },
    "awards": {
        "type": "list",
        "required": False,
        "require_all": True,
        "schema": {"type": "dict", "schema": award},
    },
}
