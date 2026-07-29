from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import HumanMessage
import sqlite3

@tool
def find_user(name: str) -> dict:
    """Looks up a registered user's stored information by their exact first name.
    Only use this for looking up people who might be in the user database,
    not for general knowledge questions about places, countries, or facts."""
    
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    connection.close()
    if result:
        return {"id": result[0], "name": result[1], "age": result[2]}
    return {"error": f"No user found with name {name}"}

@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

llm = ChatGroq(model="llama-3.3-70b-versatile").bind_tools([find_user, add_numbers])

def call_model(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode([find_user, add_numbers]))
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", lambda state: "tools" if state["messages"][-1].tool_calls else END)
graph.add_edge("tools", "agent")

app = graph.compile()

result = app.invoke({"messages": [HumanMessage(content="Can you find Ali's info?")]})
print(result["messages"][-1].content)

result = app.invoke({"messages": [HumanMessage(content="What is 15 plus 27?")]})
print(result["messages"][-1].content)

result = app.invoke({"messages": [HumanMessage(content="What's the capital of Japan?")]})
print(result["messages"][-1].content)