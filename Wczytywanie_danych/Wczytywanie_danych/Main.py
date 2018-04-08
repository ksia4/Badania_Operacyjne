from Wczytywanie_danych import Root as r
from Wczytywanie_danych import Choice as ch
from Wczytywanie_danych import Criterion as cr
from Wczytywanie_danych import Subcriterion as sc

print("Witaj w programie pomagającym w podjęciu wielokryterialnej decyzji :)")
print("Czy chcesz:\n0 - zakończyć działanie programu\n1 - wczytać dane z pliku\n2 - stworzyć nowy plik z danymi")
to_do = int(input(" "))


if to_do == 0:
    exit()


elif to_do == 1:
    print("podaj nazwe pliku xml, z którego chcesz odczytać dane: ")
    name = input() + ".xml"
    read_root = r.Root()
    read_root.read_data(name)
    print(name)
    read_root.calc_rank_eig()


elif to_do == 2:
    root = r.Root()
    no_of_choices = int(input("Podaj ilość alternatyw: "))
    for i in range(no_of_choices):
        choice = input("Podaj nzwę alternatywy: ")
        root.add_choice(ch.Choice(choice))

    criterium = input("Podaj nazwę głównego kryterium: ")
    has_Subcriteries = int(input("Czy to kryterium będzie miało podkryteria? 1 - tak 0 - nie "))
    if has_Subcriteries == 0:
        last_criterium = sc.Subcriterion(criterium)
        root.add_subcriterion(last_criterium)
        root.MainSubcriterion[0].read_matrix(root.ChoiceList)

    if has_Subcriteries == 1:
        main_crit = cr.Criterion(criterium)
        root.add_criterion(main_crit)
        no_of_subcriterions = int(input("Podaj ile podkryteriów będzie miało to kryterium: "))
        for subcrit in range(no_of_subcriterions):
            root.CriterionList[0].add_subcriterion()

        for crit in root.CriterionList:
            crit.read_matrix(root.ChoiceList)

    print(root.print())
    print("Tak będzie wyglądał wygenerowany dokument")
    path = input("podaj nazwę pliku xml do którego chcesz wpisać wygenerowaną strukturę")
    path += ".xml"
    plik = open(path, 'w')
    plik.write(root.print())
    plik.close()
    root.calc_rank_eig()
