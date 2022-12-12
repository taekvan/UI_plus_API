import os
from pathlib import Path


class Reporter:

    def __init__(self, driver, config):
        self._driver = driver
        self._reports_path = config['reports_path']

    def save_screenshot_and_page_source(self, filename: str) -> None:
        screenshot_filename = f'{filename}.png'
        screenshot_filepath = os.path.join(self._reports_path, screenshot_filename)
        source_filename = f'{filename}.html'
        source_filepath = os.path.join(self._reports_path, source_filename)

        self.save_page_source(file_path=source_filepath)
        self.save_screenshot(file_path=screenshot_filepath)

    def save_page_source(self, file_path, source) -> None:
        source = source or self._driver.page_source
        try:
            with open(file=file_path, mode='a', encoding='utf-8') as path:
                path.write(source)
        except FileNotFoundError:
            file_dir = Path(file_path).parent
            os.makedirs(file_dir)
            self.save_page_source(file_path=file_path, source=source)

    def save_screenshot(self, file_path: str) -> None:
        self._driver.save_screenshot(filename=file_path)
