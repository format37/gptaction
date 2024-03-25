from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def get_handler(request: Request):
    query_params = request.query_params
    print("Received GET request")
    print("Query parameters:")
    for param, value in query_params.items():
        print(f"{param}: {value}")
    return {"message": "GET request received"}

@app.post("/")
async def post_handler(request: Request):
    payload = await request.json()
    print("Received POST request")
    print("Payload:")
    print(payload)
    return {"message": "POST request received"}
