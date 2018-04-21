#!/usr/bin/python

def fib1(n):
    a, b = 0, 1
    while(b<n):
        print b
        a, b = b, a+b
print "================="
def fib2(n):
    result = []
    a, b = 0, 1
    while(b<n):
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    print fib1(5)
    print fib2(10)
