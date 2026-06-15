# One playlist for BOBPlayer (everything in one URL)

## Use this single URL in BOBPlayer

Paste this into **Playlist URL** — world + Arabic + movies + series + news + sports (all legal free):

```
https://iptv-org.github.io/iptv/index.m3u
```

- **~12,600** channels  
- **Name** on each channel  
- **Logo** where available (`tvg-logo`)  
- Updates automatically on iptv-org’s side  

### In BOBPlayer

1. **Choose Your Playlist** → **+** / **Add**
2. **General** tab
3. **Playlist Name:** e.g. `All Channels`
4. **Playlist URL:** paste the URL above
5. **Save** → select playlist → **Reload**

You only need **one** playlist entry in BOBPlayer.

---

## Your own URL (optional — same content)

If you want **your** GitHub link instead:

1. Upload **`playlist.m3u`** or **`playlist-all.m3u`** (same file, ~3 MB) to a GitHub repo
2. Open the file → **Raw**
3. Copy that Raw URL into BOBPlayer

Example shape:

```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/playlist.m3u
```

---

## Other files in this folder (optional — not needed)

| File | Note |
|------|------|
| `playlist-arabic.m3u` | Arabic-only subset — use only if you want a smaller list |
| `playlist-world.m3u` | Duplicate of full index |
| `playlist-movies.m3u` | Already inside the main index |
| `playlist-series.m3u` | Already inside the main index |

**For “all in one URL” — use only the index URL or `playlist.m3u` on GitHub.**

---

## Limits

Legal free streams only — not Netflix, full OSN/beIN paid packages, or pirated “everything” lists.
