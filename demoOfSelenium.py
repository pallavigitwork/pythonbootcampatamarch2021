from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='D:\WORK\BootCamp\Python\LearnPython\drivers\chromedriver.exe')
browser.get('http://5elementslearning.dev/demosite')
time.sleep(3)

browser.quit()
