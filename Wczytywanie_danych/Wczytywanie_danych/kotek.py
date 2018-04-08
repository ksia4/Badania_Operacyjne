from xml.dom import minidom

a = []
b=[1,2,3]
c=[2,3,4]

a.append(b)
a.append(c)
print(a)
diff = [b[i] - c[i] for i in range(len(b))]
print(diff)
