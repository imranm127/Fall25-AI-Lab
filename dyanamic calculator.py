import re

def dynamic_calculator(expr: str) -> float:
    # Replace special operators with Python equivalents
    expr = expr.replace("×", "*").replace("÷", "/")
    
    # Handle implicit multiplication: e.g. "2(3+4)" → "2*(3+4)"
    expr = re.sub(r'(\d)\(', r'\1*(', expr)
    expr = re.sub(r'\)(\d)', r')*\1', expr)

    try:
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error: {e}"

# Interactive calculator loop
print(" Dynamic Calculator (type 'exit' to quit)")
while True:
    expression = input("\nEnter expression: ")
    if expression.lower() == "exit":
        print("Goodbye")
        break
    print("Result:", dynamic_calculator(expression))
