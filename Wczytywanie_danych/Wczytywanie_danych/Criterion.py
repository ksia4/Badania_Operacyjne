from Wczytywanie_danych import Subcriterion as sc
import numpy.linalg as lin
import math

class Criterion:

    def __init__(self, name):
        self.name = name
        self.SubcriterionList = []
        self.opener = "\t<CRITERION "
        self.closer = "\t</CRITERION>\n"
        self.matrix = []
        self.rank_eig = []
        self.rank_geo = []
        self.weights_vector_eig = []
        self.weights_vector_geo = []

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
            strip_el = el_vect.strip()
            print(strip_el)
            if(len(strip_el) < 1):
                continue
            temp_row = []
            # temp_el_vect = el_vect.split(' ')
            temp_el_vect = strip_el.split(' ')
            for el in temp_el_vect:
                print(el)
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

    def norm_vector(self, vect):
        sum = 0
        for el in vect:
            sum += el
        rank = [x / sum for x in vect]
        return rank

    def calc_eig_weights_vector(self):
        [val, vect] = lin.eig(self.matrix)
        max_ind = 0
        max_val = val[0].real
        for i in range(len(val)):
            if val[i].real > max_val:
                max_val = val[i].real
                max_ind = i
        rank_vect = vect[:, max_ind]
        self.weights_vector_eig = self.norm_vector(rank_vect)
        return self.weights_vector_eig

    def calc_rank_eig(self):
        self.calc_eig_weights_vector()
        sub_rank_list = []
        for ind, subcrit in enumerate(self.SubcriterionList):
            subcrit_rank = subcrit.calc_rank_eig()
            subcrit_rank = [x * self.weights_vector_eig[ind] for x in subcrit_rank]
            sub_rank_list.append(subcrit_rank)

        rank = []
        for i in range(len(sub_rank_list[0])):
            sum = 0
            for el in sub_rank_list:
                sum += el[i]
            rank.append(sum.real)
        self.rank_eig = rank
        return self.rank_eig

    def calc_geo_weights_vector(self):
        for row in self.matrix:
            mul = 1
            for el in row:
                mul*= el
            val = math.pow(mul, 1.0/len(row))
            self.weights_vector_geo.append(val)
        self.weights_vector_geo = self.norm_vector(self.weights_vector_geo)
        return self.weights_vector_geo

    def calc_rank_geo(self):
        self.calc_geo_weights_vector()
        sub_rank_list = []
        for ind, subcrit in enumerate(self.SubcriterionList):
            subcrit_rank = subcrit.calc_rank_geo()
            subcrit_rank = [x * self.weights_vector_geo[ind] for x in subcrit_rank]
            sub_rank_list.append(subcrit_rank)

        rank = []
        for i in range(len(sub_rank_list[0])):
            sum = 0
            for el in sub_rank_list:
                sum += el[i]
            rank.append(sum.real)
        self.rank_geo = rank
        return self.rank_geo

