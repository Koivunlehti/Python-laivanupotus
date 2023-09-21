import pygame

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

    pelaajan_kentta = pygame.Surface(pelialue_koko, pygame.SRCALPHA)
    pelaajan_kentta.fill(pelialue_vari)
    pelaajan_kentta = viivoita_pelialue(pelaajan_kentta,len(pelaajan_laivat),len(pelaajan_laivat[0]))

    vastustajan_kentta =  pygame.Surface(pelialue_koko, pygame.SRCALPHA)
    vastustajan_kentta.fill(pelialue_vari)
    vastustajan_kentta = viivoita_pelialue(vastustajan_kentta,len(vastustajan_laivat),len(vastustajan_laivat[0]))


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
        ruudukko.append(rivi)
        #print(rivi)
    #print("--------------------")
    return ruudukko

def viivoita_pelialue(pelialue:pygame.Surface,ruutu_maara_y,ruutu_maara_x):
    ruutu_korkeus = pelialue.get_height() / ruutu_maara_y
    ruutu_leveys = pelialue.get_width() / ruutu_maara_x

    for i in range(ruutu_maara_y):
        viiva = pygame.draw.line(pelialue,(0,0,0),(0, i * ruutu_korkeus),(pelialue.get_width(), i * ruutu_korkeus))
    for i in range(ruutu_maara_x):
        viiva = pygame.draw.line(pelialue,(0,0,0),(i * ruutu_leveys, 0),(i * ruutu_leveys, pelialue.get_width()))
    return pelialue

if __name__ == "__main__":
    peli()