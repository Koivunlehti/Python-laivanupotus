from pygame import Surface, draw, SRCALPHA, font

def soutuvene(ruutukoko:tuple, vari:tuple[int,int,int] | str, vaaka:bool = True) -> Surface:
    laiva = Surface(ruutukoko, SRCALPHA)
    x = 0
    y = 0
    if vaaka:
        draw.ellipse(laiva, vari, (x, y + 4, ruutukoko[0], ruutukoko[1] - 8))
        draw.line(laiva, "black", (ruutukoko[0] / 2, ruutukoko[1] / 2 - 2),(ruutukoko[0] / 2, 0), 2)
        draw.line(laiva, "black", (ruutukoko[0] / 2, ruutukoko[1] / 2 + 2),(ruutukoko[0] / 2, ruutukoko[1]), 2)
    else:
        draw.ellipse(laiva, vari, (x + 4, y, ruutukoko[0] - 8, ruutukoko[1]))
        draw.line(laiva, "black", (ruutukoko[0] / 2 - 2, ruutukoko[1] / 2),(0, ruutukoko[1] / 2), 2)
        draw.line(laiva, "black", (ruutukoko[0] / 2 + 2, ruutukoko[1] / 2),(ruutukoko[0], ruutukoko[1] / 2), 2)
    return laiva

def keula(ruutukoko:tuple, vari:tuple[int,int,int] | str, vaaka:bool = True) -> Surface:
    laiva = Surface(ruutukoko, SRCALPHA)
    x = 0
    y = 0
    if vaaka:
        # runko
        draw.polygon(laiva, vari, [(x, ruutukoko[1] / 2), 
                                   (ruutukoko[0] / 2, 0), 
                                   (ruutukoko[0], 0), 
                                   (ruutukoko[0], ruutukoko[1]), 
                                   (ruutukoko[0] / 2, ruutukoko[1])])
        # koppi
        draw.polygon(laiva, "darkgray", [(ruutukoko[0], ruutukoko[1] / 2 - 4), 
                                         (ruutukoko[0] - 4, ruutukoko[1] / 2 - 4), 
                                         (ruutukoko[0] - 4, ruutukoko[1] / 2 + 4), 
                                         (ruutukoko[0], ruutukoko[1] / 2 + 4)])
        
        # tykki
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black",(ruutukoko[0] / 2 - 2, ruutukoko[1] / 2),(ruutukoko[0] / 2 - 6, ruutukoko[1] / 2), 2)

    else:
        # runko
        draw.polygon(laiva, vari, [(ruutukoko[0] / 2, y), 
                                   (ruutukoko[0], ruutukoko[1] / 2), 
                                   (ruutukoko[0], ruutukoko[1]), 
                                   (0, ruutukoko[1]), 
                                   (0, ruutukoko[1] / 2)])
        # koppi
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 4, ruutukoko[1]), 
                                         (ruutukoko[0] / 2 - 4, ruutukoko[1] - 4), 
                                         (ruutukoko[0] / 2 + 4, ruutukoko[1] - 4), 
                                         (ruutukoko[0] / 2 + 4, ruutukoko[1])])
        
        # tykki
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black",(ruutukoko[0] / 2, ruutukoko[1] / 2 - 2),(ruutukoko[0] / 2, ruutukoko[1] / 2 - 6), 2)
    
    return laiva

def pera(ruutukoko:tuple, vari:tuple[int,int,int] | str, vaaka:bool = True) -> Surface:
    laiva = Surface(ruutukoko, SRCALPHA)
    x = 0
    y = 0
    if vaaka:
        # runko
        draw.polygon(laiva, vari, [(x, y), 
                                   (ruutukoko[0] - 8, y), 
                                   (ruutukoko[0] - 4, 4), 
                                   (ruutukoko[0] - 4, ruutukoko[1] - 4), 
                                   (ruutukoko[0] - 8, ruutukoko[1]), 
                                   (x, ruutukoko[1])])
        # koppi
        draw.polygon(laiva, "darkgray", [(x, ruutukoko[1] / 2 - 4), 
                                         (x + 4, ruutukoko[1] / 2 - 4), 
                                         (x + 4, ruutukoko[1] / 2 + 4), 
                                         (x, ruutukoko[1] / 2 + 4)])
        
        # tykki
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black",(ruutukoko[0] / 2 + 2, ruutukoko[1] / 2),(ruutukoko[0] / 2 + 6, ruutukoko[1] / 2), 2)

    else:
        # runko
        draw.polygon(laiva, vari, [(x, y), 
                                   (ruutukoko[0], 0), 
                                   (ruutukoko[0], ruutukoko[1] - 8), 
                                   (ruutukoko[0] - 4, ruutukoko[1] - 4), 
                                   (x + 4, ruutukoko[1] - 4), 
                                   (x, ruutukoko[1] - 8)])
        # koppi
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 4, y), 
                                         (ruutukoko[0] / 2 - 4, y + 4), 
                                         (ruutukoko[0] / 2 + 4, y + 4), 
                                         (ruutukoko[0] / 2 + 4, y)])
        
        # tykki
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black",(ruutukoko[0] / 2, ruutukoko[1] / 2 + 2),(ruutukoko[0] / 2, ruutukoko[1] / 2 + 6), 2)
    return laiva

def keskiosa(ruutukoko:tuple, vari:tuple[int,int,int] | str, vaaka:bool = True) -> Surface:
    laiva = Surface(ruutukoko, SRCALPHA)
    x = 0
    y = 0
    if vaaka:
        # runko
        draw.polygon(laiva, vari, [(x, y), 
                                   (ruutukoko[0], y), 
                                   (ruutukoko[0], ruutukoko[1]), 
                                   (x,ruutukoko[1])])
        
        # koppi
        draw.polygon(laiva, "darkgray", [(x, ruutukoko[1] / 2 - 4), 
                                         (ruutukoko[0], ruutukoko[1] / 2 - 4), 
                                         (ruutukoko[0], ruutukoko[1] / 2 + 4), 
                                         (x, ruutukoko[1] / 2 + 4)])
        
        # tykki oikea
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 4),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 - 8),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 8),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 - 4)])
        draw.line(laiva, "black", (ruutukoko[0] / 2, ruutukoko[1] / 2 - 4), (ruutukoko[0] / 2, ruutukoko[1] / 2 - 10), 2)

        # tykki vasen
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 4),
                                         (ruutukoko[0] / 2 - 3, ruutukoko[1] / 2 + 8),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 8),
                                         (ruutukoko[0] / 2 + 3, ruutukoko[1] / 2 + 4)])
        draw.line(laiva, "black", (ruutukoko[0] / 2, ruutukoko[1] / 2 + 4), (ruutukoko[0] / 2, ruutukoko[1] / 2 + 10), 2)

    else:
        # runko
        draw.polygon(laiva, vari, [(x, y), 
                                   (ruutukoko[0], y), 
                                   (ruutukoko[0], ruutukoko[1]), 
                                   (x,ruutukoko[1])])
        # koppi
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 4, y), 
                                         (ruutukoko[0] / 2 - 4, ruutukoko[1]), 
                                         (ruutukoko[0] / 2 + 4, ruutukoko[1]), 
                                         (ruutukoko[0] / 2 + 4, y)])
        # tykki oikea
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 + 4, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 8, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 + 8, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 + 4, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black", (ruutukoko[0] / 2 + 4, ruutukoko[1] / 2), (ruutukoko[0] / 2 + 10, ruutukoko[1] / 2), 2)

        # tykki vasen
        draw.polygon(laiva, "darkgray", [(ruutukoko[0] / 2 - 4, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 - 8, ruutukoko[1] / 2 - 3),
                                         (ruutukoko[0] / 2 - 8, ruutukoko[1] / 2 + 3),
                                         (ruutukoko[0] / 2 - 4, ruutukoko[1] / 2 + 3)])
        draw.line(laiva, "black", (ruutukoko[0] / 2 - 4, ruutukoko[1] / 2), (ruutukoko[0] / 2 - 10, ruutukoko[1] / 2), 2)

    return laiva

def ohi(ruutukoko:tuple, vari:tuple[int,int,int]) -> Surface:
    ohi = Surface(ruutukoko, SRCALPHA)
    draw.ellipse(ohi, vari, (0, 0, ruutukoko[0], ruutukoko[1]), 2)
    draw.ellipse(ohi, vari, (ruutukoko[0] / 2 - 5, ruutukoko[1] / 2 - 5, 10, 10), 3)
    return ohi

def osuma(ruutukoko:tuple) -> Surface:
    osuma = Surface(ruutukoko, SRCALPHA)
    draw.ellipse(osuma, (255,100,25), (0, 0, ruutukoko[0], ruutukoko[1]))
    draw.ellipse(osuma, (255,150,25), (ruutukoko[0] / 2 - 5, ruutukoko[1] / 2 - 5, 10, 10))
    return osuma

# Käyttöliittymä

def teksti(teksti:str, vari:tuple[int,int,int] | str = (255,255,255), fontti:str = "Arial", fontti_koko:int = 20) -> Surface:
    kirjoitus_fontti = font.SysFont(fontti, fontti_koko)
    kirjoitus = kirjoitus_fontti.render(teksti, True, vari)
    return kirjoitus

def painike(koko:tuple, vari:tuple[int,int,int] | str, teksti:Surface | None = None) -> Surface:
    koko_x = koko[0]
    koko_y = koko[1]
    if teksti != None:
        if koko_x < teksti.get_width():
            koko_x = teksti.get_width()
        if koko_y < teksti.get_height():
            koko_y = teksti.get_height()
    
    painike = Surface((koko_x, koko_y), SRCALPHA)
    painike.fill(vari)
    if teksti != None:
        painike.blit(teksti,(painike.get_width() / 2 - teksti.get_width() / 2, painike.get_height() / 2 - teksti.get_height() / 2))

    return painike