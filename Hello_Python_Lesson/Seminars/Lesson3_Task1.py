sp=[5.11,2,3,4,8]
def max_average(sp):
    max=sp[0]
    sr=0
    for i in sp:
        if i > max:
         max=i
     sr += i
    sr=sr/len(sp)
    rez={}
    rez['максимальный элемент']=max
    rez['среднее арифметическое']=sr

    k=(max,sr,rez)

...
print(len(rez))
for x,y in rez.item():
    print(x,y)
