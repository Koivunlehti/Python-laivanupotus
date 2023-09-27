import random
from laiva import Laiva

class Vastustaja:
    def __init__(self) -> None:
        self.viimeisin_osuma = ()
        self.laiva_tuhottu = True
        self.ammuntojen_maara = 0

    def pelaa(self, pelialue:list, laivat:list[Laiva]) -> tuple[list, list]:
        yrita = True
        OHI = -1
        TYHJA = 0
        while yrita:
            # Jos edellisellä kerralla tuli osuma, mutta laiva ei tuhoutunut
            if self.laiva_tuhottu == False:
                mahdolliset_kohteet = []
                x = self.viimeisin_osuma[0]
                y = self.viimeisin_osuma[1]
                if y - 1 >= 0:
                    if pelialue[y - 1][x] not in [OHI]:
                        mahdolliset_kohteet.append((x, y - 1))
                if y + 1 < len(pelialue):
                    if pelialue[y + 1][x] not in [OHI]:
                        mahdolliset_kohteet.append((x, y + 1))
                if x - 1 >= 0:
                    if pelialue[y][x - 1] not in [OHI]:
                        mahdolliset_kohteet.append((x - 1, y))
                if x + 1 < len(pelialue[0]):
                    if pelialue[y][x + 1] not in [OHI]:
                        mahdolliset_kohteet.append((x + 1, y))

                for kohde in mahdolliset_kohteet:
                    for laiva in laivat:
                        if kohde in laiva.osumat:
                            print(f"Poista kohde {kohde}")
                            mahdolliset_kohteet.remove(kohde)

                if len(mahdolliset_kohteet) <= 0:
                    print("ei mahdollisia kohteita")
                    self.viimeisin_osuma = ()
                    self.laiva_tuhottu = True
                else:
                    print(f"mahdolliset kohteet {mahdolliset_kohteet}")
                    arvottu_koordinaatti = mahdolliset_kohteet[random.randint(0, len(mahdolliset_kohteet) - 1)]
                    x = arvottu_koordinaatti[0]
                    y = arvottu_koordinaatti[1]
                    print(f"kohteeksi valittu koordinaatti {x} {y}")
            else:
                x = random.randint(0, len(pelialue[0]) - 1)
                y = random.randint(0, len(pelialue) - 1)

            if pelialue[y][x] not in [OHI, TYHJA]:
                for laiva in laivat:
                    if pelialue[y][x] == laiva.nimi:
                        if laiva.osuma(x,y):
                            print("vastustaja osuma")
                            if laiva.tuhottu != True:
                                self.viimeisin_osuma = (x, y)
                                self.laiva_tuhottu = False
                            else:
                                self.viimeisin_osuma = ()
                                self.laiva_tuhottu = True
                            yrita = False
                            self.ammuntojen_maara += 1
                            
            elif pelialue[y][x] in [TYHJA]:
                pelialue[y][x] = OHI
                print("vastustaja ohi")
                yrita = False
                self.ammuntojen_maara += 1

        print(f"vastustaja ampunut {self.ammuntojen_maara} kertaa")
        return pelialue, laivat
    
