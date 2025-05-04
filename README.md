Vamos escolher um problema menos comum, porém ainda simples e didático: **Maximizar o Lucro na Venda de Vinhos com Envelhecimento**. Esse problema é realista, envolve tomada de decisão sequencial e ilustra bem a aplicação de programação dinâmica (PD) em cenários com estados multidimensionais. 

---

### **Problema: Venda Ótima de Vinhos**

**Enunciado:**  
Você tem `N` vinhos alinhados em uma prateleira. O preço do `i`-ésimo vinho é `p[i]`. A cada ano, você pode vender **apenas o vinho mais à esquerda ou mais à direita**. No ano `y` (começando em 1), o preço de um vinho vendido será `y * p[i]`. Qual é o lucro máximo possível após vender todos os vinhos?

**Exemplo:**  
- Vinhos: `[1, 4, 2, 3]`  
- Solução ótima: Vender na ordem `1º, 4º, 3º, 2º` → Lucro = \(1*1 + 2*3 + 3*2 + 4*4 = 1 + 6 + 6 + 16 = 29\).

---

### **Solução com Programação Dinâmica**

#### **1. Definição do Estado**
Defina `dp[i][j]` como o lucro máximo obtido ao vender os vinhos da posição `i` até `j` (inclusive), considerando o ano atual `y`.  
- `i`: Índice do vinho mais à esquerda disponível.  
- `j`: Índice do vinho mais à direita disponível.  
- `y = N - (j - i)`: O ano é calculado com base no número de vinhos já vendidos .

#### **2. Recorrência**
A cada passo, decidimos vender o vinho da esquerda ou da direita:  
- **Vender da esquerda:** Lucro = `y * p[i] + dp[i+1][j]`  
- **Vender da direita:** Lucro = `y * p[j] + dp[i][j-1]`  
- **Equação:**  
  `dp[i][j] = max(y * p[i] + dp[i+1][j], y * p[j] + dp[i][j-1])`

#### **3. Caso Base**
Se `i == j`, só resta um vinho:  
`dp[i][j] = y * p[i]` (onde `y = N`, pois é o último ano).

#### **4. Implementação (Bottom-Up)**
```python
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
```

---

### **Análise de Complexidade**
- **Tempo:** \(O(N^2)\) – Preenchemos uma tabela \(N \times N\).  
- **Espaço:** \(O(N^2)\) – Armazenamos a tabela `dp`.

---

### **Vantagens deste Problema**
1. **Aplicação Prática:** Simula decisões sequenciais com impacto cumulativo (como investimentos ou vendas com valorização temporal).  
2. **Estado Multidimensional:** Ensina a trabalhar com PD em duas dimensões (`i` e `j`), útil para problemas como subsequências ou intervalos.  
3. **Menos Comum:** Não é tão explorado quanto o problema do troco ou da mochila, mas mantém a simplicidade conceitual .

---

### **Alternativa Simplificada: Número de Combinações com 1, 3 e 4**
Se preferir algo ainda mais rápido de implementar, um problema clássico menos óbvio é **calcular o número de maneiras de somar um valor `N` usando 1, 3 e 4**. Por exemplo, para \(N=5\), há 6 combinações:  
- \(1+1+1+1+1\), \(1+4\), \(4+1\), \(1+1+3\), \(1+3+1\), \(3+1+1\).  

**Recorrência:**  
\[ dp[n] = dp[n-1] + dp[n-3] + dp[n-4] \]  
**Implementação:**  
```python
def count_combinations(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = 2
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[n]

print(count_combinations(5))  # Saída: 6
```  
**Complexidade:** \(O(N)\) .

---

Ambos os problemas são excelentes para demonstrar PD, com abordagens distintas (multidimensional vs. linear) e aplicações variadas. O dos vinhos é ideal para aprofundar em otimização de decisões, enquanto o das combinações é ótimo para introduzir recorrências criativas.