from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router

app = FastAPI()


# ---------------------------------------------------------------------------------------------------
# Origin은 Protocol, Domain, Port 묶음을 이르는 말이다. (Path나 Query String 등은 해당하지 않는다.)
# CORS란 HTTP 헤더를 통해 한 Origin에서 실행 중인 웹 어플리케이션이 다른 Origin의 리소스에 접근할 수 있도록 브라우저에 권한을 부여하는 정책이다
# origin을 등록하고 미들웨어를 등록한다 (origin은 https나 특정포트를 지정하는 등의 경우 등록필요)

origins = [
    "http://localhost:5173",    # 또는 "http://127.0.0.1:5173"
    "http://localhost:8000"
    "http://127.0.0.1:8000"
    "http://13.125.234.195:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------------------------------------------------------------------

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")