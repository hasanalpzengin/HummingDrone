import sys

#recursive
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
        

if __name__ == "__main__":
    #first parameter
    try:
        num = int(sys.argv[1])
        output = fibonacci(num)
        print("Fibonacci {} = {}".format(num ,output))
    except:
        print("Parameter should be integer value")