class PracticePage:
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
        self.dropdown1 = "option[value='option1']"
        self.dropdown2 = "option[value='option2']"
        self.dropdown3 = "option[value='option3']"

        # Szenario 2: Text Input
        self.text_input = "input[id='autocomplete']"

        #Szenario 3: Web Table Location
        self.table_course_3 =  "table[name='courses'] tr:nth-child(3) td:nth-child(2)"
        self.table_price_3 = "table[name='courses'] tr:nth-child(3) td:nth-child(3)"