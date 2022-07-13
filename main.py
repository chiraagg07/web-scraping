from selenium import webdriver
from selenium.webdriver.common.by import By
import re
class test:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        items = []
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.options)

        self.driver.get("https://fdamfg.maharashtra.gov.in/frm_G_Cold_S_Query.aspx?ST=MH")
        license = self.driver.find_element(By.XPATH,'//*[@id="txtLicense"]')
        license.send_keys('188900')
        license = self.driver.find_element(By.NAME,'btnSearch').click()
        self.driver.implicitly_wait(10)
        data1 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[1]')
        data2 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[1]')
        data3 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[2]')
        data4 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[2]')
        data5 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[3]')
        data6 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[3]')
        data7 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[4]')
        data8 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[4]')
        data9 = 'hovertext'
        data10 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]')
        data = data10.get_attribute('onmouseover')
        dd = data[174:-10]
        dd1 = dd[:8]
        dd2 = dd[15:47]
        dd3 = dd[53:]
        final = dd1 + dd2 + dd3
        my_dict = {
            data1.text:data2.text,
            data3.text:data4.text,
            data5.text:data6.text,
            data7.text:data8.text,
            data9:final
        }
        print(my_dict)
test()