from xml.dom import minidom
from Wczytywanie_danych import Choice, Criterion

class Root:
    def __init__(self):
        self.path_to_file = ""
        self.ChoiceList = []
        self.MainSubcriterion = []
        self.CriterionList = []
        self.opener = "<ROOT>\n"
        self.closer = "</ROOT>"
        self.rank = []

    def read_data(self, name):
        self.path_to_file = name
        xmldoc = minidom.parse(self.path_to_file)
        choices = xmldoc.getElementsByTagName('CHOICE')
        for i in range(len(choices)):
            self.add_choice(Choice.Choice(choices[i].firstChild.data))
        criterion_list = xmldoc.getElementsByTagName('CRITERION')
        self.CriterionList.append(Criterion.Criterion(criterion_list[0].attributes["name"].value))
        main_crit_string_matrix = criterion_list[0].attributes["m"].value
        print(main_crit_string_matrix)
        self.CriterionList[0].set_matrix(self.CriterionList[0].convert_string_matrix_to_float(main_crit_string_matrix))
        self.CriterionList[0].make_tree(criterion_list)
        print(self.print())

    def add_choice(self, choice):
        self.ChoiceList.append(choice)

    def add_subcriterion(self, subcriterion):
        self.MainSubcriterion.append(subcriterion)

    def add_criterion(self, criterion):
        self.CriterionList.append(criterion)

    def print(self):
        text = self.opener
        for choice in self.ChoiceList:
            text +=choice.print()
        for crit in self.CriterionList:
            text += crit.print()
        for subcrit in self.MainSubcriterion:
            text += subcrit.print()
        text += self.closer
        return text

    def calc_rank_eig(self):
        if len(self.MainSubcriterion) > 0:
            self.rank = self.MainSubcriterion[0].calc_rank_eig()
        else:
            self.rank = self.CriterionList[0].calc_rank_eig()
        print(self.rank)

    def calc_rank_geo(self):
        if len(self.MainSubcriterion) > 0:
            self.rank = self.MainSubcriterion[0].calc_rank_geo()
        else:
            self.rank = self.CriterionList[0].calc_rank_geo()
        print(self.rank)




