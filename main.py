from fastapi import FastAPI
from routes import enrollments
from routes import auth


app = FastAPI(title='matriculas API', docs_url='/')
app.include_router(auth.router)
app.include_router(enrollments.router)
