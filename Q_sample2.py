from database import SessionLocal
from models import Question
from datetime import datetime
from sqlalchemy import select, insert, delete, FetchedValue

db = SessionLocal()
# for i in range(300):
#     q = Question(subject='its a test data:[%03d]' % i, content='no data', create_date=datetime.now())
#     db.add(q)    
# db.commit()


for i in range(15,300):
    d = Question(id = i)
    db.delete(d)
    db.commit()    

db.delete(Question).filter(id=10)

# 일반적인 sqlalchemy 조회방식. cmd에서 실행 시 object만 표시되고 있음
stmt = select(Question)
datas = db.execute(stmt)
for data in datas:
    print(data)