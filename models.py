
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table

# orm : object relational Mapper : 데이터베이스에서의 테이블의 데이터와 코드상의 객체와 연결을 지어주는 맵퍼이다.
from sqlalchemy.orm import relationship

from database import Base

Question_voter = Table (
    'question_voter', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id'), primary_key=True)
)

answer_voter = Table(
    'answer_voter', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('answer_id', Integer, ForeignKey('answer.id'), primary_key=True)
)


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    # Question과 같은 모델 클래스는 앞서 database.py에서 정의한 Base 클래스를 상속하여 만들어야 한다.
    # __tablename__은 모델에 의해 관리되는 테이블의 이름을 뜻한다.
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=Question_voter, backref='question_voters')


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    # question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가했다. 위와 같이 relationship으로 question 속성을 생성하면 답변 객체(예: answer)에서 연결된 질문의 제목을 answer.question.subject처럼 참조할 수 있다
    # relationship으로 question 속성을 생성하면 답변 객체(예: answer)에서 연결된 질문의 제목을 answer.question.subject처럼 참조할 수 있다.
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=answer_voter, backref='answer_voters')

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)