import urllib.request
import re

p = re.compile('\S+')
f = open("Image_url.txt","r") # 읽기 모드로 오픈
strs = "imageNet_person"
count = 1
while True: # 무한 반복
    line = f.readline()
    if not line : break # 파일 끝
    url = p.findall(line) #  url변수에 파일 내용 저장
    try:
        urllib.request.urlretrieve(url[1],"./image/"+strs+str(count)+ ".jpg")
        count += 1
    except :
        pass


f.close() # 파일 닫기