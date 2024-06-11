# run.py
from tensor_framework.gui import TensorFramework
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TensorFramework()
    ex.show()
    sys.exit(app.exec_())

