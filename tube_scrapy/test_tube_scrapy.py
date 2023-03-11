import unittest

from tube_scrapy import TubeScrapy
from exceptions import AddToSearchError, SearchTitleError, SearchRangeError

class TestTubeScrapy(unittest.TestCase):
    
    def setUp(self) -> None:
        self.tube_scrapy = TubeScrapy()

    def test_search_video_info_raising_search_title_error(self) -> None:
        with self.assertRaises(SearchTitleError):
            self.tube_scrapy.search_video_info(
                search_title= 42
            )

    def test_search_video_info_raising_search_range_error(self) -> None:
        with self.assertRaises(SearchRangeError):
            self.tube_scrapy.search_video_info(
                search_title='Me corte na boca do céu a morte não pede perdão',
                search_range='42'
            )


if __name__ == '__main__':
    unittest.main()