from model.googleDriver import GoogleDriver
import argparse
from model.dataProcessor import DataProcessor
def run(keywords):
    driver = GoogleDriver()
    tool = DataProcessor(keywords)
    for keyword in keywords:
        driver.go_google_image(keyword=keyword)
        while True:
            driver.scroll_down()
            driver.click_show_more()
            if driver.is_end():
                break
        driver.scroll_down()
        image_urls = driver.get_image_urls()
        tool.output(keyword, image_urls)
    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter keywords for searching...(sep by ,)")
    parser.add_argument("--keywords",'-k', default="", help="Enter keywords for searching...(sep by ,)")
    args = parser.parse_args()
    run(args.keywords.split(","))
