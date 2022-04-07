from fastapi import FastAPI
from routes import enrollments
from routes import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='matriculas API', docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(auth.router)
app.include_router(enrollments.router)
