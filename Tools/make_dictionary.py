import re

def get_text_from_file():
    s = []
    with open('/home/piotrek/Dokumenty/iso9.txt', mode='r', encoding='utf-8') as ff:
        for line in ff.readlines():
            s.append(re.split(r"\s+", line)[:4] if re.search(r"\d",re.split(r"\s+", line)[3]) else re.split(r"\s+", line)[:6])
    return s


a=get_text_from_file()
result = {}

i = 0
while i < len(a):

    if len(a[i]) == 5 and a[i][4]=='' :
        a[i]=a[i][:4]

    if len(a[i]) == 4 :
        result[a[i][0]] = a[i][2]
        result[a[i][1]] = a[i][3]
    if len(a[i]) == 6 :
        result[a[i][0]] = a[i][4]
        result[a[i][1]] = a[i][5]
    i+=1

print(result, )
#def make_dictionary(sss):
