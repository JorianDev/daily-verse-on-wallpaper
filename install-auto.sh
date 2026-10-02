#!/usr/bin/env bash
set -euo pipefail

APP_NAME="bijbeltekst-wallpaper"
APP_DIR="$HOME/.local/share/$APP_NAME"
BIN_DIR="$HOME/.local/bin"
SYSTEMD_DIR="$HOME/.config/systemd/user"

fail() { printf 'Fout: %s\n' "$1" >&2; exit 1; }

command -v python3 >/dev/null || fail "Python 3 is niet gevonden."
command -v systemctl >/dev/null || fail "systemd/systemctl is vereist."
command -v qdbus >/dev/null || fail "qdbus is niet gevonden; dit programma gebruikt KDE Plasma."
command -v plasma-apply-wallpaperimage >/dev/null || fail "plasma-apply-wallpaperimage is niet gevonden; KDE Plasma is vereist."

if [[ $# -ne 0 ]]; then
    fail "Gebruik: ./install-auto.sh"
fi

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$APP_DIR" "$BIN_DIR" "$SYSTEMD_DIR"

python3 -m venv "$APP_DIR/.venv" || fail "Kon geen virtual environment maken. Installeer Python 3 met venv-ondersteuning."
"$APP_DIR/.venv/bin/python" -m pip install Pillow feedparser

{
    printf '#!%s/bin/python\n' "$APP_DIR/.venv"
    tail -n +2 "$repo_dir/bijbeltekst-wallpaper.py"
} > "$BIN_DIR/bijbeltekst-wallpaper.py"
chmod 755 "$BIN_DIR/bijbeltekst-wallpaper.py"
install -m 755 "$repo_dir/bijbeltekst-wrapper.sh" "$BIN_DIR/bijbeltekst-wrapper.sh"
install -m 644 "$repo_dir/systemd/bijbeltekst.service" "$SYSTEMD_DIR/bijbeltekst.service"
install -m 644 "$repo_dir/systemd/bijbeltekst.timer" "$SYSTEMD_DIR/bijbeltekst.timer"

systemctl --user daemon-reload
systemctl --user enable --now bijbeltekst.timer

printf '\nInstallatie klaar. De timer draait dagelijks om 06:00.\n'
printf 'Status bekijken: systemctl --user list-timers bijbeltekst.timer\n'
