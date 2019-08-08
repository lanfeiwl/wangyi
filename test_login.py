from selenium import webdriver
import unittest
class LoginTest(unittest.TestCase):
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
    def test_loginsucess(self):
        self.login("lanfeiwl","213250fei")
        t = self.driver.find_element_by_id("spnUid").text
        print("获取到我的账户:", t)
        self.assertEqual(t,"lanfeiwl@163.com")
    def test_nulluser(self):
        self.login('','')
        u=self.driver.find_element_by_css_selector(".ferrorhead").text
        print("错误提示:", u)
        self.assertEqual(u, "请输入帐号")