LETRAS = "ABCDEFGHIJKLMNOPQRS"

"""
TAD INTERSECAO
"""


# Construtor
def cria_intersecao(coluna, linha):
    """
    Cria uma interseção formada por uma linha e uma coluna.

    cria intersecao: str x int → intersecao
    Parâmetros:
    coluna: str
        A letra(A-S) associada à coluna

    linha: int
        O número(1-19) associado à linha.

    Returna:
    intersecao
        A intersecao resultante.
    """
    # Uma intersecao é um tuplo em que o primeiro elemento é uma string que representa a coluna
    # e o segundo elemtento é uma int entre 1 e 19 que representa a linha
    # Criação de interseção caso os inputs dados sejam válidos
    if (
        isinstance(coluna, str)
        and type(linha) == int
        and coluna in LETRAS
        and 1 <= linha <= 19
        and len(coluna) == 1
    ):
        return (coluna, linha)
    raise ValueError("cria_intersecao: argumentos invalidos")


# Seletores
def obtem_col(intersecao):
    """
    Obtém a coluna da interseção.

    obtem col: intersecao → str
    Parâmetros:
    intersecao
        Uma interseção.

    Retorna:
    str
        A coluna da interseção.
    """
    return intersecao[0]


def obtem_lin(intersecao):
    """
    Obtém a linha da interseção.

    obtem lin: intersecao → int
    Parâmetros:
    intersecao
        Uma interseção.

    Retorna:
    int
        A linha da interseção
    """
    return intersecao[1]


# Reconhecedor
def eh_intersecao(intersecao):
    """
    Cria uma interseção com base em uma coluna e uma linha.

    eh intersecao: universal → booleano
    Parâmetros:
    arg:
        Um argumento qualquer

    Retorna:
    bool
        True se o argumento for uma intersecao , False caso contrário
    """
    if (
        isinstance(intersecao, tuple)
        and len(intersecao) == 2
        and isinstance(obtem_col(intersecao), str)
        and type(obtem_lin(intersecao)) == int
        and obtem_col(intersecao) in LETRAS
        and 1 <= obtem_lin(intersecao) <= 19
    ):
        return True
    return False


# Teste
def intersecoes_iguais(intersecao1, intersecao2):
    """
    Verifica se duas interseções são iguais.

    intersecoes iguais: universal x universal → booleano
    Parâmetros:
    intersecao:
        A primeira interseção a ser comparada.

    intersecao:
        A segunda interseção a ser comparada.

    Retorna:
    bool
        True se i1 e i2 são interseções iguais, False caso contrário.
    """
    if (
        eh_intersecao(intersecao1)
        and eh_intersecao(intersecao2)
        and obtem_lin(intersecao1) == obtem_lin(intersecao2)
        and obtem_col(intersecao1) == obtem_col(intersecao2)
    ):
        return True
    return False


# Transformador
def intersecao_para_str(i):
    """
    Converte uma intersecao numa string.

    intersecao para str : intersecao → str
    Parâmetros:
    intersecao:
        A interseção a ser convertida.

    Retorna:
    str
        A representação em string da interseção.
    """
    return f"{obtem_col(i)}{obtem_lin(i)}"


def str_para_intersecao(texto):
    """
    Converte uma string representativa duma intersecao numa intersecao.

    str para intersecao: str → intersecao
    Parâmetros:
    s: str
        A string que representa a intersecao.

    Retorna:
    intersecao:
        A intersecao correspondente.
    """
    return cria_intersecao(texto[0], int(texto[1:]))


# Funções de alto nível
def obtem_intersecoes_adjacentes(intersecao, ultima_intersecao):
    """
    Obtém as interseções adjacentes à interseção i de acordo com a ordem de leitura.

    obtem intersecoes adjacentes: intersecao x intersecao → tuplo
    Parâmetros:
    intersecao:
        A interseção para a qual se desejam obter as interseções adjacentes.

    intersecao:
        A intersecao do canto superior direito(ultima intersecao) tabuleiro de Go.

    Retorna:
    tuple:
        Um tuplo com as interseções adjacentes à interseção primeira intersecao fornecida.
    """
    direcoes, intersecoes_adjacentes = ((0, -1), (-1, 0), (1, 0), (0, 1)), ()

    # procura de intersecoes adjacentes inferiores à última nas suas 4 possíveis posições
    for x, y in direcoes:
        if 1 <= obtem_lin(intersecao) + y <= obtem_lin(
            ultima_intersecao
        ) and "A" <= chr(ord(obtem_col(intersecao)) + x) <= obtem_col(
            ultima_intersecao
        ):
            intersecoes_adjacentes += (
                cria_intersecao(
                    chr(ord(obtem_col(intersecao)) + x), obtem_lin(intersecao) + y
                ),
            )
    return intersecoes_adjacentes


def ordena_intersecoes(intersecoes):
    """
    Ordena um tuplo de interseções de acordo com a ordem de leitura do tabuleiro de Go.

    ordena intersecoes: tuplo → tuplo
    Parâmetros:
    tuplo
        O tuplo de interseções a ser ordenado.

    Retorna:
    tuplo
        O tuplo de interseções ordenado.
    """
    return tuple(
        sorted(
            intersecoes,
            key=lambda intersecao: (obtem_lin(intersecao), obtem_col(intersecao)),
        )
    )


"""
TAD PEDRA
"""


# Construtor
def cria_pedra_branca():
    """
    Cria uma pedra branca

    cria pedra branca: {} → pedra
    Retorna:
    pedra:
        Uma pedra branca
    """
    return "O"


def cria_pedra_preta():
    """
    Cria uma pedra preta

    cria pedra preta: {} 7→ pedra
    Retorna:
    pedra:
        Uma pedra preta
    """
    return "X"


def cria_pedra_neutra():
    """
    Cria uma pedra neutra

    cria pedra neutra: {} → pedra
    Retorna:
    pedra:
        Uma pedra neutra
    """
    return "."


# Reconhecedor
def eh_pedra(pedra):
    """
    Verifica se o argumento é uma pedra

    eh pedra: universal → booleano
    Parâmetros:
    arg:
        Um argumento qualquer

    Retorna:
    bool
        True se o argumento é uma pedra, False caso contrário.
    """
    return pedra in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra())


def eh_pedra_branca(pedra):
    """
    Verifica se o argumento é uma pedra branca

    eh pedra branca: pedra → booleano
    Parâmetros:
    arg:
        Um argumento qualquer

    Retorna:
    bool
        True se o argumento é uma pedra branca, False caso contrário.
    """
    return pedra == cria_pedra_branca()


def eh_pedra_preta(pedra):
    """
    Verifica se o argumento é uma pedra preta

    eh pedra preta: pedra → booleano
    Parâmetros:
    arg:
        Um argumento qualquer

    Retorna:
    bool
        True se o argumento é uma pedra preta, False caso contrário.
    """
    return pedra == cria_pedra_preta()


# Teste
def pedras_iguais(pedra1, pedra2):
    """
    Verifica se dois argumentos são pedras e se são iguais são iguais

    pedras iguais: universal x universal → booleano
    Parâmetros:
    arg:
        Um argumento qualquer
    arg:
        Um argumento qualquer

    Retorna:
    bool
        True se o argumento é uma pedra preta, False caso contrário.
    """
    return (eh_pedra(pedra1) and eh_pedra(pedra2)) and pedra1 == pedra2


# Transformador
def pedra_para_str(pedra):
    """
    Converte uma pedra numa string.

    pedra para str : pedra → str
    Parâmetros:
    pedra:
        A pedra a ser convertida.

    Retorna:
    str
        A representação em string da pedra.
    """
    # Como a predra já é a sua própria representação como string, é necessário realizar alterações
    return pedra


# Funções de alto nível
def eh_pedra_jogador(pedra):
    """
    Verifica se uma pedra pertence a um jogador

    eh pedra jogador : pedra → booleano
    Parâmetros:
    pedra:
        A pedra a ser testada
    Retorna:
    bool
        True se a pedra pertence a um jogador, False caso contrário.
    """
    return eh_pedra_preta(pedra) or eh_pedra_branca(pedra)


"""
TAD GOBAN
"""


# Construtor
def cria_goban_vazio(n):
    """
    Cria um goban vazio com um determinado tamanho(9,13,19).

    cria goban vazio: int → goban
    Parâmetros:
    tamanho: int
        O tamanho do goban (número de linhas/colunas).

    Retorna:
        Um goban vazio de tamanho n
    """
    # Um goban vazio é formado por uma lista formada por n(9,13,19) listas cada uma com n intersecoes
    # vazias
    if n not in (9, 13, 19) or type(n) != int:
        raise ValueError("cria_goban_vazio: argumento invalido")
    return [[cria_pedra_neutra() for x in range(n)] for x in range(n)]


def eh_intersecao_do_goban(tamanho, intersecao):
    """
    Verifica se um argumento é uma intersecão e se pertence a um goban de um tamanho fornecido

    eh_intersecao_do_goban: int x argumento → bool
    Parâmetros:
    int:
        O tamanho do goban
    argumento:
        Um argumento qualquer
    Retorna:
        bool:
            True se o argumento é uma intersecao do goban, False caso contrário.
    """
    if (
        eh_intersecao(intersecao)
        and LETRAS[tamanho - 1] >= obtem_col(intersecao)
        and tamanho >= obtem_lin(intersecao)
    ):
        return True
    return False


def converte_intersecoes(intersecoes):
    """
    Converte tuplos de intersecoes, com intersecoes representadas por strings em tuplos com apenas intersecoes

    converte_intersecoes: tuplo → tuplo
    Parâmetros:
        tuplo:
            Um tuplo de intersecoes e strings representativas de intersecoes
        argumento:
            Um argumento qualquer
        Retorna:
            tuplo:
                Tuplo com apenas intersecoes
    """

    if type(intersecoes) != tuple:
        return intersecoes

    # Caso o elemento do tuplo seja uma string que representa um intersecao, ele será convertida nessa intersecao
    for i in range(len(intersecoes)):
        if (
            type(intersecoes[i]) == str
            and len(intersecoes[i]) >= 2
            and intersecoes[i][0] in LETRAS
            and intersecoes[i][1:].isdigit()
            and 1 <= int(intersecoes[i][1:]) <= 19
        ):
            intersecoes = (
                intersecoes[:i]
                + (str_para_intersecao(intersecoes[i]),)
                + intersecoes[i + 1 :]
            )

    return intersecoes


def cria_goban(n, intersecoes_brancas, intersecoes_pretas):
    """
    Cria um goban de tamanho n x n com interseções ocupadas por pedras brancas e pretas.

    cria goban: int x tuplo x tuplo → goban
    Parâmetros:
        int:
            Tamanho do goban (9, 13 ou 19).
        tuplo:
            Tuplo de interseções ocupadas por pedras brancas.
        tuple:
            Tuplo de interseções ocupadas por pedras pretas.

    Retorna:
        goban:
            Um goban composto pelas pedras nas intersecoes desejadas.
    """
    intersecoes_brancas, intersecoes_pretas = converte_intersecoes(
        intersecoes_brancas
    ), converte_intersecoes(intersecoes_pretas)
    # Verifica se o inteiro fornecido representa um tamanho correto e se as intersecoes
    # fornecidas estão dentro de tuplos
    if (
        n not in (9, 13, 19)
        or type(n) != int
        or type(intersecoes_brancas) != tuple
        or type(intersecoes_pretas) != tuple
    ):
        raise ValueError("cria_goban: argumentos invalidos")
    goban = cria_goban_vazio(n)
    # Verifica se uma intersecao já foi criada e se é uma intersecao válida atraves de uma funcao auxiliar
    # no goban e a adição das respetivas pedras ao goband
    intersecoes_criadas = ()
    for i in intersecoes_brancas:
        if not eh_intersecao_do_goban(len(goban), i) or i in intersecoes_criadas:
            raise ValueError("cria_goban: argumentos invalidos")
        intersecoes_criadas += (i,)
        goban[obtem_lin(i) - 1][LETRAS.find(obtem_col(i))] = cria_pedra_branca()
    for i in intersecoes_pretas:
        if not eh_intersecao_do_goban(len(goban), i) or i in intersecoes_criadas:
            raise ValueError("cria_goban: argumentos invalidos")
        intersecoes_criadas += (i,)
        goban[obtem_lin(i) - 1][LETRAS.find(obtem_col(i))] = cria_pedra_preta()
    return goban


def cria_copia_goban(goban):
    """
    Cria uma cópia dum goban.

    cria copia goban: goban → goban
    Parâmetros:
        goban: O goban a ser copiado.

    Retorna:
        goban: Uma cópia do goban.
    """
    # realiza uma deep copy do goban fornecido
    copia = []
    for coluna in goban:
        col = []
        for elemento in coluna:
            col += [elemento]
        copia += [col]
    return copia


# Seletores
def obtem_ultima_intersecao(goban):
    """
    Obtém a última interseção do goban (canto superior direito).

    obtem ultima intersecao: goban → intersecao
    Parâmetros:
        goban:
            Um goban qualquer.

    Retorna:
        intersecao:
            A interseção correspondente ao canto superior direito.
    """
    return cria_intersecao(LETRAS[len(goban) - 1], len(goban))


def obtem_pedra(goban, intersecao):
    """
    Obtém a pedra na interseção i do goban.

    obtem pedra: goban x intersecao → pedra
    Parâmetros:
        goban:
            O goban.
        intersecao:
            A interseção que se deseja obter a pedra

    Retorna:
        pedra: A pedra na intersecao, ou uma pedra neutra se a posição não estiver ocupada.
    """

    coluna, linha = obtem_col(intersecao), obtem_lin(intersecao)
    if eh_pedra_branca(goban[linha - 1][LETRAS.find(coluna)]):
        return cria_pedra_branca()
    if eh_pedra_preta(goban[linha - 1][LETRAS.find(coluna)]):
        return cria_pedra_preta()
    return cria_pedra_neutra()


def obtem_cadeia(goban, intersecao):
    """
    Obtém as interseções da cadeia que a intersecao pertence

    obtem cadeia: goban x intersecao → tuplo
    Parâmetros:
        goban:
            O goban.
        intersecao:
            A interseção que se deseja obter a cadeia.

    Retorna:
        tuplo:
            Tuplo formado pelas interseções da cadeia em ordem de leitura.
    """
    # tipo de pedra que a cadeia é formada
    tipo = obtem_pedra(goban, intersecao)

    # Função recursiva que obtêm a cadeia de intersecoes, através da procura de interseções
    # do mesmo tipo que a original que sejam adjacentes umas às outras
    def cadeia(goban, intersecao, tipo, res):
        if intersecao in res:
            return res
        res += (intersecao,)
        for i in obtem_intersecoes_adjacentes(
            intersecao, obtem_ultima_intersecao(goban)
        ):
            if pedras_iguais(obtem_pedra(goban, i), tipo):
                res = cadeia(goban, i, tipo, res)
        return res

    return ordena_intersecoes(cadeia(goban, intersecao, tipo, ()))


# Modificadores
def coloca_pedra(goban, intersecao, pedra):
    """
    Coloca uma pedra numa intersecao do goban.

    coloca pedra: goban x intersecao x pedra → goban
    Parâmetros:
        goban:
            O goban.
        intersecao:
            A interseção onde a pedra será colocada.
        pedra:
            A pedra que se deseja colocar.

    Retorna:
        goban: O próprio goban com a pedra modificada.
    """
    goban[obtem_lin(intersecao) - 1][LETRAS.find(obtem_col(intersecao))] = pedra
    return goban


def remove_pedra(goban, intersecao):
    """
    Remove uma pedra numa intersecao do goban.

    remove pedra: goban x intersecao → goban
    Parâmetros:
        goban:
            O goban.
        intersecao:
            A interseção onde a pedra será colocada.
        pedra:
            A pedra que se deseja colocar.
    Retorna:
        goban:
            O próprio goban com a pedra removida.
    """
    goban = coloca_pedra(goban, intersecao, cria_pedra_neutra())
    return goban


def remove_cadeia(goban, intersecoes):
    """
    Remove as pedras nas interseções do tuplo t do goban.

    remove cadeia: goban x tuplo → goban
    Parâmetros:
        goban:
            O goban.
        tuplo:
            O tuplo contendo as interseções da cadeia a ser removida.

    Retorna:
        goban:
            O próprio goban com as pedras removidas
    """
    for intersecao in intersecoes:
        goban = remove_pedra(goban, intersecao)
    return goban


# Reconhecedor
def eh_goban(goban):
    """
    Verifica se o argumento é do tipo goban.

    eh goban: universal → booleano
    Parâmetros:
        argumento:
            Qualquer argumneto

    Retorna:
        bool:
            True se o argumento for do um goban, False caso contrário.
    """
    return (
        isinstance(goban, list)
        and len(goban) in (9, 13, 19)
        and isinstance(goban[0], list)
        and len(goban[0]) in (9, 13, 19)
        and all((type(v) == list and len(goban[0]) == len(v)) for v in goban)
        and all(eh_pedra(elemento) for coluna in goban for elemento in coluna)
    )


def eh_intersecao_valida(goban, intersecao):
    """
    Verifica se uma interseção é válida dentro do goban fornecido.

    eh intersecao valida: goban x intersecao → booleano
    Parâmetros:
        goban:
            O goban.
        intersecao:
            A interseção a ser verificada.

    Retorna:
        bool:
            True se a interseção é válida no goban, False caso contrário.
    """
    # Recurso a uma função auxiliar definida anteriormente
    return eh_intersecao_do_goban(len(goban), intersecao)


# Teste
def gobans_iguais(goban1, goban2):
    """
    Verifica se dois argumentos são gobans e se estes são iguais.

    gobans iguais: universal x universal → booleano

    Parâmetros:
    argumento:
        qualquer argumento
    argumento:
        qualquer argumento

    Retorna:
    bool
        True se as os argumentos são gobans iguais, False caso contrário.
    """
    # verifica se os gobans são iguais avaliando se as pedras de cada intersecao são iguais
    return (
        eh_goban(goban1)
        and eh_goban(goban2)
        and len(goban1) == len(goban2)
        and all(
            pedras_iguais(intersecao1, intersecao2)
            for coluna1, coluna2 in zip(goban1, goban2)
            for intersecao1, intersecao2 in zip(coluna1, coluna2)
        )
    )


# Transformador
def goban_para_str(goban):
    """
    Converte um goban para a sua representação como string.

    goban para str : goban → str
    Parâmetros:
        goban:
            O goban a ser convertido.

    Retorna:
        str: A representação em string do goban.
    """
    # Cria os números que representam as colunas e também as pedras das intersecoes
    goban_string = ""
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    for linha in reversed(range(tamanho)):
        goban_string += f"{linha + 1:2d} "
        for coluna in range(tamanho):
            goban_string += f"{pedra_para_str(obtem_pedra(goban,cria_intersecao(LETRAS[coluna],linha + 1)))} "
        goban_string += f"{linha + 1:2d}\n"
    # Cria as letras que correspondem às colunas
    letras = "  "
    for coluna in range(tamanho):
        letras += " " + LETRAS[coluna]
    return letras + "\n" + goban_string + letras


# Funções de Alto Nível
def obtem_territorios(goban):
    """
    Obtém os territórios(cadeias formadas por pedras neutras) do goban.

    obtem territorios: goban → tuplo
    Parâmetros:
        goban:
            O goban.

    Retorna:
        tuplo: Um tuplo formado pelos territórios, onde cada território é um tuplo
               contendo as interseções ordenadas em ordem de leitura do tabuleiro de Go.
    """
    res, cadeias, intersecoes_visitadas = (), (), ()
    ult_intersecao = obtem_ultima_intersecao(goban)
    # Descobre todas as cadeias do território
    for linha in range(obtem_lin(ult_intersecao)):
        for coluna in range(obtem_lin(ult_intersecao)):
            intersecao = cria_intersecao(LETRAS[coluna], linha + 1)
            if intersecao not in intersecoes_visitadas:
                cadeia = obtem_cadeia(goban, intersecao)
                cadeias += (cadeia,)
                intersecoes_visitadas += cadeia
    # Verifica quais das cadeias são territórios(cadeias formadas por pedras neutras)
    for cadeia in cadeias:
        if all(not eh_pedra_jogador(obtem_pedra(goban, posicao)) for posicao in cadeia):
            res += (cadeia,)
    return res


def obtem_adjacentes_diferentes(goban, intersecoes):
    """
    Obtém as interseções adjacentes diferentes às interseções de um tuplo.

    obtem adjacentes diferentes: goban x tuplo → tuplo
    Parâmetros:
        goban:
            O goban.
        tuplo:
            Um tuplo contendo interseções do território.

    Retorna:
        tuplo: O tuplo ordenado formado pelas interseções adjacentes diferentes às
               intersecoes fornecidas.
    """
    ultima_intersecao, adjacentes_diferentes = obtem_ultima_intersecao(goban), ()
    for intersecao in intersecoes:
        # caso a intersecao esteja ocupada por um jogador procuram-se pedras eutras, caso contrário
        # procuram-se pedras ocupadas por jogadores
        tipo = eh_pedra_jogador(obtem_pedra(goban, intersecao))
        # Busca de pedras do tipo desejado nas intersecoes adjacentes
        adjacentes = obtem_intersecoes_adjacentes(intersecao, ultima_intersecao)
        for adjacente in adjacentes:
            if (
                tipo != eh_pedra_jogador(obtem_pedra(goban, adjacente))
                and adjacente not in adjacentes_diferentes
            ):
                adjacentes_diferentes += (adjacente,)
    return ordena_intersecoes(adjacentes_diferentes)


def jogada(goban, intersecao, pedra):
    """
    Modifica destrutivamente o goban colocando a pedra na interseção e removendo pedras do jogador contrário sem liberdades.

    jogada: goban x intersecao x pedra → goban
    Parâmetros:
    goban:
        O goban a ser modificado.
    intersecao:
        A interseção onde a pedra será colocada.
    pedra:
        A pedra a ser colocada.

    Retorna:
    Goban:
        O próprio goban modificado.
    """
    # Coloca-se a pedra no intersecao desejada
    goban = coloca_pedra(goban, intersecao, pedra)
    adjacentes = obtem_intersecoes_adjacentes(
        intersecao, obtem_ultima_intersecao(goban)
    )

    for adjacente in adjacentes:
        # caso uma das intersecoes adjacentes sejam ocupada pelo adversário, descubrir essa cadeia e caso
        # não haja livres à volta da cadeia, ela é removida
        if eh_pedra_jogador(obtem_pedra(goban, adjacente)) and not pedras_iguais(
            obtem_pedra(goban, adjacente), pedra
        ):
            cadeia = obtem_cadeia(goban, adjacente)
            if obtem_adjacentes_diferentes(goban, cadeia) == ():
                goban = remove_cadeia(goban, cadeia)
    return goban


def obtem_pedras_jogadores(goban):
    """
    Obtém o número de interseções ocupadas por pedras brancas e pretas

    obtem pedras jogadores: goban → tuplo
    Parâmetros:
    goban:
        O goban.

    Retorna:
    tuplo
        Um tuplo formado por dois inteiros que representam o número de interseções ocupadas
        por pedras dos jogadores branco e preto, respectivamente.
    """
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    brancas, pretas = 0, 0
    for coluna in range(tamanho):
        for linha in range(tamanho):
            if eh_pedra_preta(
                obtem_pedra(goban, cria_intersecao(LETRAS[coluna], linha + 1))
            ):
                pretas += 1
            elif eh_pedra_branca(
                obtem_pedra(goban, cria_intersecao(LETRAS[coluna], linha + 1))
            ):
                brancas += 1
    return (brancas, pretas)


def calcula_pontos(goban):
    """
    Calcula os pontos dos jogadores branco e preto em um goban.

    calcula pontos: goban → tuple
    Parâmetros:
    goban:
        O goban.

    Retorna:
    tuplo
        Um tuplo formado por dois inteiros que representam a pontuação dos jogadores branco e preto, respectivamente.
    """
    # Caso o território não tenha peças, devolve que as pontuações são nulas
    pedras = obtem_pedras_jogadores(goban)
    pretas, brancas = pedras[1], pedras[0]
    if pretas == brancas == 0:
        return (0, 0)

    # Procura os territorios que estão rodeados por intersecoes de apenas um jogador
    territorios = obtem_territorios(goban)
    for territorio in territorios:
        adjacentes_diferentes = obtem_adjacentes_diferentes(goban, territorio)
        if all(
            eh_pedra_branca(obtem_pedra(goban, intersecao))
            for intersecao in adjacentes_diferentes
        ):
            brancas += len(territorio)
        elif all(
            eh_pedra_preta(obtem_pedra(goban, intersecao))
            for intersecao in adjacentes_diferentes
        ):
            pretas += len(territorio)
    return (brancas, pretas)


def eh_jogada_legal(goban, intersecao, pedra, goban_l):
    """
    Verifica se a jogada é legal.

    eh jogada legal: goban x intersecao x pedra x goban → booleano
    Parâmetros:
        goban:
            O goban original.
        intersecao:
            A interseção da jogada.
        pedra:
            A pedra do jogador.
        goban:
            O goban que se vai verificar se existe repetição.

    Retorna:
        bool: True se a jogada for legal, False caso contrário.
    """
    # se a intersecao estiver ocupada por uma peça a jogada é inválida e se a intersecao é válida
    if not eh_intersecao_valida(goban, intersecao) or eh_pedra_jogador(
        obtem_pedra(goban, intersecao)
    ):
        return False
    # se a jogada causa um suícidio ela é inválida
    w = jogada(cria_copia_goban(goban), intersecao, pedra)
    cadeia = obtem_cadeia(w, intersecao)
    adj = obtem_adjacentes_diferentes(w, cadeia)
    if adj == ():
        return False
    # se existe repetição a jogada é inválida
    if gobans_iguais(w, goban_l):
        return False
    return True


def turno_jogador(goban, pedra, goban_l):
    """
    Oferece ao jogador a opção de passar ou realizar uma jogada.

    turno jogador: goban x pedra x goban → booleano
    Parâmetros:
        goban:
            O goban.
        pedra:
            A pedra do jogador do turno realizar.
        goban:
            O goban em que se será verificada a.

    Retorna:
        bool: True se o jogador realizou uma jogada, False se passou.
    """
    escolha = input(
        f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(pedra)}]:"
    )
    if escolha == "P":
        return False
    # verifica se o input pode ser uma intersecao
    if (
        len(escolha) < 2
        or escolha[0] not in LETRAS
        or not escolha[1:].isdigit()
        or not 1 <= int(escolha[1:]) <= 19
    ):
        return turno_jogador(goban, pedra, goban_l)
    intersecao = str_para_intersecao(escolha)
    # verifica se a intersecao escolhida pertence ao goban e se a jogada é válida
    if not eh_intersecao_valida(goban, intersecao) or not eh_jogada_legal(
        goban, intersecao, pedra, goban_l
    ):
        return turno_jogador(goban, pedra, goban_l)
    goban = jogada(goban, str_para_intersecao(escolha), pedra)
    return True


def go(n, intersecoes_brancas, intersecoes_pretas):
    """
    Joga uma partida completa de Go entre dois jogadores.

    go: int x tuple x tuple → booleano
    Parâmetros:
        int:
            Dimensão do tabuleiro.
        tuplo:
            Representação externa das interseções ocupadas por pedras brancas.
        tuplo:
            Representação externa das interseções ocupadas por pedras pretas.

    Retorna:
        bool: True se o jogador com pedras brancas ganhou, False caso contrário.
    """
    try:
        goban = cria_goban(
            n,
            converte_intersecoes(intersecoes_brancas),
            converte_intersecoes(intersecoes_pretas),
        )
    except ValueError:
        raise ValueError("go: argumentos invalidos")
    # flag permite a execução de dois breaks consecutivos para terminar os loops em cadeia
    # passou representa o número de jogadores que passaram a jogada consecutivamente
    flag = False
    passou = 0
    goban_anterior_anterior, goban_anterior = cria_goban_vazio(n), cria_goban_vazio(n)
    while True:
        for pedra in (cria_pedra_preta(), cria_pedra_branca()):
            goban_anterior = cria_copia_goban(goban)
            score = calcula_pontos(goban)
            print(f"Branco (O) tem {score[0]} pontos")
            print(f"Preto (X) tem {score[1]} pontos")
            print(goban_para_str(goban))
            # permite que um jogador jogue, atribuindo o goban anterior ao anterior jogado para se evitar ko
            if not turno_jogador(goban, pedra, goban_anterior_anterior):
                passou += 1
            else:
                passou = 0
            if passou == 2:
                flag = True
                break
            goban_anterior_anterior = cria_copia_goban(goban_anterior)
        if flag:
            break
    score = calcula_pontos(goban)
    print(f"Branco (O) tem {score[0]} pontos")
    print(f"Preto (X) tem {score[1]} pontos")
    print(goban_para_str(goban))
    # retorna True se pontuação das brancas for igual ou superior às das pretas, False caso contrário
    return score[0] >= score[1]
