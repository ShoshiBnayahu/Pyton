import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from tasks_Router import tasks_router
from users_Router import users_router

app = FastAPI()
app.include_router(tasks_router, prefix='/tasks')
app.include_router(users_router, prefix='/users')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
