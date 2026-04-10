from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    id: Optional[int] = None
    title: str
    course_classes: int
    hours: int

courses = [
    Course(id=1, title='Programming for laymen', course_classes=42, hours=56),
    Course(id=2, title='Algorithm and programming logic', course_classes=52, hours=67)
]
