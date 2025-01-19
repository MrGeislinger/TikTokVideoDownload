import json



def pull_data(
    data: dict,
    key_name: str,
    debug: bool = True,
):
    inner_data = data.get(key_name, dict())
    if debug:
        print(f'{key_name} - # of Items: {len(inner_data)}')
    return inner_data

def get_urls_from_favs(
    data: list[dict],
    limit: int | None = None,
    debug: bool = True,
) -> list[str]:
    key_name: str = 'Link'
    if limit is None:
        limited_data = data
    else:
        limited_data = data[:limit]
    just_urls = [
        item.get(key_name)
        for item in limited_data
    ]
    if debug:
        print(f'Pulled from {key_name=} - # of Items: {len(just_urls)}')
    return just_urls


if __name__ == '__main__':

    fname = 'user_data_tiktok.json'
    debug: bool = True
    video_limit: int = 5

    with open(fname,'r') as fp:
        full_data = json.load(fp)
        print(f'Found file - # of Items: {len(full_data)}')
        data = full_data

        nested_keys = (
            "Activity",
            "Favorite Videos",
            "FavoriteVideoList",
        )
        # Get favorite videos
        for k in nested_keys:
            data = pull_data(
                data=data,
                key_name=k,
                debug=debug,
            )
        
        # Get video URLs
        urls = get_urls_from_favs(
            data=data,
            limit=video_limit,
            debug=True,
        )
        print('Video Urls')
        print(urls)
    
    
    
    