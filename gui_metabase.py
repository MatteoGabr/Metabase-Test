import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import os

os.system(r'Z: && cd Metabase && java -jar metabase.jar')

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl("http://localhost:3000"))
web.show()

sys.exit(app.exec())
