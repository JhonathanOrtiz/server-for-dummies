from fastapi import FastAPI, Request, status, HTTPException
import json


app = FastAPI()

@app.get("/paginator/{p}")
def server_test(p: int, request: Request):
    client_host = request.client.host
    client_forwarded_for = request.headers.get("x-forwarded-for")
    client_user_agent = request.headers.get("user-agent")
    if client_forwarded_for is not None:
        client_data =  {
            'x-forwarded-for': client_forwarded_for,
            "user-argent": client_user_agent
        }
    else:
        client_data = {
            "x-forwarded-for": client_host,
            "user-agent": client_user_agent
        }
    with open("db.json", "r") as f:
        data = json.load(f)
    if data.count(client_data) > 3:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many Requests",
    )
    data.append(client_data)
    with open("db.json", "w") as f:
        json.dump(data, f)
    return p

