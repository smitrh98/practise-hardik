# Python – Convert Snake case to Pascal case
# Input : geeks_for_geeks Output : GeeksforGeeks
#1
s1="geeks_for_geeks"
li=s1.split("_")
pas_s=''
for i in li:
    pas_s+=i.capitalize()
print(pas_s)
#2
s1="geeks_for_geeks"
pas_s=s1.replace("_"," ").title().replace(" ","")
print(pas_s)