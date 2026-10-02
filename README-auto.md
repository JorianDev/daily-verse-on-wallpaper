# Automatische installatie

Deze handleiding is voor Linux met KDE Plasma en systemd. Het installatiescript zet de generator, Python-afhankelijkheden en dagelijkse timer klaar. De generator gebruikt de huidige KDE-achtergrond als bronafbeelding.

## Benodigd

- Linux met KDE Plasma en systemd voor gebruikersservices
- Python 3 met ondersteuning voor `venv` en `pip`
- De opdrachten `qdbus` en `plasma-apply-wallpaperimage`
- Een internetverbinding tijdens installatie en voor het ophalen van de dagelijkse tekst

## Installeren

Open een terminal in de map van deze repository en voer uit:

```bash
./install-auto.sh
```

Het script maakt een eigen Python-omgeving aan in `~/.local/share/bijbeltekst-wallpaper`, installeert daarin `Pillow` en `feedparser`, en zet `bijbeltekst-wallpaper.py` en `bijbeltekst-wrapper.sh` in `~/.local/bin`. Het Python-script krijgt een verwijzing naar de eigen omgeving, zodat zowel direct starten als starten via de wrapper dezelfde afhankelijkheden gebruikt. De systemd-bestanden komen in `~/.config/systemd/user` en de timer wordt ingeschakeld. Hij draait dagelijks om 06:00; een gemiste uitvoering wordt na het opnieuw starten van de timer ingehaald.

Controleer de timer met:

```bash
systemctl --user list-timers bijbeltekst.timer
```

Er is geen `sudo` nodig. Als Python geen `venv`-ondersteuning heeft, installeer dan het bijbehorende pakket voor jouw Linux-distributie en voer het script opnieuw uit. De eerste uitvoering van de wallpaper-generator moet plaatsvinden in een actieve KDE Plasma-sessie, zodat `qdbus` de huidige achtergrond kan uitlezen.

Om de timer uit te schakelen:

```bash
systemctl --user disable --now bijbeltekst.timer
```
