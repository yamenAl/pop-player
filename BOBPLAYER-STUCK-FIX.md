# BOBPlayer STUCK on screen — fix

App frozen / loading forever = BOBPlayer cannot download or read your playlist.

---

## TRY THIS FIRST (on TV, not website)

**Add playlist directly on the TV app** — more reliable than bobplayer.com.

1. On TV open **BOBPlayer**
2. **Choose Your Playlist** → **+** → **General**
3. Name: `NASA`
4. Paste **ONE** of these URLs (try in order):

### URL 1 — 1 channel only (simplest)
```
https://cdn.jsdelivr.net/gh/yamenAl/pop-player@main/playlist-nasa.m3u
```

### URL 2 — if GitHub blocked on TV, use iptv-org (not your repo)
```
https://iptv-org.github.io/iptv/index.category.m3u
```

### URL 3 — GitHub raw
```
https://raw.githubusercontent.com/yamenAl/pop-player/main/playlist-nasa.m3u
```

5. **Save** → select **NASA** → **Reload**
6. Wait 30 seconds
7. Open **Live TV** → click **NASA TV**

---

## On bobplayer.com — delete old playlists

Delete **shafak tv** and **All Channels** from website.

Too many / broken playlists can make app stuck on load.

Add only **one** playlist after TV test works.

---

## Check these on TV

| Check | What to do |
|-------|------------|
| **Expired** on screen | bobplayer.com → **Activate Device** |
| **MAC different** | Website MAC must match TV MAC exactly |
| **WiFi** | TV must have internet (open YouTube to test) |
| **Stuck loading** | Force close app → reopen → try URL 1 above |

---

## Push new files to GitHub first

Run on your Mac:

```bash
cd pop-player1
git add playlist-nasa.m3u playlist-bob-minimal.m3u playlist-test.m3u
git commit -m "Add minimal BOBPlayer playlists"
git push
```

Then use URL 1 on TV.

---

## If NASA plays → your app works

Then use full list:
```
https://cdn.jsdelivr.net/gh/yamenAl/pop-player@main/playlist-test.m3u
```

---

## Still stuck?

Tell me:
1. TV brand (Samsung / LG / Android TV?)
2. Screen text: **Expired** / **Loading** / **Playlist error**?
3. MAC on TV = `a0:d0:5b:13:b0:ad` ?
