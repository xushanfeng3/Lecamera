#encoding:utf-8
import random
class localDlete:
    def __init__(self,driver):
        self.driver = driver
        self.deleteData = {}
    def enterLocalPicture(self):
        #通过底部导航栏进入到相册页面进行图片分享
        self.driver.find_element_by_id("com.leautolink.leautocamera:id/tab_rb_photo").click()
        self.driver.find_element_by_id("com.leautolink.leautocamera:id/activity_local_gallery_photo_btn").click()
        elms = self.driver.find_elements_by_id("com.leautolink.leautocamera:id/item_photo_iv_photo")
        if(len(elms)==0):
            print("相册分类下图片内容为空")
        else:
            tmp = random.randrange(0,len(elms))
            elms[tmp].click()
            self.deleteData['fileName'] = self.driver.find_element_by_id("com.leautolink.leautocamera:id/iv_top_thumb").text
            self.driver.back()
            self.driver.find_element_by_id("com.leautolink.leautocamera:id/navigation_bar_right_bt").click()
            elms[tmp].click()
            self.driver.find_element_by_id("com.leautolink.leautocamera:id/ibtn_del").click()
            els = self.driver.find_elements_by_class_name("android.widget.Button")
            for i in range(0,len(els)):
                if els[i].text == u"确定":
                    els[i].click()
            fileNameEls = self.driver.find_elements_by_id("com.leautolink.leautocamera:id/item_photo_tv_time")
            tmp2 = []
            for i in range(0,len(fileNameEls)):
                tmp2.append(fileNameEls[i].text)

            if self.deleteData['fileName'] in tmp2:
                print("删除失败")
            else:
                print("删除成功")