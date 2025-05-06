### **Problema: Venda Ótima de Vinhos**

**Enunciado:**  
Você tem `N` vinhos alinhados em uma prateleira. O preço do `i`-ésimo vinho é `p[i]`. A cada ano, você pode vender **apenas o vinho mais à esquerda ou mais à direita**. No ano `y` (começando em 1), o preço de um vinho vendido será `y * p[i]`. Qual é o lucro máximo possível após vender todos os vinhos?

**Exemplo:**  
- Vinhos: `[1, 4, 2, 3]`  
- Solução ótima: Vender na ordem `1º, 4º, 3º, 2º` → Lucro = \(1*1 + 2*3 + 3*2 + 4*4 = 1 + 6 + 6 + 16 = 29\).

---

#### **4. Implementação (Bottom-Up)**
```python
import random

def profit(prices):
    n = len(prices)
    dp = [[0] * n for _ in range(n)]
    order = [0] * n  # Inicializa a lista de ordem
    
    # Preenche a tabela dp
    for y in range(1, n + 1):
        for i in range(n - y + 1):
            j = i + y - 1
            current_year = n - (j - i)
            
            if i == j:
                dp[i][j] = current_year * prices[i]
            else:
                left = current_year * prices[i] + dp[i + 1][j]
                right = current_year * prices[j] + dp[i][j - 1]
                dp[i][j] = max(left, right)

    # Reconstruir a ordem de venda
    i, j = 0, n - 1
    year = 1
    while i <= j:
        if i == j:
            order[i] = year  # Último vinho restante
            break
        if (prices[i] * year + dp[i + 1][j]) > (prices[j] * year + dp[i][j - 1]):
            order[i] = year
            i += 1
        else:
            order[j] = year
            j -= 1
        year += 1

    return dp, order

if __name__ == "__main__":
    n = 3
    prices = [random.randint(1, 5) for _ in range(n)]
    
    print("Preços gerados: ", prices)
    
    dp, order = profit(prices)

    print("Tabela de lucros: ")
    for row in dp:
        print(row)

    print("Ordem de vendas: ", order)
    print("Lucro máximo: ", dp[0][n-1])
```

---

### **Análise de Complexidade**
- **Tempo:** \(O(N^2)\) – Preenchemos uma tabela \(N \times N\).  
- **Espaço:** \(O(N^2)\) – Armazenamos a tabela `dp`.

---
