
name = "Andrii"
print(__name__)

def foo(a, b):
    return a+b

if __name__ == "__main__":  # ранить __name__ == "__main__", коли викликається з середини файла
    print(foo(10,4))