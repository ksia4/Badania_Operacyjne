from xml.dom import minidom

xmldoc = minidom.parse('./nowy.xml')
criterion_list = xmldoc.getElementsByTagName('CRITERION')
print(len(criterion_list))
main_crit = criterion_list[0]
print(len(main_crit.getElementsByTagName('CRITERION')))
# print(len(banan))
# banan2 = banan[0]
print(main_crit.toxml())
print(main_crit.attributes["m"].value)
# for choice in choice_list:
#     print(choice.firstChild.data)
# print(choice_list[0].firstChild.data)
# print(choice_list[1].toxml())
#main_choice = choice_list[0]
# print(main_choice.attributes)
# print(main_choice.attributes.keys())
# print(main_choice.attributes["name"])
# a = main_choice.attributes["m"]
# print(a.name)
# print(a.value)
# nowy = choice_list[0].getElementsByTagName('CRITERION')
# print(nowy[0].toxml())
#getElementByTagName zwraca liste wszystkich elementóœ jakie znajdzie

def convert_string_matrix_to_float(string_matrix):
    rows = string_matrix.split('; ')
    matrix = []
    for el_vect in rows:
        temp_row = []
        temp_el_vect = el_vect.split(' ')
        print(len(temp_el_vect))
        print(temp_el_vect)
        for el in temp_el_vect:
            print(el)
            temp_row.append(float(el))
        matrix.append(temp_row)
    return matrix

moj = "1.0 1.0 2.0; 1.0 1.0 3.0; 0.5 0.3333333333333333 1.0"
m = convert_string_matrix_to_float(moj)
