# 스키마 : 스프링이나 nestJS의 DTO와 같은 개념
# DTO란 Data Transfer Object의 약자로서 어떤 메소드나 클래스간 객체정보를 주고 받을 때 특정 모양으로 주고 받겠다는 일종의 약속이다.
# FastAPI의 스키마는 pydantic model에 종속돼있다. 말이 종속이지 그냥 pydantic 패키지를 그대로 갖다 쓴다

import datetime
from pydantic import BaseModel, validator
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    user : User | None
    modify_date: datetime.datetime | None = None
    answers: list[Answer] = []
    voter: list[User] = []

    class Config:
        orm_mode = True
    # 모델에서 사용하는 모든 타입을 JSON 변환로직을 수행하지 않고 pydantic 이용 : 위의 CLASS를 pydantic -> JSON 순서로 변환


class QuestionCreate(BaseModel):
    subject: str
    content: str
    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []
    

class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id : int

class QuestionVote(BaseModel):
    question_id: int