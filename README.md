# Resolvedor de Sistemas Lineares 2x2

Pequeno programa em Python que resolve sistemas 2x2 usando o método de Cramer.

## Como usar
1. Execute:
   ```bash
   python main.py
   ```
2. Informe duas linhas com `a b p` e `c d q` (ex.: `2 3 13` e `1 -1 -1`).

## Saídas
- **SPD** — Sistema Possível e Determinado (única solução).
- **SPI** — Sistema Possível e Indeterminado (infinitas soluções).
- **SI**  — Sistema Impossível (sem solução).

## Exemplo
Entrada:
```
2 3 13
1 -1 -1
```
Saída esperada:
```
Solução: x = 2.0 e y = 3.0
Sistema Possível e Determinado (SPD)
```

## Tecnologias
- Python 3
