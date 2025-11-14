from fastapi import FastAPI,Security
# from fastapi.middleware.cors import CORSMiddleware
import students
from auth import azure_scheme

# app = FastAPI(
#     swagger_ui_oauth2_redirect_url='/oauth2-redirect',
#     swagger_ui_init_oauth={
#         'usePkceWithAuthorizationCodeGrant': True,
#         'clientId': 'b10ae25f-404b-472c-9c46-1083cd645716',
#         'scopes': 'api://80d4fbf6-4eaf-438e-9600-567b4441a2ca/access_as_user',
#     },
# )

app = FastAPI()
# app.add_middleware(CORSMiddleware,
#                    allow_origins = ["http//localhost:5173"],
#                    allow_credentials = True,
#                    allow_methods = ["*"],
#                    allow_headers = ["*"])

app.include_router(students.router,dependencies=[Security(azure_scheme)])

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world! This is a Uvicorn FastAPI app."}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "query": q}

if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
