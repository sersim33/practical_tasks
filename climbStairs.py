
def climbStairs(n):
    # n = int(input("Enter the number of steps (an integer between 1 and 45): "))
    if n < 1 or n > 45:
        print("Number of steps must be between 1 and 45.")
        return
    
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[-1]

print(climbStairs(56))
