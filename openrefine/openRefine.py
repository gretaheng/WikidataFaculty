"""
Author: Sheetal Prasad
Created on: 3 June 2022
Subject: Automate Reconciliation steps on open refine. Once all columns are reconciled, allow user to do manual review.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def openRefineSteps(filename, chromedriverPath):
    toBeAddedLater = []
    # run "xattr -d com.apple.quarantine chromedriver in the chromedriver folder for macOS
    driver = webdriver.Chrome(executable_path=chromedriverPath,
                              options=chrome_options)
    driver.get("http://127.0.0.1:3333/")

    driver.maximize_window()

    wait = WebDriverWait(driver, 20)

    time.sleep(4)

    file = filename

    isTenure = True if 'tenure' in file else False

    uploadElement = driver.find_element(by=By.XPATH, value="//input[@type='file']")
    uploadElement.send_keys(file)

    nextButton = driver.find_element(by=By.XPATH,
                                     value="//*[@id='create-project-ui-source-selection-tab-bodies']/div[1]/form/div/table/tbody/tr[3]/td/button")
    nextButton.click()
    time.sleep(2)

    createProjectButton = driver.find_element(by=By.XPATH,
                                              value="//*[@id='right-panel-body']/div[1]/div[5]/div/div[1]/div/table/tbody/tr/td[8]/button")
    createProjectButton.click()
    time.sleep(4)

    perPage25 = driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[1]/div[2]/a[3]")
    perPage25.click()
    time.sleep(2)

    # No website for Emeritus
    if not isTenure:
        driver.find_element(by=By.XPATH, value='//*[@id="view-panel"]/div[2]/table/thead/tr/th[10]/div[1]/a').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[5]/a[3]/table/tbody/tr/td[1]').click()
        driver.find_element(by=By.XPATH, value='/html/body/div[6]/a[4]').click()

    time.sleep(2)
    # Reconciling the degree
    # Column Dropdown
    driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[2]/table/thead/tr/th[7]/div[1]/a").click()
    # Reconcile Option
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[8]/table/tbody/tr/td[1]").click()
    # Start reconciling side option
    driver.find_element(by=By.LINK_TEXT, value="Start reconciling").click()
    time.sleep(2)
    # wikidata bot link
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/a").click()
    # User defined reconcile radio button
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="againstType"]'))).click()
    except:
        time.sleep(1)

    # data in user defined input
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[5]/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input[2]").send_keys(
        "Q189533")
    # Final reconcile submit button
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[3]/table/tbody/tr/td[2]/button[1]").click()
    print("Adjust the degree values.")

    continueCode1 = str(input("Write \'continue\' for further processing or \'next\' to skip adding DegreeQnum: "))

    if continueCode1.lower() == 'continue':
        # add DegreeQnum
        # Column Dropdown and Reconcile option
        driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[2]/table/thead/tr/th[7]/div[1]/a").click()
        # Add side column option
        driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[8]/table/tbody/tr/td[1]").click()
        # Set XQnum input
        driver.find_element(by=By.XPATH, value="/html/body/div[6]/a[6]").click()
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[5]/div/form/div/div[2]/div/table/tbody/tr/td[2]/input').send_keys(
            "DegreeQnum")
        # Add
        driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/form/div/div[3]/input').click()
        time.sleep(2)
    else:
        toBeAddedLater.append("DegreeQnum")
        print("Add DegreeQnum manually once this process finishes.")

    # Reconciling school
    # Column Dropdown
    driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[2]/table/thead/tr/th[6]/div[1]/a").click()
    # Reconcile option
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[8]/table/tbody/tr/td[1]").click()
    # Start reconciling side option
    driver.find_element(by=By.LINK_TEXT, value="Start reconciling").click()
    time.sleep(2)
    # wikidata bot link
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/a").click()
    time.sleep(5)
    # User defined reconcile radio button
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="againstType"]'))).click()
    except:
        time.sleep(1)

    # data in user defined input
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[5]/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input[2]").send_keys(
        "Q3918")
    # Final reconcile submit button
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[3]/table/tbody/tr/td[2]/button[1]").click()
    print("Adjust the school values.")

    continueCode2 = str(input("Write \'continue\' for further processing or \'next\' to skip adding SchoolQnum: "))

    if continueCode2.lower() == 'continue':
        # add SchoolQnum
        # Column Dropdown and Reconcile option
        driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[2]/table/thead/tr/th[6]/div[1]/a").click()
        # Add side column option
        driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[8]/table/tbody/tr/td[1]").click()
        # Set XQnum input
        driver.find_element(by=By.XPATH, value="/html/body/div[6]/a[6]").click()
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[5]/div/form/div/div[2]/div/table/tbody/tr/td[2]/input').send_keys(
            "SchoolQnum")
        # Add
        driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/form/div/div[3]/input').click()
        time.sleep(4)
    else:
        toBeAddedLater.append("SchoolQnum")
        print("Add SchoolQnum manually once this process finishes.")

    # Reconsiling Faculty Name for Wiki
    # Column Dropdown
    driver.find_element(by=By.XPATH, value="//*[@id='view-panel']/div[2]/table/thead/tr/th[5]/div[1]/a").click()
    # Reconcile option
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/a[8]/table/tbody/tr/td[1]").click()
    # Start reconciling side option
    driver.find_element(by=By.LINK_TEXT, value="Start reconciling").click()
    time.sleep(2)
    # wikidata bot link
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/a").click()
    time.sleep(5)
    # User defined reconcile radio button
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="againstType"]'))).click()
    except:
        time.sleep(1)

    # data in user defined input
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[5]/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[4]/td[1]/input[2]").send_keys(
        "Q5")
    time.sleep(2)
    # Final reconcile submit button
    driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div[3]/table/tbody/tr/td[2]/button[1]").click()

    return toBeAddedLater


def callOpenRefine(ready4orFile):
    print("\nRunning Open Refine...")

    print("Processing...")
    chromeDriverPath = str(input("Enter path to your chromedriver executable (enter till chromedriver, not .exe):"))
    toBeAdded = openRefineSteps(ready4orFile, chromeDriverPath)
    time.sleep(4)
    separator = ','
    toBeAddedString = separator.join(toBeAdded) + ' and ' if len(toBeAdded) > 0 else ''

    print("\nSUCCESS: OpenRefine project ready for manual review.\n"
        "1. Check all websites.\n"
        "2. Check and remove unnecessary LC urls.\n"
        "3. Check and adjust Faculty name and wikidata links or create new.\n"
        "4. Add " + toBeAddedString + "FQnum.\n"
        "5. Export to CSV once review is completed.\n")
