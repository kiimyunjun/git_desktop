def func_defining_func(num1):
    def func(num2):
        return num1*num2
    return func

a = func_defining_func(5)
b = func_defining_func(6)

print(a(10))
print(b(10))