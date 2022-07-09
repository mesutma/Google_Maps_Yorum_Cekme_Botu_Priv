import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()
url = 'https://www.google.com/maps/place/B%C3%BCy%C3%BCk+Adana+Kebap/@37.000814,35.3297878,17z/data=!4m7!3m6!1s0x15288f14e792b11d:0xcb64a6a7c1aebd73!8m2!3d37.000814!4d35.3297878!9m1!1b1' #Yorumların tamamının olduğu kısmın urlsi

global_delay = 3
driver = webdriver.Chrome()
driver.get(url)
log('Bu program Can Tarafından Yapılmıştır.')
log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
log('Program başlatıldı')
time.sleep(global_delay)


yorumlar = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]').text
yorumlar_say = yorumlar.replace(' yorum', '')
time.sleep(global_delay)
log('Yorum sayısı: ' + str(yorumlar_say))
driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]').click()

log('Yorumların tamamı yükleniyor...')
for(yorum) in range(int(yorumlar_say)):
    try:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        if(yorum % 2 == 0):
            time.sleep(0.2)
    except:
        continue
    if(yorum == int(yorumlar_say) - 1):
        log('Yorumların tamamı yüklendi.')
    
time.sleep(global_delay)
tum_yorumlar = int(yorumlar_say) * 3
for(yorum) in range(int(tum_yorumlar)):
    def yorumu_al():
        yorummuz = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div[' + str(yorum) + ']/div/div[3]/div[4]/div[2]/span[2]').text
        if(yorummuz == '' or yorummuz == ' '):
            return
        else:
            log(yorummuz)
            yorum_file = open("yorumlar.txt", "a", encoding='utf-8')
            yorum_file.write(yorummuz + "\n")
            yorum_file.close()
            html.send_keys(Keys.END)
            time.sleep(0.2)
            if(yorum == int(tum_yorumlar) - 1):
                log('Yorumların tamamı yorumlar.txt dosyasına yazıldı.')
    try:
        try:
            onemli =  driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div[' + str(yorum) + ']/div/div[3]/div[4]/jsl/button').text
            if onemli == 'Daha fazla':
                driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[11]/div[' + str(yorum) + ']/div/div[3]/div[4]/jsl/button').click()
                yorumu_al()
            else:
                yorumu_al()
        except:
            yorumu_al()
            continue
    except:
        continue
