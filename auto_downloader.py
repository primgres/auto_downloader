import requests
from bs4 import BeautifulSoup

builds = ["http://198.199.91.139:8333/awesome_feature/", "http://198.199.91.139:8333/handsome_feature/", "http://198.199.91.139:8333/master/"]

for n in builds:
    #Get all existing links
    r = requests.get(n, auth=("qa", "te5tc0munn1tyrock5"))
    soup = BeautifulSoup(r.text, 'html.parser')
    linksArray = []
    for i in soup.find_all("a"):
        if len(i.get("href")) >= 21:
            linksArray.append(i.get("href"))
        else:
            pass

    #Get an index of the latest build
    num_list = []
    num = ""
    for link in linksArray:
        for i in link:
            if i.isdigit():
                num = num + i
            else:
                if num != "":
                    num_list.append(int(num))
                    num = ""
        if num != "":
            num_list.append(int(num))
    index = num_list.index(max(num_list))

    #Download a required file
    gfile = requests.get(n + str(linksArray[index]), auth=("qa", "te5tc0munn1tyrock5"))
    open(linksArray[index], "wb").write(gfile.content)
