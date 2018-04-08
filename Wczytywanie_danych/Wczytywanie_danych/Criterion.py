from Wczytywanie_danych import Subcriterion as sc

class Criterion:

    def __init__(self, name):
        self.name = name
        self.SubcriterionList = []
        self.opener = "\t<CRITERION "
        self.closer = "\t</CRITERION>\n"
        self.matrix = []

    def add_subcriterion(self):
        subcriterium = input("Podaj nazwę podkryterium: " + self.name + " ")
        temp = int(input("Czy kryterium " + subcriterium + " będzie miało podkryteria? 1 - tak 0 - nie"))
        if temp == 0:
            subcriterium2 = sc.Subcriterion(subcriterium)
            self.SubcriterionList.append(subcriterium2)
        elif temp != 0:
            subcriterium2 = Criterion(subcriterium)
            subcriterium2.opener = "\t" + subcriterium2.opener
            subcriterium2.closer = "\t" + subcriterium2.closer
            self.SubcriterionList.append(subcriterium2)
            ile = int(input("Ile podkryteriów będzie mieć " + subcriterium + " "))
            for i in range(ile):
                last = len(self.SubcriterionList) - 1
                self.SubcriterionList[last].add_subcriterion()

    def add_subcriterion_from_file(self, subcriterion):
        self.SubcriterionList.append(subcriterion)

    def set_matrix(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        text_matrix = "\""
        for i in self.matrix:
            for j in i:
                text_matrix += str(j) + " "
            text_matrix = text_matrix.strip(' ')
            text_matrix += "; "
        text_matrix = text_matrix.strip('; ')
        text_matrix += "\">\n"
        return text_matrix

    def print(self):
        text = self.opener + "name=\"" + self.name + "\" m=" + self.print_matrix()
        for crit in self.SubcriterionList:
            text += crit.print()
        text += self.closer
        return text

    def read_matrix(self, List_of_alternatives):
        print("Podaj macierz wag dla kryterium: " + self.name)
        temp = []
        for ind in range(len(self.SubcriterionList)-1):
            subcrit = self.SubcriterionList[ind]
            for vs in range(ind+1, len(self.SubcriterionList)):
                print("Ile razy ważniejsze jest dla Ciebie " + subcrit.name + " od " + self.SubcriterionList[vs].name)
                temp.append(float(input(" ")))
        matrix = []
        for i in range(len(self.SubcriterionList)):
            row = []
            for j in range(len(self.SubcriterionList)):
                if i == j:
                    row.append(float(1))
                elif i > j:
                    row.append(1/matrix[j][i])
                else:
                    row.append(temp[0])
                    temp.pop(0)
            matrix.append(row)
        self.set_matrix(matrix)
        self.read_subcriterion_matrix(List_of_alternatives)

    def read_subcriterion_matrix(self, List_of_alternatives):
        for subcrit in self.SubcriterionList:
            if len(subcrit.SubcriterionList) > 0:
                subcrit.read_matrix(List_of_alternatives)
            else:
                matrix = subcrit.read_matrix(List_of_alternatives)
                subcrit.set_matrix(matrix)

    def convert_string_matrix_to_float(self, string_matrix):
        rows = string_matrix.split('; ')
        matrix = []
        for el_vect in rows:
            temp_row = []
            temp_el_vect = el_vect.split(' ')
            for el in temp_el_vect:
                temp_row.append(float(el))
            matrix.append(temp_row)
        return matrix

    def make_tree(self, criterion_list, start=1):
        all_len = len(criterion_list)
        print("dlugosc drzewa")
        print(all_len)
        i = start
        while i < all_len:
            print("ktory element")
            print(i)
            subtree = criterion_list[i].getElementsByTagName('CRITERION')
            subtree_size = len(subtree)
            main_subcrit_name = criterion_list[i].attributes["name"].value
            main_subcrit_string_matrix = criterion_list[i].attributes["m"].value
            main_subcrit_matrix = self.convert_string_matrix_to_float(main_subcrit_string_matrix)
            if subtree_size == 0:
                print("Dodałem Liścia!")
                main_subcrit = sc.Subcriterion(main_subcrit_name)
                main_subcrit.set_matrix(main_subcrit_matrix)
                i += 1
            else:
                main_subcrit = Criterion(main_subcrit_name)
                main_subcrit.set_matrix(main_subcrit_matrix)
                #wywołaj znów te funkcje od właśnie utworzonego kryterium
                main_subcrit.make_tree(subtree, 0)
                i += subtree_size + 1

            self.add_subcriterion_from_file(main_subcrit)


