import funkcja
import matplotlib.pyplot as plt
import random


class Zbior_funkcji:
    def __init__(self):
        self.tablica_funkcji = []

    def dodaj_funkcje(self, funkcja):
        self.tablica_funkcji.append(funkcja)

    def zwraca_indeksy_rownan(self):
        lista_indeksow_rownan = []
        for ind in range(len(self.tablica_funkcji)):
            if self.tablica_funkcji[ind].czy_funkcja_jest_rownaniem():
                lista_indeksow_rownan.append(ind)
        return lista_indeksow_rownan

    def korekcta_punktow_do_rownan(self, punkt):
        for funkcja in self.tablica_funkcji:
            funkcja.koryguj_do_spelnienia_rownania(punkt)
        return punkt

    def sprawdz_wszystkie_warunk(self, punkt):
        for funkcja in self.tablica_funkcji:
            if funkcja.czy_punkt_spelnia_funkcje(punkt) == False:
                return False
        return True

    def losuj_zbior_punktow_spelniajacych_warunki_z_odpowiedniego_zakresu(self, punkt_srodkowy, promien):
        tablica_punktow = []
        while len(tablica_punktow) < 1000:
            punkt = []
            for i in range(len(punkt_srodkowy)):
                wartosc = 2*promien*random.random() + (punkt_srodkowy[i] - promien)
                punkt.append(wartosc)
            punkt = self.korekcta_punktow_do_rownan(punkt)
            if self.sprawdz_wszystkie_warunk(punkt):
                tablica_punktow.append(punkt)
                plt.plot(punkt[0], punkt[1], 'o')
        plt.show()
        return tablica_punktow
