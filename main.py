import concurrent.futures as cf
import time
import asyncio
import selenium
import seleniumwire
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from seleniumwire.webdriver import EdgeOptions


class Driver_Adapter(webdriver.Edge):
    def __init__(self, link, *args, **kwargs):
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("start-maximized")
        edge_options.page_load_strategy = "eager"
        edge_options.add_argument("disable-gpu")
        edge_options.add_argument("headless")
        edge_options.add_argument("--proxy_server=%s" % "http://24.158.29.166:80")
        super().__init__(edge_options=edge_options)
        self.link = link
        self.start_time = time.perf_counter()
        self.valid_resps = [200, 301, 302, 307, 404]


def make_driver(link, program_start) -> webdriver:
    driver = Driver_Adapter(link)
    driver.get(driver.link)
    print(f"Adapter Created {driver.start_time - program_start:.2f}")
    return driver

def get_deck():
    print("test")
    return


with cf.ThreadPoolExecutor(max_workers=16) as executor:
    with open("blue_farm_links", "r") as file:
        successful_drivers = []
        program_start = time.perf_counter()
        test_links = file.read().strip().split('\n')
        futures = [executor.submit(make_driver(link, program_start)) for link in test_links]
        futures = [future.add_done_callback(fn=get_deck()) for future in futures]
        for future in cf.as_completed(futures):
            testing = [request.response.status_code for request in future.result().requests if
                       request.url == future.result().link]
