import sys
from PyQt6.QtWidgets import QApplication
from app import TheRightPriceApp

def main():
    app = QApplication(sys.argv)
    window = TheRightPriceApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()