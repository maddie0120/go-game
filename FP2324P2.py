#------------------------------------------------
#                2º projeto: Go
#------------------------------------------------
"""
Instituto Superior Tecnico - Campus Alameda
Curso: Licenciatura em Engenharia Informatica e de Computadores (LEIC - A)
Cadeira: Fundamentos de Programacao (FP)
Corpo Docente responsavel: Arlindo Oliveira
Ano letivo 2023/24
Aluno: Madalena Yang | ist1110206
"""

#*******************************************
#     2.1.1 TAD intersecao - imutavel      #  
#*******************************************
"""O TAD imutavel intersecao e usado para representar uma intersecao
do tabuleiro de Go"""

#construtor
#======================================
# cria_intersecao: str x int -> intersecao
#======================================
def cria_intersecao(col, lin):
    """
    Esta funcao recebe um caracter e um inteiro correspondentes a
    coluna col e a linha lin e devolve a intersecao correspondente.
    O construtor verifica a validade dos seus argumentos, gerando um
    ValueError com a mensagem 'cria_intersecao: argumentos invalidos'
    caso os seus argumentos nao sejam validos
    """

    if not (isinstance(col, str) and type(lin) == int and\
            'A' <= col <= 'S' and len(col) == 1 and 0 < lin < 20):
        raise ValueError('cria_intersecao: argumentos invalidos')
    
    return (col, lin)


#seletores
#======================================
# obtem_col: intersecao -> str
#======================================
def obtem_col(i):
    """Esta funcao devolve a coluna col da intersecao i"""

    return i[0]


#======================================
# obtem_lin: intersecao -> int
#======================================
def obtem_lin(i):
    """Esta funcao devolve a linha lin da intersecao i"""

    return i[1]


#reconhecedor
#======================================
# eh_intersecao: universal -> booleano
#======================================
def eh_intersecao(arg):
    """
    Esta funcao recebe um argumento universal e devolve True caso
    o seu argumento seja um TAD intersecao e False caso contrario
    """

    return isinstance(arg, tuple) and len(arg) == 2 and\
        isinstance(arg[0], str) and type(arg[1]) == int and\
        'A' <= arg[0] <= 'S' and len(arg[0]) == 1 and 0 < arg[1] < 20


#teste
#======================================
# intersecao_iguais: universal x universal -> booleano
#======================================
def intersecoes_iguais(i1, i2):
    """
    Esta funcao recebe dois argumentos universais e devolve True
    apenas se esses argumentos forem intersecoes e se forem iguais
    e False caso contrario
    """

    return eh_intersecao(i1) and eh_intersecao(i2) and\
        obtem_col(i1) == obtem_col(i2) and\
        obtem_lin(i1) == obtem_lin(i2)


#transformador
#======================================
# intersecao_para_str: intersecao -> str
#======================================
def intersecao_para_str(i):
    """Esta funcao recebe uma intersecao e devolve a cadeia de
    caracteres que o representa"""

    return f'{obtem_col(i)}{obtem_lin(i)}'


#======================================
# str_para_intersecao: str -> intersecao
#======================================
def str_para_intersecao(s):
    """Esta funcao recebe uma str e devolve uma intersecao"""

    if not (isinstance(s, str) and 1 < len(s) < 4 and 'A' <= s[0] <= 'S' and\
            0 < int(s[1:]) < 20):
        raise ValueError
    
    return (s[0], int(s[1:]))


#*******************************************
#     FAN associadas ao TAD intersecao     #
#*******************************************
#======================================
# obtem_intersecoes_adjacentes: intersecao x intersecao -> tuplo
#======================================
def obtem_intersecoes_adjacentes(i, l):
    """
    Esta funcao recebe duas intersecoes (i, l) e devolve um tuplo com
    as intersecoes adjacentes a intersecao i de acordo com a ordem de
    leitura em que l corresponde a intersecao superior direita do
    tabuleiro de Go. A ordem de leitura das intersecoes do goban e
    feita da esquerda para a direita seguida de baixo para cima
    """

    adj = ()
    col, lin = obtem_col(i), obtem_lin(i)
    
    #as seguintes condicoes ifs verificam se a intersecao dada
    #encontra-se nalguma borda do territorio
    if lin > 1: #baixo
        adj += (cria_intersecao(col, lin - 1),)

    if col > 'A': #esquerda
        adj += (cria_intersecao(chr(ord(col) - 1), lin),)
        
    if col < obtem_col(l): #direita
        adj += (cria_intersecao(chr(ord(col) + 1), lin),)
    
    if lin < obtem_lin(l): #cima
        adj += (cria_intersecao(col, lin + 1),)

    return adj


#======================================
# ordena_intersecoes: tuplo -> tuplo
#======================================
def ordena_intersecoes(t):
    """
    Esta funcao recebe um tuplo e devolve um tuplo de intersecoes
    com as mesmas intersecoes de t ordenadas de acordo com a ordem
    de leitura do tabuleiro de Go
    """

    #primeiro linha, depois coluna
    return tuple(sorted(t, key=lambda i:(obtem_lin(i), obtem_col(i))))



#*******************************************
#             2.1.2 TAD pedra              # 
#*******************************************
"""
O TAD pedra e usado para representar as pedras do Go. As pedras podem
pertencer ao jogador branco ('O') ou ao jogador preto ('X'). Por
conveniencia, e tambem definido o conceito pedra neutra, que e uma
pedra que nao pertence a nenhum jogador
"""

#construtor
#======================================
# cria_pedra_branca: {} -> pedra
#======================================
def cria_pedra_branca():
    """Esta funcao devolve uma pedra pertencente ao jogador branco"""

    return 'O'


#======================================
# cria_pedra_preta: {} -> pedra
#======================================
def cria_pedra_preta():
    """Esta funcao devolve uma pedra pertencente ao jogador preto"""

    return 'X'


#======================================
# cria_pedra_neutra: {} -> pedra
#======================================
def cria_pedra_neutra():
    """Esta funcao devolve uma pedra neutra"""

    return '.'


#reconhecedor
#======================================
# eh_pedra: universal -> booleano
#======================================
def eh_pedra(arg):
    """Esta funcao um argumento universal e devolve True caso o seu
    argumento seja um TAD pedra e False caso contrario"""

    return isinstance(arg, str) and arg in ['O', 'X', '.']


#======================================
# eh_pedra_branca: pedra -> booleano
#======================================
def eh_pedra_branca(p):
    """Esta funcao recebe uma pedra e devolve True caso a pedra p seja
    do jogador branco e False caso contrario"""

    return p == 'O'


#======================================
# eh_pedra_preta: pedra -> booleano
#======================================
def eh_pedra_preta(p):
    """Esta funcao recebe uma pedra e devolve True caso a pedra p seja
    do jogador preto e False caso contrario"""

    return p == 'X'


#teste
#======================================
# pedras_iguais: universal x universal -> booleano
#======================================
def pedras_iguais(p1, p2):
    """Esta funcao recebe dois argumentos universais e devolve True
    apenas eles forem pedras iguais"""

    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


#transformador
#======================================
# pedras_para_str: pedra -> str
#======================================
def pedra_para_str(p):
    """
    Esta funcao recebe uma pedra e devolve a cadeia de caracteres
    que representa o jogador dono da pedra, ou seja, 'O', 'X' ou '.'
    para pedras do jogador branco, preto ou neutra, respetivamente
    """

    return p


#*******************************************
#       FAN associadas ao TAD pedra        #
#*******************************************
#======================================
# eh_pedra_jogador: pedra -> booleano
#======================================
def eh_pedra_jogador(p):
    """Esta funcao recebe uma pedra e devolve True caso a pedra p
    seja de um jogador e False caso contrario"""

    return eh_pedra_branca(p) or eh_pedra_preta(p)



#*******************************************
#             2.1.3 TAD goban              #  
#*******************************************
"""O TAD goban e usado para representar um tabuleiro do jogo Go e as
pedras dos jogadores que nele sao colocadas"""

#construtor
#======================================
# cria_goban_vazio: int -> goban
#======================================
def cria_goban_vazio(n):
    """
    Esta funcao recebe um inteiro e devolve um goban de tamanho n x n,
    sem intersecoes ocupadas. O construtor verifica a validade do
    argumento, gerando um ValueError com a mensagem 'cria_goban_vazio:
    argumento invalido' caso os seu argumento nao seja valido. O
    tamanho de um goban pode ser de dimensao 9 x 9, 13 x 13 ou 19 x 19
    """

    if not type(n) == int or n not in [9, 13, 19]:
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    return {pedra_para_str(cria_pedra_branca()): [],
            pedra_para_str(cria_pedra_preta()): [],
            pedra_para_str(cria_pedra_neutra()): [cria_intersecao(chr(col + 65), lin)
            for lin in range(1, n + 1) for col in range(n)]}
            #chr(65) = 'A'


#======================================
# cria_goban: int x tuplo x tuplo -> goban
#======================================
def cria_goban(n, ib, ip):
    """
    Esta funcao recebe tres argumento, um inteiro, e dois tuplos. 
    Devolve um goban de tamanho n x n, com as intersecoes do tuplo ib
    ocupadas por pedras brancas e as intersecoes do tuplo ip ocupadas
    por pedras pretas. O construtor verifica a validade dos argumentos,
    gerando um ValueError com a mensagem 'cria_goban: argumentos
    invalidos' caso os seus argumentos nao sejam validos.
    """

    if not (type(n) == int and n in [9, 13, 19] and\
            isinstance(ib, tuple) and isinstance(ip, tuple)):
        raise ValueError('cria_goban: argumentos invalidos')
    
    if all(isinstance(b, str) for b in ib) and\
        all(isinstance(p, str) for p in ip):

        #caso os elementos do tuplo sejam str:
        #transforma-se em tuplos de intersecoes
        try:
            ib = tuple(str_para_intersecao(b) for b in ib)
            ip = tuple(str_para_intersecao(p) for p in ip)
        except ValueError:
            raise ValueError('cria_goban: argumentos invalidos')

    if not (all(eh_intersecao(b) and\
                eh_intersecao_valida(cria_goban_vazio(n), b) for b in ib) and\
            all(eh_intersecao(p) and\
                eh_intersecao_valida(cria_goban_vazio(n), p) for p in ip) and\
            len(ib) == len(set(ib)) and\
            len(ip) == len(set(ip)) and not any(i in ib for i in ip)):
        raise ValueError('cria_goban: argumentos invalidos')
    
    goban = cria_goban_vazio(n)

    #vai adicionar as intersecoes do tuplo ao goban
    for pedra_b in ib:
        goban[pedra_para_str(cria_pedra_neutra())].remove(pedra_b)
        goban[pedra_para_str(cria_pedra_branca())].append(pedra_b)

    for pedra_p in ip:
        goban[pedra_para_str(cria_pedra_neutra())].remove(pedra_p)
        goban[pedra_para_str(cria_pedra_preta())].append(pedra_p)
        
    return goban


#======================================
# cria_copia_goban: goban -> goban
#======================================
def cria_copia_goban(t):
    """Esta funcao recebe um goban e devolve uma copia do goban"""

    return {pedra: [tuple(intersecao) for intersecao in lst] 
            for pedra, lst in t.items()}


#seletores
#======================================
# obtem_ultima_intersecao: goban -> intersecao
#======================================
def obtem_ultima_intersecao(g):
    """Esta funcao recebe um goban e devolve a intersecao que
    corresponde ao canto superior direito do goban g"""

    lst = []

    for sublista in g.values():
        lst += sublista

    return ordena_intersecoes(lst)[-1]


#======================================
# obtem_pedra: goban x intersecao -> pedra
#======================================
def obtem_pedra(g, i):
    """
    Esta funcao recebe um goban e uma intersecao e devolve a pedra
    na intersecao i do goban g. Se a intersecao nao estiver ocupada,
    devolve uma pedra neutra
    """
    
    if i in g[pedra_para_str(cria_pedra_branca())]:
        return cria_pedra_branca()
    
    elif i in g[pedra_para_str(cria_pedra_preta())]:
        return cria_pedra_preta()
    
    else:
        return cria_pedra_neutra()


#======================================
# obtem_cadeia: goban x intersecao -> tuplo
#======================================
def obtem_cadeia(g, i):
    """
    Esta função recebe um goban e uma interseção e devolve o tuplo
    formado pelas interseções (em ordem de leitura) das pedras da mesma
    cor que formam a cadeia que passa pela interseção i. Se a posição
    não estiver ocupada, devolve a cadeia de interseções livres.
    """
    pedra = cria_pedra_branca() if i in g[pedra_para_str(cria_pedra_branca())]\
        else cria_pedra_preta() if i in g[pedra_para_str(cria_pedra_preta())]\
        else cria_pedra_neutra()

    cadeia = set()
    por_ver = [i]

    while por_ver:
        atual = por_ver.pop()
        cadeia.add(atual)
        adj = obtem_intersecoes_adjacentes(atual, obtem_ultima_intersecao(g))
        for intersecao in adj:
            if intersecao in g[pedra_para_str(pedra)] and\
                intersecao not in cadeia:
                por_ver.append(intersecao)

    return tuple(ordena_intersecoes(cadeia))


#modificadores
#======================================
# coloca_pedra: goban x intersecao x pedra -> goban
#======================================
def coloca_pedra(g, i, p):
    """
    Esta funcao recebe um goban, uma intersecao e uma pedra.
    Ela modifica destrutivamente o goban g colocando a pedra do
    jogador p na intersecao i, e devolve o proprio goban
    """

    g[pedra_para_str(obtem_pedra(g, i))].remove(i)
    g[pedra_para_str(p)].append(i)

    return g


#======================================
# remove_pedra: goban x intersecao -> goban
#======================================
def remove_pedra(g, i):
    """
    Esta funcao recebe um goban e uma intersecao e modifica
    destrutivamente o goban g removendo a pedra da intersecao i,
    e devolve o proprio goban
    """

    coloca_pedra(g, i, cria_pedra_neutra())
    
    return g


#======================================
# remove_cadeia: goban x tuplo -> goban
#======================================
def remove_cadeia(g, t):
    """
    Esta funcao recebe um goban e um tuplo e modifica destrutivamente
    o goban g removendo as pedras nas intersecoes to tuplo t, e
    devolve o proprio goban
    """

    for i in t:
        for pedra in g.keys():
            if i in g[pedra_para_str(pedra)]:
                g[pedra_para_str(pedra)].remove(i)
                g[pedra_para_str(cria_pedra_neutra())].append(i)
    return g


#reconhecedor
#======================================
# eh_goban: universal -> booleano
#======================================
def eh_goban(arg):
    """Esta funcao recebe um argumento universal e devolve True caso
    o seu argumento seja um TAD goban e False caso contrario"""

    return (isinstance(arg, dict) and\
        all(pedra in arg for pedra in [pedra_para_str(cria_pedra_branca()), 
                                       pedra_para_str(cria_pedra_preta()),
                                       pedra_para_str(cria_pedra_neutra())]) and\
        all(isinstance(lst, list) for lst in arg.values())) and\
        all(all(eh_intersecao(i) for i in lst) for lst in arg.values())


#======================================
# eh_intersecao_valida: goban x intersecao -> booleano
#======================================
def eh_intersecao_valida(g, i):
    """
    Esta funcao recebe um goban e uma intersecao e devolve True caso i
    seja uma intersecao valida dentro do goban g e False caso contrario
    """

    return any(i in lst for lst in g.values())


#teste
#======================================
# gobans_iguais: universal x universal -> booleano
#======================================
def gobans_iguais(g1, g2):
    """Esta funcao recebe dois argumentos universais e devolve
    True apenas se g1 e g2 forem gobans e forem iguais"""

    if not (eh_goban(g1) and eh_goban(g2)):
        return False

    for key in g1.keys():
        if sorted(g1[key]) != sorted(g2[key]):
            return False
        
    return True


#transformador
#======================================
# goban_para_str: goban -> str
#======================================
def goban_para_str(g):
    """Esta funcao recebe um goban e devolve a representacao externa
    do tabuleiro de Go, em cadeia de caracteres"""

    letras = '  ' #linha com as letras do tabuleiro
    goban = '' #tabuleiro excluindo as linhas das letras

    ult_col = ord(obtem_col(obtem_ultima_intersecao(g)))
    ult_lin = obtem_lin(obtem_ultima_intersecao(g))

    for letra in range(65, ult_col + 1):
        letras += ' ' + chr(letra)

    for num in range(ult_lin, 0, -1):
        goban += '{:2d}'.format(num) + ' '

        for letra in range(65, ult_col + 1):

            i = cria_intersecao(chr(letra), num)

            goban += ('O' if i in g[pedra_para_str(cria_pedra_branca())]\
                    else 'X' if i in g[pedra_para_str(cria_pedra_preta())]\
                    else '.') + ' '

        goban += '{:2d}'.format(num) +'\n'

    return letras + '\n' + goban + letras


#*******************************************
#       FAN associadas ao TAD goban        #
#*******************************************
#======================================
# obtem_territorios: goban -> tuplo
#======================================
def obtem_territorios(g):
    """
    Esta funcao recebe um goban e devolve o tuplo formado pelos tuplos
    com as intersecoes de cada territorio de g. A funcao devolve as
    intersecoes de cada territorio ordenadas em ordem de leitura do
    tabuleiro de Go, e os territorios ordenados em ordem de leitura da
    primeira intersecao do territorio
    """

    ter = ()
    vistos = ()
    
    goban = cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(g)))
    for i in obtem_cadeia(goban, cria_intersecao('A', 1)):
        if not eh_pedra_jogador(obtem_pedra(g, i)) and i not in vistos:
            cadeia = obtem_cadeia(g, i)
            vistos += cadeia
            ter += (cadeia,)

    return ter


#======================================
# obtem_adjacentes_diferentes: goban x tuplo -> tuplo
#======================================
def obtem_adjacentes_diferentes(g, t):
    """
    Esta funcao recebe um goban e um tuplo e devolve o tuplo ordenado
    formado pelas intersecoes adjacentes as intersecoes do tuplo t:
    (1) livres, se as intersecoes do tuplo t estao ocupadas por pedras
    de jogador. Isto corresponde as liberdades de uma cadeia de pedras
    (2) ocupadas por pedras de jogador, se as intersecoes do tuplo t
    estao livres. Isto corresponde a fronteira de um territorio
    """

    adj_dif = ()
    ult = obtem_ultima_intersecao(g)

    if all(eh_pedra_jogador(obtem_pedra(g, i)) for i in t):
        for i in t:
            conj_adj = obtem_intersecoes_adjacentes(i, ult)
            for adj in conj_adj:
                if not eh_pedra_jogador(obtem_pedra(g, adj)) and\
                    adj not in adj_dif:
                    adj_dif += (adj,)
    else:
        for i in t:
            conj_adj = obtem_intersecoes_adjacentes(i, ult)
            for adj in conj_adj:
                if eh_pedra_jogador(obtem_pedra(g, adj)) and\
                    adj not in adj_dif:
                    adj_dif += (adj,)


    return ordena_intersecoes(adj_dif)


#======================================
# jogada: goban x intersecao x pedra -> goban
#======================================
def jogada(g, i, p):
    """
    Esta funcao recebe um goban, uma intersecao e uma pedra. Ela
    modifica destrutivamente o goban g colocando a pedra de jogador p
    na intersecao i e remove todas as pedras do jogador contrario
    pertencentes a cadeias adjacentes a i sem liberdades, devolvendo o
    proprio goban.
    """

    coloca_pedra(g, i, p)

    for adj in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g)):
        if not pedras_iguais(p, obtem_pedra(g, adj)) and eh_pedra_jogador(p):
            cadeia = obtem_cadeia(g, adj)
            if obtem_adjacentes_diferentes(g, cadeia) == ():
                remove_cadeia(g, cadeia)
    return g


#======================================
# obtem_pedras_jogadores: goban -> tuplo
#======================================
def obtem_pedras_jogadores(g):
    """
    Esta funcao recebe um goban e devolve um tuplo de dois inteiros
    que correspondem ao numero de intersecoes ocupadas por pedras do
    jogador branco e preto, respetivamente
    """
    
    preta = 0
    branca = 0

    goban = cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(g)))

    for i in obtem_cadeia(goban, cria_intersecao('A', 1)):
            if eh_pedra_branca(obtem_pedra(g, i)):
                branca += 1
            elif eh_pedra_preta(obtem_pedra(g, i)):
                preta += 1

    return (branca, preta)



#*******************************************
#            Funcoes adicionais            #
#*******************************************
#======================================
# calcula_pontos: goban -> tuplo
#======================================
def calcula_pontos(g):
    """
    Esta e uma funcao auxiliar que recebe um goban e devolve o tuplo
    de dois inteiros com as pontuacoes dos jogadores branco e preto,
    respetivamente
    """

    ter_b, ter_p = 0, 0
    if obtem_pedras_jogadores(g) == (0, 0): return (0, 0)

    for territorio in obtem_territorios(g):
        if all(eh_pedra_branca(obtem_pedra(g, i))\
               for i in obtem_adjacentes_diferentes(g, territorio)):
            ter_b += len(territorio)
        if all(eh_pedra_preta(obtem_pedra(g, i))\
               for i in obtem_adjacentes_diferentes(g, territorio)):
            ter_p += len(territorio)

    return (obtem_pedras_jogadores(g)[0] + ter_b,\
            obtem_pedras_jogadores(g)[1] + ter_p)


#======================================
# eh_jogada_legal: goban x intersecao x pedra x goban -> booleano
#======================================
def eh_jogada_legal(g, i, p, l):
    """
    Esta funcao auxiliar recebe um goban g, uma intersecao i, uma
    pedra do jogador p e um outro goban l. Devolve True se a jogada
    for legal ou False caso contrario, sem modificar g ou l. Para a
    detecao de repeticao, l representa o estado de tabuleiro que nao
    pode ser obtido apos a resolucao completa da jogada
    """

    if not eh_intersecao_valida(g, i) or\
        not pedras_iguais(obtem_pedra(g, i), cria_pedra_neutra()):
        return False

    copia = cria_copia_goban(g)
    jogada(copia, i, p)
    
    if obtem_adjacentes_diferentes(copia, obtem_cadeia(copia, i)) == () or gobans_iguais(copia, l):
        return False
    
    return True


#======================================
# turno_jogador: goban x pedra x goban -> booleano
#======================================
def turno_jogador(g, p, l):
    """
    Esta funcao auxiliar recebe um goban g, uma pedra de jogador p e um
    outro goban l oferecendo ao jogador que joga com pedras p a opcao
    de passar ou de colocar uma pedra propria numa intersecao. Se o
    jogador passar, a funcao devolve False sem modificar os argumentos.
    Caso contrario, a funcao devolve True e modifica destrutivamente o
    tabuleiro g de acordo com a jogada realizada. A funcao apresenta a
    mensagem a seguir, repetindo-a ate que o jogador introduzir 'P' ou
    a representacao externa de uma intersecao do tabuleiro de Go que
    corresponda a uma jogada legal. l representa o estado de tabuleiro
    que nao pode ser obtido apos a resolucao completa da jogada
    """
    
    while eh_pedra_jogador(p):
        
        try:
            escolha = input("Escreva uma intersecao ou 'P' para passar "
                            f"[{pedra_para_str(p)}]:")
            if escolha == 'P':
                return False
            i = str_para_intersecao(escolha)
            if eh_intersecao_valida(g, i) and eh_jogada_legal(g, i, p, l):
                jogada(g, i, p)
                return True
            
        except ValueError:
            continue


#======================================
# go: int x tuplo x tuplo -> booleano
#======================================
def go(n, tb, tp):
    """
    Esta e a funcao principal que permite jogar um jogo completo do Go
    de dois jogadores. A funcao recebe um inteiro correspondente a
    dimensao do tabuleiro, e dois tuplos (potencialmente vazios) com a
    representacao externa das intersecoes ocupadas por pedras brancas
    (tb) e pretas (tp) inicialmente. O jogo termina quando os dois
    jogadores passam a vez de jogar consecutivamente. A funcao devolve
    True se o jogador com pedras brancas conseguir ganhar o jogo, ou
    False caso contrario. A funcao deve verificar a validade dos seus
    argumentos, gerando um ValueError com a mensagem 'go: argumentos
    invalidos' caso os seus argumentos nao sejam validos
    """

    if not (isinstance(tb, tuple) and isinstance(tp, tuple)):
        raise ValueError('go: argumentos invalidos')
    
    try:
        g = cria_goban(n, tuple(str_para_intersecao(b) for b in tb), 
                        tuple(str_para_intersecao(p) for p in tp))
        
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    
    #o jogador com pedras pretas joga primeiro
    prox_joga = cria_pedra_preta()
    passar = 0 
    tab_atual = cria_copia_goban(g)
    tab_anterior = cria_copia_goban(g)

#-------------------- funcoes auxiliares para a funcao go --------------------
    def joga(pedra):
        if eh_pedra_branca(pedra):
            return cria_pedra_preta()
        else:
            return cria_pedra_branca()
        
    def msg_para_jogo(g):
        print(f"Branco (O) tem {calcula_pontos(g)[0]} pontos")
        print(f"Preto (X) tem {calcula_pontos(g)[1]} pontos")
        print(goban_para_str(g))
#-------------------- funcoes auxiliares para a funcao go --------------------

    msg_para_jogo(g)
    
    while not passar == 2:
        if not turno_jogador(g, prox_joga, tab_anterior):
            passar += 1
        else:
            passar = 0
        
            tab_anterior = cria_copia_goban(tab_atual)
            tab_atual = cria_copia_goban(g)

        msg_para_jogo(g)
        
        prox_joga = joga(prox_joga)
 
    return calcula_pontos(g)[0] >= calcula_pontos(g)[1]