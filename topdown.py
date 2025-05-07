import random
import sys
sys.setrecursionlimit(10**6)

def top_down(prices):
    n = len(prices)
    dp = [[-1] * n for _ in range(n)]
    order = [0] * n  # Ordem de venda dos vinhos
    
    # Função recursiva com memoização
    def compute(i, j, year):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        sell_left = prices[i] * year + compute(i + 1, j, year + 1)
        sell_right = prices[j] * year + compute(i, j - 1, year + 1)
        
        dp[i][j] = max(sell_left, sell_right)
        return dp[i][j]
    
    # Reconstrução da ordem de vendas
    def reconstruct_order():
        i, j = 0, n - 1
        year = 1
        while i <= j:
            if i == j:
                order[i] = year
                break
            left = prices[i] * year + dp[i + 1][j]
            right = prices[j] * year + dp[i][j - 1]
            if left >= right:
                order[i] = year
                i += 1
            else:
                order[j] = year
                j -= 1
            year += 1

    max_profit = compute(0, n - 1, 1)
    reconstruct_order()
    return dp, order, max_profit

# Uso: python3 topdown.py <menor-valor> <maior-valor> <quantidade-de-itens>
if __name__ == "__main__":
    n = int(sys.argv[3])
    prices = [random.randint(int(sys.argv[1]), int(sys.argv[2])) for _ in range(n)]

    print("Preços gerados:", prices)

    dp, order, max_profit = top_down(prices)

    print("Tabela de lucros:")
    for row in dp:
        print(row)

    print("Ordem de vendas:", order)
    print("Lucro máximo:", max_profit)
