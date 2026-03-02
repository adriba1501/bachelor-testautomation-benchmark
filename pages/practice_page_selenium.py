from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticePageSelenium(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Szenario 1: Radio Buttons
        self.radio1 = (By.CSS_SELECTOR, "input[value='radio1']")
        self.radio2 = (By.CSS_SELECTOR, "input[value='radio2']")
        self.radio3 = (By.CSS_SELECTOR, "input[value='radio3']")

        # Szenario 1: Chechboxen
        self.checkbox1 = (By.ID, "checkBoxOption1")
        self.checkbox2 = (By.ID, "checkBoxOption2")

        # Szenarion 2: Dropdown
        self.dropdown_box = (By.ID, "dropdown-class-example")

        # Szenario 2: Text Input
        self.text_input = (By.ID, "autocomplete")

        # Szenario 3: Web Table Location
        self.table_course_3 = (By.CSS_SELECTOR, "table[name='courses'] tr:nth-child(3) td:nth-child(2)")
        self.table_price_3 = (By.CSS_SELECTOR, "table[name='courses'] tr:nth-child(3) td:nth-child(3)")

    def scenario_1(self):
        # Radio Buttons von 1 bis 3 durchklicken
        self.wait_and_click(self.radio1)
        self.wait_and_click(self.radio2)
        self.wait_and_click(self.radio3)

        # Checkbox 1 und 2 aktivieren und wieder deaktivieren
        self.wait_and_click(self.checkbox1)
        self.wait_and_click(self.checkbox1)
        self.wait_and_click(self.checkbox2)
        self.wait_and_click(self.checkbox2)

    def scenario_2(self):
        # Dropdownmenü Option 2 und dann Option 3 anklicken
        self.wait_and_select_dropdown(self.dropdown_box, "option2")
        self.wait_and_select_dropdown(self.dropdown_box, "option3")

        # Text in Textfeld eintragen und wieder löschen
        self.wait_and_fill(self.text_input, "Aus")
        self.wait_and_fill(self.text_input, "")

    def scenario_3(self):
        # Webtable auslesen
        kursname = self.wait_and_get_text(self.table_course_3)
        preis = self.wait_and_get_text(self.table_price_3)
        assert preis != "", f"Fehler: Der Preis für den Kurs '{kursname}' ist leer!"



