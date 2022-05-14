#preparing the list of download links to send requests to
import os 
with open("/home/...") as f:
    content = f.read().splitlines()
for line in content:
    RID_Pos = line.rfind("/apis/") + 6
    RID = line[RID_Pos:]
    link = ("https://api.data.gov.in/resource/"+RID)
    print(link, file=open("/home/...", "a"))


  
