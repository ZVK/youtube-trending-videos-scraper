import requests
import json
import html
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


class Scraper:
    """
    Scraper for all urls on a YouTube page.
    """

    URL = "{0}"

    @staticmethod
    def scrape(url="https://youtube.com/"):
        json_array = []

        try:
            response = requests.get(Scraper.URL.format(url))
        except ConnectionError as err:
            json_array.append({"error": str(err)})
            return json.dumps(json_array)

        soup = BeautifulSoup(response.text, "html.parser")
        trending_videos = soup.find_all(attrs={"class": "expanded-shelf-content-item"})
        print(len(trending_videos), 'videos found')
        for video_element in trending_videos:
            video_obj = dict()
            title_content = video_element.find(attrs={"class": "yt-lockup-title"})
            link_meta = title_content.find("a")
            video_obj["video_url"] = link_meta.get("href")
            print(video_obj["video_url"])
            video_obj["video_title"] = link_meta.get("title")
            video_time = title_content.select("span.accessible-description")
            if len(video_time) != 0:
                video_obj["video_time"] = video_time[0].text
            else:
                video_obj["video_time"] = "LIVE NOW"

            profile_content = video_element.find(attrs={"class": "yt-lockup-byline"})
            profile_meta = profile_content.find("a")
            video_obj["profile_url"] = profile_meta.get("href")
            video_obj["profile_name"] = profile_meta.string

            meta_info = video_element.find(attrs={"class": "yt-lockup-meta-info"})
            if len(meta_info.contents) > 1:
                video_obj["upload_date"] = meta_info.contents[0].string
                video_obj["view_count"] = meta_info.contents[1].string.split(" ")[0]
            else:
                video_page_response = requests.get(Scraper.URL.format(country_code) + video_obj["video_url"])
                parsed_response = BeautifulSoup(video_page_response.text, "html.parser")
                if parsed_response.find("span", class_="date"):
                    video_obj["upload_date"] = parsed_response.find("span", class_="date").string
                elif parsed_response.find("strong", class_="watch-time-text"):
                    video_obj["upload_date"] = parsed_response.find("strong", class_="watch-time-text").string
                video_obj["view_count"] = meta_info.contents[0].string

            description_content = video_element.select("div.yt-lockup-description")
            video_description = ""
            if len(description_content) > 0:
                video_description = description_content[0].text
            video_obj["video_desc"] = html.escape(str(video_description))
            json_array.append(video_obj)

        return json.dumps(json_array, sort_keys=True)
