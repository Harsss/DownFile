import requests

for i in range(1,72):
    url="https://libgen.is/search.php?&req=Very+Short+Introductions&phrase=0&view=simple&column=series&sort=extension&sortmode=ASC&page="+str(i) 
    r=requests.get(url)
    HtmlContent=r.content
    a=open('test.txt','wb')
    a.write(HtmlContent)
    f=open('test.txt','rb')
    for line in f:
        encoding = 'utf-8'
        line=str(line, encoding)
        if (line.count("[1]")>0):
            k=open("lk.txt",'a')
            k.write(line)
    
ak=open('lk.txt','r')
for line in ak:
    if len(line)>70:
        z=open("link.txt",'a')
        z.write(line)





