def criaTabuleiro():
    matriz = []
    matriz.append([' '] * 3)
    matriz.append([' '] * 3)
    matriz.append([' '] * 3)
    return matriz

def haGanhador(tab):
    for i in range(3):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2] and tab[i][0] != ' ':
            return True
        if tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i] and tab[0][i] != ' ':
            return True
    #diagonal principal  
    if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] != ' ':
        return True
    #diagonal secundaria 
    if tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[0][2] != ' ':
        return True

    return False

def temEspaco(tab):
    for i in range(3):
        for j in range(3):
            if tab[i][j] == ' ':
                return True
    return False

def joga(tab, lin, col, jogador):
    if lin < 0 or lin > 2 or col < 0 or col > 2 or tab[lin][col] != ' ':
        return False

    tab[lin][col] = jogador
    return True

def trocaJogador(jogador):
    if jogador == 'X':
        return  'O'
    else:
        return 'X'

def imprime(tab):
    for lin in tab:
        print(lin)

print()
