# Go Game Project

## Overview
This project is developed for the "Fundamentals of Programming" course and focuses on implementing a program to play the board game Go. The project requires defining abstract data types (ADTs) to manage game-related information and implementing various functions to simulate the gameplay.

## Features
The program provides functionalities to:
- Represent and manipulate the Go board (goban), intersections, and stones.
- Determine valid moves based on game rules.
- Capture opponent's stones when surrounded.
- Calculate controlled territories and determine the game winner.

## Board Representation
- The board (goban) is a square grid, typically of size 9×9, 13×13, or 19×19.
- Each intersection is identified by a capital letter (A-S) for columns and a number (1-19) for rows.
- Intersections can be free or occupied by a stone (black or white).
- Chains of stones are formed by connected pieces of the same color.
- Liberties represent the adjacent free intersections of a stone or chain.

## Implemented Functions
### Intersection Functions
- `cria_intersecao(col, lin)`: Creates a valid board intersection.
- `obtem_col(i)`: Retrieves the column of an intersection.
- `obtem_lin(i)`: Retrieves the row of an intersection.
- `eh_intersecao(arg)`: Checks if the argument is a valid intersection.
- `intersecoes_iguais(i1, i2)`: Checks if two intersections are equal.
- `intersecao_para_str(i)`: Converts an intersection to its string representation.
- `str_para_intersecao(s)`: Converts a string to an intersection.
- `obtem_intersecoes_adjacentes(i, l)`: Returns adjacent intersections.
- `ordena_intersecoes(t)`: Sorts intersections in reading order.

### Stone Functions
- `cria_pedra_branca()`: Creates a white stone.
- `cria_pedra_preta()`: Creates a black stone.
- `cria_pedra_neutra()`: Creates a neutral (empty) stone.
- `eh_pedra(arg)`: Checks if the argument is a valid stone.
- `eh_pedra_branca(p)`: Checks if a stone is white.
- `eh_pedra_preta(p)`: Checks if a stone is black.
- `pedras_iguais(p1, p2)`: Checks if two stones are identical.
- `pedra_para_str(p)`: Converts a stone to its string representation.

### Board (Goban) Functions
- `cria_goban_vazio(n)`: Creates an empty board of size n×n.
- `cria_goban(n, ib, ip)`: Creates a board with specified initial black and white stones.
- `cria_copia_goban(g)`: Creates a copy of a given board.
- `obtem_ultima_intersecao(g)`: Gets the top-right intersection of the board.
- `obtem_pedra(g, i)`: Retrieves the stone at a given intersection.
- `obtem_cadeia(g, i)`: Returns all connected stones forming a chain.
- `coloca_pedra(g, i, p)`: Places a stone on the board.
- `remove_pedra(g, i)`: Removes a stone from the board.
- `remove_cadeia(g, t)`: Removes all stones in a specified chain.
- `eh_goban(arg)`: Checks if the argument is a valid board.
- `eh_intersecao_valida(g, i)`: Checks if an intersection is valid on a given board.
- `goban_para_str(g)`: Converts the board to a string representation.

### Game Logic Functions
- `obtem_territorios(g)`: Identifies the controlled territories of each player.
- `obtem_adjacentes_diferentes(g, t)`: Returns adjacent intersections with different states.
- `jogada(g, i, p)`: Performs a move by placing a stone and capturing opponent stones if necessary.
- `obtem_pedras_jogadores(g)`: Counts stones placed by each player.
- `calcula_pontos(g)`: Calculates the final score of both players.
- `eh_jogada_legal(g, i, p, l)`: Checks if a move is legal according to Go rules.
- `turno_jogador(g, p, l)`: Executes a player's turn, allowing them to place a stone or pass.
- `go(n, tb, tp)`: Runs a full Go game session, determining the winner.

## Execution Instructions
1. Ensure you have Python 3 installed.
2. Run the Python script: `python FP2023P2.py`
3. Use the implemented functions to simulate and analyze Go gameplay.

