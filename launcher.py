import sys
from PySide6.QtWidgets import (
    QFileDialog, QApplication, QMainWindow, QTextEdit,
    QPushButton, QVBoxLayout, QWidget, QLabel
)

from PySide6.QtCore import QThread

from core.bootstrap import boot_system
from core.logger import log
from services.document_loader import DocumentLoader
from services.qdrant_service import QdrantService 
from PySide6.QtCore import QObject, Signal, Slot

class AIWorker(QObject):
    finished = Signal(str)

    def __init__(self, services, question):
        super().__init__()
        self.services = services
        self.question = question

    @Slot()
    def run(self):
        qdrant = self.services["qdrant"]
        ai = self.services["ai"]

        context_items = qdrant.search(self.question)
        context = "\n".join([str(i) for i in context_items])

        answer = ai.ask(self.question, context)
        self.finished.emit(answer)

class MainWindow(QMainWindow):

    def __init__(self, services):
        super().__init__()

        self.services = services
        self.loader = DocumentLoader()

        # Qdrant client
        self.qdrant = services ["qdrant"]

        self.setWindowTitle("Law Firm OS v11 - AI Interface")
        self.setGeometry(200, 200, 900, 600)

        self.label = QLabel("AI Legal Assistant (Local Mode)")

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText(
            "Ask a question about your documents..."
        )

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.ask_btn = QPushButton("Ask AI")
        self.ingest_btn = QPushButton("Ingest Text")
        self.motion_btn = QPushButton("Generate Motion Outline")
        self.file_btn = QPushButton("Import PDF")

        # Connect buttons
        self.ask_btn.clicked.connect(self.ask_ai)
        self.ingest_btn.clicked.connect(self.ingest_text)
        self.motion_btn.clicked.connect(self.generate_motion)
        self.file_btn.clicked.connect(self.load_file)

        # Layout (FIXED: layout must be created BEFORE adding widgets)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.ingest_btn)
        layout.addWidget(self.ask_btn)
        layout.addWidget(self.motion_btn)
        layout.addWidget(self.file_btn)
        layout.addWidget(self.output_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # -----------------------------
    # METHODS INSIDE THE CLASS
    # -----------------------------

    def ingest_text(self):
        text = self.input_box.toPlainText()
        doc_id = f"doc_{len(text)}"

        self.services["ingestion"].ingest_text(doc_id, text)
        self.output_box.append("[INGESTED DOCUMENT]")

    def ask_ai(self):
        question = self.input_box.toPlainText()

        self.output_box.append("\n[Thinking…]\n")

        self.thread = QThread()
        self.worker = AIWorker(self.services, question)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_ai_result)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

        # Show immediate feedback
        self.output_box.append("\n[Thinking…]\n")

        # Create thread + worker
        self.thread = QThread()
        self.worker = AIWorker(self.services, question)
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_ai_result)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Start background work
        self.thread.start()

    def on_ai_result(self, answer):
        self.output_box.append("\n=== AI RESPONSE ===\n")
        self.output_box.append(answer)
        self.output_box.append("\n")

    def generate_motion(self):
        text = self.input_box.toPlainText()

        draft = self.services["drafting"].generate_motion_outline(
            motion_type="summary judgment motion",
            facts=text,
            law="Celotex, Anderson, Matsushita standards apply"
        )

        self.output_box.append("\n--- MOTION OUTLINE ---\n")
        self.output_box.append(draft)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF File",
            "",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        text = self.loader.load_pdf(path)
        self.services["ingestion"].ingest_file_text(path, text)

        self.output_box.append(f"[IMPORTED PDF] {path}")


def main():
    ok, services = boot_system()

    if not ok:
        print("Boot failed")
        return

    app = QApplication(sys.argv)
    window = MainWindow(services)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

