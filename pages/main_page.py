from playwright.sync_api import Page

class MainPage:
    BASE_URL = "https://demoqa.com/"
    URL_AUT_PRAC_FORM = "https://demoqa.com/automation-practice-form"
    FORMS_TEXT = "text=Forms"
    TEXT_PRAC_FORM = "text=Practice Form"
    FORM_STUD_REG = "text=Student Registration Form"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)

    def is_main_title_visible(self):
        return self.page.is_visible("text=Elements")

    def go_to_practice_form(self):
        self.page.click(self.FORMS_TEXT)
        self.page.click(self.TEXT_PRAC_FORM)
        self.page.wait_for_url(self.URL_AUT_PRAC_FORM)

    def is_form_visible(self):
        return self.page.is_visible(self.FORM_STUD_REG)