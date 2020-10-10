import unittest
from model.googleDriver import GoogleDriver
class googleDriverTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GoogleDriver()

    def test_01_go_google_image(self):
        self.driver.go_google_image(keyword="orange")
        actual_element = self.driver.find_element_by_xpath('//input[@aria-label="搜尋" or @aria-label="Search"]')
        # src href id
        actual = actual_element.get_attribute("value")
        expect = "orange"
        self.assertEqual(expect,actual)

    def test_02_get_image_urls_1(self):
        self.driver.go_google_image(keyword="orange")
        image_urls=self.driver.get_image_urls()
        test_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQc_GhedODNS3-tw2MHvVfK5jNzFFH5coL-IQ&usqp=CAU"
        actual = test_url in image_urls
        expect = True
        self.assertEqual(expect, actual)

    def test_03_get_image_urls_with_scroll_down(self):
        self.driver.go_google_image(keyword="orange")
        while True:
            self.driver.scroll_down()
            element=self.driver.find_element_by_xpath('//input[@value="Show more results"]')
            if element.is_displayed():
                self.driver.click_show_more()
                break
        self.driver.scroll_down()
        image_urls=self.driver.get_image_urls()
        test_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRQLuZpO6s6-0h8XA7fecoBCVpezui64mMcmQ&usqp=CAU"
        actual = test_url in image_urls
        expect = True
        self.assertEqual(expect, actual)

    def test_04_get_image_urls_with_is_end(self):
        self.driver.go_google_image(keyword="orange")
        test_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQY0_Wna_Tsw7__5Loyv_pKSrnFlqdiSIFUWg&usqp=CAU"
        while True:
            self.driver.scroll_down()
            self.driver.click_show_more()
            if self.driver.is_end():
                break
        self.driver.scroll_down()
        image_urls = self.driver.get_image_urls()
        actual = test_url in image_urls
        expect = True
        self.assertEqual(expect, actual)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()