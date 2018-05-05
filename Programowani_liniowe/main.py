import funkcja
import zbior_funkcji
import random
import matplotlib.pyplot as plt
import Parser
import ply.lex as lex

if __name__ == '__main__':
    print("Witaj w programie który rozwiąże Twój problem")
#     # lexer = lex.lex
#     # lexer2 = Parser.lex
#
#     # Test it out
#     data = '''
#     3 + 4 * 10.5
#       + -20 *x2
#     '''
#
# # Give the lexer some input
#     Parser.lexer.input(data)
#     while True:
#         tok = Parser.lexer.token()
#         if not tok:
#             break      # No more input
#         print(tok)
#
#     exit(0)


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
    print(tryb)
    funkcja_celu = funkcja.Funkcja(max_or_min)

    print("Proszę wprowadzić współczynniki funkcji celu, numeracja zmiennych od 1")
    funkcja_celu.wczytaj_wspolczynniki()

    print(funkcja_celu.tablica_wspolczynnikow)
    tablica_funkcji = zbior_funkcji.Zbior_funkcji()
    i = 1
    while True:
        znak = input("Podaj znak funkcji f" + str(i))
        i += 1
        temp_funkcja = funkcja.Funkcja(znak)
        temp_funkcja.wczytaj_wspolczynniki()
        temp_funkcja.wczytaj_wyraz_wolny()
        print("Dodano funkcję, jej znak to: " + temp_funkcja.znak)
        print("Jej współczynniki to ")
        print(temp_funkcja.tablica_wspolczynnikow)
        tablica_funkcji.dodaj_funkcje(temp_funkcja)
        print("Czy to już ostatnia funkcja celu? [t/n]")
        next = input(' ')
        if next == 't':
            break

    # lista_indeksow_rownan = tablica_funkcji.zwraca_indeksy_rownan()
    # najkrotsze_rownanie = funkcja_celu
    # for ind in range(len(tablica_funkcji.tablica_funkcji)):
    #     if tablica_funkcji.tablica_funkcji[ind].czy_funkcja_jest_rownaniem():
    #         lista_indeksow_rownan.append(ind)

    # tablica_punktow = []
    # punkt1 = [100, 100]
    # punkt2 = [0, 100]
    # punkt3 = [3500, 0]
    # punkt4 = [2500, 3500]
    # punkt5 = [100, 4000]
    # punkt6 = [1000, 4100]
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt1))
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt2))
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt3))
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt4))
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt5))
    # print(tablica_funkcji.sprawdz_wszystkie_warunk(punkt6))

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

#dalej coś się troszke źle robi...
