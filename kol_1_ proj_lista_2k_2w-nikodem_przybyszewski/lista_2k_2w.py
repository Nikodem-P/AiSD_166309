# kol_1_ proj_lista_2k_2w
# Nikodem Przybyszewski 3IO 166309

from typing import Any, Callable


class ListaWpis:
    wart: str
    nast: 'ListaWpis'
    poprz: 'ListaWpis'

    def __init__(self, wart: Any) -> None:
        self.wart = wart
        self.nast = None
        self.poprz = None

    def dodaj_po_nim(self, wart: Any) -> None:
        nowy = ListaWpis(str(wart))
        nowy.nast = self.nast
        # if nowy.nast is not None:
        nowy.nast.poprz = nowy
        self.nast = nowy
        nowy.poprz = self

    def dodaj_przed_nim(self, wart: Any) -> None:
        nowy = ListaWpis(str(wart))
        nowy.nast = self
        nowy.poprz = self.poprz
        self.poprz = nowy
        nowy.poprz.nast = nowy


class Lista_2k_2w:
    przed_pie: ListaWpis
    za_ost: ListaWpis

    def __init__(self) -> None:
        self.przed_pie = ListaWpis(None)
        self.za_ost = ListaWpis(None)
        self.przed_pie.nast = self.za_ost
        self.za_ost.poprz = self.przed_pie

    def __str__(self) -> str:
        napis = ""
        element: ListaWpis = self.przed_pie

        while element.nast != self.za_ost:
            element = element.nast
            if napis == "":
                napis = f'{element.wart}'
            else:
                napis = f'{napis} <-> {element.wart}'

        # DEBUG
        if napis == "":
            return "LISTA JEST PUSTA"
        return napis

    def dodaj_przed_poczatkiem(self, wart: Any) -> None:
        nowy = ListaWpis(str(wart))
        self.przed_pie.nast.poprz = nowy
        nowy.nast = self.przed_pie.nast
        self.przed_pie.nast = nowy
        nowy.poprz = self.przed_pie
        # self.debug()

    def dodaj_za_koniec(self, wart: Any) -> None:
        nowy = ListaWpis(str(wart))
        self.za_ost.poprz.nast = nowy
        nowy.poprz = self.za_ost.poprz
        self.za_ost.poprz = nowy
        nowy.nast = self.za_ost

    def pobierz_el(self, idx: int) -> ListaWpis:
        if self.przed_pie.nast == self.za_ost:
            raise IndexError("Lista jest pusta.")

        if idx >= self.podaj_dlugosc() - 1:
            raise IndexError("Indeks poza zakresem listy.")

        if idx >= 0:
            element: ListaWpis = self.przed_pie
            for x in range(0, idx + 1):
                element = element.nast
            return element

        if idx < 0:
            element: ListaWpis = self.za_ost
            for x in range(0, idx, -1):
                element = element.poprz
            return element

    def usun_pierwszy(self) -> str:
        # Metoda zakłada, że lista nie jest pusta
        wart = self.przed_pie.nast.wart
        self.przed_pie.nast = self.przed_pie.nast.nast
        self.przed_pie.nast.poprz = self.przed_pie
        return wart

    def usun_ostatni(self) -> str:
        # Metoda zakłada, że lista nie jest pusta
        wart = self.za_ost.poprz.wart
        self.za_ost.poprz = self.za_ost.poprz.poprz
        self.za_ost.poprz.nast = self.za_ost
        return wart

    def podaj_dlugosc(self) -> int:
        dlugosc: int = 0
        element: ListaWpis = self.przed_pie

        while element.nast != self.za_ost:
            element = element.nast
            dlugosc += 1
        return dlugosc

    def odwroc(self) -> 'Lista_2k_2w':
        nowa = Lista_2k_2w()
        element: ListaWpis = self.za_ost.poprz

        while element.poprz is not None:
            nowa.dodaj_za_koniec(element.wart)
            element = element.poprz
        return nowa

    def obrob_wartosci(self, funkcja: Callable[[str], str]) -> None:
        element: ListaWpis = self.przed_pie

        while element.nast != self.za_ost:
            element = element.nast
            element.wart = funkcja(element.wart)
