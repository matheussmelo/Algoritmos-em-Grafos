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

    # Print do grafo
    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} -> {self.graph[node]}\n"
        return return_str

    # Função para buscar as relações de uma aresta específica através da chave 'key'.
    def __getitem__(self, key):
        return self.graph[key]

    # Acumulador para saber a quantidade de arestas.
    def contador(self):
        count = 0
        for i in self.nodes:
            count += 1
        return count


if __name__ == "__main__":

    
    g = Graph()

    # Exemplo utilizando um grafo não-direcionado com 7 arestas.

    g.adicionaArco(1, 5)
    g.adicionaArco(5, 1)
    g.adicionaArco(1, 4)
    g.adicionaArco(4, 1)
    g.adicionaArco(1, 2)
    g.adicionaArco(2, 1)
    g.adicionaArco(2, 7)
    g.adicionaArco(7, 2)
    g.adicionaArco(2, 6)
    g.adicionaArco(6, 2)
    g.adicionaArco(2, 3)
    g.adicionaArco(3, 2)

    
    grafo = g.__str__()
    print(grafo)

    numero_arestas = g.contador()

    for x in range(1,numero_arestas):
        grau = len(g.__getitem__(x))
        print(f"O grau da aresta {x} resulta em {grau}.")    

