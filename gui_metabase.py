import sys
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import subprocess
import time

mainPath = r"Z:/Metabase"
command = 'java -jar metabase.jar'
run = subprocess.Popen('start cmd /k '+ command,cwd=mainPath,shell=True)

time.sleep(20)

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl("http://localhost:3000"))
web.show()

sys.exit(app.exec())
