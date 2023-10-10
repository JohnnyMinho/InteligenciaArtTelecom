#Ficha1
#Definimos o grafo a ser utilizado através de 2 dicionários. Um para indicar os arcos de cada node e um para indicar as informações de cada arco.

import sys
from Grafo import Graph 

#DFS

def DFS(Destiny,Start,Current_Path,current_cost,Total_Paths,Position,Visited):
    #Solução, escolher um dos caminhos e tentar chegar à "bruta" ao destino.
    cost = current_cost
    current_node = Position
    Visited_Nodes = Visited
    if(Position == None):
        current_node = Start
    else:
        current_cost = Position
    if(Visited == None):
        Visited_Nodes = []
    Path = Current_Path
    if(Total_Paths == None):
        Total_Paths = {}
    if(Current_Path == None):
        Path = []
        Path.append(current_node)
    options = graph.get(current_node)
    for option in options:
        if(option not in Path and Destiny not in Path):
            if(option not in Visited_Nodes):
                cost += graph.get(current_node,{}).get(option)
                Path.append(option)
                if(option != str(Start)):
                    Visited_Nodes.append(option)
                DFS(Destiny,Start,Path,cost,Total_Paths,option,Visited_Nodes)
        if(Destiny in Path and tuple(Path) not in Total_Paths):
            Total_Paths.update({tuple(Path): cost})
            temp_path = list(reversed(Path))
            for Node in temp_path:
                if(Node in Visited_Nodes):
                    Path.pop()
            Visited_Nodes.remove(Destiny)
            cost = 0
    return Total_Paths

#BFS

def BFS(Destiny,Start,Queue):
    current_queue = Queue
    if(Queue == None):
        current_queue = []
    options = graph.get()

    return 0

def main():
    #Definição de grafo
    g = Graph()

    g.add_edge("s","a",2)
    g.add_edge("s","e",2)
    g.add_edge("a","b",2)
    g.add_edge("e","f",5)
    g.add_edge("b","c",2)
    g.add_edge("f","g",2)
    g.add_edge("c","d",3)
    g.add_edge("g","t",2)
    g.add_edge("d","t",3)

    ArgOption = sys.argv[1] #Valor numérico, 1-> DFS, 2-> BFS
    DestinyNode = sys.argv[2] #Indica o destino.
    StartNode = sys.argv[3] #Indica o estado inicial
    if(ArgOption == "1"):
        #DFS
        results = DFS(DestinyNode,StartNode,None,0,None,None,None) #Usar inicio, fim Path e Visited só
        print("Caminhos Possiveís:")
        print(results)
    elif(ArgOption == "2"):
        #BFS
        print(BFS(DestinyNode,StartNode))
    elif(ArgOption == "3"):
        #Imprimir Grafo
        print(g.m_graph)
    elif(ArgOption == "4"):
        #Desenhar Grafo
        g.desenha()
    elif(ArgOption == "5"):
        #Imprimir nodos de Grafo
        print(g.m_graph.keys())
    elif(ArgOption == "6"):
        #Imprimir arestas de GRafo
        print(g.imprime_aresta())

if __name__ == "__main__":
    main()