from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()

# Define your expected API key (in production, store this in Vercel Environment Variables)
API_KEY = "my_secret_api_key_123"
API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials / Invalid API Key"
        )

@app.get("/")
def public_route():
    return {"message": "This is a public endpoint. No API key needed."}

@app.get("/secure-data")
def protected_route(api_key: str = Security(get_api_key)):
    return {"message": "Success! You accessed a secure endpoint using a valid API key."}
