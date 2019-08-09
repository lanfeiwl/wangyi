#from 网易test.test_login import LoginTest
import unittest
from selenium import webdriver
import time

class SendEmail(unittest.TestCase):
    def setUp(self):
        self.url="https://mail.163.com/"
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.url)
    def login(self,username,pwd):
        self.driver.find_element_by_id('lbNormal').click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]"))
        self.driver.find_element_by_css_selector("[name='email']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pwd)
        self.driver.find_element_by_id("dologin").click()
    def tearDown(self):
        self.driver.quit()
    def test_sendemail0(self):
        '''内容为空发送邮件'''
        self.login("lanfeiwl","213250fei")
        self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']/span[@class='nui-btn-text']").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".nui-mainBtn[tabindex='0'] > .nui-btn-text").click()
        time.sleep(2)
        send=self.driver.find_element_by_css_selector(".tK1").text
        self.assertEqual(send,"发送成功手机收发邮件更方便")



