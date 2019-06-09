import requests,urllib.request,json
import mp3play,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
header2 = {
            'Host': 'songsearch.kugou.com',
            'Origin': 'http://www.kugou.com/',
            'Referer': 'http://www.kugou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
url2 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=A11F7A8BD2EA5BBDB32F58A9081F27B4&album_id=&dfid=1su9ai3vuKEp0AvUgT0sXDoE&mid=8a2d9e872bdbd1b9d25aa62d1473aa1f&platid=4&_=1559998974444'
url3 = 'https://www.kugou.com/song/#hash=A11F7A8BD2EA5BBDB32F58A9081F27B4'
#req = urllib.request.Request(url2)#
#response = urllib.request.urlopen(req, None, 30)  # 设置超时时间
#html = response.read().decode('utf-8')
#html = json.loads(html)
#play_url = html['data']['play_url']
#print(play_url)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome()
driver.get(url3)
driver.find_element_by_xpath('//*[@id="toggle"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="toggle"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="toggle"]').click()
time.sleep(5)
driver.close()
