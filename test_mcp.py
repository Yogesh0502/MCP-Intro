from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("test_mco")

@mcp.tool()
def hello_mcp(name):
    """
    To check if mcp server is working or not.
    Takes name of user as argument and return a statment
    """
    return f"Hi {name}, I am going to rule this world !!!"

if __name__=="__main__":
    mcp.run(transport="sse")