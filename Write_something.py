f = open("text.txt","w")

strs = '/home/kdy/information/cfg/img/imageNet_person'
n = int(input('최종번호를 입력하시오 : '))


for i in range(1, n+1):
    data = strs+str(i)+'.jpg\n'
    f.write(data)

f.close()