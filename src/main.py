from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class YoutubeFree:
    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument('no--sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-extensions')

        self.browser = webdriver.Chrome(
            service = Service(ChromeDriverManager().install()),
            options = self.chrome_options
            )

    def search_videos(self, 
                      query: str, 
                      add_to_search: str = None, 
                      search_range: int = 0) -> List[Dict[str, str]]:
        
        treated_query = query.replace(' ', '+')

        if add_to_search != None:
            treated_add_search = add_to_search.replace(' ', '+')
            treated_query = f'{treated_query}+{treated_add_search}'
        self.browser.get(f'https://www.youtube.com/results?search_query={treated_query}')

        if search_range == 0:
            videos = self.browser.find_elements(By.TAG_NAME, 'ytd-video-renderer')[:1]
        else:
            videos = self.browser.find_elements(By.TAG_NAME, 'ytd-video-renderer')[:search_range]

        videos_info = []
        for video in videos:
            title = video.find_element(By.ID, 'title-wrapper').text
            video_url = video.find_element(By.TAG_NAME, 'a').get_property('href')
            thumbnail = video.find_element(By.TAG_NAME, 'img').get_property('src')
            views = video.find_element(By.ID, 'metadata-line').text
            video_info = {
                'title': title,
                'url': video_url,
                'thumbnail': thumbnail,
                'views': views,
            }
            videos_info.append(video_info)
        return videos_info


api = YoutubeFree()
print(api.search_videos('esquiva esgrima criolo'))

