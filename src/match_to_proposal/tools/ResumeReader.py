# pdf_to_md_tool.py
import pdfplumber
from markdownify import markdownify as md
from crewai_tools.tools.base_tool import BaseTool 
import os

def convert_pdf_to_md(pdf_path):
                # Extract text from the PDF
        extracted_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n\n"

                # Convert extracted text to Markdown format
        markdown_text = md(extracted_text)

                # Save as Markdown file
        md_path = os.path.splitext(pdf_path)[0] + '.md'  # Output file with the same name but .md extension
        with open(md_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)

        return md_path



# class ResumeReaderTool(BaseTool):

#     def convert_pdf_to_md(pdf_path):
#                 # Extract text from the PDF
#         extracted_text = ""
#         with pdfplumber.open(pdf_path) as pdf:
#             for page in pdf.pages:
#                 extracted_text += page.extract_text() + "\n\n"

#                 # Convert extracted text to Markdown format
#         markdown_text = md(extracted_text)

#                 # Save as Markdown file
#         md_path = os.path.splitext(pdf_path)[0] + '.md'  # Output file with the same name but .md extension
#         with open(md_path, 'w', encoding='utf-8') as md_file:
#             md_file.write(markdown_text)

#         return md_path

