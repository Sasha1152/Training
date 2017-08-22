D = dict()
for i in range(int(input())):
    eng,lat = input().split(" - ")
    for j in lat.split(", "):
        if j in D:
            D[j].append(eng)
        else:
            D[j] = [eng]
print(D)            
L = []
for key,val in D.items():
    L.append([key,val])
L.sort()
print(L)
print(len(L))
for lat,eng in L:
    print(lat,", ".join(eng),sep=" - ")
