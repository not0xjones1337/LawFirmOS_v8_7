from search import search
from llm import run_llm
from export import export_docx, export_pdf

def build_prompt(context, motion_type):

    return f"""
You are drafting a federal court motion: {motion_type}

Use ONLY the facts below:

{context}

Structure:
1. Introduction
2. Statement of Facts
3. Legal Standard
4. Argument
5. Conclusion
"""


def draft_motion(case_id, motion_type):
    context = search(case_id, motion_type)
    prompt = build_prompt(context, motion_type)
    return run_llm(prompt)


def export_motion(case_id, motion_type, text):

    docx_path = f"exports/{case_id}_{motion_type}.docx"
    pdf_path = f"exports/{case_id}_{motion_type}.pdf"

    export_docx(motion_type, [{"heading": "Motion", "text": text}], docx_path)
    export_pdf(motion_type, [{"heading": "Motion", "text": text}], pdf_path)

    return {"docx": docx_path, "pdf": pdf_path}