# BOBPlayer TEST playlist

## 11 channels — all tested working (HTTP 200)

| Group | Channels |
|-------|----------|
| News | NASA TV, Al Jazeera Arabic, Al Jazeera English, France 24, DW |
| Sports | Alkass 1, Alkass 2, Arryadia, Al Iraqia Sport, Bahrain Sports, Red Bull TV |

Each channel has **name** + **logo** (`tvg-logo`).

---

## beIN Sports — NOT in this test

**beIN Sport** (بي إن سبورت) is a **paid** channel. It is not in free legal playlists.

- Pirate sites (e.g. panda-hd.online) → illegal, often broken in BOBPlayer  
- Legal way → **beIN subscription** or **beIN Connect** app  

**Sports you CAN open in this test:** Alkass, Arryadia, Bahrain Sports (Arabic free sports).

---

## Use on TV (3 steps)

### 1. Upload to GitHub

1. Go to [github.com](https://github.com) → New repository  
2. Upload **`playlist-test.m3u`**  
3. Click the file → **Raw**  
4. Copy the URL, e.g.  
   `https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/playlist-test.m3u`

### 2. Add in BOBPlayer

1. **Choose Your Playlist** → **+**  
2. Name: `Test`  
3. **Playlist URL:** paste your GitHub Raw URL  
4. **Save**

### 3. Load channels

1. Select **Test** playlist  
2. Press **Reload** — wait 10 seconds  
3. Open **Channels** / **Live TV**  
4. Try **NASA TV** first (always works)  
5. Then open **Alkass One** under **2-Sports | رياضة**

---

## Test on Mac first (optional)

Open `playlist-test.m3u` in **VLC** → you should see 11 channels and video plays.

---

## If test works → use full list

```
https://iptv-org.github.io/iptv/index.m3u
```

If test is **empty** on TV → problem is GitHub URL or BOBPlayer setup (see `BOBPLAYER-FIX-EMPTY.md`).
