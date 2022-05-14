import os
import requests
import csv
#from multiprocessing.pool import ThreadPool

def download_url(url):
    output_directory = '/home/.../'
    file_name_start_pos = url.rfind("/resource/") + 1
    file_name = url[file_name_start_pos:]
    file_path = os.path.join(output_directory, file_name+".csv")
    r = requests.get(url, stream = True, params={'api-key':'     ', 
                                                    'format': 'csv', 
                                                    'limit': 20000})
    with open(file_path, 'wb') as f:
        for ch in r:
            f.write(ch)
          
#file with links to datasets
with open("/home/...") as i:
    urls = i.read().splitlines()
    for line in urls:
        download_url(line)
        
