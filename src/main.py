import datetime
import pprint
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

url = "https://rgbcolorcode.com/"

class RGB:

    def __init__(self):

        self.driver_path = "../driver/geckodriver"
        options = Options()
        options.headless = True
        # self.driver = webdriver.Chrome(executable_path=self.driver_path, options=self.chrome_options)

        self.driver = webdriver.Firefox(executable_path=self.driver_path, service_log_path="../logs/geckodriver.log",
                                        options=options)
        self.driver.set_window_size(1280, 720)
        self.wait = WebDriverWait(self.driver, 10)

        self.time_stamp = datetime.datetime.now().strftime('%Y_%m_%d')

    def get_webdriver(self):
        return self.driver

    def get_colors(self):
        self.driver.get(url)
        time.sleep(1)
        r_number = 1
        color_dict = []
        for r in range(1,37):
            color = self.driver.find_element_by_xpath("//*[@id='bigPalette']/div[20]/a["+str(r)+"]")
            color_rgb = str(color.get_attribute("style"))

            color_rgb = color_rgb.replace("background-color: rgb(", "").replace(");","")
            colors = color_rgb.split(",")


            temp = {
            "color": "black",
            "rgb": (int(colors[0]),int(colors[1]),int(colors[2])),
            "r":int(colors[0]),
            "g":int(colors[1]),
            "b":int(colors[2])
            }
            color_dict.append(temp)

        return color_dict



def main():
    rgb = RGB()
    color_dict = rgb.get_colors()


if __name__ == '__main__':
    main()
