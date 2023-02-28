from .classModule import Module
from bs4 import BeautifulSoup

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
