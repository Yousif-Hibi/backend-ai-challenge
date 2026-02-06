from pydantic import BaseModel, EmailStr, Field,ValidationError , field_validator
from datetime import datetime
BAD_WORDS = ["bad", "ass"]
class User(BaseModel):
    name: str 
    email: EmailStr
    age: int = Field(ge=18)
    is_active: bool = True
    created_at: datetime = None

    @field_validator('name')
    @classmethod
    def check_bad_words(cls, v: str) -> str:
        if any(bad in v.lower() for bad in BAD_WORDS):
            raise ValueError('Username contains prohibited language')
        return v
# Test with clean data
clean_data = {
   "name": "Alice Johnson bad",
   "email": "alice@example.com",
   "age": 19
}


try :
    user = User(**clean_data)

    print(f"User created: {user.name}, Age: {user.age}")
    print(f"Model output: {user.model_dump()}")
except ValidationError as e:
   print(f"Validation errors: {e} issues found")