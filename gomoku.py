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
    pass


def esta_limitada(tabuleiro, y_fim, x_fim, comprimento, d_y, d_x):
    pass


def detecta_linha(tabuleiro, cor, y_ini, x_ini, comprimento, d_y, d_x):
    # mude-me
    return qtd_seq_aberta, qtd_seq_semiaberta


def detecta_linhas(tabuleiro, cor, comprimento):
    # mude-me
    qtd_seq_aberta, qtd_seq_semiaberta = 0, 0
    return qtd_seq_aberta, qtd_seq_semiaberta


def busca_max(tabuleiro):
    # mude-me
    return movimento_y, movimento_x


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
    pass


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
    x = 5; y = 1; d_x = 0; d_y = 1; comprimento = 3
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
    x = 5; y = 1; d_x = 0; d_y = 1; comprimento = 3
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)
    if detecta_linha(tabuleiro, "b", 0, x, comprimento, d_y, d_x) == (1, 0):
        print("CASO DE TESTE P/ detecta_linha PASSOU")
    else:
        print("CASO DE TESTE P/ detecta_linha FALHOU")


def teste_detecta_linhas():
    tabuleiro = limpa_tabuleiro(8)
    x = 5; y = 1; d_x = 0; d_y = 1; comprimento = 3;
    cor = 'b'
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, "b")
    imprime_tabuleiro(tabuleiro)
    if detecta_linhas(tabuleiro, cor, comprimento) == (1, 0):
        print("CASO DE TESTE P/ detecta_linhas PASSOU")
    else:
        print("CASO DE TESTE P/ detecta_linhas FALHOU")


def teste_busca_max():
    tabuleiro = limpa_tabuleiro(8)
    x = 5; y = 0; d_x = 0; d_y = 1; comprimento = 4; cor = 'b'
    por_seq_no_tabuleiro(tabuleiro, y, x, d_y, d_x, comprimento, cor)
    x = 6; y = 0; d_x = 0; d_y = 1; comprimento = 4; cor = 'p'
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
    y = 5; x = 2; d_x = 0; d_y = 1; comprimento = 3
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

    y = 3; x = 5; d_x = -1; d_y = 1;
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

    y = 5; x = 3; d_x = -1; d_y = 1;
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