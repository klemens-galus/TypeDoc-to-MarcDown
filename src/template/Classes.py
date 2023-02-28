from bs4 import BeautifulSoup
from ..classModule import Module

def TemplateClasses(mod, sf):
    webpage = open("./docs/"+mod)
    soup = BeautifulSoup(webpage, 'html.parser')
    for cat in soup.find_all("section", {"class":"tsd-index-section"}):
        cate = cat.find("h3", {"class":"tsd-index-heading"})
        sf.write("## "+cate.text + "\n")
        for cat2 in cat.find_all("a"):
            cate2 = str(cat2.find('span')).replace("<span>", "").replace("<wbr/>", "").replace("</span>", "")
            cate2ref = str(cat2.get('href')).rsplit('#', 1)[-1]

            sf.write("- ["+cate2+"](#"+cate2ref+")\n")

    sf.write("---\n")
    for cat in soup.find_all("section", {"class":"tsd-panel-group tsd-member-group"}):
        cate = cat.find("h2")
        sf.write("# "+cate.text+"\n")
        for cateSection in cat.find_all("section", {"class":"tsd-panel tsd-member tsd-kind-method tsd-parent-kind-class"}):
            cate = cateSection.find("h3")
            sf.write("### "+str(cate.find("span")).replace("<span>", "").replace("<wbr/>", "").replace("</span>", "") + "\n")
        
    sf.close()