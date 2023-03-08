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

    def search_video_info(self, 
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
        elif search_range > 0:
            videos = self.browser.find_elements(By.TAG_NAME, 'ytd-video-renderer')[:search_range]
        else:
            raise Exception('Parameter "search_range" just allow numeric values >= 0')

        videos_infos = []
        for video in videos:
            title = video.find_element(By.ID, 'title-wrapper').text
            video_url = video.find_element(By.TAG_NAME, 'a').get_property('href')
            thumbnail = video.find_element(By.TAG_NAME, 'img').get_property('src')
            views = video.find_element(By.ID, 'metadata-line').text.split('\n')[0]
            video_info = {
                'title': title,
                'url': video_url,
                'thumbnail': thumbnail,
                'views': views,
            }
            videos_infos.append(video_info)
        return videos_infos


api = YoutubeFree()
print(api.search_video_info('esquiva esgrima criolo', 'karaoke', 5))

