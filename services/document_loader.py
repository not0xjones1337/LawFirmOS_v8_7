from pypdf import PdfReader
from core.logger import log


class DocumentLoader:

    def load_pdf(self, path):

        try:
            reader = PdfReader(path)
            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            log(f"PDF LOADED: {path}")
            return text

        except Exception as e:
            log(f"PDF ERROR: {path} -> {e}")
            return ""
