from datetime import datetime
from functools import wraps

# ex1
def time(func):
     def wraper(*args, **kwargs):
            start = datetime.now()
            func(*args, **kwargs)
            print(datetime.now() - start)
     return wraper

@time
def func1():
    for i in range(3000):
        print(i)

func1()
# ex2

cache= {}
def cachedec(func):
    def wraper(*args, **kwargs):
        if args[0] in cache:
            print(f"{args[0]} כבר היתה הרצה על: ")
            return cache[args[0]]
        else:
            result=func(*args, **kwargs)
            cache.update({args[0]:result})
            return result
    return wraper

@cachedec
@time
def FibonacciWithCache(x):
    if x == 0:
        return [0]
    result = [0, 1]
    if x == 1:
        return result
    prev1 = 0
    prev2 = 1
    for i in range(1, x):
        temp = prev2
        prev2 = prev1 + prev2
        prev1 = temp
        result.append(prev2)
    return result

@time
def Fibonacci(x):
    if x==0:
        return [0]
    result=[0,1]
    if x==1:
        return result
    prev1=0
    prev2=1
    for i in range(1,x):
        temp=prev2
        prev2=prev1+prev2
        prev1=temp
        result.append(prev2)
    return result

FibonacciWithCache(20000)
Fibonacci(20000)
# חזרה על הרצת הפונקציה על אותו ארגומנט
print("the time with cache:")
print(FibonacciWithCache(20000))
print("the time without cache:")
print(Fibonacci(20000))

