# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("SimpleDemo")


# Add an addition tool
@mcp.tool()
def custom_add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b + 10


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_custom_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to the MCP server!"
