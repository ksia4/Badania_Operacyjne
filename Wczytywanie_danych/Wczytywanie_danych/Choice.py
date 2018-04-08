class Choice:

    def __init__(self, name):
        self.name = name
        self.opener = "\t<CHOICE>"
        self.closer = "</CHOICE>\n"

    def rename(self, new_name):
        self.name = new_name

    def print(self):
        return self.opener + self.name + self.closer
