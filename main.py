import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QFileDialog, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class ModelicaRunner(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(int)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            )

            for line in process.stdout:
                self.output_signal.emit(line.strip())

            process.stdout.close()
            return_code = process.wait()
            self.finished_signal.emit(return_code)

        except Exception as e:
            self.error_signal.emit(str(e))

class ModelicaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('OpenModelica Runner')
        self.setGeometry(300, 300, 600, 350)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Path Layout
        path_layout = QHBoxLayout()
        self.exe_path = QLineEdit()
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self.browse_exe)
        path_layout.addWidget(QLabel("Modelica Executable:"))
        path_layout.addWidget(self.exe_path)
        path_layout.addWidget(browse_btn)

        # Time Inputs
        self.start_time = QLineEdit()
        self.stop_time = QLineEdit()

        # Console Output
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        
        # Run Button
        run_btn = QPushButton("Run Simulation")
        run_btn.clicked.connect(self.run_simulation)

        # Add to layout
        layout.addLayout(path_layout)
        layout.addWidget(QLabel("Start Time (s):"))
        layout.addWidget(self.start_time)
        layout.addWidget(QLabel("Stop Time (s):"))
        layout.addWidget(self.stop_time)
        layout.addWidget(self.console)
        layout.addWidget(run_btn)
        
    def browse_exe(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(
            self, "Select Modelica Executable", "",
            "Executable Files (*.exe);;All Files (*)", options=options
        )
        if file:
            self.exe_path.setText(file)
            
    def validate_inputs(self):
        if not os.path.isfile(self.exe_path.text()):
            QMessageBox.critical(self, "Error", "Invalid executable path")
            return False
        try:
            float(self.start_time.text())
            float(self.stop_time.text())
            return True
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid time values (must be numbers)")
            return False
            
    def run_simulation(self):
        if not self.validate_inputs():
            return
            
        exe_path = self.exe_path.text()
        start = self.start_time.text()
        stop = self.stop_time.text()
        
        command = [
            exe_path,
            f"-override=startTime={start},stopTime={stop}"
        ]
        
        self.console.append(f"Starting simulation...\nCommand: {' '.join(command)}")

        # Run in a separate thread
        self.runner_thread = ModelicaRunner(command)
        self.runner_thread.output_signal.connect(self.console.append)
        self.runner_thread.error_signal.connect(lambda e: QMessageBox.critical(self, "Error", f"Execution failed: {e}"))
        self.runner_thread.finished_signal.connect(self.on_simulation_finished)
        self.runner_thread.start()

    def on_simulation_finished(self, return_code):
        if return_code == 0:
            QMessageBox.information(self, "Success", "Simulation completed successfully")
        else:
            QMessageBox.critical(self, "Error", f"Simulation failed with code {return_code}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelicaApp()
    window.show()
    sys.exit(app.exec_())
