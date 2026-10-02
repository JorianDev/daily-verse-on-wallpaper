# Wallpaper generator met Bijbeltekst
Deze repo genereert elke dag opnieuw je wallpaper met een dagelijkse bijbeltekst erop. De bijbeltekst wordt opgehaald van [dailyverses.net](https://dailyverses.net/nl/rss.xml).

:us: below

## Table of contents
1. Dutch
    - [Benodigd](#benodigd)
    - [Installeren - Automatisch](installeren-automatisch)
    - [Installeren - Handmatig](installeren-handmatig)
2. English
    - [English - Daily Verse Generator](#english---daily-verse-generator-on-wallpaper)
    - [Required](#required)
    - [Installing - Automatically](#installing---automatically)
    - [Installing - Manually](#installing---manually)

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
This repo regenerates your wallpaper every day with a daily Bible verse on it. The Bible verse is retrieved from [dailyverses.net](https://dailyverses.net/nl/rss.xml).

## Required
- Linux with KDE Plasma
- Python 3 with support for `venv` and `pip`
- The `qdbus` and `plasma-apply-wallpaperimage` commands
- An internet connection during installation and for retrieving the daily text

## Installing - Automatically
Open a terminal in this repo and run:
```bash
./install-auto.sh
```
The script creates a dedicated Python environment in `~/.local/share/bible-text-wallpaper`, installs `Pillow` and `feedparser` there, and places `bible-text-wallpaper.py` and `bible-text-wrapper.sh` in `~/.local/bin`. The Python script is set to use this local environment, so that both direct execution and execution via the wrapper use the same dependencies. The systemd files are placed in `~/.config/systemd/user`, and the timer is enabled. It runs daily at 6:00 AM; any missed runs are made up after the timer restarts.

Check if the timer is running with:
```bash
systemctl --user list-timers bijbeltekst.timer
```
No `sudo` is required. If Python does not support `venv`, install it on your Linux distribution and run the script again. The first time you run the wallpaper generator, it must be done within an active KDE session so that `qdbus` can read the current wallpaper.

To disable the timer:
```bash
systemctl --user disable --now Bible-verse.timer
```

## Installing - Manually
If automatic installation does not work, follow these steps:
1. Place `bijbeltekst.service` and `bijbeltekst.timer` in the systemd folder at `~/.config/systemd/user`
2. Place `bijbeltekst-wallpaper.py` and `bijbeltekst-wrapper.sh` in `~/.local/bin`
3. To make the scripts executable, run the following command:
```bash
chmod +x ~/.local/bin/bijbeltekst-wallpaper.py ~/.local/bin/bijbeltekst-wrapper.sh
```
4. To activate the timers, run the following commands:
```bash
systemctl --user daemon-reload
systemctl --user enable --now Bible-verse.timer
systemctl --user list-timers Bible-verse.timer
```
5. Verification. To verify that the timers are running, run the following commands
```bash
systemctl --user list-timers bible-verse.timer
systemctl --user is-enabled bible-verse.timer
```
---
If you’ve made any changes to the timer files, run the following command to reload the systemd configuration:
```bash
systemctl --user daemon-reload
```