import uvicorn
from fastapi import FastAPI, HTTPException,APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
users_router = APIRouter()




class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    userId:int
    status:str

    @field_validator('status')
    def check_status(cls, status):
        if status not in ['admin','user']:
            raise ValueError('status error')
        return status

    @field_validator('userId')
    def check_user(cls, userId):
        if userId <0:
            raise ValueError('error')
        return userId


users= {}


@users_router.get("/")
async def getUsers():
    return users
    raise HTTPException(status_code=404, detail="oops... your user didn't find")

def depends_func(id: int):
    if users[id] is not None:
        return False
    return True

@users_router.post("/")
async def add_user(user:User,is_not_exist: bool = Depends(depends_func)):
    try:
        if is_not_exist==False:
         raise HTTPException(status_code=422, detail="oops... an error occurred")
        users[user.userId]=user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"

@users_router.put("/{id}", response_model=User)
async def update_user(id: int, item: User):
    update_item = jsonable_encoder(item)
    users[id] = update_item
    return update_item



@users_router.delete("/{id}")
async def delete_user(id: int):
    del users[id]
    return {"message": "Item deleted"}