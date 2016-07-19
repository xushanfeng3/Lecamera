from src.config.config import *
from src.untils.discoverPage import  discoverPage
from  src.test_case.sharePicture import sharePictureAlbum
from src.test_case.localPictureDelete import localDlete
from appium import webdriver
from  time import sleep

desired_caps = {}
desired_caps['platformName'] = platformName
desired_caps['platformVersion'] = platformVersion
desired_caps['deviceName'] = deviceName
desired_caps['appPackage'] = appPackage
desired_caps['appActivity'] = appActivity
driver = webdriver.Remote(baseUrl,desired_caps)
driver.implicitly_wait(30)

try:

    # a = discoverPage(driver)
    # print(driver.current_activity)
    localDlete(driver).enterLocalPicture()
    sleep(10)
    driver.quit()


except Exception,e:
    print("fail",e.message)
    driver.quit()
