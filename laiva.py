from pygame import Surface, draw, SRCALPHA
import grafiikka

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
        if len(self.koordinaatit) == 1:
            if self.koordinaatit[0] in self.osumat:
                laiva = grafiikka.osuma(self.ruutu_koko)
            else:
                laiva = grafiikka.soutuvene(self.ruutu_koko, "brown", vaaka = self.vaaka)
                
        else:
            if self.vaaka:
                laiva = Surface((self.ruutu_koko[0] * self.pituus, self.ruutu_koko[1]), SRCALPHA)
                for i in range(len(self.koordinaatit)):
                    if i == 0:
                        laiva.blit(grafiikka.keula(self.ruutu_koko,"gray", self.vaaka),(0,0))
                    elif i == len(self.koordinaatit) - 1:
                        laiva.blit(grafiikka.pera(self.ruutu_koko,"gray", self.vaaka),(i * self.ruutu_koko[0],0))
                    else:
                        laiva.blit(grafiikka.keskiosa(self.ruutu_koko,"gray", self.vaaka),(i * self.ruutu_koko[0],0))
                    if self.koordinaatit[i] in self.osumat:
                        laiva.blit(grafiikka.osuma(self.ruutu_koko),(i * self.ruutu_koko[0],0))
            else:
                laiva = Surface((self.ruutu_koko[0], self.ruutu_koko[1] * self.pituus), SRCALPHA)
                for i in range(len(self.koordinaatit)):
                    if i == 0:
                        laiva.blit(grafiikka.keula(self.ruutu_koko,"gray", self.vaaka),(0,0))
                    elif i == len(self.koordinaatit) - 1:
                        laiva.blit(grafiikka.pera(self.ruutu_koko,"gray", self.vaaka),(0, i * self.ruutu_koko[1]))
                    else:
                        laiva.blit(grafiikka.keskiosa(self.ruutu_koko,"gray", self.vaaka),(0, i * self.ruutu_koko[1]))
                    if self.koordinaatit[i] in self.osumat:
                        laiva.blit(grafiikka.osuma(self.ruutu_koko),(0, i * self.ruutu_koko[1]))
        return laiva