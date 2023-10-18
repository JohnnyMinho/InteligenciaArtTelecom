import math

import queue
from Node import node
import matplotlib.pyplot as plt
import networkx as nx #biblioteca de tratamento de grafos para desenhar grafos
import networkx


#definição da class grafo:
#Um grafo tem uma lista de nodos,
#um dicionario: nome_nodo -> lista de tuplos (nome_nodo, peso)
#para representar as arestas
#uma flag para indicar se é direcionado ou nao

class Graph:
    # Construtor da classe
    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed #se o grafo é direcionado ou nao
        self.m_graph = {}   #   dicionario para armazenar os nodos, arestas e pesos
        self.m_heuristica = {} #Euristica

    ##############################
    # Escrever o grafo com string
    ##############################
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node " + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    
    #############################
    # encontrar nodo pelo nome
    #############################

    def get_node_by_name(self,name):
        search_node = node(name)
        for nodo in self.m_nodes:
            if nodo == search_node:
                return nodo
            else:
                return None
            
    #############################
    # Adicionar Aresta + Nodo
    ############################

    def add_edge(self,Node1,Node2, custo):
        n2 = node(Node2)
        n1 = node(Node1)
        if(Node1 not in self.m_nodes):
            n1_id = len(self.m_nodes)
            n1.setId(n1_id)
            self.m_nodes.append(Node1)
            self.m_graph[Node1] = []
        else:
            n1 = self.get_node_by_name(Node1)
        if(Node2 not in self.m_nodes):
            n2_id = len(self.m_nodes)
            n2.setId(n2_id)
            self.m_nodes.append(Node2)
            self.m_graph[Node2] = []
        else:
            n2 = self.get_node_by_name(Node2)
        self.m_graph[Node1].append((Node2 , custo))
        #self.m_graph[Node2].append((Node2 , custo))

    ############################
    # Imprime as arestas 
    ############################

    def imprime_arestas(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2,custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + '->' + nodo2 + " custo:"+str(custo) + "\n"
        return listaA
    
    ##########################
    #
    ##########################

    def getNodes(self):
        return self.m_nodes
    
    def get_arc_cost(self,Node1,Node2):
        custoT = math.inf
        a = self.m_graph[Node1]
        for (nodo,custo) in a:
            if nodo == Node2:
                custoT = custo
            else:
                custoT = 0
                print("A aresta não existe")
        return custoT

    def calcula_custo(self,caminho):
        #caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i +1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i],teste[i+1])
            i = i + 1
        return custo

    #Devolve todos os nodes adjacente aos Node em questão
    def get_neighbours(self,Node1):
        temp = {}
        for (adjacente,custo) in self.m_nodes:
            if adjacente == Node1:
                temp[adjacente] = [custo, self.getH(self,Node1)]
        return temp

    def desenha(self):
        # criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = node(nodo)
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[nodo]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ###########################
    # Algoritmos de procura não informada
    ###########################

    def procura_DFS(self,start,end,path=[],visited=set()):
        path.append(start)
        visited.add(start)
        if start == end:
            custoT = self.calcula_custo(path)
            return (path,custoT)
        for (adjacente,peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente,end,path,visited)
                if resultado is not None:
                    return resultado
        path.pop() #Se não encontrar remove o que está no caminho
        return None
    
    def Procurar_BFS(self,start,end):
        visited = set()
        path = []
        fila = queue.Queue()
        custo = 0

        fila.put(start)
        visited.add(start)

        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente,peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            #function to calculate the cost of the path
            custo = self.calcula_custo(path)
            return path
            
        return None
    
    ###########################
    # Algoritmos de procura informada
    ###########################

    def Procura_Gulosa(self, start, end,path=[]):
        path = []
        available_options = {}
        custo_max = 0
        final_decision = ""
        for (adjacente,custo) in self.m_graph[start]:
            print(adjacente)
            if(adjacente == end):
                path.append(adjacente)
                return path
            elif(adjacente not in path):
                available_options[adjacente] = self.m_heuristica[adjacente]
        for heuristica,option in available_options,available_options.keys():
            if heuristica > custo_max:
                final_decision = option
        path.append(final_decision)
        resultado = self.Procura_Gulosa(self,final_decision,end,path)
        if(resultado is not None):
            return resultado
             
        return None
    
    #############
    #Heuristica
    ###############
    def add_heuristica(self,Node,estima):
        n1 = node(Node)
        if(Node in self.m_nodes):
            #print("Hello")
            self.m_heuristica[Node] = estima

    #Devolve o valor da heuristica para um dado node
    def getH(self,node):
        for(Nodo,custo) in self.m_heuristica:
            if(Nodo == node):
                return custo

    #Imprime a lista de heuristica
    #Devolve o valor da heuristica para um dado node
    def printH(self):
        for(Nodo,custo) in self.m_heuristica:
            print("Nodo:"+Nodo+" Heuristica:"+custo)

    #
    def heuristica(self):
        nodes = self.m_graph.keys()
        for nodo in nodes:
            self.m_heuristica = 1 #define a heuristica para cada nodo como 1, aramazenando essa informação em um dicionário chamado self.heuristica

        return True