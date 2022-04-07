import time

def getTime(n):
    startTime = time.time()*1000
    k = 0
    for i in range(n):
        k = k + 25
    endTime = time.time()*1000
    print("Execution time for n =", n, "is",
        endTime - startTime, "Miliseconds")

def main():
    getTime(10000)
    getTime(100000)
    getTime(1000000)
    getTime(10000000)
    getTime(100000000)
    getTime(1000000000)

main()
