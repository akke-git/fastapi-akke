
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, question_crud
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/question",
)
#  APIRouter는 FastAPI에서 여러 개의 파일을 통해 프로젝트 구조를 구성하여 더 큰 애플리케이션을 만들 수 있도록 하는 도구
# prefix는 경로 공통적용



@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db), page: int = 0, size: int = 10, keyword: str = ''):
        total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size, keyword=keyword)
        return {
            'total': total,
            'question_list': _question_list
        }
        
        

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    question_crud.create_question(db=db, question_create=_question_create,
                                user=current_user)

        
@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: question_schema.QuestionUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 불가임. 노 권한.")
    question_crud.update_question(db=db, db_question=db_question,
                                question_update=_question_update)
    
@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    question_crud.delete_question(db=db, db_question=db_question)

@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def question_vote(_question_vote: question_schema.QuestionVote,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_vote.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    question_crud.vote_question(db, db_question=db_question, db_user=current_user)



# from fastapi import APIRouter
# # from sqlalchemy.orm import session

# from database import SessionLocal
# from models import Question
# from domain.question import question_schema, quesiton_crud

# 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router 객체이다. 
# router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
# prefix 속성은 요청 URL에 항상 포함되어야 하는 값이다
#  /api/question/list 라는 URL 요청이 발생하면 /api/question 이라는 prefix가 등록된 question_router.py 파일의 /list로 등록된 함수 question_list가 실행되는 것이다.
# router = APIRouter(
#     prefix="/api/question",
# )

# # question_list 함수는 db 세션을 생성하고 해당 세션을 이용하여 질문 목록을 조회하여 리턴하는 함수이다. 
# # 그리고 사용한 세션은 db.close()를 수행하여 사용한 세션을 반환했다.
# @router.get("/list",  response_model=list[question_schema.Question])
# # 추가한 response_model=list[question_schema.Question]의 의미는 question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미한다.
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()
#     return _question_list
#     # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     # return _question_list
    