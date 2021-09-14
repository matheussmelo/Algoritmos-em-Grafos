from collections import defaultdict

# A classe Graph utilizado é a mesma para a questão 2.
class Graph():
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def adicionaAdjacencia(self, origem, destino):
        self.graph[origem].append(destino)
        self.nodes.add(origem)
        self.nodes.add(destino)

    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} -> {self.graph[node]}\n"
        return return_str

    def __getitem__(self, key):
        return self.graph[key]
    
    # Função para checar se o grafo é conexo ou desconexo notando se algum valor dos vértices do grafo foi ou não foi visitado.
    def conexao(self,visitados):
        a = 0
        for vertex in self.nodes:
            if vertex not in visitados:
                a += 1
        if a != 0:
            print("O grafo nao-direcionado correspondente eh desconexo.")
        else:
            print("O grafo nao-direcionado correspondente eh conexo.")


# Função bfs utilizada baseada nos slides sobre Busca em Largura (slides 90 a 92).
def bfs(g, node):
    visitados = []
    fila = []
    fila.append(node)
    visitados.append(node)
    while len(fila) > 0:
        n = fila[0]
        fila.pop(0)
        for adjacente in sorted(g[n], reverse=False):
            if adjacente not in visitados:
                visitados.append(adjacente)
                if adjacente not in fila:
                    fila.append(adjacente)
    return visitados


if __name__ == "__main__":
    g = Graph()

    g.adicionaAdjacencia(0, 3), g.adicionaAdjacencia(3, 0)
    g.adicionaAdjacencia(0, 4), g.adicionaAdjacencia(4, 0)
    g.adicionaAdjacencia(0, 5), g.adicionaAdjacencia(5, 0)

    g.adicionaAdjacencia(1, 2), g.adicionaAdjacencia(2, 1)
    g.adicionaAdjacencia(1, 3), g.adicionaAdjacencia(3, 1)
    g.adicionaAdjacencia(1, 4), g.adicionaAdjacencia(4, 1)


    grafo = g.__str__()
    print(grafo)

    visit = bfs(g, 5) # O segundo argumenta representa o vértice que se pretende começar a percorrer o grafo.
    print(f"Vertices visitados: {visit}")

    g.conexao(visit)
