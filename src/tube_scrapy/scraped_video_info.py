class ScrapedVideoInfo:
    def __init__(self, title: str, video_url: str, thumbnail_url: str, views: str) -> None:
        self.__title: str = title,
        self.__video_url: str = video_url,
        self.__thumbnail_url: str = thumbnail_url,
        self.__views: str =  views

    @property
    def title(self):
        return self.__title
    
    @property
    def video_url(self):
        return self.__video_url
    
    @property
    def thumbnail_url(self):
        return self.__thumbnail_url
    
    @property
    def views(self):
        return self.__views