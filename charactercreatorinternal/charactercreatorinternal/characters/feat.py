class Feat:
    fname = ""
    fdescription = ""
    fpreq = []
    fpreqful = True

    def __init__(self, fname, fdescription, fpreq):
        self.fname = fname
        self.fdescription = fdescription
        self.fpreq = fpreq
