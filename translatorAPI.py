import requests
import re
result=[]
url="https://www.translatorscafe.com/cafe/SearchJobs.asp?Page="
for i in range(100):
    if i >=1:
        url=url+str(i)
    response=requests.api.get(url=url)
    a=response.text
    dumb=re.findall('%s(.*)%s' % ("/cafe/SelectedJob.asp", "\'>"), a)
    if dumb==[]:
        break
    for i in range(len(dumb)):
        result.append("https://www.translatorscafe.com/cafe/"+dumb[i])
for i in range(len(result)):
    print(result[i])
