import pygame
import random

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
    aseta_laivat(pelaajan_laivat)
    aseta_laivat(vastustajan_laivat)

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
                        if vastustajan_laivat[y][x] == 1:
                            vastustajan_laivat[y][x] = 2
                            print("Osuma")
                            if tarkista_voitto(vastustajan_laivat):
                                print("voitto!!!")
                        if vastustajan_laivat[y][x] == 0:
                            vastustajan_laivat[y][x] = -1
                            print("Huti")
                        vastustajan_vuoro = True

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

def laivataulukon_alustus(ruutu_maara_y:int, ruutu_maara_x:int) -> list:
    ruudukko = []
    for i in range(ruutu_maara_y):
        rivi = []
        for j in range(ruutu_maara_x):
            rivi.append(0)
            #rivi.append(random.randint(-1,1))
        ruudukko.append(rivi)
    return ruudukko

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
    
    # Päivitetään pelialue laivataulukon mukaan
    for i in range(ruutu_maara_y):
        for j in range(ruutu_maara_x):
            arvo = laivataulukko[i][j]
            if arvo == 0:
                pass
            if arvo == -1:
                pygame.draw.rect(pelialue, (100,0,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            if arvo == 1:
                if piirra_laivat:
                    pygame.draw.rect(pelialue, (0,100,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            if arvo == 2:
                pygame.draw.rect(pelialue, (226,138,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            
    return pelialue

def aseta_laivat(laivataulukko:list) -> None:
    for i in range(10):
        while True:
            y = random.randint(0, len(laivataulukko) -1)
            x = random.randint(0, len(laivataulukko[0]) -1)
            if laivataulukko[y][x] == 0:
                laivataulukko[y][x] = 1
                break

def tarkista_voitto(laivataulukko:list) -> bool:
    voitto = True
    for i in range(len(laivataulukko)):
        if 1 in laivataulukko[i]:
            voitto = False
    return voitto

def vastustaja_pelaa(laivataulukko: list) -> None:
    while True:
        x = random.randint(0, len(laivataulukko[0])- 1)
        y = random.randint(0, len(laivataulukko)- 1)
        if laivataulukko[y][x] == 0 or laivataulukko[y][x] == 1:
            if laivataulukko[y][x] == 1:
                laivataulukko[y][x] = 2
                print("vastustaja osuma")
            if laivataulukko[y][x] == 0:
                laivataulukko[y][x] = -1
                print("vastustaja ohi")
            return laivataulukko

    

if __name__ == "__main__":
    peli()