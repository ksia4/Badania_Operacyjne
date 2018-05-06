import funkcja
import zbior_funkcji
import random
import matplotlib.pyplot as plt
import eksperymenty
import ply.lex as lex

if __name__ == '__main__':
    print("Witaj w programie który rozwiąże Twój problem")
    tryb = -1
    max_or_min = ''
    while tryb < 0:
        print("Czy będziemy maksymalizować czy minimalizować funkcję celu? [max/min]")
        max_or_min = input(' ')
        # 0 - minimalizacja
        # 1 - maksymalizacja
        if max_or_min == 'max':
            tryb = 1
        elif max_or_min == 'min':
            tryb = 0
        else:
            print("Proszę wpisać max lub min :)")
    funkcja_celu = funkcja.Funkcja(max_or_min)

    data = input('Proszę podać funkcję celu (numeracja zmiennych od 1)\nf(X) = ')
    f_celu_dane = eksperymenty.znajdz_wspolczynniki(data)
    f_celu_wsp = f_celu_dane[0]
    funkcja_celu.wyraz_wolny = f_celu_dane[1]
    for wsp in f_celu_wsp:
        funkcja_celu.dodal_wspolczynnik(wsp)

    print(funkcja_celu.tablica_wspolczynnikow)
    tablica_funkcji = zbior_funkcji.Zbior_funkcji()
    i = 1
    while True:
        warunek = input('Proszę podać warunek:\n')
        znak = eksperymenty.rozpoznaj_znak(warunek)
        print(znak)
        print("To był znak")
        [rownanie, wyraz_wolny] = warunek.split(znak)
        print(wyraz_wolny)
        print("A współczynniki:")
        wsp_warunku = eksperymenty.znajdz_wspolczynniki(rownanie)
        temp_funkcja = funkcja.Funkcja(znak)
        for wsp in wsp_warunku[0]:
            temp_funkcja.dodal_wspolczynnik(wsp)
        while len(funkcja_celu.tablica_wspolczynnikow) > len(temp_funkcja.tablica_wspolczynnikow):
            temp_funkcja.dodal_wspolczynnik(float(0))
        while len(funkcja_celu.tablica_wspolczynnikow) < len(temp_funkcja.tablica_wspolczynnikow):
            funkcja_celu.dodal_wspolczynnik(float(0))
        temp_funkcja.wyraz_wolny = float(wyraz_wolny)
        print("Dodano funkcję, jej znak to: " + temp_funkcja.znak)
        print("Jej współczynniki to ")
        print(temp_funkcja.tablica_wspolczynnikow)
        tablica_funkcji.dodaj_funkcje(temp_funkcja)
        print("Czy chcesz dodać kolejną funkcję celu? [t/n]")
        next = input(' ')
        if next == 'n':
            break

    tablica_punktow = []
    while len(tablica_punktow) < 100:
        punkt = []
        for i in range(len(funkcja_celu.tablica_wspolczynnikow)):
            wartosc = 5000*random.random()
            punkt.append(wartosc)
        punkt = tablica_funkcji.korekcta_punktow_do_rownan(punkt)
        if tablica_funkcji.sprawdz_wszystkie_warunk(punkt):
            tablica_punktow.append(punkt)
            plt.plot(punkt[0], punkt[1], 'o')

    plt.show()
    indeks_najlepszego_punktu = funkcja_celu.znajdz_punkt_najblizej_celu(tablica_punktow)
    najlepszy_punkt = tablica_punktow[indeks_najlepszego_punktu]
    # punkt_najblizej_najlepszego_punktu = tablica_punktow[funkcja_celu.znajdz_indeks_najblizszego_punktu(tablica_punktow, indeks_najlepszego_punktu)]
    promien = funkcja_celu.znajdz_promien_nowej_przestrzeni(tablica_punktow, indeks_najlepszego_punktu)
    odleglosc_od_poprzedniego_najlepszego_punktu = 1000000
    while odleglosc_od_poprzedniego_najlepszego_punktu > 1e-5:
        print("Najlepszy punkt ma x wspolrzedna = " + str(najlepszy_punkt[0]))
        print("A promien = " + str(promien))
        nowa_tablica_punktow = tablica_funkcji.losuj_zbior_punktow_spelniajacych_warunki_z_odpowiedniego_zakresu(najlepszy_punkt, promien)
        nowy_indeks_najlepszego_punktu = funkcja_celu.znajdz_punkt_najblizej_celu(nowa_tablica_punktow)
        nowy_najlepszy_punkt = nowa_tablica_punktow[nowy_indeks_najlepszego_punktu]
        promien = funkcja_celu.znajdz_promien_nowej_przestrzeni(nowa_tablica_punktow, nowy_indeks_najlepszego_punktu)
        odleglosc_od_poprzedniego_najlepszego_punktu = funkcja_celu.oblicz_odleglosc_punktow(najlepszy_punkt, nowy_najlepszy_punkt)
        najlepszy_punkt = nowy_najlepszy_punkt
        print("To jest odleglosc_od_wczesniejszego najlepszego punky" + str(odleglosc_od_poprzedniego_najlepszego_punktu))

    for i in range(len(najlepszy_punkt)):
        print("Koordynat: " + str(najlepszy_punkt[i]))
