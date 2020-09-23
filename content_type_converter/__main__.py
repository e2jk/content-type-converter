import sys

from content_type_converter.content_type_converter import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
