import pytest
from board import *
from error import (
                    InvalidHeightError,
                    InvalidWidthError,
                    InvalidTypesAmountError,
                    WrongBlocksChoosenError
                    )


def test_checkMatrixSize1():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'a', 'e', 'd'],
            ['a', 'b', 'a', 'e']
    ]
    assert Board.checkmatrixSize(4, 3, matrix) is False


def test_checkMatrixSize2():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'a', 'e'],
            ['a', 'b', 'a', 'e']
    ]
    assert Board.checkmatrixSize(4, 3, matrix) is True


def test_checkMatrixSize3():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'a', 'e'],
    ]
    assert Board.checkmatrixSize(4, 3, matrix) is False


def test_checkPosition():
    assert Board.checkPosition((3, 3), (3, 2)) is True
    assert Board.checkPosition((3, 3), (2, 2)) is False
    assert Board.checkPosition((3, 3), (3, 3)) is False
    assert Board.checkPosition((0, 1), (1, 1)) is True


def test_invalidPosition():
    board = Board()
    with pytest.raises(WrongBlocksChoosenError):
        board.changePlaces((3, 2), (2, 3))


def test_findTrees():
    assert Board.findThrees(['a', 'a', 'a', 'b', 'b', 'b', 'e', 'f']) == [0, 1, 2, 3, 4, 5]
    assert Board.findThrees(['a', 'b', 'b', 'b', 'b', 'c']) == [1, 2, 3, 4]
    assert Board.findThrees(['b', 'b', 'b']) == [0, 1, 2]
    assert Board.findThrees(['c', 'c', 'a', 'a', 'c', 'c']) == []


def test_findSeries():
    ser1 = [5, 5, 5, 1, 2, 1, 2, 3, 2, 3, 5, 6, 6, 6]
    ser2 = [1, 1, 1]
    ser3 = [4, 4, 4, 2, 2, 1, 1, 1, 1]

    assert Board.findSeries(ser1, columnToCheck=6) == [(0, 6), (1, 6), (2, 6), (11, 6), (12, 6), (13, 6)]
    assert Board.findSeries(ser1, rowToCheck=0) == [(0, 0), (0, 1), (0, 2), (0, 11), (0, 12), (0, 13)]
    assert Board.findSeries(ser2, columnToCheck=5) == [(0, 5), (1, 5), (2, 5)]
    assert Board.findSeries(ser3, rowToCheck=8) == [(8, 0), (8, 1), (8, 2), (8, 5), (8, 6), (8, 7), (8, 8)]


def test_rowsOnColumns():
    matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
    ]
    matrixChanged = Board.rowsOnColumns(matrix)
    assert matrixChanged == [
        ['a', 'd', 'g'],
        ['b', 'e', 'h'],
        ['c', 'f', 'i']
    ]
    assert Board.columnsOnRows(matrixChanged) == matrix


def test_constructor():
    board = Board(5, 7, 5)
    assert board.width() == 5
    assert board.height() == 7
    assert board.blockTypes() == 5
    assert len(board.matrix()) == board.height()
    for row in board.matrix():
        assert len(row) == board.width()


def test_invalidWidth():
    with pytest.raises(InvalidWidthError):
        Board(2, 4, 4)
    with pytest.raises(InvalidWidthError):
        Board(13, 4, 4)


def test_invalidHeight():
    with pytest.raises(InvalidHeightError):
        Board(5, 2, 4)
    with pytest.raises(InvalidHeightError):
        Board(5, 13, 5)


def test_invalidBlockTypes():
    with pytest.raises(InvalidTypesAmountError):
        Board(5, 5, 2)
    with pytest.raises(InvalidTypesAmountError):
        Board(5, 5, 11)


def test_change():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'a', 'e'],
            ['a', 'b', 'a', 'e']
    ]
    board = Board(5, 5, blockTypes=10, matrix=matrix)
    board.changePlaces((0, 3), (0, 2))
    assert board.matrix() == [
            ['a', 'b', 'a', 'c'],
            ['d', 'e', 'a', 'e'],
            ['a', 'b', 'a', 'e']
    ]


def test_noEfectChange():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'b', 'e'],
            ['a', 'b', 'a', 'e']
    ]
    board = Board(5, 5, 8, matrix)
    board.changePlaces((0, 3), (0, 2))
    assert board.matrix() == [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'b', 'e'],
            ['a', 'b', 'a', 'e']
    ]


def test_markThrees():
    matrix = [
            ['a', 'b', 'c', 'd'],
            ['d', 'e', 'f', 'd'],
            ['a', 'b', 'd', 'd']
    ]
    board = Board(5, 5, 10, matrix)
    board.markThrees()
    assert board.matrix() == [
            ['a', 'b', 'c', 0],
            ['d', 'e', 'f', 0],
            ['a', 'b', 'd', 0]
    ]


def test_markThrees2():
    matrix = [
            ['a', 'b', 'c', 'b'],
            ['b', 'b', 'b', 'b'],
            ['a', 'b', 'c', 'b']
    ]
    board = Board(5, 5, 10, matrix)
    board.markThrees()
    assert board.matrix() == [
            ['a', 0, 'c', 0],
            [0, 0, 0, 0],
            ['a', 0, 'c', 0]
    ]


def test_markThrees3():
    matrix = [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'f', 'e'],
            ['a', 'b', 'd', 'e']
    ]
    board = Board(5, 5, 10, matrix)
    board.markThrees()
    assert board.matrix() == [
            ['a', 'b', 'c', 'a'],
            ['d', 'e', 'f', 'e'],
            ['a', 'b', 'd', 'e']
    ]


def test_usuwnaie_trójek(monkeypatch):
    matrix = [
            [1, 5, 3, 5, 1],
            [5, 5, 5, 5, 4],
            [7, 5, 9, 5, 6],
            [3, 3, 1, 4, 6],
            [5, 3, 2, 1, 4]
    ]

    def five(a):
        return 2
    monkeypatch.setattr("board.choice", five)
    board = Board(5, 5, 10, matrix)
    board.removeThrees()
    assert board.matrix() == [
            [2, 2, 2, 2, 1],
            [1, 2, 3, 2, 4],
            [7, 2, 9, 2, 6],
            [3, 3, 1, 4, 6],
            [5, 3, 2, 1, 4]
    ]


def test_findOpportunities1():
    matrix = [
            ['a', 'b', 'c', 'a', 'd'],
            ['d', 'e', 'f', 'e', 'a'],
            ['a', 'b', 'd', 'e', 'e'],
            ['e', 'c', 'a', 'b', 'c'],
            ['a', 'e', 'c', 'd', 'a']
    ]
    board = Board(5, 5, 8, matrix)
    assert board.findOpportunities() is None
    assert board.matrix() == [
            ['a', 'b', 'c', 'a', 'd'],
            ['d', 'e', 'f', 'e', 'a'],
            ['a', 'b', 'd', 'e', 'e'],
            ['e', 'c', 'a', 'b', 'c'],
            ['a', 'e', 'c', 'd', 'a']
    ]



def test_findOpportunities2():
    matrix = [
            ['a', 'b', 'e', 'a', 'd'],
            ['d', 'e', 'f', 'e', 'a'],
            ['a', 'b', 'd', 'e', 'e'],
            ['e', 'c', 'a', 'b', 'c'],
            ['a', 'e', 'c', 'd', 'a']
    ]
    board = Board(5, 5, 8, matrix)
    board.findOpportunities() == [(0, 2), (0, 3)]
    assert board.matrix() == [
            ['a', 'b', 'e', 'a', 'd'],
            ['d', 'e', 'f', 'e', 'a'],
            ['a', 'b', 'd', 'e', 'e'],
            ['e', 'c', 'a', 'b', 'c'],
            ['a', 'e', 'c', 'd', 'a']
    ]
