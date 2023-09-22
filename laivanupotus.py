import pygame
import random

OHI = -1
OSUMA = -2
TYHJA = 0

LAIVA_1 = 1
LAIVA_2 = 2
LAIVA_3 = 3

def peli():
    pygame.init()

    # Kello
    kello = pygame.time.Clock()

    # Näytön asetukset
    naytto = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Laivanupotus")

    # Pelin alustus
    pelaajan_laivat = laivataulukon_alustus(20,20)
    vastustajan_laivat = laivataulukon_alustus(20,20)

    laivat = [LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_3,LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_2]

    aseta_laivat(pelaajan_laivat, laivat)
    aseta_laivat(vastustajan_laivat, laivat)

    marginaali = 20
    pelialue_koko = (400,400)
    pelialue_vari = (0,162,232)

    vastustajan_vuoro = False

    # Pelisilmukka alkaa
    while True:
        # Näytön tyhjennys
        naytto.fill((0, 0, 0))

        hiiri_x, hiiri_y = pygame.mouse.get_pos()

        pelaajan_kentta = piirra_pelialue(pelaajan_laivat, pelialue_koko, pelialue_vari)
        vastustajan_kentta = piirra_pelialue(vastustajan_laivat, pelialue_koko, pelialue_vari, True)
        pelaajan_kentta = naytto.blit(pelaajan_kentta,(marginaali, naytto.get_height() / 2 - pelaajan_kentta.get_height() / 2))
        vastustajan_kentta = naytto.blit(vastustajan_kentta,(naytto.get_width() - vastustajan_kentta.get_width() - marginaali, naytto.get_height() / 2 - vastustajan_kentta.get_height() / 2))
        
        fontti = pygame.font.SysFont("Arial",20)
        teksti_pelaaja = fontti.render("Pelaajan laivat", True, (255,255,255))
        naytto.blit(teksti_pelaaja,(marginaali, naytto.get_height() / 2 - pelialue_koko[1] / 2 - teksti_pelaaja.get_height()))

        teksti_vastustaja = fontti.render("Vastustajan laivat", True, (255,255,255))
        naytto.blit(teksti_vastustaja,(naytto.get_width() - teksti_vastustaja.get_width() - marginaali, naytto.get_height() / 2 - pelialue_koko[1] / 2 - teksti_pelaaja.get_height()))

        # Tapahtumien käsittely
        for tapahtuma in pygame.event.get():

            # Ikkunan yläkulman X painike
            if tapahtuma.type == pygame.QUIT:   
                exit()

            # Hiiren vasen klikkaus
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == True:
                # Hiirtä klikattu pelaajan alueen päällä
                if pelaajan_kentta.collidepoint(tapahtuma.pos):
                    pelaajan_kentta_x = hiiri_x - marginaali    # Lasketaan uusi hiiren x ja y niin, että pelaajan pelialueen yläkulma on 0,0
                    pelaajan_kentta_y = hiiri_y - (naytto.get_height() / 2 - pelialue_koko[1] / 2)
                    #print("pelaajan kenttä")
                    #print(f"x {pelaajan_kentta_x}, y {pelaajan_kentta_y}")
                    x = int(pelaajan_kentta_x / len(pelaajan_laivat[0]))
                    y = int(pelaajan_kentta_y / len(pelaajan_laivat))
                    print(f"pelaajan x: {x}, y: {y}")

                # Hiirtä klikattu vastustajan alueen päällä
                if vastustajan_vuoro == False:
                    if vastustajan_kentta.collidepoint(tapahtuma.pos):
                        vastustajan_kentta_x = hiiri_x - (naytto.get_width()-(marginaali + pelialue_koko[0]))   # Lasketaan uusi hiiren x ja y niin, 
                        vastustajan_kentta_y = hiiri_y - (naytto.get_height() / 2 - pelialue_koko[1] / 2)       # että vastustajan pelialueen yläkulma on 0,0
                        #print("vastustajan kenttä")
                        #print(f"x {vastustajan_kentta_x}, y {vastustajan_kentta_y}")
                        x = int(vastustajan_kentta_x / len(vastustajan_laivat[0]))
                        y = int(vastustajan_kentta_y / len(vastustajan_laivat))
                        print(f"vastustajan x: {x}, y: {y}")

                        if vastustajan_laivat[y][x] not in [OHI,OSUMA]: 
                            if vastustajan_laivat[y][x] in [LAIVA_1,LAIVA_2,LAIVA_3]:
                                vastustajan_laivat[y][x] = OSUMA
                                print("Osuma")
                                if tarkista_voitto(vastustajan_laivat):
                                    print("voitto!!!")
                            if vastustajan_laivat[y][x] == TYHJA:
                                vastustajan_laivat[y][x] = OHI
                                print("Huti")
                            vastustajan_vuoro = True
                        else:
                            print("Ei voi klikata tähän")

        if vastustajan_vuoro:
            pelaajan_laivat = vastustaja_pelaa(pelaajan_laivat)
            if tarkista_voitto(pelaajan_laivat):
                print("Häviö!!!")
            print("vastustajan vuoro ohi")
            vastustajan_vuoro = False
        # Päivitetään näyttö
        pygame.display.flip()

        # Seuraava frame
        kello.tick(60)

# Funktio, jolla alustetaan laivataulukko
def laivataulukon_alustus(ruutu_maara_y:int, ruutu_maara_x:int) -> list:
    ruudukko = []
    for i in range(ruutu_maara_y):
        rivi = []
        for j in range(ruutu_maara_x):
            rivi.append(TYHJA)
            #rivi.append(random.randint(-1,1))
        ruudukko.append(rivi)
    return ruudukko

# Funktio, jolla piirretään pelitilanne pelaajan ja vastustajan pelialueelle.
def piirra_pelialue(laivataulukko:list, pelialue_koko:tuple=(400, 400), pelialue_vari:tuple=(0, 162, 232), piirra_laivat:bool=True) -> pygame.Surface:
    # Luodaan pelialue
    pelialue = pygame.Surface(pelialue_koko, pygame.SRCALPHA)
    pelialue.fill(pelialue_vari)

    ruutu_maara_y = len(laivataulukko)
    ruutu_maara_x = len(laivataulukko[0])
    ruutu_korkeus = pelialue.get_height() / ruutu_maara_y
    ruutu_leveys = pelialue.get_width() / ruutu_maara_x

    # Piirra pelialueen ruudukko
    for i in range(ruutu_maara_y):
        viiva = pygame.draw.line(pelialue, (0,0,0), (0, i * ruutu_korkeus), (pelialue.get_width(), i * ruutu_korkeus))
    for i in range(ruutu_maara_x):
        viiva = pygame.draw.line(pelialue, (0,0,0), (i * ruutu_leveys, 0), (i * ruutu_leveys, pelialue.get_width()))
    
    # Piirretään pelialue laivataulukon mukaan
    for i in range(ruutu_maara_y):
        for j in range(ruutu_maara_x):
            arvo = laivataulukko[i][j]
            if arvo == TYHJA:
                pass
            if arvo == OHI:
                pygame.draw.rect(pelialue, (100,0,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            if arvo == OSUMA:
                pygame.draw.rect(pelialue, (226,138,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            if arvo in [LAIVA_1,LAIVA_2,LAIVA_3]:
                if piirra_laivat:
                    if arvo == LAIVA_1:
                        pygame.draw.rect(pelialue, (0,100,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
                    elif arvo == LAIVA_2:
                        pygame.draw.rect(pelialue, (255,242,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
                    elif arvo == LAIVA_3:
                        pygame.draw.rect(pelialue, (255,128,255), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            
    return pelialue

# Funktio, jolla laivat lisätään pelaajan ja vastustajan laivataulukkoon.
def aseta_laivat(laivataulukko:list, laivat:list) -> None:
    for i in range(len(laivat)):
        while True:
            # Arvotaan x ja y koordinaatti
            y = random.randint(0, len(laivataulukko) -1)
            x = random.randint(0, len(laivataulukko[0]) -1)

            # Tarkistetaan onko paikka tyhjä ruudukossa
            if laivataulukko[y][x] == TYHJA:
                # Jos laiva on yhden ruudun kokoinen, se voidaan asettaa suoraan.
                if laivat[i] == LAIVA_1:
                    laivataulukko[y][x] = laivat[i]
                    break
                # Jos laiva on pidempi kuin yksi ruutu, tarvitaan lisätarkistuksia
                else:
                    vaaka = random.choice((True,False))     # Arvotaan vaaka- tai pystysuunta
                    if tarkista_laivan_sopivuus(laivataulukko, x, y, laivat[i], vaaka):     # Tarkistetaan sopiiko laiva aiottuun kohtaan kokonaisuudessaan
                        # Asetetaan laiva joko vaaka tai pystysuuntaan ruudukkoon
                        if vaaka:
                            for j in range(laivat[i]):
                                laivataulukko[y][x + j] = laivat[i]
                        else:
                            for j in range(laivat[i]):
                                laivataulukko[y + j][x] = laivat[i]
                        break

# Funktio, jolla tarkistetaan sopiiko laiva aiottuun kohtaan ruudukkoa.
def tarkista_laivan_sopivuus(laivataulukko, x, y, laiva, vaaka):
    sopii = True
    if vaaka == False: # Pystysuunta
        for i in range(laiva):
            if y + i < len(laivataulukko):    # Tarkistetaan meneekö laiva yli ruudukosta 
                if laivataulukko[y][x] == TYHJA:    # Tarkistetaan onko laivan alla tyhjää. 
                    sopii = True
                else:
                    sopii = False                   # Jos löytyy huono kohta, lopetetaan tarkistus
                    break
            else:
                sopii = False
                break
    else: # Vaakasuunta
        for i in range(laiva):
            if x + i < len(laivataulukko[0]):
                if laivataulukko[y][x + i] == TYHJA:
                    sopii = True
                else:
                    sopii = False
                    break
            else:
                sopii = False
                break
    return sopii


# Funktio, jolla tarkistetaan onko laivoja jäljellä
def tarkista_voitto(laivataulukko:list) -> bool:
    voitto = True
    for i in range(len(laivataulukko)):
        if 1 in laivataulukko[i]:
            voitto = False
    return voitto

# Funktio, joka hoitaa vastustajan tekemiset
def vastustaja_pelaa(laivataulukko: list) -> None:
    while True:
        x = random.randint(0, len(laivataulukko[0]) - 1)
        y = random.randint(0, len(laivataulukko) - 1)
        if laivataulukko[y][x] in [TYHJA, LAIVA_1, LAIVA_2, LAIVA_3]:
            if laivataulukko[y][x] in [LAIVA_1, LAIVA_2, LAIVA_3]:
                laivataulukko[y][x] = OSUMA
                print("vastustaja osuma")
            if laivataulukko[y][x] == TYHJA:
                laivataulukko[y][x] = OHI
                print("vastustaja ohi")
            return laivataulukko

if __name__ == "__main__":
    peli()