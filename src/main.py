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
            )

    def search_video(self, query: str) -> str:
        treated_query = query.replace(' ', '+')
        self.browser.get(f'https://www.youtube.com/results?search_query={treated_query}')
        self.browser.find_element(By.XPATH, '//*[@id="thumbnail"]/yt-image/img').click()
        return self.browser.current_url


api = YoutubeFree()
print(api.search_video('drivers license olivia rodrigo'))

