import pygame
import random

from laiva import Laiva

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

    # Käytössä olevat laivat
    #laivat = [LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_1,LAIVA_2,LAIVA_2,LAIVA_2,LAIVA_3,LAIVA_3]

    #DEBUG
    laiva = Laiva("nimi1",3)
    print(laiva.aseta(0,0,True))
    print(laiva.aseta(0,0,False))
    #laiva.vaaka = True
    laiva.osuma(0,1)
    laiva.osuma(1,0)
    print(laiva.osumat)
    print(laiva.tuhottu)
    laiva.osuma(0,0)
    laiva.osuma(2,0)
    #laiva.osuma(0,2)
    print(laiva.osumat)
    print(laiva.tuhottu)
    # laiva = Laiva("nimi2",2)
    # print(laiva.aseta(0,0,True))
    # print(laiva.aseta(0,0,False))

    def luo_laivoja(maara, nimi, pituus, ruutu_koko, vari):
        laivat = []
        for i in range(maara):
            laivat.append(Laiva(f"{nimi}{i+1}", pituus, ruutu_koko, vari))
        return laivat
    p_laivat = luo_laivoja(5, "TosiPieni", LAIVA_1, (20,20), (100,100,100))
    p_laivat.extend(luo_laivoja(3, "Pieni", LAIVA_2, (20,20), (100,100,100)))
    p_laivat.extend(luo_laivoja(2, "keski", LAIVA_3, (20,20), (100,100,100)))

    v_laivat = luo_laivoja(5, "TosiPieni", LAIVA_1, (20,20), (100,100,100))
    v_laivat.extend(luo_laivoja(3, "Pieni", LAIVA_2, (20,20), (100,100,100)))
    v_laivat.extend(luo_laivoja(2, "keski", LAIVA_3, (20,20), (100,100,100)))
    print(v_laivat)
    
    #DEBUG LOPPU

    # Laivataulukot
    pelaajan_laivat = laivataulukon_alustus(20,20)
    vastustajan_laivat = laivataulukon_alustus(20,20)

    # Laivojen asettelu
    #aseta_laivat_satunnainen(pelaajan_laivat, laivat)
    aseta_laivat_satunnainen(vastustajan_laivat, v_laivat)
    print(vastustajan_laivat)

    # Pelialueiden asetukset
    marginaali = 20
    pelialue_koko = (400,400)
    pelialue_vari = (0,162,232)

    # Pelaajan manuaalisen laivojen asettelun asetuksia 
    asetustila = True
    asetus_laiva_index = 0
    asetus_asento_vaaka = True

    # Muita peliasetuksia
    vastustajan_vuoro = False
    voitto = False
    havio = False

    # Ajastimia
    hidasta_vastustaja = 0

    # Pelisilmukka alkaa
    while True:
        # Näytön tyhjennys
        naytto.fill((0, 0, 0))

        # Hiiren koordinaatit
        hiiri_x, hiiri_y = pygame.mouse.get_pos()

        fontti = pygame.font.SysFont("Arial",20)

        pelaajan_kentta = piirra_pelialue(pelaajan_laivat, p_laivat, pelialue_koko, pelialue_vari)
        pelaajan_kentta = naytto.blit(pelaajan_kentta, (marginaali, naytto.get_height() / 2 - pelaajan_kentta.get_height() / 2))
        
        if asetustila == True:
            teksti_pelaaja = fontti.render("Aseta laivasi", True, (255,255,255))
            naytto.blit(teksti_pelaaja,(marginaali, naytto.get_height() / 2 - pelialue_koko[1] / 2 - teksti_pelaaja.get_height()))

            #naytto.blit(piirra_laiva(laivat[asetus_laiva_index], (20,20), asetus_asento_vaaka), (hiiri_x, hiiri_y))
            p_laivat[asetus_laiva_index].vaaka = asetus_asento_vaaka
            naytto.blit(p_laivat[asetus_laiva_index].piirra(),(hiiri_x, hiiri_y))
        else:
            if voitto or havio:
                fontti_voitto = pygame.font.SysFont("Arial",40)
                if voitto:
                    teksti_tietoja = fontti_voitto.render("Voitto!!!", True, (34,176,70))
                    naytto.blit(teksti_tietoja, (naytto.get_width() / 2 - teksti_tietoja.get_width() / 2, naytto.get_height() - 150))
                if havio:
                    teksti_tietoja = fontti_voitto.render("Häviö!!!", True, (255,0,0))
                    naytto.blit(teksti_tietoja, (naytto.get_width() / 2 - teksti_tietoja.get_width() / 2, naytto.get_height() - 150))
                painike_teksti = fontti.render("Uusi peli", True, (255,255,255))
                painike_uusi_peli = pygame.Surface((painike_teksti.get_width() + 20, painike_teksti.get_height() + 20), pygame.SRCALPHA)
                painike_uusi_peli.fill((100, 100, 100))
                painike_uusi_peli.blit(painike_teksti, (10, 10))
                painike_uusi_peli = naytto.blit(painike_uusi_peli, (naytto.get_width() / 2 - painike_uusi_peli.get_width() / 2, naytto.get_height() - 100))
            else:
                if vastustajan_vuoro:
                    teksti_tietoja = fontti.render("Vastustajan vuoro...",True,(255,255,255))
                else:
                    teksti_tietoja = fontti.render("Pelaajan vuoro...",True,(255,255,255))
                naytto.blit(teksti_tietoja, (naytto.get_width() / 2 - teksti_tietoja.get_width() / 2, naytto.get_height() - 150))

            teksti_pelaaja = fontti.render("Pelaajan laivat", True, (255,255,255))
            naytto.blit(teksti_pelaaja, (marginaali, naytto.get_height() / 2 - pelialue_koko[1] / 2 - teksti_pelaaja.get_height()))

            vastustajan_kentta = piirra_pelialue(vastustajan_laivat, v_laivat, pelialue_koko, pelialue_vari, True)
            vastustajan_kentta = naytto.blit(vastustajan_kentta, (naytto.get_width() - vastustajan_kentta.get_width() - marginaali, naytto.get_height() / 2 - vastustajan_kentta.get_height() / 2))

            teksti_vastustaja = fontti.render("Vastustajan laivat", True, (255,255,255))
            naytto.blit(teksti_vastustaja, (naytto.get_width() - teksti_vastustaja.get_width() - marginaali, naytto.get_height() / 2 - pelialue_koko[1] / 2 - teksti_pelaaja.get_height()))

        # Tapahtumien käsittely
        for tapahtuma in pygame.event.get():

            # Ikkunan yläkulman X painike
            if tapahtuma.type == pygame.QUIT:   
                exit()

            # Hiiren vasen klikkaus
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0] == True:
                if voitto or havio:
                    if painike_uusi_peli.collidepoint(tapahtuma.pos):
                        print("uusi peli")
                        asetustila = True
                        asetus_laiva_index = 0
                        asetus_asento_vaaka = True

                        vastustajan_vuoro = False
                        voitto = False
                        havio = False

                        for laiva in p_laivat:
                            laiva.resetoi()
                        for laiva in v_laivat:
                            laiva.resetoi()

                        pelaajan_laivat = laivataulukon_alustus(20,20)
                        vastustajan_laivat = laivataulukon_alustus(20,20)
                        aseta_laivat_satunnainen(vastustajan_laivat, v_laivat)
                        break

                # Hiirtä klikattu pelaajan alueen päällä
                if pelaajan_kentta.collidepoint(tapahtuma.pos):
                    pelaajan_kentta_x = hiiri_x - marginaali    # Lasketaan uusi hiiren x ja y niin, että pelaajan pelialueen yläkulma on 0,0
                    pelaajan_kentta_y = hiiri_y - (naytto.get_height() / 2 - pelialue_koko[1] / 2)
                    #print("pelaajan kenttä")
                    #print(f"x {pelaajan_kentta_x}, y {pelaajan_kentta_y}")
                    x = int(pelaajan_kentta_x / len(pelaajan_laivat[0]))
                    y = int(pelaajan_kentta_y / len(pelaajan_laivat))
                    print(f"pelaajan x: {x}, y: {y}")

                    if asetustila == True:
                        if aseta_laiva(pelaajan_laivat, p_laivat[asetus_laiva_index], x, y, asetus_asento_vaaka):
                            asetus_laiva_index += 1

                # Hiirtä klikattu vastustajan alueen päällä
                if vastustajan_vuoro == False and asetustila == False and voitto == False and havio == False:
                    if vastustajan_kentta.collidepoint(tapahtuma.pos):
                        vastustajan_kentta_x = hiiri_x - (naytto.get_width()-(marginaali + pelialue_koko[0]))   # Lasketaan uusi hiiren x ja y niin, 
                        vastustajan_kentta_y = hiiri_y - (naytto.get_height() / 2 - pelialue_koko[1] / 2)       # että vastustajan pelialueen yläkulma on 0,0
                        #print("vastustajan kenttä")
                        #print(f"x {vastustajan_kentta_x}, y {vastustajan_kentta_y}")
                        x = int(vastustajan_kentta_x / len(vastustajan_laivat[0]))
                        y = int(vastustajan_kentta_y / len(vastustajan_laivat))
                        vaihda_vuoro = True
                        print(f"vastustajan x: {x}, y: {y}")


                        if vastustajan_laivat[y][x] not in [OHI, OSUMA]: 
                            for laiva in v_laivat:
                                if vastustajan_laivat[y][x] == laiva.nimi:
                                    #vastustajan_laivat[y][x] = OSUMA
                                    if laiva.osuma(x,y):
                                        print("Osuma")
                                    else:
                                        print("Ei voi klikata tähän")
                                        vaihda_vuoro = False
                                    break
                            if tarkista_voitto(v_laivat):
                                print("voitto!!!")
                                voitto = True
                            # if vastustajan_laivat[y][x] in [LAIVA_1, LAIVA_2, LAIVA_3]:
                            #     vastustajan_laivat[y][x] = OSUMA
                            #     print("Osuma")
                            #     if tarkista_voitto(v_laivat):
                            #         print("voitto!!!")
                            #         voitto = True
                            if vastustajan_laivat[y][x] == TYHJA:
                                vastustajan_laivat[y][x] = OHI
                                print("Huti")
                            if vaihda_vuoro:
                                vastustajan_vuoro = True
                            hidasta_vastustaja = random.randint(10,50)
                        else:
                            print("Ei voi klikata tähän")

            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[2] == True:
                if asetus_asento_vaaka:
                    asetus_asento_vaaka = False
                else:
                    asetus_asento_vaaka = True 
                print(asetus_asento_vaaka)
            #if tapahtuma.type == pygame.MOUSEBUTTONUP:

        if vastustajan_vuoro and voitto == False and havio == False:
            if hidasta_vastustaja <= 0: 
                pelaajan_laivat = vastustaja_pelaa(pelaajan_laivat, p_laivat)
                if tarkista_voitto(p_laivat):
                    print("Häviö!!!")
                    havio = True
                print("vastustajan vuoro ohi")
                vastustajan_vuoro = False

        if asetus_laiva_index >= len(p_laivat):
            asetustila = False

        if hidasta_vastustaja > 0:
            hidasta_vastustaja -= 1
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
def piirra_pelialue(laivataulukko:list, laivat:list, pelialue_koko:tuple=(400, 400), pelialue_vari:tuple=(0, 162, 232), piirra_laivat:bool=True) -> pygame.Surface:
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
    piirretyt_laivat = []
    for i in range(ruutu_maara_y):
        for j in range(ruutu_maara_x):
            arvo = laivataulukko[i][j]
            if arvo == TYHJA:
                pass
            elif arvo == OHI:
                pygame.draw.rect(pelialue, (100,0,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            elif arvo == OSUMA:
                pygame.draw.rect(pelialue, (226,138,0), (j * ruutu_leveys, i * ruutu_korkeus, ruutu_korkeus, ruutu_leveys))
            elif arvo not in piirretyt_laivat:
                if piirra_laivat:
                    for laiva in laivat:
                        if laiva.nimi == arvo:
                            #rint("piirra")
                            pelialue.blit(laiva.piirra(),(j * ruutu_leveys, i * ruutu_korkeus))
                            piirretyt_laivat.append(laiva.nimi)
                    # if arvo == LAIVA_1:
                    #     pelialue.blit(piirra_laiva(LAIVA_1, (ruutu_leveys, ruutu_korkeus), vain_yksi_ruutu=True),(j * ruutu_leveys, i * ruutu_korkeus))
                    # elif arvo == LAIVA_2:
                    #     pelialue.blit(piirra_laiva(LAIVA_2, (ruutu_leveys, ruutu_korkeus), vain_yksi_ruutu=True),(j * ruutu_leveys, i * ruutu_korkeus))
                    # elif arvo == LAIVA_3:
                    #     pelialue.blit(piirra_laiva(LAIVA_3, (ruutu_leveys, ruutu_korkeus), vain_yksi_ruutu=True),(j * ruutu_leveys, i * ruutu_korkeus))
            
    return pelialue

# Funktio, jonka avulla laivat piirretään pelialueelle, tai hiiren kursorin alle
# def piirra_laiva(laiva_koko:int, ruutu_koko:tuple, vaaka:bool = True, vain_yksi_ruutu:bool = False) -> pygame.Surface:
#     if vaaka:
#         x = ruutu_koko[0] * laiva_koko
#         if vain_yksi_ruutu:
#             x = ruutu_koko[0]
#         y = ruutu_koko[1]
#     else:
#         x = ruutu_koko[0]
#         y = ruutu_koko[1] * laiva_koko
#         if vain_yksi_ruutu:
#             y = ruutu_koko[1]

#     laiva = pygame.Surface((x, y), pygame.SRCALPHA)

#     if laiva_koko == LAIVA_1:
#         laiva.fill((0,100,0))
#     elif laiva_koko == LAIVA_2:
#         laiva.fill((255,242,0))
#     elif laiva_koko == LAIVA_3:
#         laiva.fill((255,128,255))
#     return laiva

# Funktio, jonka avulla pelaaja itse asettaa laivansa laivataulukkoon.
def aseta_laiva(laivataulukko:list, laiva:Laiva, x:int, y:int, vaaka:bool) -> bool:
    if tarkista_laivan_sopivuus(laivataulukko, x, y, laiva.pituus, vaaka):
        if vaaka:
            for j in range(laiva.pituus):
                laivataulukko[y][x + j] = laiva.nimi
            print("vaaka")
        else:
            for j in range(laiva.pituus):
                laivataulukko[y + j][x] = laiva.nimi
            print("pysty")
        laiva.aseta(x,y,vaaka)
        return True
    else:
        return False

# Funktio, jolla laivat lisätään laivataulukkoon satunnaisesti.
def aseta_laivat_satunnainen(laivataulukko:list, laivat:list) -> None:
    for i in range(len(laivat)):
        laiva:Laiva = laivat[i]
        while True:
            # Arvotaan x ja y koordinaatti
            y = random.randint(0, len(laivataulukko) -1)
            x = random.randint(0, len(laivataulukko[0]) -1)

            # Tarkistetaan onko paikka tyhjä ruudukossa
            if laivataulukko[y][x] == TYHJA:
                # Jos laiva on yhden ruudun kokoinen, se voidaan asettaa suoraan.
                if laiva.pituus == LAIVA_1:
                    laivataulukko[y][x] = laiva.nimi
                    laiva.aseta(x, y)
                    break
                # Jos laiva on pidempi kuin yksi ruutu, tarvitaan lisätarkistuksia
                else:
                    vaaka = random.choice((True,False))     # Arvotaan vaaka- tai pystysuunta
                    if tarkista_laivan_sopivuus(laivataulukko, x, y, laiva.pituus, vaaka):     # Tarkistetaan sopiiko laiva aiottuun kohtaan kokonaisuudessaan
                        # Asetetaan laiva joko vaaka tai pystysuuntaan ruudukkoon
                        if vaaka:
                            for j in range(laiva.pituus):
                                laivataulukko[y][x + j] = laiva.nimi
                        else:
                            for j in range(laiva.pituus):
                                laivataulukko[y + j][x] = laiva.nimi
                        laiva.aseta(x, y, vaaka)
                        break

# Funktio, jolla tarkistetaan sopiiko laiva aiottuun kohtaan ruudukkoa.
def tarkista_laivan_sopivuus(laivataulukko, x, y, laiva_koko, vaaka):
    sopii = True
    if vaaka == False: # Pystysuunta
        for i in range(laiva_koko):
            if y + i < len(laivataulukko):    # Tarkistetaan meneekö laiva yli ruudukosta 
                if laivataulukko[y + i][x] == TYHJA:    # Tarkistetaan onko laivan alla tyhjää. 
                    sopii = True
                else:
                    sopii = False                   # Jos löytyy huono kohta, lopetetaan tarkistus
                    break
            else:
                sopii = False
                break
    else: # Vaakasuunta
        for i in range(laiva_koko):
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
def tarkista_voitto(laivat:list) -> bool:
    for laiva in laivat:
        if laiva.tuhottu == False:
            return False
    return True
    # voitto = True
    # for i in range(len(laivataulukko)):
    #     if LAIVA_1 in laivataulukko[i]:
    #         voitto = False
    #     if LAIVA_2 in laivataulukko[i]:
    #         voitto = False
    #     if LAIVA_3 in laivataulukko[i]:
    #         voitto = False
    # return voitto

# Funktio, joka hoitaa vastustajan tekemiset
def vastustaja_pelaa(laivataulukko: list,laivat:list) -> None:
    while True:
        x = random.randint(0, len(laivataulukko[0]) - 1)
        y = random.randint(0, len(laivataulukko) - 1)
        if laivataulukko[y][x] not in [OHI, OSUMA, TYHJA]:
            for laiva in laivat:
                if laivataulukko[y][x] == laiva.nimi:
                    if laiva.osuma(x,y):
                        print("vastustaja osuma")
                        break
                        
        elif laivataulukko[y][x] in [TYHJA]:
            laivataulukko[y][x] = OHI
            print("vastustaja ohi")
            break
        #         print("vastustaja ohi")

    return laivataulukko
        # if laivataulukko[y][x] in [TYHJA, LAIVA_1, LAIVA_2, LAIVA_3]:
        #     if laivataulukko[y][x] in [LAIVA_1, LAIVA_2, LAIVA_3]:
        #         laivataulukko[y][x] = OSUMA
        #         print("vastustaja osuma")
        #     if laivataulukko[y][x] == TYHJA:
        #         laivataulukko[y][x] = OHI
        #         print("vastustaja ohi")
        #     return laivataulukko

if __name__ == "__main__":
    peli()
