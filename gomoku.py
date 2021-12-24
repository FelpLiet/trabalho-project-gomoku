"""Gomoku código inicial
Você deveria completar cada função incompleta e adcionar
mais funções e variáveis de acordo com sua necessidade.

Note que algumas funções incompletas tem 'pass' como seu primeiro comando:
pass é uma palavra chame em python que indica para o computador fazer nada.
Isso indica o lugar onde deve estar a sua implementação. Remova o pass
quando a fizer.

Outras funções tem "mude-me".
"""


def esta_vazia(tabuleiro):
    '''Retorna True caso o tabuleiro esteja vazio'''
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] != " ":
                return False
    return True


def esta_cheia(tabuleiro):
    """Retorna True ou False dependendo se o tabuleiro esta cheio de peças ou não"""

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                return False
    return True


def esta_limitada(tabuleiro, y_fim, x_fim, comprimento, d_y, d_x):
    """Restorna se a sequencia esta aberta, fechada ou semiaberta de acordo com a posicao dela"""

    estado_incial = ""
    estado_final = ""

    # checa de y_fim e x_fim sao coodenadas validas
    if (max(y_fim, x_fim) >= len(tabuleiro)) or (min(y_fim, x_fim) < 0):
        return "FECHADA"

    # verifica o fim adjacente a y_fim e x_fim
    if (min(y_fim + d_y, x_fim + d_x) < 0) or (max(y_fim + d_y, x_fim + d_x) >= len(tabuleiro)):
        estado_final = "FECHADA"
    elif tabuleiro[y_fim + d_y][x_fim + d_x] == " ":
        estado_final = "ABERTA"
    else:
        estado_final = "FECHADA"

    # verifica o fianl oposto a y_fim e x_fim
    if (min(y_fim - (d_y * comprimento), x_fim - (d_x * comprimento)) < 0) or (
            max(y_fim - (d_y * comprimento), x_fim - (d_x * comprimento)) >= len(tabuleiro)):
        estado_incial = "FECHADA"
    elif tabuleiro[y_fim - (d_y * comprimento)][x_fim - (d_x * comprimento)] == " ":
        estado_incial = "ABERTA"
    else:
        estado_incial = "FECHADA"

    # analiza o estado em que se encontra
    if estado_final != estado_incial:
        return "SEMIABERTA"
    elif estado_incial == "ABERTA" and estado_final == "ABERTA":
        return "ABERTA"
    else:
        return "FECHADA"


def verifica_comprimento(tabuleiro, cor, y_ini, x_ini, d_y, d_x):
    """Retorna um comprimento inteiro que é o comprimento da sequência da coluna de cores,
       começando em y_início, x_início e procedendo na direção d_y, d_x."""

    y = y_ini
    x = x_ini
    comprimento = 1

    if tabuleiro[y_ini][x_ini] != cor:
        return 0

    for i in range(len(tabuleiro)):
        if (max(y + d_y, x + d_x) >= len(tabuleiro)) or (min(y + d_y, x + d_x) < 0) or tabuleiro[y + d_y][
            x + d_x] != cor:
            return comprimento
        comprimento += 1
        y += d_y
        x += d_x


def detecta_linha(tabuleiro, cor, y_ini, x_ini, comprimento, d_y, d_x):
    """ Retorna uma tupla do número de sequências ABERTAS e SEMIABERTAS de coluna de cor e comprimento de
        comprimento na linha começando em y_ini, x_ini e continuando na direção d_y, d_x."""

    qtd_seq_semiaberta = 0
    qtd_seq_aberta = 0
    comprimento_atual = 0

    for i in range(len(tabuleiro) + 1):
        if y_ini + d_y > len(tabuleiro) or x_ini + d_x > len(tabuleiro) or y_ini + d_y < 0 or x_ini + d_x < 0:
            return qtd_seq_aberta, qtd_seq_semiaberta
        elif tabuleiro[y_ini][x_ini] == cor:
            comprimento_atual = verifica_comprimento(tabuleiro, cor, y_ini, x_ini, d_y, d_x)
            if comprimento == comprimento_atual:
                estado = esta_limitada(tabuleiro, y_ini + ((comprimento - 1) * d_y), x_ini + ((comprimento - 1) * d_x),
                                       comprimento, d_y, d_x)
                if estado == "ABERTA":
                    qtd_seq_aberta += 1
                if estado == "SEMIABERTA":
                    qtd_seq_semiaberta += 1

                y_ini += (comprimento - 1) * d_y
                x_ini += (comprimento - 1) * d_x
            else:
                y_ini += (comprimento_atual - 1) * d_y
                x_ini += (comprimento_atual - 1) * d_x

        y_ini += d_y
        x_ini += d_x


def detecta_linha_vence(tabuleiro, cor, y_ini, x_ini, comprimento, d_y, d_x):
    """Retorna verdadeiro ou falso dependendo se as sequências de cor e comprimento 5 na linha começando em
       y_start, x_start e procedendo na direção d_y, d_x."""
    
    comprimento_atual = 0
    resultado = False

    for i in range(len(tabuleiro) + 1):
        if y_ini + d_y > len(tabuleiro) or x_ini + d_x > len(tabuleiro) or y_ini + d_y < 0 or x_ini + d_x < 0:
            return resultado
        elif tabuleiro[y_ini][x_ini] == cor:
            comprimento_atual = verifica_comprimento(tabuleiro, cor, y_ini, x_ini, d_y, d_x)
            if comprimento == comprimento_atual:
                resultado = True
            else:
                y_ini += (comprimento_atual - 1) * d_y
                x_ini += (comprimento_atual - 1) * d_x
        y_ini += d_y
        x_ini += d_x


def detecta_linhas(tabuleiro, cor, comprimento):
    """Retorne uma tupla do número de sequências abertas e semiabertas de cores e comprimentos no tabuleiro."""
    
    qtd_seq_aberta = 0
    qtd_seq_semiaberta = 0

    # teste de linhas
    for linha in range(len(tabuleiro)):
        quantidade_tuplas = detecta_linha(tabuleiro, cor, linha, 0, comprimento, 0, 1)
        qtd_seq_aberta += quantidade_tuplas[0]
        qtd_seq_semiaberta += quantidade_tuplas[1]

    # teste de colunas
    for coluna in range(len(tabuleiro)):
        quantidade_tuplas = detecta_linha(tabuleiro, cor, 0, coluna, comprimento, 1, 0)
        qtd_seq_aberta += quantidade_tuplas[0]
        qtd_seq_semiaberta += quantidade_tuplas[1]

    # teste de diagonais
    for diagonal in range(len(tabuleiro) - 1):
        for direcao in (1, -1):
            quantidade_tuplas = detecta_linha(tabuleiro, cor, 0, diagonal, comprimento, 1, direcao)
            qtd_seq_aberta += quantidade_tuplas[0]
            qtd_seq_semiaberta += quantidade_tuplas[1]

            quantidade_tuplas = detecta_linha(tabuleiro, cor, len(tabuleiro) - 1, diagonal, comprimento, -1, direcao)
            qtd_seq_aberta += quantidade_tuplas[0]
            qtd_seq_semiaberta += quantidade_tuplas[1]

    return qtd_seq_aberta, qtd_seq_semiaberta


def detecta_linhas_vence(tabuleiro, cor):
    """Retorna False ou True se a sequencia de cores e o comprimento for 5 na linha 
    e iniciam em y_ini, x_ini indo em direção a d_y, d_x."""
    
    comprimento = 5

    # teste de linhas
    for linha in range(len(tabuleiro)):
        if detecta_linha_vence(tabuleiro, cor, linha, 0, comprimento, 0, 1):
            return True

    # teste de colunas
    for coluna in range(len(tabuleiro)):
        if detecta_linha_vence(tabuleiro, cor, 0, coluna, comprimento, 1, 0):
            return True

    # teste de diagonal
    for diagonal in range(len(tabuleiro) - 1):
        for direcao in (1, -1):
            if detecta_linha_vence(tabuleiro, cor, 0, diagonal, comprimento, 1, direcao):
                return True
            if detecta_linha_vence(tabuleiro, cor, len(tabuleiro) - 1, diagonal, comprimento, -1, direcao):
                return True
    return False


def busca_max(tabuleiro):
    """Retorne as coordenadas, linha, coluna, do melhor movimento que o preto poderia fazer, dado o tabuleiro atual."""

    pontuacao_atual = pontuacao(tabuleiro)
    melhor_movimento = (-1, -1)

    # cria um copia do tabuleiro
    tabuleiro_de_teste = []
    for sublista in tabuleiro:
        tabuleiro_de_teste.append(sublista[:])

    # verifica o moviemto para a peça preta de maior pontuação
    for movimento_y in range(len(tabuleiro_de_teste)):
        for movimento_x in range(len(tabuleiro_de_teste)):
            if tabuleiro_de_teste[movimento_y][movimento_x] != ' ':
                continue
            tabuleiro_de_teste[movimento_y][movimento_x] = 'p'
            pontuacao_nova = pontuacao(tabuleiro_de_teste)
            if pontuacao_nova > pontuacao_atual:
                pontuacao_atual = pontuacao_nova
                melhor_movimento = movimento_y, movimento_x
            tabuleiro_de_teste[movimento_y][movimento_x] = ' '

    if melhor_movimento != (-1, -1):
        return melhor_movimento
    # se nao tiver nenhuma jogada melhor, ele movimentará a peça para a primeira casa vazia
    else:
        for movimento_y in range(len(tabuleiro_de_teste)):
            for movimento_x in range(len(tabuleiro_de_teste)):
                if tabuleiro_de_teste[movimento_y][movimento_x] == ' ':
                    return movimento_y, movimento_x
    pass


def pontuacao(tabuleiro):
    PONTUACAO_MAX = 100000

    pretas_abertas = {}
    pretas_semiabertas = {}
    brancas_abertas = {}
    brancas_semiabertas = {}

    for i in range(2, 6):
        pretas_abertas[i], pretas_semiabertas[i] = detecta_linhas(tabuleiro, "p", i)
        brancas_abertas[i], brancas_semiabertas[i] = detecta_linhas(tabuleiro, "b", i)

    if pretas_abertas[5] >= 1 or pretas_semiabertas[5] >= 1:
        return PONTUACAO_MAX

    elif brancas_abertas[5] >= 1 or brancas_semiabertas[5] >= 1:
        return -PONTUACAO_MAX

    return (-10000 * (brancas_abertas[4] + brancas_semiabertas[4]) +
            500 * pretas_abertas[4] +
            50 * pretas_semiabertas[4] +
            -100 * brancas_abertas[3] +
            -30 * brancas_semiabertas[3] +
            50 * pretas_abertas[3] +
            10 * pretas_semiabertas[3] +
            pretas_abertas[2] + pretas_semiabertas[2] - brancas_abertas[2] - brancas_semiabertas[2])


def e_vitoria(tabuleiro):
    '''retorna o resulta se a partida continua ou se houve um vencedor'''

    if detecta_linhas_vence(tabuleiro, 'p'):
        return "Pretas vencem"
    elif detecta_linhas_vence(tabuleiro, 'b'):
        return "Brancas vencem"
    elif esta_cheia(tabuleiro):
        return "Empate"
    else:
        return "Continue a jogada"


def imprime_tabuleiro(tabuleiro):
    s = "*"
    for i in range(len(tabuleiro[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(tabuleiro[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(tabuleiro)):
        s += str(i % 10)
        for j in range(len(tabuleiro[0]) - 1):
            s += str(tabuleiro[i][j]) + "|"
        s += str(tabuleiro[i][len(tabuleiro[0]) - 1])

        s += "*\n"
    s += (len(tabuleiro[0]) * 2 + 1) * "*"

    print(s)


def limpa_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        tabuleiro.append([" "] * tamanho)
    return tabuleiro


def analise(tabuleiro):
    for c, nome_completo in [["p", "Preto"], ["b", "Branco"]]:
        print("%s pedras" % (nome_completo))
        for i in range(2, 6):
            aberto, semiaberto = detecta_linhas(tabuleiro, c, i);
            print("Linhas abertas de comprimento %d: %d" % (i, aberto))
            print("Linhas semiabertas de comprimento %d: %d" % (i, semiaberto))


def jogar_gomoku(tamanho_tabuleiro):
    tabuleiro = limpa_tabuleiro(tamanho_tabuleiro)
    altura_tabuleiro = len(tabuleiro)
    largura_tabuleiro = len(tabuleiro[0])

    while True:
        imprime_tabuleiro(tabuleiro)
        if esta_vazia(tabuleiro):
            movimento_y = altura_tabuleiro // 2
            movimento_x = largura_tabuleiro // 2
        else:
            movimento_y, movimento_x = busca_max(tabuleiro)

        print("Movimento computador: (%d, %d)" % (movimento_y, movimento_x))
        tabuleiro[movimento_y][movimento_x] = "p"
        imprime_tabuleiro(tabuleiro)
        analise(tabuleiro)

        resultado_jogo = e_vitoria(tabuleiro)
        if resultado_jogo in ["Venceram as brancas", "Venceram as pretas", "Empate"]:
            return resultado_jogo

        print("Seu movimento:")
        movimento_y = int(input("Coord y: "))
        movimento_x = int(input("Coord x: "))
        tabuleiro[movimento_y][movimento_x] = "b"
        imprime_tabuleiro(tabuleiro)
        analise(tabuleiro)

        resultado_jogo = e_vitoria(tabuleiro)
        if resultado_jogo in ["Venceram as brancas", "Venceram as pretas", "Empate"]:
            return resultado_jogo


def por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, cor):
    for i in range(comprimento):
        tabuleiro[y][x] = cor
        y += d_y
        x += d_x


def teste_esta_vazia():
    board = limpa_tabuleiro(8)
    if esta_vazia(board):
        print("CASO DE TESTE P/ esta_vazia PASSOU")
    else:
        print("CASO DE TESTE P/ esta_vazia FALHOU")


def teste_esta_limitada():
    tabuleiro = limpa_tabuleiro(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    comprimento = 3
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)

    y_fim = 3
    x_fim = 5

    if esta_limitada(tabuleiro, y_fim, x_fim, comprimento, d_y, d_x) == 'ABERTA':
        print("CASO DE TESTE P/ esta_limitada PASSOU")
    else:
        print("CASO DE TESTE P/ esta_limitada FALHOU")


def teste_detecta_linha():
    tabuleiro = limpa_tabuleiro(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    comprimento = 3
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)
    if detecta_linha(tabuleiro, "b", 0, x, comprimento, d_y, d_x) == (1, 0):
        print("CASO DE TESTE P/ detecta_linha PASSOU")
    else:
        print("CASO DE TESTE P/ detecta_linha FALHOU")


def teste_detecta_linhas():
    tabuleiro = limpa_tabuleiro(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    comprimento = 3;
    cor = 'b'
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)
    if detecta_linhas(tabuleiro, cor, comprimento) == (1, 0):
        print("CASO DE TESTE P/ detecta_linhas PASSOU")
    else:
        print("CASO DE TESTE P/ detecta_linhas FALHOU")


def teste_busca_max():
    tabuleiro = limpa_tabuleiro(8)
    x = 5;
    y = 0;
    d_x = 0;
    d_y = 1;
    comprimento = 4;
    cor = 'b'
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, cor)
    x = 6;
    y = 0;
    d_x = 0;
    d_y = 1;
    comprimento = 4;
    cor = 'p'
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, cor)
    imprime_tabuleiro(tabuleiro)
    if busca_max(tabuleiro) == (4, 6):
        print("CASO DE TESTE P/ busca_max PASSOU")
    else:
        print("CASO DE TESTE P/ busca_max FALHOU")


def conjunto_testes_faceis_para_main():
    teste_esta_vazia()
    teste_esta_limitada()
    teste_detecta_linha()
    teste_detecta_linhas()
    teste_busca_max()


def alguns_testes():
    tabuleiro = limpa_tabuleiro(8)

    tabuleiro[0][5] = "b"
    tabuleiro[0][6] = "p"
    y = 5;
    x = 2;
    d_x = 0;
    d_y = 1;
    comprimento = 3
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)
    analise(tabuleiro)

    # Saída esperada:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |b|p| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |b| | | | | *
    #       6 | |b| | | | | *
    #       7 | |b| | | | | *
    #       *****************
    #       Pedras pretas:
    #       Linhas abertas de comprimento 2: 0
    #       Linhas semiabertas de comprimento 2: 0
    #       Linhas abertas de comprimento 3: 0
    #       Linhas semiabertas de comprimento 3: 0
    #       Linhas abertas de comprimento 4: 0
    #       Linhas semiabertas de comprimento 4: 0
    #       Linhas abertas de comprimento 5: 0
    #       Linhas semiabertas de comprimento 5: 0
    #       Pedras brancas:
    #       Linhas abertas de comprimento 2: 0
    #       Linhas semiabertas de comprimento 2: 0
    #       Linhas abertas de comprimento 3: 0
    #       Linhas semiabertas de comprimento 3: 1
    #       Linhas abertas de comprimento 4: 0
    #       Linhas semiabertas de comprimento 4: 0
    #       Linhas abertas de comprimento 5: 0
    #       Linhas semiabertas de comprimento 5: 0

    y = 3;
    x = 5;
    d_x = -1;
    d_y = 1;
    comprimento = 2

    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "p")
    imprime_tabuleiro(tabuleiro)
    analise(tabuleiro)

    # Saída esperada:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |b|p| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |p| | *
    #        4 | | | |p| | | *
    #        5 | |b| | | | | *
    #        6 | |b| | | | | *
    #        7 | |b| | | | | *
    #        *****************
    #
    #         Pedras pretas:
    #         Linhas abertas de comprimento 2: 1
    #         Linhas semiabertas de comprimento 2: 0
    #         Linhas abertas de comprimento 3: 0
    #         Linhas semiabertas de comprimento 3: 0
    #         Linhas abertas de comprimento 4: 0
    #         Linhas semiabertas de comprimento 4: 0
    #         Linhas abertas de comprimento 5: 0
    #         Linhas semiabertas de comprimento 5: 0
    #         Pedras brancas:
    #         Linhas abertas de comprimento 2: 0
    #         Linhas semiabertas de comprimento 2: 0
    #         Linhas abertas de comprimento 3: 0
    #         Linhas semiabertas de comprimento 3: 1
    #         Linhas abertas de comprimento 4: 0
    #         Linhas semiabertas de comprimento 4: 0
    #         Linhas abertas de comprimento 5: 0
    #         Linhas semiabertas de comprimento 5: 0
    #

    y = 5;
    x = 3;
    d_x = -1;
    d_y = 1;
    comprimento = 1
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "p");
    imprime_tabuleiro(tabuleiro);
    analise(tabuleiro);

    #        Saída esperada:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |b|p| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |p| | *
    #           4 | | | |p| | | *
    #           5 | |b|p| | | | *
    #           6 | |b| | | | | *
    #           7 | |b| | | | | *
    #           *****************
    #
    #
    #        Pedras pretas:
    #        Linhas abertas de comprimento 2: 0
    #        Linhas semiabertas de comprimento 2: 0
    #        Linhas abertas de comprimento 3: 0
    #        Linhas semiabertas de comprimento 3: 1
    #        Linhas abertas de comprimento 4: 0
    #        Linhas semiabertas de comprimento 4: 0
    #        Linhas abertas de comprimento 5: 0
    #        Linhas semiabertas de comprimento 5: 0
    #        Pedras brancas:
    #        Linhas abertas de comprimento 2: 0
    #        Linhas semiabertas de comprimento 2: 0
    #        Linhas abertas de comprimento 3: 0
    #        Linhas semiabertas de comprimento 3: 1
    #        Linhas abertas de comprimento 4: 0
    #        Linhas semiabertas de comprimento 4: 0
    #        Linhas abertas de comprimento 5: 0
    #        Linhas semiabertas de comprimento 5: 0


if __name__ == '__main__':
    jogar_gomoku(8)
