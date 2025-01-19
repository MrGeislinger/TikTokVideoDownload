mkdir -p downloads/favs
jq -r '.[]' videos.json | while read url; do
    uvx yt-dlp \
      -o "downloads/favs/%(id)s.%(ext)s" \
      --exec 'echo "%(id)s : %(title)s" >> downloads/favs/log.txt' \
      "$url" 
    if [[ $? -eq 0 ]]; then
        echo "Successfully downloaded: $url"
    else
        echo "Failed to download: $url"
    fi
    sleep 1
done