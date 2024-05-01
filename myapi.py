from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name": "John Doe",
        "age": "12",
        "year": "Year 8"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year: str
    
class UpdateStudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    year:Optional[str] = None

@app.get("/")
def index():
    return{"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student you want to view.", gt=0)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"error": "No student with that name found."}
    
@app.post('/create-student/{student_id}')
def create_student(student_id : int , student : Student):
    if student_id in student:
        return {"Error: Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_students(student_id:int, student:UpdateStudent):
    