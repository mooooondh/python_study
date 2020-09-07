# selection_sort01.py

data= [5, 9, 6, 1, 0, 4, 3, 2, 7, 8]

for i in range(len(data)):
    for j in range(i, len(data)):
        if(data[i]> data[j]):
            data[i], data[j]= data[j], data[i]
            pass
        pass
    pass

print(data)
