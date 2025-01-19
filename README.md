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

## Disclaimer

I make no claims this will keep working or that will keep working in the long-run. Best of luck ♥️
 
