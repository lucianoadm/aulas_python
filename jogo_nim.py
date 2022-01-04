print("Para entrar no jogo Digite NIM()")

def NIM():
        nim = 0
        teste = 1
        print()
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print()
        while (teste == 1):
                print()
                nim = int(input("Digite 1 para uma Partida e 2 para um Campeonato: "))
                if (nim == 1):
                        print()
                        print ("Você escolheu uma Partida!")
                        print()
                        teste = 2
                        partida()
                elif (nim == 2):
                        print()
                        print ("Você escolheu um Campeonato!")
                        print()
                        teste = 2
                        campeonato()
                else:
                        print()
                        print ("Opss... Opçãos inválida!!! Tente novamente.")
        



def usuario_escolhe_jogada (restantes, limite, j):
        
        while (j<=0 or j > limite or j>restantes):
                print("Oops! Jogada inválida! Tente de novo.")
                print()
                j = int(input("Quantas peças você vai tirar? "))
        restantes = restantes - j

        if (restantes <= limite):
                jogada_pc = restantes
                print()
                print("O computador retirou",restantes,",peças.")
                print("Fim do jogo! O computador ganhou!")
        else:
                jogada_pc = limite       
                print()
                print("Você retirou,", j,"peças.")
                print("Agora restam,", restantes,"peças no tabuleiro.")
                print()
                computador_escolhe_jogada(restantes, limite, jogada_pc)
        


def computador_escolhe_jogada(restantes, limite, jogada_pc):
        while (restantes%(limite + 1)!= jogada_pc):
                
                jogada_pc = jogada_pc - 1
        if (jogada_pc ==0):
                jogada_pc = 1
        elif (restantes <= limite):
                jogada_pc = restantes
                print()
                print("O computador retirou",restantes,",peças.")
                print("Fim do jogo! O computador ganhou!")
                print()
        else:                        
                restantes = restantes - jogada_pc
                print()
                print("O computador retirou,", jogada_pc,"peças.")
                print("Agora restam,", restantes,"peças no tabuleiro.")
                print()
                j = int(input("Quantas peças você vai tirar? "))
                usuario_escolhe_jogada (restantes, limite, j)

        
        
def partida():
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        restantes = n
        limite = m
        if ((n%(m+1))==0):
                print()
                print("Você começa!!!")
                print()
                j = int(input("Quantas peças você vai tirar? "))
                usuario_escolhe_jogada (restantes, limite, j)
        else:
                print()
                print("Computador começa!")
                print()
                jogada_pc = limite
                restantes = n
                computador_escolhe_jogada(restantes, limite, jogada_pc)


def campeonato():
        rodada = 0
        while (rodada < 3):
                rodada = rodada + 1
                print()
                print("**** Rodada",rodada,"° Rodada ****")
                print()
                n = int(input("Quantas peças? "))
                m = int(input("Limite de peças por jogada? "))
                restantes = n
                limite = m
                if ((n%(m+1))==0):
                        print()
                        print("Você começa!!!")
                        print()
                        j = int(input("Quantas peças você vai tirar? "))
                        usuario_escolhe_jogada (restantes, limite, j)
                else:
                        print()
                        print("Computador começa!")
                        print()
                        jogada_pc = limite
                        restantes = n
                        computador_escolhe_jogada(restantes, limite, jogada_pc)
        print()
        print("Placar: Você 0 X 3 Computador")
