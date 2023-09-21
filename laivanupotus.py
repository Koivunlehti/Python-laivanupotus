import pygame

pygame.init()

# Kello
kello = pygame.time.Clock()

# Näytön asetukset
naytto = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Laivanupotus")

# Pelin alustus
pelaajan_laivat = []
vastustajan_laivat = []

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
    pygame.display.flip()

    # Seuraava frame
    kello.tick(60)