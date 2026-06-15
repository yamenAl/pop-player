# How to Make Your Own Playlist for BOBPlayer

## What You Need

- A computer (Windows, Mac, or Linux)
- A text editor (Notepad on Windows, TextEdit on Mac)
- Stream URLs (links to video/TV streams — `.m3u8` or `.ts`)
- A place to host your file online

## Step 1: Create Your M3U Playlist File

1. Open Notepad (Windows) or TextEdit (Mac).
2. On Mac: go to **Format → Make Plain Text** first.
3. Type or paste the following structure:

```m3u
#EXTM3U

#EXTINF:-1 group-title="News",BBC News
http://your-stream-link-here.m3u8

#EXTINF:-1 group-title="News",Al Jazeera
http://your-stream-link-here.m3u8

#EXTINF:-1 group-title="Sports",My Sports Channel
http://your-stream-link-here.m3u8
```

### Understanding the Format

| Part | What it means |
|------|----------------|
| `#EXTM3U` | Always the first line — marks this as a playlist |
| `#EXTINF:-1` | Start of a channel entry (`-1` means no time limit) |
| `group-title="News"` | The category/group shown in BOBPlayer |
| `BBC News` | The channel name shown in BOBPlayer |
| `http://...` | The actual stream link (must be on its own line) |

4. Save the file as `playlist.m3u`:
   - **Windows**: choose "All Files" in save type, then name it `playlist.m3u`
   - **Mac**: make sure it ends in `.m3u` not `.txt`

## Step 2: Find Free Stream URLs

You need working stream URLs to put in your playlist.

⚠️ **Only use legal, licensed streams. Do not use pirated content.**

### Free Public Streams

| Channel | URL |
|---------|-----|
| NASA TV | `https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8` |
| France 24 English | `https://stream.france24.com/hls/live/2037194/F24_EN_HI_HLS/master.m3u8` |
| DW English | `https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8` |

For Al Jazeera English and others: search for the current live `m3u8` URL — links change over time.

### Finding More Streams

- Search for: free iptv m3u8 streams (legal sources only)
- GitHub has many free public IPTV lists: [github.com/iptv-org/iptv](https://github.com/iptv-org/iptv)
- URLs must end in `.m3u8` or `.ts` to work in BOBPlayer

Test each stream URL in a browser or VLC first before adding it.

## Step 3: Host Your Playlist Online

BOBPlayer needs a URL to your file — it cannot read files directly from your computer.

### Option A: GitHub (Recommended — Free & Reliable)

1. Go to [github.com](https://github.com) and create a free account.
2. Click **New Repository** → name it `my-playlist` → click **Create**.
3. Click **Add file** → **Upload files** → upload your `playlist.m3u`.
4. Click the file → click **Raw**.
5. Copy the URL from your browser — it will look like:

`https://raw.githubusercontent.com/yourusername/my-playlist/main/playlist.m3u`

### Option B: Google Drive (Easy)

1. Upload `playlist.m3u` to Google Drive.
2. Right-click the file → **Share** → **Anyone with the link**.
3. Copy the file ID from the share link.
4. Your direct URL will be:

`https://drive.google.com/uc?export=download&id=YOUR_FILE_ID`

### Option C: Dropbox

1. Upload `playlist.m3u` to Dropbox.
2. Click **Share** → **Create link**.
3. Change `www.dropbox.com` to `dl.dropboxusercontent.com` in the URL.

## Step 4: Add Playlist to BOBPlayer

1. Open BOBPlayer on your TV.
2. Go to **Choose Your Playlist**.
3. Click the **+** or **Add** button.
4. Select the **General** tab.
5. Enter a **Playlist Name** (e.g. "My Channels").
6. Paste your hosted URL into the **Playlist URL** field.
7. Click **Save**.
8. Select your playlist and press **Reload**.

## Example Complete Playlist

```m3u
#EXTM3U

#EXTINF:-1 group-title="Space",NASA TV
https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8

#EXTINF:-1 group-title="News",France 24 English
https://stream.france24.com/hls/live/2037194/F24_EN_HI_HLS/master.m3u8

#EXTINF:-1 group-title="News",DW English
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Channel won't play | The stream URL may be dead — find a new one |
| Playlist not loading | Check your URL is correct and publicly accessible |
| Channels show but no video | Stream may be geo-blocked in your country |
| BOBPlayer says expired | This is your old subscription — a new playlist fixes it |

## Tips

- Keep your playlist updated — stream URLs can stop working
- Use `group-title` to organise channels into categories
- You can have multiple playlists saved in BOBPlayer
- Test each stream URL in a browser or VLC first before adding it
