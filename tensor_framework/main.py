# tensor_framework/main.py
import sympy as sp

def calculate_tensor_expression(expression):
    """
    Calculate and simplify a given tensor expression.

    Parameters:
    expression (str): A string representation of the tensor expression.

    Returns:
    str: The simplified tensor expression or an error message.
    """
    try:
        # Parse the string expression to a SymPy expression
        expr = sp.sympify(expression)
        
        # Simplify the SymPy expression
        simplified_expr = sp.simplify(expr)
        
        # Return the simplified expression as a string
        return str(simplified_expr)
    except Exception as e:
        # Return an error message in case of an exception
        return f"Error: {e}"

if __name__ == '__main__':
    # For testing purposes, you can uncomment the following lines:
    expression = "2*x + 3*x"
    result = calculate_tensor_expression(expression)
    print(f"Simplified Expression: {result}")

