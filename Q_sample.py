# 질문 입력 ---------------------------------------------------------------------------------

from models import Question, Answer
from datetime import datetime

q = Question(subject='astalavista babe?', content='TTTTT#', create_date=datetime.now())

from database import SessionLocal
db = SessionLocal()
db.add(q)
db.commit()



# 쿼리 조회 ---------------------------------------------------------------------------------

db.query(Question).filter(Question.id==1).all()
# filter 함수는 인자로 전달한 조건에 맞는 데이터를 찾아서 반환한다. 여기서는 기본 키인 id를 이용했으므로 값을 1개만 반환한다

db.query(Question).get(1)
# id는 유일한 값이므로 filter 함수 대신 get 함수를 이용해 조회할 수도 있다
# 다만 get 함수의 리턴은 단 1건만 가능하므로 리스트가 아닌 Question 객체가 리턴된다

db.query(Question).filter(Question.subject.like('%FastAPI%')).all()
# "FastAPI"라는 문자열이 포함된 질문이 조회되었다. filter 함수에 전달한 Question.subject.like('%FastAPI%') 코드의 의미는 Question 모델 subject 속성에 "FastAPI"라는 문자열이 포함되는가?"이다


# 수정 ---------------------------------------------------------------------------------
q = db.query(Question).get(2)
q.subject = 'FastAPI Model Question'
db.commit()


# 삭제 ---------------------------------------------------------------------------------
q = db.query(Question).get(2)
db.delete(q)
db.commit()



# 답변 데이터 저장 ---------------------------------------------------------------------------------

from datetime import datetime
from models import Question, Answer
from database import SessionLocal

db = SessionLocal()
q = db.query(Question).get(2)
a = Answer(question=q, content='오케바리 ㄱㄱㄱㄱㄱㄱㄱ', create_date=datetime.now())
db.add(a)
db.commit()






