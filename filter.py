pRo = open('pro.txt', 'r')
rPro = pRo.read()
rPro = rPro.split('\n')
final = open('final.txt', 'a')

for x in rPro:
        newX = x.split(":")
        print(newX[-1])
        final.write(newX[-1] + '\n')

    