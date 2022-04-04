from fastapi import FastAPI
from routes import enrollments
from routes import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='matriculas API', docs_url='/')
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


app.include_router(auth.router)
app.include_router(enrollments.router)
