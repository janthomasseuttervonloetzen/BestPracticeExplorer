from selenium import webdriver
from time import sleep


def findLoBs():
    loBCount = len(driver.find_elements_by_xpath("//button[contains(@id,'button4-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]"))
    i = 0

    buttons = driver.find_elements_by_xpath("//button[contains(@id,'button4-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

    while i <= (loBCount - 1):
        buttons[i].click()

        findScopeCategories()

        sleep(3)

        buttons = driver.find_elements_by_xpath("//button[contains(@id,'button4-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

        buttons[i].click

        buttons = driver.find_elements_by_xpath(
            "//button[contains(@id,'button4-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

        i += 1

def findScopeCategories():
    solCount = len(driver.find_elements_by_xpath(
        "//button[contains(@id,'button5-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]"))

    sub_buttons = driver.find_elements_by_xpath(
        "//button[contains(@id,'button5-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

    m = 0

    while m <= (solCount - 1):
        sub_buttons[m].click()

        findScopeItems()

        sub_buttons = driver.find_elements_by_xpath(
            "//button[contains(@id,'button5-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

        sub_buttons[m].click()

        sub_buttons = driver.find_elements_by_xpath(
            "//button[contains(@id,'button5-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

        m += 1

def findScopeItems():
    scopeItems = driver.find_elements_by_xpath(
        "//a[contains(@id,'__link2-__xmlview0--solutionScopeXmlView--scopeItemGroupList')]")

    for link in scopeItems:
        print(link.get_attribute('title'))

        print(link.get_attribute('href'))


driver = webdriver.Chrome("C:/Users/seutt/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://rapid.sap.com/bp/BP_CLD_ENTPR")

sleep(5)

findLoBs()

driver.close()
