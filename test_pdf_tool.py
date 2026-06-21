import register_tools

from mcp_client import execute_tool

result = execute_tool(
    "pdf_reader",
    "data/sample.pdf"
)

print(type(result))
print(result[:1000])