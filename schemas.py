from pydantic import BaseModel

class SignUpModel(BaseModel):
    id: int | None = None
    username: str
    email: str
    password: str
    is_staff: bool | None = None
    is_active: bool | None = None

    model_config = {
        "json_schema_extra": {
              "examples": [
                  {
                    "username": "johndoe",
                    "email": "johndoe@gmail.com",
                    "password": "password",
                    "is_staff": False,
                    "is_active": True
                }   
            ]

        }
    }