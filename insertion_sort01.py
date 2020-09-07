# insertion_soer01

data= [5, 9, 6, 1, 0, 4, 3, 2, 7, 8]

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j- 1]>= data[j]:
            data[j], data[j- 1]= data[j- 1], data[j]
            pass
        else:
            break
            pass
        pass
    pass

print(data)
