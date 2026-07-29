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
    """Looks up a user's information by their name."""
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    connection.close()
    if result:
        return {"id": result[0], "name": result[1], "age": result[2]}
    return {"error": f"No user found with name {name}"}

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

llm = ChatGroq(model="llama-3.3-70b-versatile").bind_tools([find_user])

def call_model(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode([find_user]))
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", lambda state: "tools" if state["messages"][-1].tool_calls else END)
graph.add_edge("tools", "agent")

app = graph.compile()

result = app.invoke({"messages": [HumanMessage(content="Can you find Ali's info?")]})
print(result["messages"][-1].content)