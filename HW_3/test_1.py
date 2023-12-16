from testpage import OperationsHelper
import logging
import yaml
import time


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test1 starting")
    test_page = OperationsHelper(browser)
    test_page.log_in('test', 'test')
    assert test_page.get_error_text() == '401'


def test_step_2(browser):
    logging.info("Test2 starting")
    test_page = OperationsHelper(browser)
    test_page.log_in(testdata['login'], testdata['password'])
    assert test_page.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(browser):
    logging.info("Test3 starting")
    test_page = OperationsHelper(browser)
    test_page.click_contact_link()
    time.sleep(testdata['sleep_time'])
    assert test_page.get_go_to_contact_text() == 'Contact us!'


def test_step_4(browser):
    logging.info("Test4 starting")
    test_page = OperationsHelper(browser)
    test_page.enter_contact_name('test')
    assert True


def test_step_5(browser):
    logging.info("Test5 starting")
    test_page = OperationsHelper(browser)
    test_page.enter_contact_name('test')
    assert True


def test_step_6(browser):
    logging.info("Test6 starting")
    test_page = OperationsHelper(browser)
    test_page.enter_contact_email('test@mail.ru')
    assert True


def test_step_7(browser):
    logging.info("Test7 starting")
    test_page = OperationsHelper(browser)
    test_page.enter_contact_content('test')
    assert True


def test_step_8(browser):
    logging.info("Test8 starting")
    test_page = OperationsHelper(browser)
    test_page.click_contact_us_button()
    assert True


def test_step_9(browser):
    logging.info("Test9 starting")
    test_page = OperationsHelper(browser)
    time.sleep(testdata['sleep_time'])
    assert test_page.get_alert_text() == "Form successfully submitted"