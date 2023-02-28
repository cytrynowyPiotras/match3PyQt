from error import (
    InvalidWidthError,
    InvalidHeightError,
    InvalidTypesAmountError,
    WrongBlocksChoosenError,
    )
from random import choices, choice
import copy

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


class Board:
    def __init__(self, width=8, height=8, blockTypes=7, matrix=None):
        if width not in range(5, 13):
            raise InvalidWidthError(width)
        self._width = width
        if height not in range(5, 13):
            raise InvalidHeightError(height)
        self._height = height
        if blockTypes not in range(5, 11):
            raise InvalidTypesAmountError(blockTypes)
        self._blockTypes = blockTypes
        if matrix is None:
            self.generateBoard()
            while Board.findThreesOnBoard(self._matrix):
                self.removeThrees()
        else:
            Board.checkmatrixSize(width, height, matrix)
            self._matrix = matrix

    def width(self):
        return self._width

    def height(self):
        return self._height

    def blockTypes(self):
        return self._blockTypes

    def matrix(self):
        return self._matrix

    def type(self, wiersz, kolumna) -> str:
        return copy.deepcopy(self.matrix()[int(wiersz)][int(kolumna)])

    def generateBoard(self) -> None:
        typesList = copy.deepcopy(letters)
        matrix = []
        for wiersz in range(self.height()):
            wiersz_lista = choices(typesList[:self.blockTypes()], k=self.width())
            matrix.append(wiersz_lista)
        self._matrix = matrix

    def changePlaces(self, firstPos: tuple, secPos: tuple):
        matrix = copy.deepcopy(self.matrix())
        if Board.exchangePossibility(firstPos, secPos, matrix):
            y1, x1 = firstPos
            y2, x2 = secPos
            rodzaj1 = self.matrix()[y1][x1]
            rodzaj2 = self.matrix()[y2][x2]
            self._matrix[y2][x2] = rodzaj1
            self._matrix[y1][x1] = rodzaj2

    def markThrees(self):
        listToRemove = Board.findThreesOnBoard(self.matrix())
        if listToRemove:
            for position in listToRemove:
                X, Y = position
                self._matrix[X][Y] = 0

    def removeThrees(self, marked=False):
        if not marked:
            self.markThrees()
        matrix = self.matrix()
        columns = Board.rowsOnColumns(matrix)
        newColumns = []
        for column in columns:
            newColumn = []
            for number in column:
                if number != 0:
                    newColumn.append(number)
            while len(newColumn) != self.height():
                newColumn.insert(0, choice(letters[:self.blockTypes()]))
            newColumns.append(newColumn)
        matrix = Board.columnsOnRows(newColumns)
        self._matrix = matrix

    def findOpportunities(self) -> list:
        row = 0
        for line in self.matrix():
            column = 0
            for litera in line:
                pos = row, column
                posRight = row, column + 1
                posDown = row + 1, column
                if (column + 1) < self.width() and Board.exchangePossibility(pos, posRight, copy.deepcopy(self.matrix())):
                    return [pos, posRight]
                if (row + 1) < self.height() and Board.exchangePossibility(pos, posDown, copy.deepcopy(self.matrix())):
                    return [pos, posDown]
                column += 1
            row += 1
        return None

    def __str__(self):
        text = "   "
        for column in range(self._width):
            text += "%2d" % column
        text += "\n"
        for row in range(self._height):
            text += "%2d " % row
            for column in range(self._width):
                if self._matrix[row][column] is None:
                    text += " " + " "
                else:
                    dane = self._matrix[row][column]
                    if type(dane) == int:
                        dane = str(dane)
                    text += " " + dane
            text += "\n"
        return text

    def countPoints(self) -> int:
        zerosNumber = 0
        for line in self.matrix():
            zerosNumber += line.count(0)
        return zerosNumber

    def checkmatrixSize(width, height, matrix) -> bool:
        if height == len(matrix):
            for wiersz in matrix:
                if len(wiersz) != width:
                    return False
            return True
        return False

    @staticmethod
    def checkPosition(posX: tuple, posY: tuple) -> bool:
        y1, x1 = posX
        y2, x2 = posY
        difX = abs(x1 - x2)
        difY = abs(y1 - y2)
        if difX == 1 and difY == 0:
            return True
        if difX == 0 and difY == 1:
            return True
        else:
            return False

    @staticmethod
    def findThrees(lista) -> list:
        placesList = []
        place = 2
        for type in lista[2:]:
            if lista[place - 1] == type:
                if lista[place - 2] == type:
                    placesList += [place - 2, place - 1, place]
            place += 1
        return list(set(placesList))

    @staticmethod
    def findSeries(lista, columnChecked=None, rowChecked=None) -> list:
        """
        Zwraca listę współrzędnych bloków do usunięcia z danego rzędu
        """
        listToRemove = Board.findThrees(lista)
        pointsList = []
        if columnChecked is not None:
            for row in listToRemove:
                pointsList.append((row, columnChecked))
        if rowChecked is not None:
            for column in listToRemove:
                pointsList.append((rowChecked, column))
        return pointsList

    @staticmethod
    def rowsOnColumns(matrix) -> list:
        width = len(matrix[0])
        columnList = []
        for columnNumber in range(width):
            column = []
            for row in matrix:
                column.append(row[columnNumber])
            columnList.append(column)
        return columnList

    @staticmethod
    def columnsOnRows(matrix) -> list:
        """
        Zmienia listę wierszy na listę kolumn danej matrixy
        """
        return Board.rowsOnColumns(matrix)

    @staticmethod
    def findThreesOnBoard(matrix) -> list:
        """
        Funkcja zwraca listę współrzędnych bloków do usunięcia
        """
        listToRemove = []
        rowNumber = 0
        for row in matrix:
            listToRemove += Board.findSeries(row, rowChecked=rowNumber)
            rowNumber += 1
        columns = Board.rowsOnColumns(matrix)
        columnNumber = 0
        for kolumna in columns:
            listToRemove += Board.findSeries(kolumna, columnChecked=columnNumber)
            columnNumber += 1
        if listToRemove == []:
            return None
        return list(set(listToRemove))

    @staticmethod
    def exchangePossibility(firstPos, secPos, matrix) -> bool:
        matrix_kopia = copy.deepcopy(matrix)
        if Board.checkPosition(firstPos, secPos):
            y1, x1 = firstPos
            y2, x2 = secPos
            rodzaj1 = matrix[y1][x1]
            rodzaj2 = matrix[y2][x2]
            matrix_kopia[y1][x1] = rodzaj2
            matrix_kopia[y2][x2] = rodzaj1
            if Board.findThreesOnBoard(matrix_kopia):
                return True
            else:
                return False
        else:
            raise WrongBlocksChoosenError(firstPos, secPos)
