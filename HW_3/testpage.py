from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
	LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
	LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
	LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
	LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
	LOCATOR_SUCCESS_FIELD = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
	LOCATOR_CONTACT_LINK = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]''')
	LOCATOR_GO_TO_CONTACT = (By.XPATH, '''//*[@id="app"]/main/div/div/h1''')
	LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
	LOCATOR_SUCCESS_CONTACT_NAME = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
	LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
	LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
	LOCATOR_CONTACT_US_BTN = (By.XPATH, '''//*[@id="contact"]/div[4]/button/span''')


class OperationsHelper(BasePage):
	def enter_login(self, word):
		logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
		login_field.clear()
		login_field.send_keys(word)

	def enter_pass(self, word):
		logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
		login_field.clear()
		login_field.send_keys(word)

	def click_login_button(self):
		logging.info('Click login button')
		self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

	def log_in(self, login, password):
		logging.info('Log in to the site')
		self.go_to_site()
		self.enter_login(login)
		self.enter_pass(password)
		self.click_login_button()

	def get_error_text(self):
		error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
		text = error_field.text
		logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
		return text

	def get_success_text(self):
		success_field = self.find_element(TestSearchLocators.LOCATOR_SUCCESS_FIELD, time=3)
		text = success_field.text
		logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_SUCCESS_FIELD[1]}")
		return text

	def click_contact_link(self):
		logging.info('Click contact link')
		self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

	def get_go_to_contact_text(self):
		go_to_contact_field = self.find_element(TestSearchLocators.LOCATOR_GO_TO_CONTACT, time=3)
		text = go_to_contact_field.text
		logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_GO_TO_CONTACT[1]}")
		return text

	def enter_contact_name(self, word):
		logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD, time=3)
		login_field.clear()
		login_field.send_keys(word)

	def enter_contact_email(self, word):
		logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD, time=3)
		login_field.clear()
		login_field.send_keys(word)

	def enter_contact_content(self, word):
		logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD, time=3)
		login_field.clear()
		login_field.send_keys(word)

	def click_contact_us_button(self):
		logging.info('Click contact us button')
		self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

	def get_alert_text(self):
		alert = self.driver.switch_to.alert
		text = alert.text
		logging.info(f"We find text {text} after click contact us button")
		return text