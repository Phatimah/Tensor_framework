# tensor_framework/gui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout, QComboBox, QLabel, QFileDialog
from tensor_framework.main import calculate_tensor_expression
from tensor_framework.utils import create_tensor, tensor_contraction, tensor_addition, tensor_multiplication, save_expression, load_expression

class TensorFramework(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tensor Calculation and Simplification')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        self.input_area = QTextEdit(self)
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)

        self.operation_selector = QComboBox(self)
        self.operation_selector.addItem("Simplify")
        self.operation_selector.addItem("Contract")
        self.operation_selector.addItem("Add")
        self.operation_selector.addItem("Multiply")

        self.calc_button = QPushButton('Calculate', self)
        self.calc_button.clicked.connect(self.calculate)

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_expression)

        self.load_button = QPushButton('Load', self)
        self.load_button.clicked.connect(self.load_expression)

        self.layout.addWidget(QLabel("Input Tensor Expression:", self))
        self.layout.addWidget(self.input_area)
        self.layout.addWidget(QLabel("Operation:", self))
        self.layout.addWidget(self.operation_selector)
        self.layout.addWidget(self.calc_button)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(QLabel("Output:", self))
        self.layout.addWidget(self.output_area)

        self.setCentralWidget(self.central_widget)

    def calculate(self):
        input_text = self.input_area.toPlainText()
        operation = self.operation_selector.currentText()

        if operation == "Simplify":
            result = calculate_tensor_expression(input_text)
        elif operation == "Contract":
            # Example contraction, in practice you'd need indices from user
            tensor = create_tensor(input_text.split(), (2, 2))
            result = str(tensor_contraction(tensor, (0, 1)))
        elif operation == "Add":
            tensors = input_text.split(";")
            tensor1 = create_tensor(tensors[0].split(), (2, 2))
            tensor2 = create_tensor(tensors[1].split(), (2, 2))
            result = str(tensor_addition(tensor1, tensor2))
        elif operation == "Multiply":
            tensors = input_text.split(";")
            tensor1 = create_tensor(tensors[0].split(), (2, 2))
            tensor2 = create_tensor(tensors[1].split(), (2, 2))
            result = str(tensor_multiplication(tensor1, tensor2))
        else:
            result = "Invalid operation"

        self.output_area.setText(result)

    def save_expression(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Expression", "", "JSON Files (*.json);;All Files (*)")
        if filename:
            expression = self.input_area.toPlainText()
            save_expression(expression, filename)

    def load_expression(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Expression", "", "JSON Files (*.json);;All Files (*)")
        if filename:
            expression = load_expression(filename)
            self.input_area.setText(expression)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TensorFramework()
    ex.show()
    sys.exit(app.exec_())
