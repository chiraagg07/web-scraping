from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
            query_comp = parse_qs(urlparse(self.path).query)
            license = query_comp["license"]
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
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
            self.driver = webdriver.Chrome(executable_path="chromedriver", options=self.options)

            self.driver.get("https://fdamfg.maharashtra.gov.in/frm_G_Cold_S_Query.aspx?ST=MH")
            license1 = self.driver.find_element(By.XPATH,'//*[@id="txtLicense"]')
            license1.send_keys(license)
            license1 = self.driver.find_element(By.NAME,'btnSearch').click()
            self.driver.implicitly_wait(10)
            data1 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[1]')
            data2 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[1]')
            data3 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[2]')
            data4 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[2]')
            data5 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[1]/td[4]')
            data6 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]/td[4]')
            dataa6 = data6.text
            dataaa6 = dataa6[:24]
            data7 = 'Register date'
            data8 = dataa6[26:]
            data9 = 'hovertext'
            data10 = self.driver.find_element(By.XPATH,'//*[@id="dgDisplay"]/tbody/tr[2]')
            dataa10 = data10.get_attribute('onmouseover')
            dataaa10 = dataa10[174:-10]
            dataaaa10 = dataaa10.replace("<BR />","")
            my_dict = {
            data1.text:data2.text,
            data3.text:data4.text,
            data5.text:dataaa6,
            data7:data8,
            data9:dataaaa10
        }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(my_dict),'utf-8'))
            return
handler_object = MyHttpRequestHandler
PORT = 5000
my_server = socketserver.TCPServer(("",PORT),handler_object)
my_server.serve_forever()