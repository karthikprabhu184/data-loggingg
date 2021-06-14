'''dict={'Name':45336,'Phone no':'vsvcbvc','Place':'Udupi','BodyTemp':33}
#print(list(dic))
for i in dic:
  print(i)
  print(dict.get(i))
  a=dict.values()
  b=dict.items()
  #dic.__setitem__(i,'kllk')
'''
ch=int(input("please Press 1 to Enter Persons details and Press 2 To  Exit"))
def register():
 dic = {'Name': ' ', 'Phone no': ' ', 'Place': ' ', 'BodyTemp': ' '}
 j=0
 n = list(map(str,input('Enter Persons Name,Phone no,Place,Body Temp(C) in respective manneer ').split()[:4]))
 for i in dic:
    dic.__setitem__(i,n[j] )
    j=j+1
 print(dic)
 file = open('dataset.txt', 'a')
 file.write(str(dic))
 file.close()
if ch==1:
  register()
  while(True):
   ch = int(input("please Press 1 to Enter Anoher Persons details and Press 2 To  Exit"))
   if ch==1:
      register()
   else:
      exit()
else:
    exit()




