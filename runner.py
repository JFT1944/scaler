import axios
import requests
import fs

pre = open('pre.txt', 'r')
rPre = pre.read()
rPre = rPre.split('\n')
# print(rPre)
wPro = open('pro.txt', 'a')

for url in rPre:
    # print(url)


########################################################
########################################################

    coward = requests.get(f'https://dss.sc.gov{url}')
    coward = coward.text

    coward = coward.split('\n')



    # print(coward)
    for i in coward:
        indexes = []
        # print(i)
        # print('\n')
        if '@' in i:
            # x = i.index('@')
            # print(i)
            isplit = i.split('@')
            # print(isplit)
            units = '!@#$%^&*()<>?/|}{~:;[]\, '
            for a in reversed(isplit[0]):
                if a in units:
                    indexes.append(isplit[0].index(a))
                    break
            for b in isplit[1]:
                if b in units:
                    indexes.append(isplit[1].index(b))
                    break
            # print(indexes)
            d = isplit[0][indexes[0]:]
            e = isplit[1][:indexes[1]]

            print(d + '@' + e)
            wPro.write(d + '@' + e + '\n')






########################################################
########################################################
        # if '.gov' or 'edu' in i[x:]:
        #     print(i[x:])
        
        # print(i[x:])
        # print(i[:x])
        # print(x)        

pre.close()
wPro.close()