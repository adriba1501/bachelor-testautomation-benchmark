import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.practice_page_selenium import PracticePageSelenium


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()

    # geben laufenden Browser an Test weiter
    yield chrome_driver

    # Wenn Test fertig: Schließe Browser
    chrome_driver.quit()

# Szenario 1: Radiobuttons und Checkboxen
def test_szenario_1_selenium(driver):

    # Navigation zur Rahul Shetty Seite
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Übergeben von laufenden Browser an Selenium-Klasse
    practice_page = PracticePageSelenium(driver)

    # Szenario starten
    practice_page.scenario_1()

# Szenario 2: Dropdowns und Eingabefelder
def test_szenario_2_selenium(driver):
    # Navigation zur Rahul Shetty Seite
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Übergeben von laufenden Browser an Selenium-Klasse
    practice_page = PracticePageSelenium(driver)

    # Szenario starten
    practice_page.scenario_2()

# Szenario 3: Webtabelle
def test_szenario_3_selenium(driver):
    # Navigation zur Rahul Shetty Seite
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Übergeben von laufenden Browser an Selenium-Klasse
    practice_page = PracticePageSelenium(driver)

    # Szenario starten
    practice_page.scenario_3()