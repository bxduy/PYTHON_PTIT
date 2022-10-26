class Team:
    def __init__(self, idT, nameT, nameU):
        self.idT = 'Team%02d'%idT
        self.nameT = nameT
        self.nameU = nameU
    def __str__(self):
        return '{} {}'.format(self.nameT, self.nameU)