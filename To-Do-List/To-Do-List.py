import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel('Enter task:')
        self.layout.addWidget(self.label)

        self.task_entry = QLineEdit()
        self.layout.addWidget(self.task_entry)

        self.add_button = QPushButton('Add task')
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.tasks_listbox = QListWidget()
        self.layout.addWidget(self.tasks_listbox)

        self.remove_button = QPushButton('Remove task')
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_entry.text()
        if task:
            self.tasks_listbox.addItem(task)
            self.task_entry.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a task.')

    def remove_task(self):
        selected_task = self.tasks_listbox.currentRow()
        if selected_task != -1:
            self.tasks_listbox.takeItem(selected_task)
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a task to remove.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())