#usr/bin/python
#encoding:utf-8
#足迹版登录测试
import unittest
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        #天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.driver'
        desired_caps['appActivity'] = '.activity.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("13900001127","123456",True))
    @unpack
    def testLogIn(self, username, password, expectedresult):
        global exist
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_user_name").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        sleep(3)

        try:
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").is_displayed():
                exist = False
        except Exception as e:
            exist = True

        self.assertEqual(exist,expectedresult)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
