Inspired by [@simonw](https://github.com/simonw)'s blog post on downloading TikTok's videos: https://til.simonwillison.net/tiktok/download-all-videos

This is an alternative to get the URLs needed as described by [@simonw](https://github.com/simonw) using pretty basic Python. If you know how to use Python, should be pretty simple; I made this really quickly so it's not 'dummy-proof' but hopefully helpful!

## Steps

0. Request your personal data: https://support.tiktok.com/en/account-and-privacy/personalized-ads-and-data/requesting-your-data
  - Select JSON option
  - Wait and then download to computer
1. Clone this repository
2. Ensure your file is moved to inside cloned repo
  - Right now, the file must be named `user_data_tiktok.json`
3. Run script
  - Run `python get_video_urls.py`
  - You can modify script so `video_limit` is a value (defaults to no limit)
  - Output `videos.json`
4. Copy printout of URLs (if not using the output file `videos.json`)
5. Follow [@simonw](https://github.com/simonw)'s blog at https://til.simonwillison.net/tiktok/download-all-videos


### Note on bash script from [@simonw](https://github.com/simonw)

The script used by [@simonw](https://github.com/simonw) had some issues with long
titles (see [_Download them all with yt-dlp_](https://til.simonwillison.net/tiktok/download-all-videos#download-them-all-with-yt-dlp:~:text=Download%20them%20all%20with%20yt%2Ddlp)) section:

I've slightly modified it to only name the video by ID but create a log with the
`{ID} : {Title}` for each video:

```bash
mkdir -p downloads
jq -r '.[]' videos.json | while read url; do
    uvx yt-dlp \
      -o "downloads/favs/%(id)s.%(ext)s" \
      --exec 'echo "%(id)s : %(title)s" >> downloads/log.txt' \
      "$url" 
    if [[ $? -eq 0 ]]; then
        echo "Successfully downloaded: $url"
    else
        echo "Failed to download: $url"
    fi
    sleep 1
done
```
I also added this as a file [download.sh](download.sh) that can be used 
directly. (Assumes you have [uv](https://docs.astral.sh/uv/getting-started/installation/)
and [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed.)


## Disclaimer

I make no claims this will keep working or that will keep working in the long-run. Best of luck ♥️
 
