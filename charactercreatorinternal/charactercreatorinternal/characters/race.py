class Race:
    rname = ""
    rdescription = ""
    rattributes = [0, 0, 0, 0, 0, 0, 0, 0]
    rfeats = []

    def __init__(self, rname, rdescription, rattributes, rfeats):
        self.rname = rname
        self.rdescription = rdescription
        self.rattributes = rattributes
        self.rfeats = rfeats
