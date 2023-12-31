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
        """ Palauta laiva alkutilaan."""
        self.osumat = []
        self.tuhottu = False
        self.koordinaatit = self.aseta(0,0)

    def aseta(self, x:int, y:int, vaaka:bool = True) -> list:
        """ Merkataan laivalle koordinaatit, jossa se sijaitsee pelitaulukossa.

        Parametrit
        ----------
        x : int
            X-koordinaatti.

        y : int
            Y-koordinaatti.

        vaaka : bool, valinnainen
            Onko laiva vaaka- (True) vai pystysuunnassa (False).
        
        Palauttaa 
        ----------
        list
            Palauttaa laivan koordinaatit.
        """
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
        """ Merkataan laivaan osuma, jos koordinaatit täsmäävät laivan sijainnin kanssa.

        Parametrit
        ----------
        x : int
            X-koordinaatti.
        y : int
            Y-koordinaatti.

        Palauttaa 
        ----------
        bool
            Palauttaa (True) jos osuma tuli, muuten (False).
        """
        osuma = False
        if (x,y) in self.koordinaatit:
            if (x,y) not in self.osumat:
                self.osumat.append((x,y))
                osuma = True

        if len(self.osumat) == len(self.koordinaatit):
            self.tuhottu = True
        return osuma

    def piirra(self, piirra_kaikki = True) -> Surface:
        """ Piirretään laiva.

        Parametrit
        ----------
        piirra_kaikki : bool, valinnainen
            Piirretäänkö koko laiva vai pelkästään osumat.

        Palauttaa 
        ----------
        pygame.Surface
            Palauttaa pygame.Surface olion, johon laiva on piirretty.
        """
        if len(self.koordinaatit) == 1:
            laiva = Surface((self.ruutu_koko[0], self.ruutu_koko[1]), SRCALPHA)
            if piirra_kaikki:
                laiva = grafiikka.soutuvene(self.ruutu_koko, "brown", vaaka = self.vaaka)
            if self.koordinaatit[0] in self.osumat:
                laiva = grafiikka.osuma(self.ruutu_koko)
                
        else:
            if self.vaaka:
                laiva = Surface((self.ruutu_koko[0] * self.pituus, self.ruutu_koko[1]), SRCALPHA)
                for i in range(len(self.koordinaatit)):
                    if piirra_kaikki:
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
                    if piirra_kaikki:
                        if i == 0:
                            laiva.blit(grafiikka.keula(self.ruutu_koko,"gray", self.vaaka),(0,0))
                        elif i == len(self.koordinaatit) - 1:
                            laiva.blit(grafiikka.pera(self.ruutu_koko,"gray", self.vaaka),(0, i * self.ruutu_koko[1]))
                        else:
                            laiva.blit(grafiikka.keskiosa(self.ruutu_koko,"gray", self.vaaka),(0, i * self.ruutu_koko[1]))
                    if self.koordinaatit[i] in self.osumat:
                        laiva.blit(grafiikka.osuma(self.ruutu_koko),(0, i * self.ruutu_koko[1]))
        return laiva