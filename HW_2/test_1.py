import pytest
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    assert answer.text == f'Hello, {testdata["login"]}'


def test_step_3(site, select_input_login, select_input_password, select_input_button, select_create_post,
                select_create_post_title, select_save_post, select_post_title, select_delete_post):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn1 = site.find_element('css', select_input_button)
    btn1.click()
    time.sleep(testdata['sleep_time'])
    btn2 = site.find_element('xpath', select_create_post)
    btn2.click()
    time.sleep(testdata['sleep_time'])
    input3 = site.find_element('xpath', select_create_post_title)
    input3.send_keys(testdata['title_post'])
    btn3 = site.find_element('xpath', select_save_post)
    btn3.click()
    time.sleep(testdata['sleep_time'])
    answer = site.find_element('xpath', select_post_title)
    btn4 = site.find_element('xpath', select_delete_post)
    btn4.click()
    assert answer.text == testdata['title_post']
