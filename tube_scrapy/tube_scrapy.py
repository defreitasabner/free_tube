from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from tube_scrapy.scraped_video_info import ScrapedVideoInfo
from tube_scrapy.exceptions import AddToSearchError, SearchTitleError, SearchRangeError

class TubeScrapy:
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
                      search_title: str, 
                      add_to_search: str = '', 
                      search_range: int = 1) -> List[ScrapedVideoInfo]:
        """
        Method which webscraping Youtube to return video info. The search is based in a `query` with the name of video. You could `add_to_search` to add a term to the main `query`. The argument `search_range` determine how many videos info would be returned based in order which the videos appears on Youtube page.
        """
        if type(search_title) != str:
            raise SearchTitleError('Parameter "search_title" just allow type \'strings\'.')
        if type(add_to_search) != str:
            raise AddToSearchError('Parameter "add_to_search" just allow type \'strings\'.')
        if type(search_range) != int or search_range < 0:
            raise SearchRangeError('Parameter "search_range" just allow type \'int\' and with value > 1.')
        
        treated_query = search_title.replace(' ', '+')
        
        treated_add_search = add_to_search.replace(' ', '+')
        treated_query = f'{treated_query}+{treated_add_search}'
            
        self.browser.get(f'https://www.youtube.com/results?search_query={treated_query}')

        videos = self.browser.find_elements(By.TAG_NAME, 'ytd-video-renderer')[:search_range]

        videos_infos = []
        for video in videos:
            title = video.find_element(By.ID, 'title-wrapper').text
            video_url = video.find_element(By.TAG_NAME, 'a').get_property('href')
            thumbnail = video.find_element(By.TAG_NAME, 'img').get_property('src')
            views = video.find_element(By.ID, 'metadata-line').text.split('\n')[0]
            video_info = ScrapedVideoInfo(
                title = title,
                video_url = video_url,
                thumbnail_url= thumbnail,
                views = views
            )
            videos_infos.append(video_info)
        return videos_infos
