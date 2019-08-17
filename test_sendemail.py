#from 网易test.test_login import LoginTest
import unittest
from selenium import webdriver
import os
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.support.ui import Select




class SendEmail(unittest.TestCase):
    def setUp(self):
        self.url="https://mail.163.com/"
        self.driver=webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(self.url)
        self.driver.execute_script("window.open('http://image.baidu.com/')")
    def login(self,username,pwd):
        self.driver.find_element_by_id('lbNormal').click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]"))
        self.driver.find_element_by_css_selector("[name='email']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pwd)
        self.driver.find_element_by_id("dologin").click()
    def tearDown(self):
        self.driver.quit()
    def test_sendnullemail0(self):
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
    def test_sendemail02(self):
        '''标题不为空时发送邮件'''
        self.login("lanfeiwl","213250fei")
        self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")
        self.driver.implicitly_wait(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))
        self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']/span[@class='nui-btn-text']").click()
        time.sleep(2)
        send=self.driver.find_element_by_css_selector(".tK1").text
        self.assertEqual(send,"发送成功手机收发邮件更方便")
    def test_fileuploademail03(self):
        '''发送有附件的邮件'''
        self.login("lanfeiwl", "213250fei") #登录
        self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()#写信
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")#输入收件人
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")#邮件主题
        self.driver.implicitly_wait(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))#切到iframe页面
        self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
        time.sleep(3)
        self.driver.switch_to.default_content()#切换回主页面
        self.driver.find_element_by_css_selector(".O0").send_keys("D:\\text.txt")#上传文件type为file时可以直接操作
        t= self.driver.find_element_by_css_selector(".o0").text
        print(t)
        self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']/span[@class='nui-btn-text']").click()
        time.sleep(2)
        send = self.driver.find_element_by_css_selector(".tK1").text
        self.assertEqual(send, "发送成功手机收发邮件更方便")
    def test_sendphotoemail04(self):
        '''发送图片的邮件'''
        self.login("lanfeiwl", "213250fei") #登录
        self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()#写信
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")#输入收件人
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")#邮件主题
        self.driver.implicitly_wait(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))#切到iframe页面
        self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
        time.sleep(3)
        self.driver.switch_to.default_content()#切换回主页面
        self.driver.find_element_by_css_selector(".O0").send_keys("D:\\text.txt")#上传文件type为file时可以直接操作
        t= self.driver.find_element_by_css_selector(".o0").text
        print(t)
        self.driver.find_element_by_css_selector(".ico-editor-image").click()#上传图片功能
        #网址url上传
        self.driver.find_element_by_css_selector("div.nui-normalTabs > div:nth-of-type(2)").click()
        self.driver.find_element_by_css_selector("ul.APP-editor-insertPic-panel .nui-ipt-input").send_keys("http://pic41.nipic.com/20140508/18609517_112216473140_2.jpg")
        self.driver.find_element_by_css_selector("ul.APP-editor-insertPic-panel span > .nui-mainBtn > .nui-btn-text").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("div.APP-editor-insertPic-remark > .nui-mainBtn > .nui-btn-text").click()
        time.sleep(5)
        os.system("D:\\py\\testwyi\\openfile.exe"+" "+"chrome"+" "+"D:\\py\\testwyi\\111.png")#获取需要上传的文件
        print(2)
        time.sleep(5)
        self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']/span[@class='nui-btn-text']").click()
        time.sleep(2)
        send = self.driver.find_element_by_css_selector(".tK1").text
        self.assertEqual(send, "发送成功手机收发邮件更方便")
    def test_sendemail05(self):
          '''标题不为空时发送邮件'''
          self.login("lanfeiwl","213250fei")
          self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()
          self.driver.implicitly_wait(3)
          self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")
          self.driver.implicitly_wait(3)
          self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")
          self.driver.implicitly_wait(3)
          self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))
          self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
          time.sleep(3)
          self.driver.switch_to.default_content()
          self.driver.find_element_by_css_selector("div.fq0 > .js-component-link").click()
          c=self.driver.find_element_by_xpath("//div[@class='gm0']/span[@class='js-component-checkbox nui-chk nui-chk-hasText  ']/span[.='定时发送']")
          c.click()
          #t=c.text
          #print(t)
          #time.sleep(3)
          #print(2)
          Select(self.driver.find_element_by_xpath("//select[1]")).select_by_value("2019")
          Select(self.driver.find_element_by_xpath("//select[2]")).select_by_value("8")
          Select(self.driver.find_element_by_xpath("//select[3]")).select_by_value("12")
          Select(self.driver.find_element_by_xpath("//select[4]")).select_by_value("10")
          Select(self.driver.find_element_by_xpath("//select[5]")).select_by_value("30")
          self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']/span[@class='nui-btn-text']").click()
          time.sleep(2)
          send=self.driver.find_element_by_css_selector(".tK1").text
          self.assertEqual(send,"定时发信设置成功手机收发邮件更方便")
    def test_sendemail06(self):
          '''多选框冲突'''
          self.login("lanfeiwl","213250fei")
          self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()
          self.driver.implicitly_wait(3)
          self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")
          self.driver.implicitly_wait(3)
          self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")
          self.driver.implicitly_wait(3)
          self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))
          self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
          time.sleep(3)
          self.driver.switch_to.default_content()
          self.driver.find_element_by_css_selector("div.fq0 > .js-component-link").click()
          c=self.driver.find_element_by_xpath("//div[@class='gm0']/span[@class='js-component-checkbox nui-chk nui-chk-hasText  ']/span[.='定时发送']")
          c.click()
          self.driver.find_element_by_xpath("//div[@class='gm0']/span[@class='js-component-checkbox nui-chk nui-chk-hasText  ']/span[.='邮件加密']").click()
          time.sleep(5)
          x=self.driver.find_element_by_css_selector(".nui-msgbox-title").text
          time.sleep(5)
          print(x)
          b=self.driver.find_element_by_css_selector(".nui-mainBtn[tabindex='0']")
          print(b.text)
          b.click()
          time.sleep(5)
          self.driver.find_element_by_xpath("//header[@class='frame-main-cont-head frame-main-cont-head-shadow']//div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']").click()
          self.driver.implicitly_wait(30)
          send=self.driver.find_element_by_css_selector(".tK1").text
          self.assertEqual(send,"")
          time.sleep(5)
    def test_sendemail07(self):
        '''新打开一个窗口'''
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.login("lanfeiwl", "213250fei")
        self.driver.find_element_by_css_selector("li.mD0 > .oz0").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("1486008931@qq.com")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_css_selector("input[maxlength='256']").send_keys("测试1")
        self.driver.implicitly_wait(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))
        self.driver.find_element_by_css_selector(".nui-scroll").send_keys("1111122222")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_css_selector("[src='http://e.hiphotos.baidu.com/image/h%3D300/sign=907f6e689ddda144c5096ab282b6d009/dc54564e9258d1092f7663c9db58ccbf6c814d30.jpg']").click()
        self.driver.switch_to_window(self.driver.window_handles[2])
        time.sleep(5)

        element=self.driver.find_element_by_xpath("//img[@id='currentImg']")
        action=ActionChains(self.driver).move_to_element(element)
        action.context_click()
        action.perform()
        sleep(2)
        #ActionChains(self.driver).send_keys('y').perform()
        pyautogui.typewrite(['down', 'down', 'down'])
        sleep(2)
        pyautogui.typewrite(['enter'])
        sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@class='APP-editor-iframe']"))
        self.driver.find_element_by_css_selector(".nui-scroll").send_keys(Keys.CONTROL,'v')
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element_by_xpath("//footer[@class='jp0']/div[@class='js-component-button nui-mainBtn nui-btn nui-btn-hasIcon nui-mainBtn-hasIcon  ']").click()
        self.driver.implicitly_wait(30)
        send = self.driver.find_element_by_css_selector(".tK1").text
        print(send)
        self.assertEqual(send, "")






