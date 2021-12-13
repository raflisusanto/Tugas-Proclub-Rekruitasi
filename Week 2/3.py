mylist = list(input().split())
myset = set(mylist)
mylist_conv = list(myset)

def counter(listall, listone):
    my_dict = {}
    for i in range(len(listone)):
        count = 0
        for j in range(len(listall)):
            if listone[i] == listall[j]:
                count += 1
        my_dict[listone[i]] = count
    return my_dict

jawaban = counter(mylist, mylist_conv)
jawaban = dict(sorted(jawaban.items(), key=lambda x: x[1]))

for k, v in jawaban.items():
    print(k + ':', v)

