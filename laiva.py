from pygame import Surface, draw, SRCALPHA

class Laiva():
    def __init__(self, nimi:str, pituus:int=1, ruutu_koko:tuple=(20,20), vari:tuple=(100,100,100)) -> None:
        self.nimi = nimi
        self.pituus = pituus
        self.vari = vari
        self.ruutu_koko = ruutu_koko

        self.vaaka = True
        self.koordinaatit = self.aseta(0,0)
        self.osumat = []
        self.tuhottu = False

    def resetoi(self) -> None:
        self.osumat = []
        self.tuhottu = False
        self.koordinaatit = self.aseta(0,0)

    def aseta(self, x:int, y:int, vaaka:bool = True) -> list:
        self.koordinaatit = []
        self.osumat = []
        if vaaka:
            for i in range(self.pituus):
                self.koordinaatit.append((x + i, y))
            self.vaaka = True
        else:
            for i in range(self.pituus):
                self.koordinaatit.append((x, y + i))
            self.vaaka = False
        return self.koordinaatit
    
    def osuma(self, x:int, y:int) -> bool:
        osuma = False
        if (x,y) in self.koordinaatit:
            if (x,y) not in self.osumat:
                self.osumat.append((x,y))
                osuma = True

        if len(self.osumat) == len(self.koordinaatit):
            self.tuhottu = True
        return osuma

    def piirra(self) -> Surface:
        if self.vaaka:
            laiva = Surface((self.ruutu_koko[0] * self.pituus, self.ruutu_koko[1]), SRCALPHA)
            for i in range(len(self.koordinaatit)):
                if self.koordinaatit[i] in self.osumat:
                    draw.rect(laiva,(255,0,0),(self.ruutu_koko[0] * i,0,self.ruutu_koko[0],self.ruutu_koko[1]))
                else:
                    draw.rect(laiva,self.vari,(self.ruutu_koko[0] * i,0,self.ruutu_koko[0],self.ruutu_koko[1]))
        else:
            laiva = Surface((self.ruutu_koko[0], self.ruutu_koko[1] * self.pituus), SRCALPHA)
            for i in range(len(self.koordinaatit)):
                if self.koordinaatit[i] in self.osumat:
                    draw.rect(laiva,(255,0,0),(0, self.ruutu_koko[1] * i, self.ruutu_koko[0], self.ruutu_koko[1]))
                else:
                    draw.rect(laiva,self.vari,(0, self.ruutu_koko[1] * i,self.ruutu_koko[0],self.ruutu_koko[1]))
        #laiva.fill(self.vari)
        return laiva