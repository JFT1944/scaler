import requests

call = requests.get('https://dss.sc.gov/contact-dss/upstate-region/cherokee/')
links = []

file = open('pre.txt', 'a')
# print(call.text)
newCall = call.text.split('\n')
# print(newCall)
for i in newCall:
    if 'href="' in i:
        # links.append(i)
        # print(i)
        newI = i.split('href="')
        # print(newI[1])
        if '/contact-dss/' in newI[1]:
            newI = newI[1].split('</a>')
            newI = newI[0].split('/">')
            print(newI[0])
            # links.append(newI[1])
            # print(newI[1])
            # pri
            file.write(newI[0] + '\n')


print(links)


file.close()