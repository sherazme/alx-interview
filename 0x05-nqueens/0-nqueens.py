#!/usr/bin/python3
""" N queens puzzle is challenge of placing N
non-attacking queens on an N×N chessboard

TODO:
    * Write a program that solves the N queens problem
"""


def queens(chessBoard, row, majestyz, resolve):
    """ resolve list """
    if majestyz == len(chessBoard):
        resolve.append(extract(chessBoard))
        return (resolve)

    for col in range(len(chessBoard)):
        if chessBoard[row][col] == -1:
            demo = copyBoard(chessBoard)
            demo[row][col] = 1
            cancel(demo, row, col)
            resolve = queens(demo, row + 1, majestyz + 1, resolve)
    return (resolve)


def cancel(chessBoard, row, col):
    """ Cancel out vulnerable positions for queen """
    length = len(chessBoard)
    """ Cancel forward position """
    for c in range(col + 1, length):
        chessBoard[row][c] = 0
    """ Cancel backwards position """
    for c in range(col - 1, -1, -1):
        chessBoard[row][c] = 0
    """ Cancel down position """
    for r in range(row + 1, length):
        chessBoard[r][col] = 0
    """ Cancel up position """
    for r in range(row - 1, -1, 1):
        chessBoard[r][col] = 0
    """ Cancel right downward diagonal position """
    c = col + 1
    for r in range(row + 1, length):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """ Cancel left upward diagonal position """
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1
    """ Cancel right upward diagonal position """
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= length:
            break
        chessBoard[r][c] = 0
        c += 1
    """ Cancel left downward diagonal position """
    c = col - 1
    for r in range(row + 1, length):
        if c < 0:
            break
        chessBoard[r][c] = 0
        c -= 1


def chessBoard(N):
    """ Create the board of size N * N """
    chessBoard = []

    """ Create the rows """
    for row in range(N):
        chessBoard.append([])

    """ Create the columns """
    for row in chessBoard:
        for n in range(N):
            row.append(-1)

    return (chessBoard)


def copyBoard(chessBoard):
    """ make copy of chessBoard """
    if type(chessBoard) == list:
        """ Recursive copy """
        return list(map(copyBoard, chessBoard))
    return (chessBoard)


def extract(chessBoard):
    """ Extract required outcome from chess board """
    outcome = []
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard)):
            if chessBoard[row][col] == 1:
                outcome.append([row, col])
                break
    return (outcome)


def execute():
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isnumeric() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess = chessBoard(int(sys.argv[1]))
    resultMatrix = queens(chess, 0, 0, [])
    for row in resultMatrix:
        print(row)


if __name__ == '__main__':
    execute()
