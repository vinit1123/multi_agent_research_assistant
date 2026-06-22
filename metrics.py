import json
import os

METRICS_FILE = "agent_metrics.json"


def load_metrics():

    if not os.path.exists(METRICS_FILE):

        return {
            "total_requests": 0,
            "tool_calls": 0,
            "memory_hits": 0,
            "pdf_searches": 0,
            "agent_usage": {},
            "tool_usage": {}
        }

    with open(
        METRICS_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_metrics(metrics):

    with open(
        METRICS_FILE,
        "w"
    ) as f:

        json.dump(
            metrics,
            f,
            indent=4
        )


def increment_request():

    metrics = load_metrics()

    metrics["total_requests"] += 1

    save_metrics(metrics)


def increment_agent(agent):

    metrics = load_metrics()

    metrics["agent_usage"][agent] = (
        metrics["agent_usage"].get(
            agent,
            0
        ) + 1
    )

    save_metrics(metrics)


def increment_tool(tool):

    metrics = load_metrics()

    metrics["tool_calls"] += 1

    metrics["tool_usage"][tool] = (
        metrics["tool_usage"].get(
            tool,
            0
        ) + 1
    )

    save_metrics(metrics)


def increment_memory_hit():

    metrics = load_metrics()

    metrics["memory_hits"] += 1

    save_metrics(metrics)


def increment_pdf_search():

    metrics = load_metrics()

    metrics["pdf_searches"] += 1

    save_metrics(metrics)