import time
from pages.practice_page_playwright import PracticePagePlaywright

# "page" in Klammern ist pytest-Fixture, öffnet automatisch frischen leeren Browser-Tab.
# test_ ist wichtig, um die Funktion mit pytest zu verwenden
def test_szenario_1_playwright(page):

    # 1. Navigieren zur Seite von Rahul Shetty
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # 2. PracticePage-Klasse an Browser-Tab übergeben
    practice_page = PracticePagePlaywright(page)

    # 3. Szenario 1, 2 starten
    practice_page.scenario_1()
    practice_page.scenario_2()
    practice_page.scenario_3()

    # weil sich das Fenster normal nach nicht mal einer Sekunde schließen würde
    time.sleep(3)