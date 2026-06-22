from typing import TypedDict

from metrics import (
    increment_agent
)

from langgraph.graph import (
    StateGraph,
    END
)

from agents.supervisor import supervisor
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from agents.writer_agent import writer_agent
from agents.chat_agent import chat_agent
from agents.tool_agent import tool_agent

from guardrails import validate_input


# ------------------
# State
# ------------------

class AgentState(TypedDict):
    question: str
    route: str
    research: str
    summary: str
    report: str
    answer: str
    tool_result: str
    


# ------------------
# Guardrail Node
# ------------------

def guardrail_node(state):

    question = state["question"]

    if not validate_input(question):

        print("\nBLOCKED BY GUARDRAILS")

        return {
            "answer": "Request blocked by guardrails."
        }

    return {
        "answer": "allowed"
    }


# ------------------
# Supervisor Node
# ------------------

def supervisor_node(state):

    increment_agent(
        "supervisor"
    )

    route = supervisor(
        state["question"]
    )

    print("\nROUTE:", route)

    return {
        "route": route
    }

# ------------------
# Tool Node
# ------------------

def tool_node(state):

    increment_agent(
        "tool"
    )

    result = tool_agent(
        state["question"]
    )

    return {
        "answer": result
    }

# ------------------
# Research Node
# ------------------

def research_node(state):

    increment_agent(
        "research"
    )

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

    increment_agent(
        "summary"
    )

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

    increment_agent(
        "writer"
    )

    result = writer_agent(
        state["summary"]
    )

    return {
        "report": result
    }


# ------------------
# Chat Node
# ------------------

def chat_node(state):

    increment_agent(
        "chat"
    )

    result = chat_agent(
        state["question"]
    )

    return {
        "answer": result
    }
# ------------------
# Routers
# ------------------

def guardrail_router(state):

    if state["answer"] == "allowed":
        return "allowed"

    return "blocked"


def router(state):
    return state["route"]


# ------------------
# Graph
# ------------------

graph = StateGraph(
    AgentState
)

graph.add_node(
    "guardrail",
    guardrail_node
)

graph.add_node(
    "supervisor",
    supervisor_node
)

graph.add_node(
    "tool",
    tool_node
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

# ------------------
# Entry Point
# ------------------

graph.set_entry_point(
    "guardrail"
)

# ------------------
# Guardrail Routing
# ------------------

graph.add_conditional_edges(
    "guardrail",
    guardrail_router,
    {
        "allowed": "supervisor",
        "blocked": END
    }
)

# ------------------
# Supervisor Routing
# ------------------

graph.add_conditional_edges(
    "supervisor",
    router,
    {
        "tool": "tool",
        "research": "research",
        "summary": "summary",
        "writer": "writer",
        "chat": "chat"
    }
)

# ------------------
# Research Flow
# ------------------

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

# ------------------
# Tool Flow
# ------------------

graph.add_edge(
    "tool",
    END
)

# ------------------
# Chat Flow
# ------------------

graph.add_edge(
    "chat",
    END
)

# ------------------
# Compile
# ------------------

workflow = graph.compile()