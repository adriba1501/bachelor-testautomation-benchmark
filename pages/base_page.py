from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Hier ist der Boilerplate-Code: Wir sagen Selenium, es soll bis zu 10 Sekunden warten
        self.wait = WebDriverWait(driver, 10)

    def wait_and_click(self, by_locator):
        """Wartet, bis Element klickbar, klickt dann."""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def wait_and_fill(self, by_locator, text):
        """Wartet, bis Textfeld da ist, leert es und tippt Text ein."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def wait_and_select_dropdown(self, by_locator, value):
        """Wartet auf Dropdown und wählt eine Option anhand des Wertes aus."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        dropdown = Select(element)
        dropdown.select_by_value(value)

    def wait_and_get_text(self, by_locator):
        """Wartet, bis das Element sichtbar ist, und gibt seinen Text zurück."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text
