import unittest

from tube_scrapy import TubeScrapy
from scraped_video_info import ScrapedVideoInfo
from exceptions import AddToSearchError, SearchTitleError, SearchRangeError

class TestTubeScrapy(unittest.TestCase):
    
    def setUp(self) -> None:
        self.tube_scrapy = TubeScrapy()

    def test_search_video_info_return_scraped_video_info(self) -> None:
        result = self.tube_scrapy.search_video_info(
            search_title='Me corte na boca do céu a morta não pede perdão'
        )
        self.assertEquals(type(result[0]), ScrapedVideoInfo)

    def test_search_video_info_raising_search_title_error(self) -> None:
        with self.assertRaises(SearchTitleError) as context:
            self.tube_scrapy.search_video_info(
                search_title=42
            )
        exception_type = type(context.exception)
        self.assertEqual(exception_type, SearchTitleError, msg='SearchTitleError Test')

    def test_search_video_info_raising_add_to_search_error(self) -> None:
        with self.assertRaises(AddToSearchError) as context:
            self.tube_scrapy.search_video_info(
                search_title='Me corte na boca do céu a morte não pede perdão',
                add_to_search=42
            )
        exception_type = type(context.exception)
        self.assertEqual(exception_type, AddToSearchError, msg='AddToSearchError Test')

    def test_search_video_info_raising_search_range_error(self) -> None:
        with self.assertRaises(SearchRangeError) as context:
            self.tube_scrapy.search_video_info(
                search_title='Me corte na boca do céu a morte não pede perdão',
                search_range='42'
            )
        exception_type = type(context.exception)
        self.assertEqual(exception_type, SearchRangeError, msg='SearchRangeError Test')


if __name__ == '__main__':
    unittest.main()