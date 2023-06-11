import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word Counter")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Enter a sentence:", self)
        self.label.setGeometry(50, 50, 200, 30)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 80, 300, 30)

        self.button = QPushButton("Count Words", self)
        self.button.setGeometry(50, 120, 100, 30)
        self.button.clicked.connect(self.count_words)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 160, 300, 30)

    def count_words(self):
        sentence = self.textbox.text()
        word_count = len(sentence.split())
        self.result_label.setText(f"Word count: {word_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())