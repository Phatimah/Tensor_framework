# TensorFramework

TensorFramework is a tool for automated tensor calculation and simplification. This tool provides a graphical user interface (GUI) to input tensor expressions and obtain simplified results.

## Features

- Symbolic tensor algebra operations:
  - Simplification
  - Contraction
  - Addition
  - Multiplication
- Save and load tensor expressions
- Interactive GUI for user input and output

## Installation

### Prerequisites

- Python 3.x
- Git

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Phatimah/Tensor_framework.git
    cd TensorFramework
    ```

2. **Create and activate a virtual environment**:
    - Using `virtualenv`:
      ```bash
      # Linux / macOS
      mkdir ~/virtualenvs
      virtualenv ~/virtualenvs/tensor_env
      source ~/virtualenvs/tensor_env/bin/activate

      # Windows
      mkdir virtualenvs
      python -m venv virtualenvs/tensor_env
      .\virtualenvs\tensor_env\Scripts\activate
      ```
    - Using `venv`:
      ```bash
      # Linux / macOS
      python3 -m venv ~/virtualenvs/tensor_env
      source ~/virtualenvs/tensor_env/bin/activate

      # Windows
      python -m venv virtualenvs/tensor_env
      .\virtualenvs\tensor_env\Scripts\activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python run.py
    ```

## Usage

1. **Enter tensor expressions** in the input area.
2. **Select an operation** from the dropdown menu.
3. **Click "Calculate"** to perform the operation.
4. **View the result** in the output area.
5. **Click "Save"** to save the current tensor expression to a file.
6. **Click "Load"** to load a tensor expression from a file.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

