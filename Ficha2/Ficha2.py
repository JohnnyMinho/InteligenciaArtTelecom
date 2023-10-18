#Ficha2

import sys
from Grafo import Graph 

#DFS


def main():
    #Definição de grafo
    g = Graph()

    g.add_edge("elvas", "alandroal", 40)
    g.add_edge("elvas", "arrailos",50)
    g.add_edge("elvas", "borba", 15)
    g.add_edge("alandroal", "redondo", 25)
    g.add_edge("redondo", "monsaraz", 30)
    g.add_edge("barreiro", "palmela", 25)
    g.add_edge("barreiro", "baixaDaBanheira", 5)
    g.add_edge("baixaDaBanheira", "moita", 35)
    g.add_edge("lisboa", "alcochete", 20)
    g.add_edge("lisboa", "vendasNovas", 50)
    g.add_edge("lisboa", "almada", 15)
    g.add_edge("almada", "palmela", 25)
    g.add_edge("palmela", "alcacer", 35)
    g.add_edge("alcacer", "arrailos", 90)
    g.add_edge("vendasNovas", "montemor", 15)
    g.add_edge("montemor", "evora", 40)
    g.add_edge("evora", "estremoz", 40)

    #Heuristica
    g.add_heuristica("elvas",270)
    g.add_heuristica("alandroal",180)
    g.add_heuristica("redondo",170)
    g.add_heuristica("monsaraz",120)
    g.add_heuristica("barreiro",30)
    g.add_heuristica("baixaDaBanheira",33)
    g.add_heuristica("boita",35)
    g.add_heuristica("alcochete",26)
    g.add_heuristica("almada",25)
    g.add_heuristica("vendasNovas",45)
    g.add_heuristica("montemor",70)
    g.add_heuristica("evora",95)
    g.add_heuristica("estremoz",145)
    g.add_heuristica("borba",250)
    g.add_heuristica("arrailos",220)
    g.add_heuristica("alcacer",140)
    g.add_heuristica("lisboa",0)
    g.add_heuristica("evora",95)

    ArgOption = sys.argv[1] #Valor numérico, 1-> DFS, 2-> BFS, 7-> Gulosa, 8-> A*
    #DestinyNode = sys.argv[2] #Indica o destino.
    #StartNode = sys.argv[3] #Indica o estado inicial
    DestinyNode = "lisboa"
    StartNode = "elvas"
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
        print(g.imprime_arestas())
    elif(ArgOption == "7"):
        #Imprimir arestas de GRafo
        print(g.Procura_Gulosa(StartNode,DestinyNode))
    elif(ArgOption == "8"):
        print("Placeholder")
    elif(ArgOption =="9"):
        print(g.m_heuristica)

if __name__ == "__main__":
    main()