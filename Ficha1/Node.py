class node:
    #   construtor do nodo...
    def __init__(self, name):
        self.m_name = str(name)
        #Posteriormente colocar o objeto que o nodo vai referenciar...

    #Devolve a representação na forma de string do modo por forma a ser de leitura 'amigavel'
    def __str__(self):
        return "node " + self.m_name

    #Devolve representação 'oficial' do objeto, neste caso particular pode ser igual a __str__
    def __repr__(self):
        return "node " + self.m_name

    #obter o nome de um nodo
    def getName(self):
        return self.m_name

    #Atualizar o nome de um nodo
    def setName(self, name):
        self.m_name = name

    #Metodo utilizado para comparar dois nodos,
    #neste caso dois nodos sao iguais se os nomes forem iguais
    def __eq__(self, other):
        # sao iguais se nomes iguais, nao usa o id
        return self.m_name == other.m_name

    #Devolve o hash de um nodo. Ao implementar o metodo __eq__
    #torna-se tambem necessário definir __hash__. Caso
    #contrário o objeto torna-se unhashable
    def __hash__(self):
        return hash(self.m_name)