from tools.pdf_reader import pdf_reader_tool

result = pdf_reader_tool(
    "data/sample.pdf"
)

print(result[:1000])