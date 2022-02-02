class Character:
    cname = ""
    cage = 0
    crace = ""
    cclass = ""
    cclassFeatures = []
    cattributes = [10, 10, 10, 10, 10, 10, 0, 25]
    cfeats = []
    ctraits = []
    cspells = {"0": [], "1": []}

    def __init__(self, cname):
        self.cname = cname

    def new(self, crace, cclass):
        self.crace = crace
        self.cclass = cclass
