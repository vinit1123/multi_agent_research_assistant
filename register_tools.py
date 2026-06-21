from tool_registry import register_tool

from tools.calculator import calculator
from tools.web_search import web_search
from tools.weather import weather_tool

from memory_manager import show_all_memories


register_tool(
    "calculator",
    "Perform mathematical calculations",
    calculator,
    takes_input=True
)

register_tool(
    "memory",
    "Retrieve user memories",
    show_all_memories,
    takes_input=False
)

register_tool(
    "web_search",
    "Search information from the internet",
    web_search,
    takes_input=True
)

register_tool(
    "weather",
    "Get weather information",
    weather_tool,
    takes_input=True
)

from tools.pdf_reader import pdf_reader_tool

register_tool(
    "pdf_reader",
    "Read text from PDF files",
    pdf_reader_tool,
    takes_input=True,
    input_type="file"
)

from tools.pdf_search import pdf_search_tool
register_tool(
    "pdf_search",
    "Search information from loaded PDF",
    pdf_search_tool,
    takes_input=True,
    input_type="text"
)