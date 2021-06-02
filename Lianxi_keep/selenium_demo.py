from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def login(driver, user, password):
    driver.get("http://10.45.29.47:8084/enterprise/#/login")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys(user)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//button[@type='button']").click()
    t = driver.find_element_by_xpath("//span[@class='name___3oikG']").text
    print("获取到的账号：%s" % t)
    if t == "iip_demo_qy":
        print("登录成功")
    else:
        print("登录失败")


def logout(driver):
    time.sleep(3)
    # 鼠标移动悬浮
    mouse = driver.find_element_by_xpath("//span[@class='name___3oikG']")
    ActionChains(driver).move_to_element(mouse).perform()
    driver.implicitly_wait(5)
    # xpath 模糊定位标签数据
    driver.find_element_by_xpath("//div[contains(@class,'ant-dropdown')]/ul/li[3]").click()
    time.sleep(1)
    s = driver.find_element_by_xpath("//button[@type='button']/span").text
    if s == "登 录":
        print("退出登录成功")
    else:
        print("退出登录失败")
    time.sleep(1)
    driver.quit()


if __name__ == "__main__":
    driver = webdriver.Chrome('E:\Google\Chrome\Application\chromedriver.exe')
    login(driver, 'iip_demo_qy', '123456A')
    logout(driver)
