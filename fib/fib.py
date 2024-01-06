import argparse

def fib(n):
    """Function returning the nth Fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    parser = argparse.ArgumentParser(description='Calculate nth Fibonacci number.')
    parser.add_argument('n', type=int, help='The index of the Fibonacci sequence to calculate')

    args = parser.parse_args()

    print(fib(args.n))

if __name__ == "__main__":
    main()