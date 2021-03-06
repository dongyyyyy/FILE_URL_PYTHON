import urllib.request
import re

def main():
    count = 1
    global p
    p= re.compile('\S+')
    nowurl = "http://image-net.org/api/text/wordnet.structure.hyponym?wnid="
    strs = "in_person"
    a = urllib.request.urlopen(nowurl + "n00007846")
    while True: # 무한 반복
        line = a.readline().decode("utf-8")
        if not line: break  # 파일 끝
        if line[0:1] == '-':
            line.rstrip('\n')
            line = line.replace('-','',1)
            print(line)
            sub(line,count)
        else:
            line.rstrip('\n')
            count = download(line,count)

def sub(wnid,count):
    nowurl = "http://image-net.org/api/text/wordnet.structure.hyponym?wnid="
    cururl = nowurl + wnid
    a = urllib.request.urlopen(cururl)
    while True:  # 무한 반복
        line = a.readline().decode("utf-8")
        if not line: break  # 파일 끝
        if line[0:1] == '-':
            line.rstrip('\n')
            line = line.replace('-', '', 1)
            print(line)
            sub(line,count)
        else:
            line.rstrip('\n')
            count = download(line,count)

def download(wnid,count):
    count = int(count)
    strs = "in_person"
    f = open("./fall11_urls.txt","rt",encoding='utf-8') # 읽기 모드로 오픈
    print("current count : " + str(count))
    while True:
        downloadurl = f.readline()
        if not downloadurl: break  # 파일 끝
        url = p.findall(downloadurl)  # url변수에 파일 내용 저장
        if url[0][0:9] in wnid and url[0][0:9] != "n00007846":
            try:
                print("directory : "  + url[0][0:9])
                urllib.request.urlretrieve(url[1], "G:/imagenet/" + strs + str(count) + ".jpg")
                count += 1
            except:
                pass
    f.close()
    print("return count : " + str(count))
    return count
main()

