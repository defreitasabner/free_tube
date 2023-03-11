class ScrapedVideoInfo:
    """
    An object which contains scraped data from a Youtube's Video.
    """
    def __init__(self, title: str, video_url: str, thumbnail_url: str, views: str) -> None:
        self.__title: str = title
        self.__video_url: str = video_url
        self.__thumbnail_url: str = thumbnail_url
        self.__views: str =  views

    def __repr__(self) -> str:
        return f'ScrapedVideoInfo({self.__title})'

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def video_url(self) -> str:
        return self.__video_url
    
    @property
    def thumbnail_url(self) -> str:
        return self.__thumbnail_url
    
    @property
    def views(self) -> str:
        return self.__views
