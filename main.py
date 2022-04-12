# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Automate exporting of invoices as PDFs
# author            : Ian Ault
# email             : service@nanosystems1.com
# date              : 03-30-2022
# version           : v1.0
# usage             : python main.py
# notes             :
# license           : MIT
# py version        : 3.10.2 (must run on 3.6 or higher)
#==============================================================================
import os
import time
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from settings import *


link = "https://secure1.mhelpdesk.com/Modules/Accounting/Invoices_Page.aspx?mhd_enc=x3bLL/enJTFdtFnkyW7OOA=="


class Scraper:
	def __init__(self):
		options = Options()
		user_data_dir = os.path.abspath("selenium_data")
		options.add_argument(f"user-data-dir={user_data_dir}")
		options.add_argument("log-level=3")
		if HEADLESS:
			options.add_argument("--headless")
			options.add_argument("--disable-gpu")
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		# self.driver.minimize()
		print("Init finished")

	def wait_until_element(self, selector, locator, timeout=10):
		wait = WebDriverWait(self.driver, timeout)
		element = wait.until(
			EC.presence_of_element_located(
				(
					selector, locator
				)
			)
		)
		return element

	def wait_until_elements(self, selector, locator, timeout=10):
		wait = WebDriverWait(self.driver, timeout)
		elements = wait.until(
			EC.presence_of_all_elements_located(
				(
					selector, locator
				)
			)
		)
		return elements

	def find_element(self, selector, sequence):
		return self.driver.find_element(selector, sequence)

	def find_elements(self, selector, sequence):
		return self.driver.find_elements(selector, sequence)

	def wait_until_element_by_xpath(self, sequence):
		return self.wait_until_element(By.XPATH, sequence)

	def wait_until_elements_by_xpath(self, sequence):
		return self.wait_until_elements(By.XPATH, sequence)

	def find_element_by_xpath(self, sequence):
		return self.find_element(By.XPATH, sequence)

	def find_elements_by_xpath(self, sequence):
		return self.find_elements(By.XPATH, sequence)

	def open_link(self, url):
		self.driver.get(url)

	def current_url(self):
		return self.driver.current_url

	def close(self):
		self.driver.close()

	def refresh(self):
		self.driver.refresh()

	def run(self):
		self.open_link(LINK)
		time.sleep(1)


def main():
	scraper = Scraper()
	scraper.run()
	# scraper.close()


if __name__ == "__main__":
	main()
