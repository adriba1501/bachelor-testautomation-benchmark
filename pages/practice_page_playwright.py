import self


class PracticePagePlaywright:
    def __init__(self, page):
        self.page = page

        # Nachstehenden sind die Selektoren

        # Szenario 1: Radio Buttons
        self.radio1 = "input[value='radio1']"
        self.radio2 = "input[value='radio2']"
        self.radio3 = "input[value='radio3']"

        # Szenario 1: Chechboxen
        self.checkbox1 = "input[id='checkBoxOption1']"
        self.checkbox2 = "input[id='checkBoxOption2']"

        # Szenarion 2: Dropdown
        self.dropdown_box = "select[id='dropdown-class-example']"

        # Szenario 2: Text Input
        self.text_input = "input[id='autocomplete']"

        #Szenario 3: Web Table Location
        self.table_course_3 =  "table[name='courses'] tr:nth-child(3) td:nth-child(2)"
        self.table_price_3 = "table[name='courses'] tr:nth-child(3) td:nth-child(3)"

    def scenario_1(self):
        # Radio Buttons von 1 bis 3 durchklicken
        self.page.locator(self.radio1).click()
        self.page.locator(self.radio2).click()
        self.page.locator(self.radio3).click()

        # Checkbox 1 und 2 aktivieren und wieder deaktivieren
        self.page.locator(self.checkbox1).check()
        self.page.locator(self.checkbox1).uncheck()

        self.page.locator(self.checkbox2).check()
        self.page.locator(self.checkbox2).uncheck()

    def scenario_2(self):
        # Dropdownmenü Option 2 und dann Option 3 anklicken
        self.page.locator(self.dropdown_box).select_option("option2")
        self.page.locator(self.dropdown_box).select_option("option3")

        # Text in Textfeld eintragen und wieder löschen
        self.page.locator(self.text_input).fill("Aus")
        self.page.locator(self.text_input).clear()

    def scenario_3(self):
        # Webtable auslesen
        kursname = self.page.locator(self.table_course_3).inner_text()
        preis = self.page.locator(self.table_price_3).inner_text()
        assert preis != "", f"Fehler: Der Preis für den Kurs '{kursname}' ist leer!"