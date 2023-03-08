from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

    def search_videos(self, query: str, add_to_search: str = None, search_range: int = 1) -> str:
        treated_query = query.replace(' ', '+')
        if add_to_search != None:
            treated_add_search = add_to_search.replace(' ', '+')
            treated_query = f'{treated_query}+{treated_add_search}'
        self.browser.get(f'https://www.youtube.com/results?search_query={treated_query}')
        first_video = self.browser.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer')
        title = first_video.find_element(By.XPATH, '//*[@id="title-wrapper"]').text
        video_url = first_video.find_element(By.TAG_NAME, 'a').get_property('href')
        thumbnail = first_video.find_element(By.TAG_NAME, 'img').get_property('src')
        views = first_video.find_element(By.XPATH, '//*[@id="metadata-line"]/span').text
        video_info = {
            'title': title,
            'url': video_url,
            'thumbnail': thumbnail,
            'views': views,
        }
        return video_info


api = YoutubeFree()
print(api.search_videos('esquiva esgrima criolo', 'karaoke'))

