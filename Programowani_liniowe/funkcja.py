import math
import Parser


class Funkcja:
    def __init__(self, znak):
        self.tablica_wspolczynnikow = []
        self.znak = znak
        self.wyraz_wolny = 0
        self.ilosc_niezerowych_wspolczynnikow = 0
        self.indeksy_niezerowych_wspolczynnikow = []

    def dodal_wspolczynnik(self, wspolczynnik):
        self.tablica_wspolczynnikow.append(wspolczynnik)
        if wspolczynnik != 0:
            self.ilosc_niezerowych_wspolczynnikow += 1
            self.indeksy_niezerowych_wspolczynnikow.append(len(self.tablica_wspolczynnikow)-1)

    def ustaw_wyraz_wolny(self, wartosc):
        self.wyraz_wolny = wartosc

    def wczytaj_wspolczynniki(self):
        ind = 0
        while True:
            print("Proszę podać współczynnik przy zmiennej x" + str(ind))
            ind += 1
            self.dodal_wspolczynnik(float(input(' ')))
            print("Czy to już ostatnia zmienna w funkcji celu? [t/n]")
            next = input(' ')
            if next == 't':
                break

    def wczytaj_wspolczynniki_parserem(self):
        data = input('Prosze wpisac rownanie')
        max_ind = Parser.znajdz_maksymalny_indeks_x(data)

    def wczytaj_wyraz_wolny(self):
        print("Podaj wyraz wolny: ")
        self.ustaw_wyraz_wolny(float(input(' ')))

    def czy_punkt_spelnia_funkcje(self, punkt):
        wartosc = 0
        for ind, wspolczynnik in enumerate(self.tablica_wspolczynnikow):
            wartosc += wspolczynnik * punkt[ind]
        if self.znak == '=':
            if wartosc == self.wyraz_wolny:
                return True
        elif self.znak == '>':
            if wartosc > self.wyraz_wolny:
                return True
        elif self.znak == '>=':
            if wartosc >= self.wyraz_wolny:
                return True
        elif self.znak == '<':
            if wartosc < self.wyraz_wolny:
                return True
        elif self.znak == '<=':
            if wartosc <= self.wyraz_wolny:
                return True

        return False

    def czy_funkcja_jest_rownaniem(self):
        return self.znak == '='

    def koryguj_do_spelnienia_rownania(self, punkt):
        if self.znak == '=':
            wartosc = self.wyraz_wolny
            korygowany_indeks = self.indeksy_niezerowych_wspolczynnikow[-1]
            for ind in range(len(punkt)):
                if ind == korygowany_indeks:
                    continue
                wartosc -= punkt[ind] * self.tablica_wspolczynnikow[ind]
            punkt[korygowany_indeks] = wartosc/self.tablica_wspolczynnikow[korygowany_indeks]

        return punkt

    def znajdz_wartosc_funkcji_celu_w_punkcie(self, punkt):
        wartosc = 0
        for wsplrz in range(len(punkt)):
            wartosc += punkt[wsplrz] * self.tablica_wspolczynnikow[wsplrz]
        return wartosc

    def znajdz_punkt_najblizej_celu(self, lista_punktow):
        wartosc_najmniejsza = self.znajdz_wartosc_funkcji_celu_w_punkcie(lista_punktow[0])
        wartosc_najwieksza = self.znajdz_wartosc_funkcji_celu_w_punkcie(lista_punktow[0])
        indeks_najlepszego_punktu = -1
        for ind, punkt in enumerate(lista_punktow):
            wartosc = self.znajdz_wartosc_funkcji_celu_w_punkcie(punkt)
            if self.znak == 'min' and wartosc < wartosc_najmniejsza:
                wartosc_najmniejsza = wartosc
                indeks_najlepszego_punktu = ind
            elif self.znak == 'max' and wartosc > wartosc_najwieksza:
                wartosc_najwieksza = wartosc
                indeks_najlepszego_punktu = ind
        if(indeks_najlepszego_punktu == -1):
            print("Coś nie pykło w znajdowaniu najbliższego punktu")
            exit(0)
        print("Najlepszy punkt ma pierwsza wpsolrzedna = " + str(lista_punktow[indeks_najlepszego_punktu][0]))
        return indeks_najlepszego_punktu

    def znajdz_indeks_najblizszego_punktu(self, lista_punktow, indeks_srodkowego):
        srodkowy = lista_punktow[indeks_srodkowego]
        odleglosc = float('inf')
        indeks_najblizszegp = -1
        for ind in range(len(lista_punktow)):
            if ind == indeks_srodkowego:
                continue
            temp_odleglosc = self.oblicz_odleglosc_punktow(srodkowy, lista_punktow[ind])
            if temp_odleglosc < odleglosc:
                odleglosc = temp_odleglosc
                indeks_najblizszegp = ind
        if indeks_najblizszegp == -1:
            print("Coś nie pykło w nwjbliższym")
            exit(0)
        return indeks_najblizszegp

    def oblicz_odleglosc_punktow(self, punkt1, punkt2):
        odleglosc = 0
        for ind in range(len(punkt1)):
            odleglosc += (punkt1[ind] - punkt2[ind])*(punkt1[ind] - punkt2[ind])
        odleglosc = math.sqrt(odleglosc)

        return odleglosc

    def znajdz_promien_nowej_przestrzeni(self, lista_punkow, indeks_srodkowego):
            indeks_najblizszego_punktu = self.znajdz_indeks_najblizszego_punktu(lista_punkow, indeks_srodkowego)
            return self.oblicz_odleglosc_punktow(lista_punkow[indeks_srodkowego], lista_punkow[indeks_najblizszego_punktu])




