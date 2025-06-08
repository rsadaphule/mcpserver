from mcp.server.fastmcp import FastMCP

# create an MCP Server
mcp = FastMCP("Demo MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two numbers together and return the sum """
    return a + b

@mcp.resource("greeing://{name}")
def greeting(name: str) -> str:
    """ Return a greeting to the user """
    return f"Hello, {name}!"




def main():
    print("Hello from mcpserver!")


if __name__ == "__main__":
    main()
