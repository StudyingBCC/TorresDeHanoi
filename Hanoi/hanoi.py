from no import No

class Hanoi():
  # Estamos inicializando o array, são vazios, pois só sabemos que a quantidade de torrestem que ser >= 3 e não a quantidade exata
  estado_Inicial =  []
  estado_Final = []

  def __init__(self, numTorres, numDiscos):
    #Aqui estamos setando o espaço de torres nos arrays, começando do 1
    for i in range(1, numTorres + 1):
      self.estado_Inicial.append([])
      self.estado_Final.append([])

    #Aqui estamos setando o numero de discos que temos
    torre = list(range(1, numDiscos + 1))
    
    #Colocando do menor para o maior, pois na torre de hanoi os maiores ficam em baixo
    torre.sort(reverse = True)
    
  #Setando como vai estar as torres no momento inicial e no final
    self.estado_Inicial[0] = torre
    self.estado_Final[-1] = torre

  #sub-listas em tuplas
    for i in range(len(self.estado_Inicial)):
      self.estado_Inicial[i] = tuple(self.estado_Inicial[i])
      self.estado_Final[i] = tuple(self.estado_Final[i])
      
  #A função cria o primeiro nó da árvore de busca (a raiz) com base no estado inicial do problema, no custo atual e no valor heurístico, como foi pedido o custo é sempre 1
  def iniciar(self):
        self.raiz = No(estado = self.estado_Inicial, custo = 1, heuristica = self.heuristica())
        return self.raiz

  #Heuristica -> técnica utilizada para resolver problemas de maneira aproximada, rápida ou simplificada, sem garantir que a solução encontrada seja a melhor ou a ótima
  def heuristica(self, no: No = None):
    #estado inicial do problema
    if no == None:
      return 0
      
    #retorna o numero de discos  da ultima torre   
    return -len(no.estado[-1])

  def mover_disco(self, origem, destino, no: No):
    #estado atual dos movimentos
    estado_Atual = []

    #Estamos movendo os discos, o último disco da torre de origem é removido e adicionado à torre de destino
    for torre in no.estado:
      estado_Atual.append(list(torre))
    disco = estado_Atual[origem].pop()
    estado_Atual[destino].append(disco)

    return No(estado = self.em_tuple(estado_Atual), no_pai = no, custo = 1, heuristica = self.heuristica())


  #Gerar todos os estados sucessores possíveis para o nó atual, aplicando todas as ações possíveis a partir desse nó e verificando se o estado resultante é válido.
  def gerar_sucessores(self, no: No):
      estado = no.estado
      sucessores = [] 
      expansoes = [list(torre) for torre in estado]
      for origem in range(len(expansoes)):
        for destino in range(len(expansoes)):
            if destino != origem and len(expansoes[origem]) > 0:
              sucessor = self.mover_disco(origem, destino, no)
              if self.validando_estado(sucessor):
                sucessores.append(sucessor)
                print(f"Expansoes de origem: {expansoes[origem]} - origem: ({origem}) -> Expansoes de destino: {expansoes[destino]} - destino: ({destino})")
      return sucessores

  # verifica se o estado desse nó é válido, ou seja, se as regras do problema das Torres de Hanói estão sendo seguidas.
  def validando_estado(self, no: No):
    for torre in no.estado:
      torre = list(torre)
      aux = list.copy(torre)
      aux.sort(reverse = True)
      if torre != aux:
        return False
    return True

  # transforma o array em tupla
  def em_tuple(self, lista):
    aux = []
    for item in lista:
      aux.append(tuple(item))
    return aux

  # É necessário a função de custo para ser usado no a_estrela
  def custo(self, no: No, destino: No):
    return 1

  #Verifica se o objetivo está alcançado
  def testar_objetivo(self, no: No):
    return no.estado == self.estado_Final
