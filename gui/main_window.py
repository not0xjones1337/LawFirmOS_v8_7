import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setWindowTitle("Law Firm OS v9.3")
        self.setGeometry(200, 200, 800, 500)

        label = QLabel("System Initialized", self)
        self.setCentralWidget(label)


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

    self.output.append(f"[IMPORTED PDF] {path}")


def launch_ui(root):
    app = QApplication(sys.argv)
    window = MainWindow(root)
    window.show()
    sys.exit(app.exec())
