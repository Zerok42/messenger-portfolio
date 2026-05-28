from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Annotated
from constants import VARCHAR_MAX_LENGTH as char_max, VARCHAR_MIN_LENGTH as char_min, TEXT_MAX_LENGTH as text_max

data = {
    "username": "Zerok0",
    "display_name": None,
    "email": "test@test.com",
    "password": "hello_world",
    "bio": None,
    'gender': None
}

allowed_pattern = r"^[a-zA-Zа-яА-ЯёЁ0-9\s!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]+$"

class UserRegisterSchema(BaseModel):
    username: Annotated[str, Field(min_length = char_min, max_length = char_max, pattern=allowed_pattern)]
    display_name: Annotated[str, Field(min_length = char_min, max_length = char_max, pattern=allowed_pattern)] | None
    email: EmailStr
    password: Annotated[str, Field(
        min_length=char_min, 
        max_length=char_max, 
        pattern=allowed_pattern
        )]
    bio: Annotated[str, Field(min_length = 1, max_length = text_max, pattern=allowed_pattern)] | None


    model_config = ConfigDict(extra='forbid')

print(repr(UserRegisterSchema(**data)))


