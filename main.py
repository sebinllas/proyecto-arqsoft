from fastapi import FastAPI
from routes import enrollments

app = FastAPI(title='matriculas API')
app.include_router(enrollments.router)
