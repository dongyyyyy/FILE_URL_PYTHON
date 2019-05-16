import urllib.request
import re
directory = []
print(directory)

p = re.compile('\S+')
f1 = open ("./checkDirectory.txt","r")
while True:
    line = f1.readline()
    if not line: break  # 파일 끝
    if line[0:1] == '-':
        directory.append(line[1:].rstrip('\n'))
    else :
        directory.append(line.rstrip('\n'))
f1.close()
print(directory);
f = open("./fall11_urls.txt","rt",encoding='UTF8') # 읽기 모드로 오픈
strs = "in_person"
count = 1
while True: # 무한 반복
    line = f.readline()
    if not line : break # 파일 끝
    url = p.findall(line) #  url변수에 파일 내용 저장
    if url[0][0:9] in directory :
        try:
            print(url[0][0:9]);
            urllib.request.urlretrieve(url[1], "G:/imagenet/" + strs + str(count) + ".jpg")
            count += 1
        except:
            pass

f.close() # 파일 닫기