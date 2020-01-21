#script to download files from web
from urllib import request
my_url= 'https://.....'
def download_file(cvs_url):
    response = request.urlopen(cvs_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'my.csv'
#create a file
    fw = open(dest_url, "w")
    for line in lines:
        fw.write(line +"\n")
    fw.close()
download_file(my_url)