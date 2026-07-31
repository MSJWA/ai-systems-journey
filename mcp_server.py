from mcp.server.fastmcp.server import FastMCP
import sqlite3

mcp = FastMCP("user-lookup-server")

@mcp.tool()
def find_user(name: str) -> dict:
    """Looks up a user's information by their name."""
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    connection.close()
    if result:
        return {"id": result[0], "name": result[1], "age": result[2]}
    return {"error": f"No user found with name {name}"}

if __name__ == "__main__":
    mcp.run()