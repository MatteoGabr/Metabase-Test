import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt, QTimer
import subprocess

mainPath = r"Z:/Metabase"
command = 'java -jar metabase.jar'
run = subprocess.Popen(['java', '-jar', 'metabase.jar'], cwd=mainPath, shell=False)

app = QApplication(sys.argv)

label = QLabel('Ciao! Aspetta Metabase!')
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 50px;")
label.showFullScreen()

def switch_to_web():
    label.close()
    web.showFullScreen()

QTimer.singleShot(15000, switch_to_web)

web = QWebEngineView()
web.load(QUrl("http://localhost:3000"))
web.hide()

sys.exit(app.exec())
