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

    marginaali = 20
    pelialue_koko = (400,400)
    pelialue_vari = (0,162,232)

    pelaajan_kentta = piirra_pelialue(pelaajan_laivat, pelialue_koko, pelialue_vari)
    vastustajan_kentta = piirra_pelialue(vastustajan_laivat, pelialue_koko, pelialue_vari)

    # Pelisilmukka alkaa
    while True:
        # Näytön tyhjennys
        naytto.fill((0, 0, 0))

        # Tapahtumien käsittely
        for tapahtuma in pygame.event.get():

            # Ikkunan yläkulman X painike
            if tapahtuma.type == pygame.QUIT:   
                exit()

        # Päivitetään näyttö
        naytto.blit(pelaajan_kentta,(marginaali, naytto.get_height() / 2 - pelaajan_kentta.get_height() / 2))
        naytto.blit(vastustajan_kentta,(naytto.get_width() - vastustajan_kentta.get_width() - marginaali, naytto.get_height() / 2 - pelaajan_kentta.get_height() / 2))
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

def piirra_pelialue(laivataulukko:list, pelialue_koko:tuple=(400,400), pelialue_vari:tuple=(0,162,232) ) -> pygame.Surface:
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
                pygame.draw.rect(pelialue, (0,100,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            
    return pelialue

if __name__ == "__main__":
    peli()