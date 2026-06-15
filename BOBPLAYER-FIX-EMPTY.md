# BOBPlayer empty? — Fix guide

## Most common reason: no playlist loaded

BOBPlayer on TV **cannot** read files from your Mac.  
It needs a **public internet URL** (starts with `https://`).

---

## Fix — step by step

### 1. Add the playlist URL

1. Open BOBPlayer on TV  
2. Go to **Choose Your Playlist** (or **Settings** → Playlist)  
3. Tap **+** or **Add**  
4. Tab: **General**  
5. **Playlist Name:** `All Channels`  
6. **Playlist URL** — paste **exactly** (no spaces):

```
https://iptv-org.github.io/iptv/index.m3u
```

7. Tap **Save**

### 2. Select and reload (easy to miss)

1. Go back to **Choose Your Playlist**  
2. **Select** the playlist you just saved (highlight it)  
3. Tap **Reload** or **Refresh**  
4. Wait 30–60 seconds (big list = slow on TV)

### 3. Open channels

- Go to **Live TV** / **Channels** / **Library** — not only the home screen  
- Channels appear **after** reload finishes

---

## If still empty — try small test list first

Big playlist (~12,000 channels) can fail on some TVs. Test with 5 channels:

**Option A — upload `playlist-test.m3u` to GitHub**

1. github.com → New repo → upload `playlist-test.m3u`  
2. Open file → **Raw**  
3. Copy URL, e.g.  
   `https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/playlist-test.m3u`  
4. Paste in BOBPlayer → Save → Reload  

**Option B — small online list (Arabic, ~450 channels)**

```
https://iptv-org.github.io/iptv/regions/arab.m3u
```

If the **small** list works but the big one doesn’t → your TV is slow; keep the smaller URL.

---

## Wrong URLs (these show empty)

| Wrong | Why |
|-------|-----|
| `/Users/yamen/.../playlist.m3u` | Local Mac path — TV can’t access |
| `file:///...` | Same — local only |
| Google Drive “share” page link | Not a direct file URL |
| `panda-hd.online/...` | Web page, not `.m3u` playlist |
| URL with spaces or missing `https://` | BOBPlayer won’t load |

**Correct:** URL must open as **plain text** in a browser and start with `#EXTM3U`

---

## “Expired” message

If BOBPlayer says **expired** → add a **new** custom playlist URL (steps above). That bypasses the old subscription screen.

---

## Checklist

- [ ] Playlist URL pasted in **Playlist URL** field (not name only)  
- [ ] Playlist **saved**  
- [ ] Playlist **selected**  
- [ ] Pressed **Reload** and waited 1 minute  
- [ ] Opened **Channels / Live TV** section  
- [ ] TV has **internet** (Wi‑Fi working)  

---

## Quick test on phone/PC

Open this in a browser — you should see text starting with `#EXTM3U`:

https://iptv-org.github.io/iptv/index.m3u

If that works in browser but not on TV → problem is BOBPlayer reload or TV network.
