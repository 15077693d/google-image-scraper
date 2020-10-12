import json
import os, pathlib
from datetime import datetime
class DataProcessor:
    def __init__(self,keywords):
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime(f"%H:%M-{'-'.join(keywords)}.json")
        images_folder_path = os.path.join(pathlib.Path(os.path.dirname(__file__)).parent,"images")
        date_folder_path = os.path.join(images_folder_path, date)
        self.json_path = os.path.join(date_folder_path, time)
        if not os.path.exists(images_folder_path):
            os.mkdir(images_folder_path)
        if not os.path.exists(date_folder_path):
            os.mkdir(date_folder_path)
        with open(self.json_path, "w") as f:
            json.dump({},f)

    def output(self, keyword, image_urls):
        with open(self.json_path, "r") as f:
            document =json.load(f)
        document[keyword] =image_urls
        with open(self.json_path, "w") as f:
            json.dump(document,f)

