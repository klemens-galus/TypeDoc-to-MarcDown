from bs4 import BeautifulSoup
import urllib.request
import os
import pathlib

from src.classModule import Module 
from src.checkFunctions import checkFunc
from src.checkVars import checkVars
from src.checkClasses import checkClasses
from src.checkTypes import checkTypes 


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
    print(module.name)
    checkClasses(module)
    checkVars(module)
    checkTypes(module)
    checkFunc(module)
    
    print('\n')


#docker run -it --rm -v C:\Users\galus.klemens\Desktop\DocToMd\mdDock:/usr/src/app/mdDock --name my-running-app my-python-app
