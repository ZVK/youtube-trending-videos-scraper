## Youtube Videos Scraper

This is a Python scraper for collecting urls any YouTube page.

## Contents

* [Requirements/Installation](#req/install)
* [Usage](#usage)
* [Output](#output)
* [Contribute](#contribute)
* [License](https://github.com/jessecordeiro/youtube-trending-videos-scraper/blob/master/LICENSE)

## <a name="req/install"></a>Requirements/Installation

1. **Install requirement(s):**
  + [Python >= 3.4.3](https://www.python.org/downloads/release/python-343/)
  + [pip](https://pip.pypa.io/en/stable/installing/)

2. **Clone repository:**

  ```bash
  git clone https://github.com/zvk/youtube-url-scraper.git
  cd youtube-trending-videos-scraper
  ```

3. **Install dependencies:**

  ```bash
  python setup.py develop
  ```

## <a name="usage"></a>Usage
```python
import youtube_url_scraper

youtube_trending_scraper.Scraper.scrape()
```
#### Required argument: url
```python
# Example: scrape news videos in France
youtube_trending_scraper.Scraper.scrape("https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw?gl=FR&hl=fr")
```

## <a name="output"></a>Output
```js
[{
  "profile_name": "Lorem ipsum",
  "profile_url": "/user/loremipsumdolor",
  "upload_date": "1 day ago",
  "video_desc": "Lorem ipsum dolor sit amet, hymenaeos sodales in, scelerisque at.",
  "video_thumbnail": "https://..",
  "video_time": "2:12",
  "video_title": "Lorem ipsum dolor sit amet",
  "video_url": "/watch?v=loR3MIpSUMgd",
  "view_count": "3,151,740"
}]
```

## <a name="contribute"></a>Contribute
1. Fork the repository
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Implemented x feature'`
4. Push to the feature branch: `git push origin x-feature`
5. Open a pull request
