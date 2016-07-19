#encoding:utf-8
import random
class sharePictureAlbum:
    def __init__(self,driver):
        self._driver = driver
        self.shareData = {}

    def enterAlbum(self):
        #通过底部导航栏进入到相册页面进行图片分享
        self._driver.find_element_by_id("com.leautolink.leautocamera:id/tab_rb_photo").click()
        self._driver.find_element_by_id("com.leautolink.leautocamera:id/activity_local_gallery_photo_btn").click()
        elms = self._driver.find_elements_by_id("com.leautolink.leautocamera:id/item_photo_iv_photo")
        if(len(elms)==0):
            print("相册分类下图片内容为空")
        else:
            tmp = random.randrange(0,len(elms))
            print(tmp)
            print(len(elms))


            elms[tmp].click()
            self.shareData['fileName'] =self._driver.find_element_by_id("com.leautolink.leautocamera:id/navigation_bar_title"
                                                                   "").text
            print(self.shareData['fileName'])
            self._driver.find_element_by_id("com.leautolink.leautocamera:id/ibtn_local_photo_share").click()

            self._driver.find_element_by_id("com.leautolink.leautocamera:id/et_theme").send_keys("autoTestShare")
            self._driver.find_element_by_id("com.leautolink.leautocamera:id/rb_3").click()
            self._driver.find_element_by_id("com.leautolink.leautocamera:id/navigation_bar_right_bt").click()
    def resultCheck(self,elm):
        self._driver

