# Wallpaper generator met Bijbeltekst
Deze repo genereert elke dag opnieuw je wallpaper met een dagelijkse bijbeltekst erop. De bijbeltekst wordt opgehaald van [dailyverses.net](https://dailyverses.net/nl/rss.xml).

:us: below

## Benodigd
- Linux met KDE Plasma
- Python3 met ondersteuning `venv` en `pip`
- Opdrachten `qdbus` en `plasma-apply-wallpaperimage`
- Een internetverbinding tijdens installatie en voor het ophalen van de dagelijkse tekst

## Installeren - Automatisch
Open terminal in deze repo en voer uit:
```bash
./install-auto.sh
```
Het script maakt een eigen Python-omgeving aan in `~/.local/share/bijbeltekst-wallpaper`, installeert daarin `Pillow` en `feedparser`, en zet `bijbeltekst-wallpaper.py` en `bijbeltekst-wrapper.sh` in `~/.local/bin`. Het Python-script krijgt een verwijzing naar de eigen omgeving, zodat zowel direct starten als starten via de wrapper dezelfde afhankelijkheden gebruikt. De systemd-bestanden komen in `~/.config/systemd/user` en de timer wordt ingeschakeld. Hij draait dagelijks om 06:00; een gemiste uitvoering wordt na het opnieuw starten van de timer ingehaald.

Controleer of de timer aanstaat met:
```bash
systemctl --user list-timers bijbeltekst.timer
```
Er is geen `sudo` nodig. Als Python geen `venv`-ondersteuning heeft, installeer deze dan bij jouw Linux-distro en voer het script opnieuw uit. De eerste uitvoering van de wallpaper-generator moet plaatsvinden in een actieve KDE-sessie, zodat `qdbus` de huidige wallpaper kan uitlezen.

Om de timer uit te schakelen:
```bash
systemctl --user disable --now bijbeltekst.timer
```


## Installeren - Handmatig
Wanneer automatisch installeren niet werkt, volg dan de volgende stappen:
1. Zet de `bijbeltekst.service` en `bijbeltekst.timer` in de systemd-folder in `~/.config/systemd/user`
2. Zet `bijbeltekst-wallpaper.py` en `bijbeltekst-wrapper.sh` in `~/.local/bin`
3. Om de scripts uitvoerbaar te maken voer je het volgende command uit:
```bash
chmod +x ~/.local/bin/bijbeltekst-wallpaper.py ~/.local/bin/bijbeltekst-wrapper.sh
```
4. Om de timers te activeren voer je de volgende commando's uit:
```bash
systemctl --user daemon-reload
systemctl --user enable --now bijbeltekst.timer
systemctl --user list-timers bijbeltekst.timer
```
5. Controle. Om te controleren of de timers aan staan voer je de volgende commando's uit
```bash
systemctl --user list-timers bijbeltekst.timer
systemctl --user is-enabled bijbeltekst.timer
```
---
Wanneer je wat verandert hebt in de timer-bestanden, voer dan het volgende commando uit om de systemd-configuratie opnieuw te laden:
```bash
systemctl --user daemon-reload 
```

# English - Daily verse generator on wallpaper