# TubeScrapy
A python package to webscrap for youtube video data as title, video url, thumbnail url, and number of views. The package runs packages  `Selenium` and `Webdriver` to access Youtube page and copy videos informations. The process is expensive and remains about 5 seconds for search. The first search could take a little more time because package `Webdriver` will download and install the web driver to control Chrome browser.

### Python minimal version
- Python 3.8

### Python packages required
- Selenium 4.8.2
- Webdriver-manager 3.8.5

## Examples
First of all, import module:
~~~python
import tube_scrapy
~~~
Create a new instance of `TubeScrapy`:
~~~python
ts = TubeScrapy()
~~~
Create a variable to save video info searched using method `search_video_info()`:
~~~python
videos_infos = ts.search_video_info(
    search_title = 'Cheia de Manias Raça Negra', # search title or query
    add_to_search = 'karaoke', # will basiclly be concatened with search_title
    search_range = 5 # quantity of videos searched
)
~~~
The videos informations will be returned in a `list` of objects `ScrapedVideoInfo`, which have this structure:
~~~python
ScrapedVideoInfo(
    title = title,              # youtube video title
    video_url = video_url,      # youtube video url
    thumbnail_url= thumbnail,   # video thumbnail url
    views = views               # video number of views
)
~~~