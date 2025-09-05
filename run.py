from src.api.api import app
import uvicorn
from fastmcp import FastMCP

mcp = FastMCP.from_fastapi(app=app)
# app.mount("/mcp", mcp.http_app())

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)    
