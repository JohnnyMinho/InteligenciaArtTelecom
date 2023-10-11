#Ficha2

import sys
from Grafo import Graph 

#DFS


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
        #results = DFS(DestinyNode,StartNode,None,0,None,None,None) #Usar inicio, fim Path e Visited só
        results = Graph.procura_DFS(g,StartNode,DestinyNode)
        print("Caminhos Possiveís:")
        print(results)
    elif(ArgOption == "2"):
        #BFS
        #print(BFS(DestinyNode,StartNode))
        results = Graph.procura_BFS(g,StartNode,DestinyNode)

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