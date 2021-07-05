import requests

f=open('finallink.txt','r')


url=f.readline
r=requests.get(url)
HtmlContent=r.content
a=open('new.txt','wb')
a.write(HtmlContent)
# f=open('new.txt','rb')
# for line in f:
#     encoding = 'utf-8'
#     line=str(line, encoding)
#     if (line.count("Cloudflare")>0):
#         k=open("lik.txt",'a')
#         k.write(line)



# for li in f:
#     url=li
#     r=requests.get(url)
#     HtmlContent=r.content
#     a=open('new.txt','wb')
#     a.write(HtmlContent)
#     f=open('new.txt','rb')
#     for line in f:
#         encoding = 'utf-8'
#         line=str(line, encoding)
#         if (line.count("Cloudflare")>0):
#             k=open("lik.txt",'a')
#             k.write(line)