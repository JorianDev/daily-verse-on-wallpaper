# Wallpaper generator met Bijbeltekst
Deze repo genereert elke dag opnieuw je wallpaper met een dagelijkse bijbeltekst erop. De bijbeltekst wordt opgehaald van [dailyverses.net](https://dailyverses.net/nl/rss.xml).

## Installeren - Automatisch
Vereist Linux met KDE Plasma en systemd. Voer vanuit de repository uit:

```bash
./install.sh
```

Het script vraagt om een afbeelding voor de achtergrond en installeert ontbrekende Python-afhankelijkheden via apt, dnf of pacman. Daarna komen de programma's in `~/.local/bin`, de instellingen in `~/.config/bijbeltekst-wallpaper` en de systemd-units in `~/.config/systemd/user`. De timer wordt meteen ingeschakeld en draait dagelijks om 06:00.

Je kunt het pad ook direct meegeven: `./install.sh /pad/naar/wallpaper.jpg`. KDE Plasma, systemd en Python 3 moeten al aanwezig zijn.

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