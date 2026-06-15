# BOBPlayer web portal — app not working fix

You added the playlist correctly on [bobplayer.com](https://bobplayer.com).
The URL works: [playlist-test.m3u](https://raw.githubusercontent.com/yamenAl/pop-player/main/playlist-test.m3u)

Problem is usually **TV sync** or **device activation**, not the URL.

---

## Step 1 — Check MAC address (most important)

Your portal shows MAC: **`a0:d0:5b:13:b0:ad`**

On your TV:
1. Open **BOBPlayer**
2. Find **MAC address** on the home screen
3. It must match **exactly** `a0:d0:5b:13:b0:ad`

**If different** → on bobplayer.com click **Switch MAC** and enter the MAC from your TV.

> BOBPlayer FAQ: MAC changes if you switch WiFi ↔ Ethernet. Restart app after network change.

---

## Step 2 — Activate device

On bobplayer.com sidebar → **Activate Device**

- New install = **7-day free trial**
- If trial expired → app won't load playlists
- Activate your MAC `a0:d0:5b:13:b0:ad`

---

## Step 3 — Clean playlists on website

You have 2 playlists:
- `shafak tv` (Protected — old, may block sync)
- `All Channels` (your GitHub URL — good)

**Delete `shafak tv`** (trash icon) → keep only **All Channels**.

Edit **All Channels** and use this URL (simpler, no `refs/heads`):

```
https://raw.githubusercontent.com/yamenAl/pop-player/main/playlist-test.m3u
```

Username and Password: **leave empty**

---

## Step 4 — Force sync on TV

1. **Close BOBPlayer completely** (not just back button — force stop app)
2. Wait 10 seconds
3. Open **BOBPlayer** again
4. Go to **Choose Your Playlist**
5. Select **All Channels**
6. Press **Reload** / **Refresh**
7. Wait 15 seconds
8. Open **Live TV** / **Channels**

---

## Step 5 — If still empty — try minimal playlist

Push `playlist-bob-minimal.m3u` to GitHub (only 3 channels, BOBPlayer-safe format).

URL:
```
https://raw.githubusercontent.com/yamenAl/pop-player/main/playlist-bob-minimal.m3u
```

Replace URL in **All Channels** on website → restart TV app.

---

## What does TV show?

| Screen message | Fix |
|----------------|-----|
| **Expired** | Activate device on website |
| **Playlist not working** | Check internet, try minimal URL |
| **Empty list** | Wrong MAC, didn't Reload, or old `shafak tv` playlist |
| **Channels listed, no video** | Stream geo-blocked — try NASA TV first |

---

## Test NASA TV first

NASA TV works almost everywhere. If NASA plays but sports don't → playlist works, sports blocked in your country.
