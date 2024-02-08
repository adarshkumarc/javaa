def example_function():
    x = 10  # Local variable
    print(x)

example_function()
# print(x)  # This would result in an error since x is not defined in this scope
global_var = 30  # Global variable

def print_global():
    print(global_var)

def modify_global():
    global global_var
    global_var += 5

print_global()
modify_global()
print_global()
