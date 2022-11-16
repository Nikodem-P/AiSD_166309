from lista_2k_2w import *

# element_a = ListaWpis("a")

lista = Lista_2k_2w()
# lista.debug()
lista.dodaj_przed_poczatkiem("a")
lista.dodaj_przed_poczatkiem("b")
lista.dodaj_za_koniec("c")
lista.dodaj_przed_poczatkiem("pierwszy")
lista.dodaj_za_koniec("ostatni")
trzeci = lista.pobierz_el(2)
drugiodkonca = lista.pobierz_el(-2)
print(lista)
print(f'Dlugosc: {lista.podaj_dlugosc()}')
print(f'Trzeci element na liscie {trzeci.wart}')
print(f'Drugi od konca na liscie {drugiodkonca.wart}')
print(f'Usunieto ostatni: {lista.usun_ostatni()}')
print(lista)
print(f'Usunieto pierwszy: {lista.usun_pierwszy()}')
print(lista)
print("==================================")
lista2 = lista.odwroc()
print(lista2)


def dodaj_plusik(s: str) -> str:
    return s + '+'


lista.obrob_wartosci(dodaj_plusik)
print(lista)

lista.pobierz_el(1).dodaj_po_nim("nowy")
lista.pobierz_el(2).dodaj_po_nim("inf")
lista.pobierz_el(1).dodaj_przed_nim("nowy2")
lista.pobierz_el(3).dodaj_przed_nim("ele")
print(lista)
