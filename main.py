def max_profit(prices):
    n = len(prices)
    dp = [[0] * n for _ in range(n)]
    
    for y in range(1, n+1):
        for i in range(n - y + 1):
            j = i + y - 1
            current_year = n - (j - i)
            if i == j:
                dp[i][j] = current_year * prices[i]
            else:
                left = current_year * prices[i] + dp[i+1][j]
                right = current_year * prices[j] + dp[i][j-1]
                dp[i][j] = max(left, right)
    
    return dp[0][n-1]

# Exemplo
print(max_profit([1, 4, 2, 3]))  # Saída: 29