from fastapi import FastAPI
from routes import enrollments
from routes import admin

app = FastAPI(title='matriculas API', docs_url='/')
app.include_router(admin.router)
app.include_router(enrollments.router)
