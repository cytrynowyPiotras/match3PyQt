class InvalidWidthError(Exception):
    def __init__(self, width) -> None:
        super().__init__("Szerokość powinna być z przedziału 5-12")
        self.szerokość = width


class InvalidHeightError(Exception):
    def __init__(self, height) -> None:
        super().__init__("Szerokość powinna być z przedziału 5-12")
        self.wysokość = height


class InvalidTypesAmountError(Exception):
    def __init__(self, types) -> None:
        super().__init__("Rodzaje powinny być z przedziału 5-10")
        self.rodzaje = types


class WrongBlocksChoosenError(Exception):
    def __init__(self, pos1, pos2) -> None:
        super().__init__('Złe współrzędne bloków')
        self.współrzędna1 = pos1
        self.współrzędna2 = pos2
