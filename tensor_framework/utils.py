# tensor_framework/utils.py
import sympy as sp
import json

def create_tensor(symbols, shape):
    """
    Create a symbolic tensor with the given symbols and shape.

    Parameters:
    symbols (list): A list of symbol names for the tensor.
    shape (tuple): The shape of the tensor (e.g., (2, 2) for a 2x2 matrix).

    Returns:
    sp.MutableDenseNDimArray: The symbolic tensor.
    """
    tensor_symbols = sp.symbols(symbols)
    tensor = sp.MutableDenseNDimArray.zeros(*shape)
    for idx, symbol in enumerate(tensor_symbols):
        tensor[idx] = symbol
    return tensor

def tensor_contraction(tensor, indices):
    """
    Perform contraction of a tensor over the given indices.

    Parameters:
    tensor (sp.MutableDenseNDimArray): The tensor to contract.
    indices (tuple): The indices to contract (e.g., (0, 1) for contraction over the first two indices).

    Returns:
    sp.Expr: The resulting contracted tensor expression.
    """
    return tensor.contract(indices)

def tensor_addition(tensor1, tensor2):
    """
    Add two tensors element-wise.

    Parameters:
    tensor1 (sp.MutableDenseNDimArray): The first tensor.
    tensor2 (sp.MutableDenseNDimArray): The second tensor.

    Returns:
    sp.MutableDenseNDimArray: The resulting tensor after addition.
    """
    return tensor1 + tensor2

def tensor_multiplication(tensor1, tensor2):
    """
    Multiply two tensors element-wise.

    Parameters:
    tensor1 (sp.MutableDenseNDimArray): The first tensor.
    tensor2 (sp.MutableDenseNDimArray): The second tensor.

    Returns:
    sp.MutableDenseNDimArray: The resulting tensor after multiplication.
    """
    return tensor1 * tensor2

def save_expression(expression, filename):
    """
    Save a tensor expression to a file.

    Parameters:
    expression (str): The tensor expression to save.
    filename (str): The file to save the expression in.
    """
    with open(filename, 'w') as file:
        json.dump({'expression': expression}, file)

def load_expression(filename):
    """
    Load a tensor expression from a file.

    Parameters:
    filename (str): The file to load the expression from.

    Returns:
    str: The loaded tensor expression.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['expression']

if __name__ == '__main__':
    # For testing purposes, you can uncomment the following lines:
    tensor1 = create_tensor(['a', 'b', 'c', 'd'], (2, 2))
    tensor2 = create_tensor(['e', 'f', 'g', 'h'], (2, 2))
    contracted_tensor = tensor_contraction(tensor1, (0, 1))
    added_tensor = tensor_addition(tensor1, tensor2)
    multiplied_tensor = tensor_multiplication(tensor1, tensor2)
    print("Contracted Tensor:", contracted_tensor)
    print("Added Tensor:", added_tensor)
    print("Multiplied Tensor:", multiplied_tensor)

    expr = "2*x + 3*x"
    save_expression(expr, 'expression.json')
    loaded_expr = load_expression('expression.json')
    print("Loaded Expression:", loaded_expr)
