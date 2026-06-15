#!/usr/bin/env python3
"""Merge legal Arabic IPTV playlists from iptv-org (names + logos)."""

import re
import urllib.request

BASE = "https://iptv-org.github.io/iptv"
SOURCES = [
    f"{BASE}/regions/arab.m3u",
    f"{BASE}/languages/ara.m3u",
    f"{BASE}/categories/movies.m3u",
    f"{BASE}/categories/series.m3u",
] + [f"{BASE}/countries/{c}.m3u" for c in (
    "ae", "sa", "eg", "qa", "lb", "iq", "jo", "ma", "tn", "dz",
    "ye", "om", "kw", "bh", "sy", "ps", "ly", "sd",
)]

ARABIC_HINTS = re.compile(
    r"arab|arabe|عرب|mbc|rotana|osn|bein|aljazeera|jazeera|"
    r"dubai|abu.?dhabi|shahid|aflam|masr|cairo|beirut|"
    r"saudi|kuwait|qatar|morocco|tunisia|algeria|lebanon|"
    r"syria|iraq|jordan|yemen|oman|bahrain|palestine|libya|sudan|"
    r"france.?24.*arab|dw.*arab|bbc.*arab",
    re.I,
)

OUTPUT = "playlist-arabic.m3u"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "pop-player/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def parse_m3u(text: str) -> list[tuple[str, list[str]]]:
    """Return list of (extinf_line, extra_lines_before_url, url)."""
    entries = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF:"):
            extinf = line
            extras = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith("#EXT"):
                extras.append(lines[i].strip())
                i += 1
            if i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("#"):
                url = lines[i].strip()
                entries.append((extinf, extras, url))
            i += 1
            continue
        i += 1
    return entries


def is_arabic_entry(extinf: str, url: str) -> bool:
    if ARABIC_HINTS.search(extinf):
        return True
    gt = re.search(r'group-title="([^"]*)"', extinf)
    if gt and ARABIC_HINTS.search(gt.group(1)):
        return True
    return False


def normalize_group(extinf: str) -> str:
    """Ensure Arabic-friendly group titles for movies/series."""
    if 'group-title="Movies"' in extinf or "Movies" in extinf.split(",")[-1]:
        return re.sub(
            r'group-title="[^"]*"',
            'group-title="أفلام | Movies"',
            extinf,
            count=1,
        )
    if 'group-title="Series"' in extinf:
        return re.sub(
            r'group-title="[^"]*"',
            'group-title="مسلسلات | Series"',
            extinf,
            count=1,
        )
    if "group-title=" not in extinf:
        return extinf.replace(
            "#EXTINF:-1",
            '#EXTINF:-1 group-title="عربي | Arabic"',
            1,
        )
    if 'group-title="عربي' not in extinf and "Arabic" not in extinf:
        return re.sub(
            r'group-title="([^"]*)"',
            r'group-title="عربي | \1"',
            extinf,
            count=1,
        )
    return extinf


def main() -> None:
    seen_urls: set[str] = set()
    out_lines = ["#EXTM3U", "# Playlist: Arabic channels, movies & series (legal free streams)"]
    count = 0

    for src in SOURCES:
        try:
            text = fetch(src)
        except Exception as e:
            print(f"skip {src}: {e}")
            continue
        is_cat = "categories/movies" in src or "categories/series" in src
        for extinf, extras, url in parse_m3u(text):
            if url in seen_urls:
                continue
            if is_cat and not is_arabic_entry(extinf, url):
                continue
            seen_urls.add(url)
            extinf = normalize_group(extinf)
            out_lines.append(extinf)
            out_lines.extend(extras)
            out_lines.append(url)
            out_lines.append("")
            count += 1
        print(f"ok {src}")

    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    out_path = root / OUTPUT
    out_path.write_text("\n".join(out_lines).strip() + "\n", encoding="utf-8")
    print(f"Wrote {count} channels -> {out_path}")


if __name__ == "__main__":
    main()
