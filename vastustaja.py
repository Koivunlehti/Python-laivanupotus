import random
from laiva import Laiva

class Vastustaja:
    def __init__(self) -> None:
        self.viimeisin_osuma = ()
        self.ensimmainen_osuma = ()
        self.laiva_tuhottu = True
        self.laiva_vaaka = None

        self.suurin_laiva_koko = 1

        self.ammuntojen_maara = 0

    def pelaa(self, pelialue:list, laivat:list[Laiva]) -> tuple[list, list]:
        yrita = True
        OHI = -1
        TYHJA = 0
        yrita_jarkevasti = 0
        ammunnan_tulos = ""

        # Suurin laiva jäljellä
        suurin_laiva = 1
        for laiva in laivat:
            if suurin_laiva < laiva.pituus:
                if laiva.tuhottu == False:
                    suurin_laiva = laiva.pituus
        self.suurin_laiva_koko = suurin_laiva
        print(f"Suurin laiva jäljellä: {self.suurin_laiva_koko}")

        while yrita:
            # Jos edellisellä kerralla tuli osuma mutta laiva ei tuhoutunut, siirrytään hakemaan osuman ympäristöstä.
            if self.laiva_tuhottu == False:
                mahdolliset_kohteet = []
                x = self.viimeisin_osuma[0]
                y = self.viimeisin_osuma[1]

                print(f"onko laiva vaakatasossa: {self.laiva_vaaka}")
                mahdolliset_kohteet = self.__valitse_ymparilta(pelialue, x, y)

                # Tarkistetaan onko mahdollisissa kohteissa jo valmiita osumia laivoihin.
                # Jos on, poistetaan kyseinen kohde
                mahdolliset_kohteet = self.__tarkista_kohteet(mahdolliset_kohteet, laivat)

                # Jos mahdollisia kohteita ei jäänyt jäljelle, palataan alkuperäisen osuman koordinaatteihin ja yritetään sieltä.
                if len(mahdolliset_kohteet) == 0:
                    x = self.ensimmainen_osuma[0]
                    y = self.ensimmainen_osuma[1]
                    mahdolliset_kohteet = self.__valitse_ymparilta(pelialue, x, y)
                    # Tarkistetaan löytyykö alkuperäisen osuman ympäriltä mahdollisia kohteita.
                    mahdolliset_kohteet = self.__tarkista_kohteet(mahdolliset_kohteet, laivat)

                # Palataan normaaliin tilaan jos mahdollisia kohteita ei ollut enää., muuten valitaan jokin mahdollisista kohteista
                if len(mahdolliset_kohteet) <= 0:
                    print("ei mahdollisia kohteita")
                    self.__lopeta_metsastys()
                else:
                    print(f"mahdolliset kohteet {mahdolliset_kohteet}")
                    arvottu_koordinaatti = mahdolliset_kohteet[random.randint(0, len(mahdolliset_kohteet) - 1)]
                    x = arvottu_koordinaatti[0]
                    y = arvottu_koordinaatti[1]
                    print(f"kohteeksi valittu koordinaatti {x} {y}")

            # Jos ei ole tiedossa tiettyä laivaa, suoritetaan satunnaista ammuntaa
            else:
                x = random.randint(0, len(pelialue[0]) - 1)
                y = random.randint(0, len(pelialue) - 1)

                # Tarkistetaan mahtuuko pelaajan suurin laiva valittuun koordinaattiin. 
                # Tällä parannetaan tekoälyn kohteiden valinnan järkevyyttä 
                if self.suurin_laiva_koko > 1:
                    print(f"sopiiko isoin laiva ({y,x}): {self.__tarkista_sopiiko_suurin_laiva(pelialue, x, y)}")
                    if self.__tarkista_sopiiko_suurin_laiva(pelialue, x, y) == False and yrita_jarkevasti < 10:
                        yrita_jarkevasti += 1
                        continue
            
            # Suoritetaan ammunta
            if pelialue[y][x] not in [OHI, TYHJA]:
                for laiva in laivat:
                    if pelialue[y][x] == laiva.nimi:
                        if laiva.osuma(x,y):
                            print("vastustaja osuma")
                            ammunnan_tulos = "Osuma"
                            if laiva.tuhottu != True:
                                if len(self.ensimmainen_osuma) == 0:
                                    self.ensimmainen_osuma = (x, y)
                                if len(self.viimeisin_osuma) > 0 and self.laiva_vaaka == None:
                                    print(f"onko sama x: {self.viimeisin_osuma[0]} == {x}")
                                    if self.viimeisin_osuma[0] == x:
                                        self.laiva_vaaka = False
                                    else:
                                        self.laiva_vaaka = True
                                self.viimeisin_osuma = (x, y)
                                self.laiva_tuhottu = False
                            else:
                                ammunnan_tulos = "Upotus"
                                self.__lopeta_metsastys()
                            yrita = False
                            self.ammuntojen_maara += 1
                            
            elif pelialue[y][x] in [TYHJA]:
                pelialue[y][x] = OHI
                print("vastustaja ohi")
                ammunnan_tulos = "Ohi"
                yrita = False
                self.ammuntojen_maara += 1

        print(f"vastustaja ampunut {self.ammuntojen_maara} kertaa")
        return pelialue, laivat, ammunnan_tulos

    def __tarkista_sopiiko_suurin_laiva(self, pelialue:list, x:int, y:int) -> bool:
        OHI = -1
        perakkaiset_ruudut = 0

        if pelialue[y][x] not in [OHI]:
            # x -akselin tarkistus
            for i in range(x - (self.suurin_laiva_koko - 1), x + self.suurin_laiva_koko):
                if i >= 0 and i < len(pelialue[0]):
                    if pelialue[y][i] in [OHI]:
                        perakkaiset_ruudut = 0
                    else:
                        perakkaiset_ruudut += 1
                    if perakkaiset_ruudut == self.suurin_laiva_koko:
                        return True
            if perakkaiset_ruudut < self.suurin_laiva_koko:
                perakkaiset_ruudut = 0
                for i in range(y - (self.suurin_laiva_koko - 1), y + self.suurin_laiva_koko):
                    if i >= 0 and i < len(pelialue[0]):
                        if pelialue[i][x] in [OHI]:
                            perakkaiset_ruudut = 0
                        else:
                            perakkaiset_ruudut += 1
                        if perakkaiset_ruudut == self.suurin_laiva_koko:
                            return True
        return False

    def __valitse_ymparilta(self, pelialue:list, x:int, y:int) -> list:
        OHI = -1
        mahdolliset_kohteet = []
        if self.laiva_vaaka == None or self.laiva_vaaka == False:
            if y - 1 >= 0:
                if pelialue[y - 1][x] not in [OHI]:
                    mahdolliset_kohteet.append((x, y - 1))
            if y + 1 < len(pelialue):
                if pelialue[y + 1][x] not in [OHI]:
                    mahdolliset_kohteet.append((x, y + 1))
        if self.laiva_vaaka == None or self.laiva_vaaka == True:
            if x - 1 >= 0:
                if pelialue[y][x - 1] not in [OHI]:
                    mahdolliset_kohteet.append((x - 1, y))
            if x + 1 < len(pelialue[0]):
                if pelialue[y][x + 1] not in [OHI]:
                    mahdolliset_kohteet.append((x + 1, y))
        return mahdolliset_kohteet

    def __tarkista_kohteet(self, kohteet:list, laivat:list[Laiva]) -> list:
        for kohde in kohteet:
            for laiva in laivat:
                if kohde in laiva.osumat:
                    print(f"Poista kohde {kohde}")
                    kohteet.remove(kohde)
        return kohteet

    def __lopeta_metsastys(self) -> None:
        self.viimeisin_osuma = ()
        self.laiva_tuhottu = True
        self.laiva_vaaka = None
        self.ensimmainen_osuma = ()
    
