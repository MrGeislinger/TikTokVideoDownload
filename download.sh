mkdir -p downloads
jq -r '.[]' videos.json | while read url; do
    uvx yt-dlp \
      -o "downloads/%(id)s.%(ext)s" \
      --exec 'echo "%(id)s : %(title)s" >> downloads/log.txt' \
      "$url" 
    if [[ $? -eq 0 ]]; then
        echo "Successfully downloaded: $url"
    else
        echo "Failed to download: $url"
    fi
    sleep 1
done