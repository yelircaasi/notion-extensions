from string import Template
from typing import Union, Callable

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from notion_extensions.utils.dicts import dotdict
from notion_extensions.utils.pauses import longpause, pause


def get_browser(
    config: dotdict,
) -> Union[webdriver.chrome.webdriver.WebDriver, webdriver.firefox.webdriver.WebDriver]:
    browser_name = config.general.browser

    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options

        opts = Options()
        opts.add_argument(f"--user-data-dir={config.paths.chrome_profile}")
        browser = webdriver.Chrome(options=opts)

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options

        opts = Options()
        opts.add_argument("-profile")
        opts.add_argument(config.paths.firefox_profile)
        browser = webdriver.Firefox(options=opts)

    return browser


def get_get_xpath_function(template_string: str) -> Callable:
    def get_xpath(week: int, day: int, hour: int, minute: int) -> str:
        day_number = int(day - 4 if week == -1 else day + 3)
        time_number = 2 * (hour - 3) - int(minute == 0)
        template_str = Template(template_string)
        return template_str.substitute(day=day_number, time=time_number)

    return get_xpath


by_xpath = By.XPATH
# escape_key = Keys.ESCAPE


def get_click_function(
    browser, long_pause=False, min_pause=0.5, max_pause=1.5
) -> Callable:
    def click(
        xpath, long_pause=long_pause, min_pause=min_pause, max_pause=min_pause
    ) -> None:
        browser.find_element(By.XPATH, xpath).click()
        if long_pause:
            longpause()
        elif max_pause:
            pause(min_length=(0 or min_pause), max_length=max_pause)

    return click


def get_escape_function(
    browser, long_pause=False, min_pause=0.5, max_pause=1.5
) -> Callable:
    def escape(
        xpath="//body", long_pause=long_pause, min_pause=min_pause, max_pause=min_pause
    ) -> None:
        browser.find_element(By.XPATH, xpath).send_keys(Keys.ESCAPE)
        if long_pause:
            longpause()
        elif max_pause:
            pause(min_length=(0 or min_pause), max_length=max_pause)

    return escape
