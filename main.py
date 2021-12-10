if __name__ == '__main__':
    fichier =open ('day1.txt', 'r')
    data = [int(i) for i in fichier.read().split("\n")]
c=0
for j in range(1, len(data)):
    v0 = data[j-1]
    v1 = data[j]

    if v1>v0:
        c=c+1
for k in range(2, len(data)):
    i = k -2
    j = k-1

    so = data[i j k]
    s1 = j k k+1

    tant que j< len(data)

print(c)
    









