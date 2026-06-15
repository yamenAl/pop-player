# Samsung TV — fix refresh loop

## Why it keeps refreshing

You added **6 playlists** including **Everything** (~12,600 channels).

Samsung TV + BOBPlayer **cannot load that much**. The app loads forever and refreshes in a loop.

| Playlist | Channels | Samsung TV |
|----------|----------|------------|
| Everything | ~12,600 | TOO BIG — causes refresh loop |
| News | ~939 | Too big alone |
| Arabic | ~450 | OK (one at a time) |
| Movies | ~415 | OK |
| Sports | ~329 | OK |
| Series | ~193 | OK |

**Never use Everything on Samsung TV.**

**Never add all 6 at the same time.**

---

## FIX — do this now

### Step 1: Delete ALL playlists

On TV or bobplayer.com — delete every playlist:
- Everything
- Arabic
- Movies
- Series
- News
- Sports

### Step 2: Force close BOBPlayer

Fully quit the app. Restart Samsung TV (power off 30 sec).

### Step 3: Add ONLY ONE playlist

Pick **one** of these (best first):

**Option A — Movies only (you said this worked):**
```
https://iptv-org.github.io/iptv/categories/movies.m3u
```

**Option B — Arabic only:**
```
https://iptv-org.github.io/iptv/categories/arab.m3u
```
(Use regions/arab: `https://iptv-org.github.io/iptv/regions/arab.m3u`)

**Option C — Small custom list (30 channels, best for Samsung):**
```
https://cdn.jsdelivr.net/gh/yamenAl/pop-player@main/playlist-samsung.m3u
```

### Step 4: Load it

1. Save playlist
2. Select it
3. Reload — wait **60 seconds** (do not click again)
4. Open Live TV / Channels

### Step 5: Want more categories?

Add a **second** playlist **only after** the first one works.
Never add Everything.

---

## Rules for Samsung TV

1. **One playlist at a time** to start
2. **No Everything** (index.m3u)
3. Wait **60 sec** on Reload — don't spam refresh
4. Max **2–3 playlists** total on Samsung
5. Prefer **Movies**, **Arabic**, or **playlist-samsung.m3u**

---

## If still refreshing

1. Uninstall BOBPlayer
2. Reinstall
3. Activate device (bobplayer.com)
4. Add **only** Movies URL
5. Try **NASA TV** channel first
