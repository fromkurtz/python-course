from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC =ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_services = Service()
chrome_browser = webdriver.Chrome()