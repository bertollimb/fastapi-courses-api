from fastapi import FastAPI, HTTPException, status, Response
from typing import Dict, List
from models import Course, courses


app = FastAPI(
    title='Courses API',
    version='0.0.1',
    description='An API for FastAPI studies'
)


@app.get('/courses', response_model=List[Course], description='Returns all courses or an empty list.', summary='Returns all courses.')
async def get_courses():
    return courses 

@app.get('/courses/{course_id}', description='Returns the course referenced by the ID.',
         summary='It returns only one specific course.')
async def get_course(course_id: int):
    try:
        course = courses[course_id]
        return course
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Course not found.')
    
@app.post('/courses',status_code=status.HTTP_201_CREATED, description='It allows you to create a course and integrate it into your list of courses.', summary='Create course.')
async def post_course(course: Course):
    next_id = max(courses.keys()) + 1 if courses else 1

    course_data = course.dict()
    course_data.pop("id", None)
    courses[next_id] = course_data
    return course_data

@app.put('/courses/{course_id}', description='Update an existing course in your list.', summary='Update course.')
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
    
@app.delete('/courses/{course_id}', description='Allows you to remove a course from your list.', summary='Delete course.')
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
