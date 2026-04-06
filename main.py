from fastapi import FastAPI, HTTPException, status, Response
from typing import Dict
from models import Course

app = FastAPI()

#DB fake
courses: Dict[int, dict] = {
    1: {
        "title": "Programming for laymen",
        "course_classes": 112,
        "hours": 55
        },
    2: {
        "title": "Algorithm and programming logic",
        "course_classes": 87,
        "hours": 67 
        },
}

@app.get('/courses', response_model=Dict[int, Course])
async def get_courses():
    return courses 

@app.get('/courses/{course_id}')
async def get_curse(course_id: int):
    try:
        course = courses[course_id]
        return course
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found.')
    
@app.post('/courses', status_code=status.HTTP_201_CREATED)
async def post_course(course: Course):
    next_id = max(courses.keys()) + 1 if courses else 1

    course_data = course.dict()
    course_data.pop("id", None)
    courses[next_id] = course_data
    return course 

@app.put('/courses/{course_id}')
async def put_course(course_id: int, course: Course):
    if course_id in courses:
        course_data = course.dict()
        course_data["id"] = course_id
        courses[course_id] = course_data
        return course_data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'There is no course with the ID:{course_id}')
    
@app.delete('/courses/{course_id}')
async def delete_course(course_id: int):
    if course_id in courses:
        del courses[course_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'There is no course with the ID: {course_id}')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
