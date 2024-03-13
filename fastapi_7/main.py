import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr, ValidationError, validator, field_validator

app = FastAPI()

class Task(BaseModel):
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    description: constr(min_length=1, max_length=120)
    taskId:int
    status:str

    @field_validator('status')
    def check_status(cls, status):
        if status not in ['open','close']:
            raise ValueError('status error')
        return status

    @field_validator('taskId')
    def check_task(cls, taskId):
        if taskId <0:
            raise ValueError('error')
        return taskId


tasks= {}
try:

@app.get("/")
async def getTasks():
    return tasks
    raise HTTPException(status_code=404, detail="oops... your task didn't find")

@app.post("/")
async def add_task(task: Task):
    try:
        tasks[task.taskId]=task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {task.name}"
@app.put("/{id}", response_model=Task)
async def update_task(id: int, item: Task):
    update_item = jsonable_encoder(item)
    tasks[id] = update_item
    return update_item



@app.delete("/{id}")
async def delete_task(id: int):
    del tasks[id]
    return {"message": "Item deleted"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080)
