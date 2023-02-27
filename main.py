from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_extension("./uBlock-Origin.crx")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.citationmachine.net/apa/cite-a-website")

def read_links():
    read_links.open_ref = open("ref.txt", "r")
    read_links.ref_file = read_links.open_ref.read()
    read_links.ref_list = read_links.ref_file.split("\n")
    read_links.count = 0
    for i in read_links.ref_list:
        if i:
            read_links.count += 1            
    print(read_links.count)
    print(read_links.ref_list)

def cite_loop(link):
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"citation-search-input\"]").send_keys(link)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"citation-search-button\"]").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".sc-fzoYHE > .styled__ResultButtonText-sc-jhqr36-14").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".sc-fzplWN > .sc-fzoYHE").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"form-next-button\"]").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".button__SpecialButton-sc-1lt38zg-1 > .sc-fzoYHE").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".sc-fznJRM:nth-child(1) > .sc-fzoYHE").click()
    time.sleep(2)

def export_refs():
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    
    
read_links()
for i in range(read_links.count):
    cite_loop(read_links.ref_list[i])
export_refs()
