from collections import defaultdict

# Criação da Classe Graph() que será utilizada 
class Graph():

    # Criação de um dict() para trabalhar com a relação entre arestas através do graph e criação de um set() para atribuição das arestas do grafo.
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    # Atribuição da relação entre arestas com direcionamento saindo do vértice de origem em direção ao destino.
    def adicionaArco_Saida(self, origem, destino):
        self.graph[origem].append(destino)
        self.nodes.add(origem)
        self.nodes.add(destino)

    # Atribuição de relação entre arestas com direcionamento que chegam na origem.
    def adicionaArco_Entrada(self, origem, destino):
        self.graph[destino].append(origem)
        self.nodes.add(origem)
        self.nodes.add(destino)

    def __str__(self):
        return_str = ''
        for node in self.graph:
            return_str += f"{node} recebe {self.graph[node]}\n"
        return return_str

    def __getitem__(self, key):
        return self.graph[key]

    def contador(self):
        count = 1
        for i in self.nodes:
            count += 1
        return count


if __name__ == "__main__":
    g = Graph()

    # Exemplo: Slide 64 do contéudo disciplinar.
    # (origem,destino)

    g.adicionaArco_Entrada(2, 1)
    g.adicionaArco_Entrada(5, 1)

    g.adicionaArco_Entrada(1, 2)
    g.adicionaArco_Entrada(3, 2)
    g.adicionaArco_Entrada(4, 2)

    g.adicionaArco_Entrada(1, 3)
    g.adicionaArco_Entrada(2, 3)
    g.adicionaArco_Entrada(5, 3)

    g.adicionaArco_Entrada(1, 4)
    g.adicionaArco_Entrada(3, 4)
    
    g.adicionaArco_Entrada(2, 5)
    g.adicionaArco_Entrada(3, 5)
    g.adicionaArco_Entrada(4, 5)
    
    grafo = g.__str__()
    print(grafo)

    numero_vertices = g.contador()
    
    for x in range(1,numero_vertices):
        grau = len(g.__getitem__(x))
        print(f"O grau de entrada do vertice {x} resulta em {grau}.")    
