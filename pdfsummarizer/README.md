## - PyPDF2
- its a free open source python library use to process pdf files
- read,write or manipulate pdfs
## - pdfplumber
is also a python libaray we can use to extarct text,tables or layout deatils from digital PDF files with high precision

## PyPDF2 vs pdfplumber
PyPDF2 is best for file manipulation like splitting and merging, while pdfplumber is best for extracting detailed text, layouts, and tables
## - extracting text
    we can have slectable and scanned images in pdfs will see it in detail alter
## - multiple pages
## - handling empty pages
## - cleaning extracted text


# IN pdfplumber
- open the pdf 
- get the pdf's page numbers using pdf.pages
- extract text from that page number using extract_text()
- extract tables using extract_tables()


# prompt_tokens = system message + your question + conversation history

# Problems we may face with Large PDFs:

- Token limit an LLM may have token limit of 8k or 32k but a pdf can have more token's txt 
- Text length : txt length can be too much for 1 LLM requset

# solution to handle this is:
- chunking means breaking large txt into smaller pieces so that LLM can process those pieces
- chunk size deciding how big each chunk should be (e.g., 1000 per wrds)
- chunk overlap each chunk share the txt with other to avoid losing context
- summarizing each chunk : after splitting txt into chunks we can get summary of each chunk 
- combining summaries :then we can combine summaries in to final summary
- Handling large documents → Managing the full pipeline above smoothly without crashing or losing data.
# What happens if page.extract_text() returns None for a PDF page?
I have not encountered None in my PDF, but if extract_text() returns None, I would need to handle it before concatenating it with extracted_txt.
If extract_text() returns text, add it.
If it returns None, skip that page.