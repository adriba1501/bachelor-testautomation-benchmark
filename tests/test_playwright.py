import time
from pages.practice_page_playwright import PracticePagePlaywright

# "page" in Klammern ist pytest-Fixture, öffnet automatisch frischen leeren Browser-Tab.
# test_ ist wichtig, um die Funktion mit pytest zu verwenden

# Szenario 1: Radiobuttons und Checkboxen
def test_szenario_1_playwright(page):

    # 1. Navigieren zur Seite von Rahul Shetty
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # 2. PracticePage-Klasse an Browser-Tab übergeben
    practice_page = PracticePagePlaywright(page)

    # 3. Szenario starten
    practice_page.scenario_1()

    # Szenario 2: Dropdown und Eingabe
def test_szenario_2_playwright(page):
        # 1. Navigieren zur Seite von Rahul Shetty
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        # 2. PracticePage-Klasse an Browser-Tab übergeben
        practice_page = PracticePagePlaywright(page)

        # 3. Szenario starten
        practice_page.scenario_2()

# Szenario 3: Webtabelle
def test_szenario_3_playwright(page):

    # 1. Navigieren zur Seite von Rahul Shetty
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # 2. PracticePage-Klasse an Browser-Tab übergeben
    practice_page = PracticePagePlaywright(page)

    # 3. Szenario starten
    practice_page.scenario_3()