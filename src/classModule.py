class Module:
    def __init__(self, link, name):
        self.link = link
        self.name = name
    def __repr__(self):
        return f"Module(link='{self.link}', name='{self.name}')"