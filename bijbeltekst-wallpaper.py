#!/usr/bin/env python3
import html
import sys
import textwrap
import urllib.request
import time
from pathlib import Path
from datetime import date

from PIL import Image, ImageDraw, ImageFont
import feedparser
import subprocess

def actieve_wallpaper():
    script = (
        "var d = desktops();"
        "d[0].currentConfigGroup = ['Wallpaper', 'org.kde.image', 'General'];"
        "print(d[0].readConfig('Image'));"
    )
    result = subprocess.run(
        ["qdbus", "org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell.evaluateScript", script],
        capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip().removeprefix("file://"))


FEED_URL = "https://dailyverses.net/nl/rss.xml"                 # Vervang met je eigen RSS-feed URL indien gewenst
# ACHTERGROND = Path.home() / "Path/To/Your/Wallpaper.jpg"      # Vervang met je eigen standaard wallpaper
ACHTERGROND = actieve_wallpaper()                               # Gebruik de huidige wallpaper als achtergrond
OUTPUT = Path.home() / f".cache/wallpaper-bijbeltekst-{date.today().isoformat()}.png"
LETTERTYPE = "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Bold.ttf"
FALLBACK = "De HEERE is mijn Herder, mij zal niets ontbreken. - Psalm 23:1"


def haal_dagtekst(pogingen=20, wachttijd=15):
    for poging in range(1, pogingen + 1):
        try:
            with urllib.request.urlopen(FEED_URL, timeout=10) as r:
                feed = feedparser.parse(r.read())
            if not feed.entries:
                raise ValueError("Lege feed")
            item = feed.entries[0]
            tekst = html.unescape(item.description).replace("\n", " ").strip()
            return f"{tekst} - {item.title}"
        except Exception as e:
            print(f"Poging {poging}/{pogingen} mislukt: {e}", file=sys.stderr)
            if poging == pogingen:
                raise
            time.sleep(wachttijd)


def laad_font(grootte):
    try:
        return ImageFont.truetype(LETTERTYPE, size=grootte)
    except OSError:
        print("Lettertype niet gevonden, standaardfont gebruikt", file=sys.stderr)
        return ImageFont.load_default()

def maak_wallpaper():
    tekst = haal_dagtekst()
    img = Image.open(ACHTERGROND).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = laad_font(int(img.width / 70))

    regels = textwrap.wrap(tekst, width=45)
    regel_hoogte = font.getbbox("A")[3] + 10
    y = 150

    # Positioneer de tekst aan de rechterbovenkant van het scherm
    for regel in regels:
        bbox = draw.textbbox((0, 0), regel, font=font)
        breedte = bbox[2] - bbox[0]
        x = max(0, img.width - breedte - 100)
        draw.text((x+2, y+2), regel, font=font, fill="black")
        draw.text((x, y), regel, font=font, fill="white")
        y += regel_hoogte

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUTPUT)

if __name__ == "__main__":
    try:
        maak_wallpaper()
    except Exception as e:
        print(f"Fout: {e}", file=sys.stderr)
        sys.exit(1)
