class discoverPage:
    def __init__(self,driver):
        self.driver = driver


    def enterPage(self):
        self.driver.find_element_by_id("com.leautolink.leautocamera:id/tab_rb_discover").click()
        print (self.driver.current_activity)
