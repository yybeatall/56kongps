#usr/bin/python
#encoding:utf-8
#足迹版测试--提货
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
        desired_caps['appActivity'] = '.activity.LaunchActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testLogIn(self):
        global exist
        try:
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_pickup").is_displayed():
                #点击首页待提区域
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_pickup").click()
                sleep(2)
                #点击上传照片
                #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_picture").click()
                #点击车况
                #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()
                #点击确认提货
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_handover").click()
                #点击确定
                #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
                #点击取消
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()

        except Exception as e:
            print("不存在提货任务")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
