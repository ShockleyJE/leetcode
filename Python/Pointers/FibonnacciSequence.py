#https://leetcode.com/problems/fibonacci-number/

def fib(self, n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1

    numbers = [0,1,]
    # calc first number
    for i in range(2,n):
        numbers.append(numbers[-1] + numbers[-2])

    return numbers[-2] + numbers[-1]
