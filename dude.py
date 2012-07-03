class Dude(object):
    "Dude est l'unite de personnage"
    def __init__(self,agi=0,str=0,wp=0,chr=0,luk=0,hp=0,lvl=0):
        self.agi=agi
        self.str=str
        self.wp=wp
        self.chr=chr
        self.luk=luk
        self.hp=hp
        self.lvl=lvl
    def d_display_caracts(self):
        print "Les caracteristiques sont :%s %s %s %s %s %s %s" %(self.agi,self.str,self.wp,self.chr,self.luk,self.hp,self.lvl)