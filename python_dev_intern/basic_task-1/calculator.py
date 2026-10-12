def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b else "Cannot divide by zero"

a,b = map(float, input("Enter two numbers: ").split())
op = input("Enter +, -, *, /: ")
print({"+":add, "-":sub, "*":mul, "/":div}.get(op, lambda a,b:"Invalid operation")(a,b))