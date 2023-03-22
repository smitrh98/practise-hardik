# Python – Vertical Concatenation in Matrix
#Input : [['Gfg', 'good'], ['is', 'for']] 
#Output : ['Gfgis', 'goodfor'] 
#Explanation : Column wise concatenated Strings, 'Gfg' concatenated with 'is', and so on.
m=[['Gfg', 'good'], ['is', 'for']]
m=[['Gfg', 'good', 'geeks'], ['is', 'for', 'best']]
op=[]
for i in range(len(m[0])):
    li=''
    for j in range(len(m)):
        li+=m[j][i]
    op.append(li)
print(op)
