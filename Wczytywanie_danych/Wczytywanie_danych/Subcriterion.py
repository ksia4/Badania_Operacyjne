class Subcriterion:

    def __init__(self, name):
        self.name = name
        self.SubcriterionList = []
        self.opener = "\n\t\t<CRITERION "
        self.closer = "/>\n"
        self.matrix = []

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
        text_matrix += "\""
        return text_matrix

    def print(self):
        text = self.opener + "name=\"" + self.name + "\" m=" + self.print_matrix()
        for crit in self.SubcriterionList:
            text += crit.print()
        text += self.closer
        return text

    def read_matrix(self,List_of_alternatives):
        print("Podaj macierz wag dla kryterium: " + self.name)
        temp = []
        for ind in range(len(List_of_alternatives)-1):
            alter = List_of_alternatives[ind]
            for vs in range(ind+1, len(List_of_alternatives)):
                print("Pod względem " + self.name + " ile razy lepsze jest " + alter.name + " od " + List_of_alternatives[vs].name)
                temp.append(float(input(" ")))
        matrix = []
        for i in range(len(List_of_alternatives)):
            row = []
            for j in range(len(List_of_alternatives)):
                if i == j:
                    row.append(float(1))
                elif i > j:
                    row.append(1/matrix[j][i])
                else:
                    row.append(temp[0])
                    temp.pop(0)
            matrix.append(row)
            self.set_matrix(matrix)
        return matrix

