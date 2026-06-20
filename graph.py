from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from agents.supervisor import supervisor
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from agents.writer_agent import writer_agent
from agents.chat_agent import chat_agent


class AgentState(TypedDict):
    question: str
    route: str
    research: str
    summary: str
    report: str
    answer: str

# ------------------
# Supervisor Node
# ------------------

def supervisor_node(state):

    route = supervisor(
        state["question"]
    )

    print("\nROUTE:", route)

    return {
        "route": route
    }
# ------------------
# Research Node
# ------------------

def research_node(state):

    result = research_agent(
        state["question"]
    )

    return {
        "research": result
    }


# ------------------
# Summary Node
# ------------------

def summary_node(state):

    result = summarizer_agent(
        state["research"]
    )

    return {
        "summary": result
    }


# ------------------
# Writer Node
# ------------------

def writer_node(state):

    result = writer_agent(
        state["summary"]
    )

    return {
        "report": result
    }
#-------------------------
# Chat_Node
#-------------------------    
    
    
def chat_node(state):

    result = chat_agent(
        state["question"]
    )

    return {
        "answer": result
    }
#----------------------------------
def router(state):
    return state["route"]


graph = StateGraph(AgentState)

graph.add_node(
    "supervisor",
    supervisor_node
)

graph.add_node(
    "research",
    research_node
)

graph.add_node(
    "summary",
    summary_node
)

graph.add_node(
    "writer",
    writer_node
)

graph.add_node(
    "chat",
    chat_node
)

graph.set_entry_point(
    "supervisor"
)

graph.add_conditional_edges(
    "supervisor",
    router,
    {
        "research": "research",
        "summary": "summary",
        "writer": "writer",
        "chat": "chat"
    }
)

graph.add_edge(
    "research",
    "summary"
)

graph.add_edge(
    "summary",
    "writer"
)

graph.add_edge(
    "writer",
    END
)

graph.add_edge(
    "chat",
    END
)

workflow = graph.compile()