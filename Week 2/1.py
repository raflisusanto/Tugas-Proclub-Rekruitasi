x = input()
myset = set(x)

def cariduplikat(s):
    setduplikat = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if i < len(s) and s[i] == s[j]:
                setduplikat.add(s[i])
                i += 1
    return setduplikat

def setstring_to_listint(buSet):
    listInt = list(buSet)
    for i in range(len(listInt)):
        listInt[i] = int(listInt[i])
    return listInt

setdupe = cariduplikat(x)
setangkamunculsekali = myset - setdupe

setangkamunculsekali_conv = setstring_to_listint(setangkamunculsekali)
print(setangkamunculsekali_conv)