#!/usr/bin/env bash
set -euo pipefail

"$HOME/.local/bin/bijbeltekst-wallpaper.py"

NIEUWSTE="$HOME/.cache/wallpaper-bijbeltekst-$(date +%F).png"
plasma-apply-wallpaperimage "$NIEUWSTE"

find "$HOME/.cache" -maxdepth 1 -name 'wallpaper-bijbeltekst-*.png' -printf '%T@ %p\n' \
    | sort -rn | tail -n +4 | cut -d' ' -f2- | xargs -r -d '\n' rm --

