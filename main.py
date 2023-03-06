from Hanoi import hanoi
from algoritmos import a_estrela, dijkstra, dfs

print("Torre de Hanoi\n")
problema = hanoi.Hanoi(3,5)
result_dfs = dfs.dfs(problema)
result_djikstra = dijkstra.dijkstra(problema)
result_a_estrela = a_estrela.a_estrela(problema)
print(f"\ndfs -> {result_dfs}")
print(f"Dijkstra -> {result_djikstra}")
print(f"A_Estrela -> {result_a_estrela}")