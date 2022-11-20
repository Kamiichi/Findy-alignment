from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import configparser

# ChromeDriver Utils
path_to_chromedriver = "/usr/local/bin/chromedriver"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get(path_to_chromedriver, options=options)


#=================================================================================================
# Element XPaths

# Target Website URL
target_url = "https://findy-code.io/"
login_button = '//*[@id="__next"]/div/div[2]/section[1]/div/div[2]/div[1]/ul/li[2]/button'
align_page_link ='//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[3]/a'
align_btn = '//*[@id="__next"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/button'

# SignIn Page
id_input_form = '//*[@id="login_field"]'
passwd_input_form = '//*[@id="password"]'
sign_in_btn = '//*[@id="login"]/div[3]/form/div/input[11]'

# GitHub SSO Page
config = configparser.ConfigParser()
config.read('./config/config.ini', encoding='utf-8')
mail = config['GITHUB_ACCOUNT_INFO']['Mail']
passwd = config['GITHUB_ACCOUNT_INFO']['Password']

# MFO Auth Page
auth_code_input_form = '//*[@id="totp"]'
# ボタン押さなくていいらしいから使わん。verify_btn = '//*[@id="login"]/div[5]/div[2]/form/button'

#=================================================================================================

# mfa_auth_code = '{ここに入力引数を渡してあげたい}'

def main():
    driver.get(target_url)
    elem = driver.find_element(By.XPATH, login_button)
    elem.click()
    time.sleep(1)
    elem_mail_form = driver.find_element(By.XPATH, id_input_form)
    elem_mail_form.send_keys(mail)
    elem_passwd_form = driver.find_element(By.XPATH, passwd_input_form)
    elem_passwd_form.send_keys(passwd)
    elem_sign_in_btn = driver.find_element(By.XPATH, sign_in_btn)
    elem_sign_in_btn.click()
    time.sleep(1)
    elem_auth_code_input_form = driver.find_element(By.XPATH, auth_code_input_form)
    elem_auth_code_input_form.send_keys(mfa_auth_code)
    time.sleep(10)
    elem_align_page_link = driver.find_element(By.XPATH, align_page_link)
    elem_align_page_link.click()
    time.sleep(5)
    elem_align_btn = driver.find_element(By.XPATH, align_btn)
    elem_align_btn.click()
    time.sleep(60)
    driver.quit() 
    

if __name__ == "__main__":
    print("start!!")
    try:
        main()
    except:
        print("何かエラーが起きたよ！もしかして他要素認証コードの期限切れかな？")
    print("end!")