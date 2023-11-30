## -----------------------------------------------------
#    Projeto: Jogo da Velha
#    Disciplina: Lógica de Programação
#    Participantes:
## -----------------------------------------------------

## ----- Funções do usuário
def criaMatriz():
    mat = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    return mat

def posicaoOcupada(matriz, posicao):
    if(posicao == 1 and matriz[0][0] != 1):
        return True
    elif(posicao == 2 and matriz[0][1] != 2):
        return True
    elif(posicao == 3 and matriz[0][2] != 3):
        return True
    elif(posicao == 4 and matriz[1][0] != 4):
        return True
    elif(posicao == 5 and matriz[1][1] != 5):
        return True
    elif(posicao == 6 and matriz[1][2] != 6):
        return True
    elif(posicao == 7 and matriz[2][0] != 7):
        return True
    elif(posicao == 8 and matriz[2][1] != 8):
        return True
    elif(posicao == 9 and matriz[2][2] != 9):
        return True
    else:
        return False
  

def registraJogada(mat,posicao,jogador):
    if(posicao == 1):
        mat[0][0] = jogador
    elif(posicao == 2):
        mat[0][1] = jogador
    elif(posicao == 3):
        mat[0][2] = jogador
    elif(posicao == 4):
        mat[1][0] = jogador
    elif(posicao == 5):
        mat[1][1] = jogador
    elif(posicao == 6):
        mat[1][2] = jogador
    elif(posicao == 7):
        mat[2][0] = jogador
    elif(posicao == 8):
        mat[2][1] = jogador
    else:
        mat[2][2] = jogador
    return mat
    
    
    
def apresentaMatriz(mat):
    print(mat[0][0], "|", mat[0][1], "|", mat[0][2])
    print("-" * 10)
    print(mat[1][0], "|", mat[1][1], "|", mat[1][2])
    print("-" * 10)
    print(mat[2][0], "|", mat[2][1], "|", mat[2][2])
    return

def trocaJogador(jogador):
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
    return jogador
    
    
def verificaGanhador(mat, jogador):
    linha1 = [mat[0][0],mat[0][1],mat[0][2]]
    linha2 = [mat[1][0],mat[1][1],mat[1][2]]
    linha3 = [mat[2][0],mat[2][1],mat[2][2]]
    coluna1 = [mat[0][1],mat[1][0],mat[2][0]]
    coluna2 = [mat[0][1],mat[1][1],mat[2][1]]
    coluna3 = [mat[0][2],mat[1][2],mat[2][2]]
    diagonal1 = [mat[0][0],mat[1][1],mat[2][2]]
    diagonal2 = [mat[0][2],mat[1][1],mat[2][0]]
    x = ["X","X","X"]
    o = ["O","O","O"]
    if linha1 == x or linha2 == x or linha3 == x:
        return True
    elif coluna1 == x or coluna2 == x or coluna3 == x:
        return True
    elif diagonal1 == x or diagonal2 == x:
        return True
    elif linha1 == o or linha2 == o or linha3 == o:
        return True
    elif coluna1 == o or coluna2 == o or coluna3 == o:
        return True
    elif diagonal1 == o or diagonal2 == o:
        return True
    else:
        return False
          
## ----- Final das funções do usuário

## ----- Programa Principal  
print("*** JOGO DA VELHA *** \n")
print("Desafie o seu colega no jogo da velha.\n")
print("Regras: a) O primeiro jogador participará com a letra X e o segundo com a letra O.")
print("        b) Os números de 1 a 9 representam os espaços que estão livres.")
print("            Você só poderá escolher as posições livres.")
print("        c)  O vencedor será o primeiro Jogador a preencher uma linha, uma coluna ou uma diagonal.")

matriz = criaMatriz()        # Cria a Matriz do Jogo
jogador = "X"
c = 0
while c < 9:                      # Controla a quantidade máxima de Jogadas (Nove).
    apresentaMatriz(matriz)
    posicao = int(input(f"(Jogador {jogador}) Informe a posição desejada :"))
    # Verifica se a posição está livre
    if posicaoOcupada(matriz, posicao):
            print("\nVocê não pode escolher uma posição que já está ocupada. Tente novamente")
            continue
    else:
        matriz = registraJogada(matriz,posicao,jogador)
        if verificaGanhador(matriz,jogador) == True:
            print(f"jogador {jogador} ganhou !!!")
            break
        jogador = trocaJogador(jogador)
        c += 1
if verificaGanhador(matriz,jogador) == False:
    print("EMPATOU !!!")
print("Fim de jogo !!!")
## ----- Final do Programa


