from selenium.webdriver import Chrome
import os
import pathlib
import logging
from resources.config import *
model_folder_path = os.path.dirname(__file__)
selenium_folder = pathlib.Path(model_folder_path).parent
executable_path = os.path.join(selenium_folder,"resources/chromedriver")
class GoogleDriver(Chrome):
    def __init__(self):
        super(GoogleDriver, self).__init__(executable_path=executable_path)
        logging.info("googleDriver init!")

    def go_google_image(self, keyword):
        logging.info(f"googleDriver go to {keyword}")
        self.get(f"https://www.google.com/search?q={keyword}&rlz=1C5CHFA_enHK895HK895&sxsrf=ALeKk02jdlNOuo091b6dCUxUdnFpoEzsiw:1602317370959&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjW4dmtyansAhUUK6YKHRJ9DpwQ_AUoAXoECAYQAw&biw=1266&bih=1029 ")

    def get_image_urls(self):
         image_elements = self.find_elements_by_xpath(xpath['image_img'])
         image_urls = list(map(lambda element: element.get_attribute("src"),image_elements))
         logging.info(f"Got image url: ({len(image_urls)}) {image_urls}")
         return image_urls

    def scroll_down(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        logging.info(f"scroll down")

    def click_show_more(self):
        btn=self.find_element_by_xpath(xpath['show_more_btn'])
        if btn.is_displayed():
            btn.click()

    def is_end(self):
        div = self.find_element_by_xpath(xpath['end_div'])
        return div.is_displayed()