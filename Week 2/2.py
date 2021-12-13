mylist = list(map(int, input().split()))
target = int(input())

def findAngka_equaltarget(listo, target):
    listIndeks = list()
    for i in range(len(listo)):
        for j in range(i+1, len(listo)):
            if i < len(listo) and listo[i] + listo[j] == target:
                listIndeks.append(i)
                listIndeks.append(j)
                break
            elif listo[i] + listo[j] > target:
                i += 1
    return listIndeks

jawaban = findAngka_equaltarget(mylist, target)
print(jawaban)