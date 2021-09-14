from collections import defaultdict

# Criação da Classe Graph() que será utilizada 
class Graph():

    # Criação de um dict() para trabalhar com a relação entre arestas através do graph e criação de um set() para atribuição das arestas do grafo.
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    # Atribuição da relação entre arestas ao defaultdict() 'graph' e adição ao set() 'nodes' das arestas(como é um set, não há repetição). Serão usados os parâmetros de origem e destino.
    def adicionaArco(self, origem, destino):
        self.graph[origem].append(destino)
        self.nodes.add(origem)
        self.nodes.add(destino)

    # Adição das relações de arestas e sua vice-versa (graças a simetria do não direcionamento)
    def adicionaAresta(self, origem, destino):
        self.graph[origem].append(destino)
        self.graph[destino].append(origem)
        self.nodes.add(origem)
        self.nodes.add(destino)

    # Print do grafo
    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} -> {self.graph[node]}\n"
        return return_str

    # Busca da relação de uma dupla de arestas especifíca através a chave 'key'
    def __getitem__(self, key):
        return self.graph[key]

    # Acumulador para obter o número de vértices
    def contador(self):
        count = 0
        for i in self.nodes:
            count += 1
        return count


if __name__ == "__main__":
    g = Graph()

    g.adicionaAresta(0, 3)
    g.adicionaAresta(1, 2)
    g.adicionaAresta(1, 6)
    g.adicionaAresta(1, 5)
    g.adicionaAresta(1, 4)
    g.adicionaAresta(3, 6)
    g.adicionaAresta(3, 4)
    g.adicionaAresta(4, 6)
    g.adicionaAresta(4, 5)
    
    grafo = g.__str__()
    print(grafo)

    numero_arestas = g.contador()

    for x in range(numero_arestas):
        grau = len(g.__getitem__(x))
        print(f"O grau do vertice {x} resulta em {grau}.")
