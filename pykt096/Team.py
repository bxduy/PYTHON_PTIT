class Member:
    def __init__(self, idM, name, idT, id):
        self.id = id
        self.idM = 'C%03d'%idM
        self.name = name
        self.idT = idT
    def __str__(self):
        return '{} {}'.format(self.idM, self.name)