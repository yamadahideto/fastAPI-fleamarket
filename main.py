from fastapi import FastAPI
from routers import item

app = FastAPI()

# routers/item.pyからinclude
app.include_router(item.router)

