class Solution:
    def fib(self, n: int) -> int:
        # 3 if statements
        # if F(0) return 0
        # if F(1) return 1
        # else do F(n-1) + F(n-2)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)