"""In fibonacci -------> 1 1 2 3 5 8 13 21
   the first two no is return the same but other no will return with recursive fun
"""
def fibonacci(n:int):
    if n<2:   #this one is a base case
        return n
    return fibonacci(n-2)+fibonacci(n-1) #recursive

if __name__ =="__main__":
    fi = fibonacci(7)
    print("Total fibonacci result: ",fi)
