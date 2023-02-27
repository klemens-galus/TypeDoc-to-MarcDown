from bs4 import BeautifulSoup
import urllib.request
import os
import pathlib
class Module:
    def __init__(self, link, name):
        self.link = link
        self.name = name
    def __repr__(self):
        return f"Module(link='{self.link}', name='{self.name}')"

def checkClasses(mod):
    webpage = open("./docs/"+mod.link)
    soup = BeautifulSoup(webpage, 'html.parser')
    classes = []

    for anchor in soup.find_all("a", {"class": "tsd-index-link tsd-kind-class tsd-parent-kind-module"}, href=True):
        link = str(anchor.get('href'))
        name = str(anchor.find('span'))
        name = name.replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
        classes.append(Module(link,name))
    for clas in classes:
        reallink = clas.link.rsplit('/', 1)[-1].replace(".html", ".md")
        sf = open('/usr/src/app/mdDock/classes/'+reallink,'w')
        print(clas.link)
        print(clas.name)

def checkVars(mod):
    webpage = open("./docs/"+mod.link)
    soup = BeautifulSoup(webpage, 'html.parser')
    classes = []

    for anchor in soup.find_all("a", {"class": "tsd-index-link tsd-kind-variable tsd-parent-kind-module"}, href=True):
        link = str(anchor.get('href'))
        name = str(anchor.find('span'))
        name = name.replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
        classes.append(Module(link,name))
    for clas in classes:
        reallink = clas.link.rsplit('/', 1)[-1].replace(".html", ".md")
        sf = open('/usr/src/app/mdDock/variables/'+reallink,'w')
        print(clas.link)
        print(clas.name)

def checkFunc(mod):
    webpage = open("./docs/"+mod.link)
    soup = BeautifulSoup(webpage, 'html.parser')
    classes = []

    for anchor in soup.find_all("a", {"class": "tsd-index-link tsd-kind-function tsd-parent-kind-module"}, href=True):
        link = str(anchor.get('href'))
        name = str(anchor.find('span'))
        name = name.replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
        classes.append(Module(link,name))
    for clas in classes:
        reallink = clas.link.rsplit('/', 1)[-1].replace(".html", ".md")
        sf = open('/usr/src/app/mdDock/functions/'+reallink,'w')
        print(clas.link)
        print(clas.name)

def checkTypes(mod):
    webpage = open("./docs/"+mod.link)
    soup = BeautifulSoup(webpage, 'html.parser')
    classes = []

    for anchor in soup.find_all("a", {"class": "tsd-index-link tsd-kind-type-alias tsd-parent-kind-module"}, href=True):
        link = str(anchor.get('href'))
        name = str(anchor.find('span'))
        name = name.replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
        classes.append(Module(link,name))
    for clas in classes:
        reallink = clas.link.rsplit('/', 1)[-1].replace(".html", ".md")
        sf = open('/usr/src/app/mdDock/types/'+reallink,'w')
        print(clas.link)
        print(clas.name)





webpage = open("./docs/modules.html")
soup = BeautifulSoup(webpage, 'html.parser')
modules = []

md_dir = "./mdDoc/"

os.mkdir("/usr/src/app/mdDock/classes")
os.mkdir("/usr/src/app/mdDock/modules")
os.mkdir("/usr/src/app/mdDock/types")
os.mkdir("/usr/src/app/mdDock/variables")
os.mkdir("/usr/src/app/mdDock/functions")




for anchor in soup.find_all("a", {"class": "tsd-index-link tsd-kind-module"}, href=True):
    link = str(anchor.get('href'))
    name = str(anchor.find('span'))
    name = name.replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
    modules.append(Module(link,name))

for module in modules:
    reallink = module.link.rsplit('/', 1)[-1].replace(".html", ".md")
    sf = open('/usr/src/app/mdDock/modules/'+reallink,'w')
    #print(module.link)
    print(module.link)
    print(module.name)
    checkClasses(module)
    checkVars(module)
    checkTypes(module)
    checkFunc(module)
    
    print('\n')


#docker run -it --rm -v C:\Users\galus.klemens\Desktop\DocToMd\mdDock:/usr/src/app/mdDock --name my-running-app my-python-app
