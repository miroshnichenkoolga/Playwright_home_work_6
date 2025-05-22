from pages.main_page import MainPage

def test_open_site(page):
    main = MainPage(page)
    main.open()
    assert "DEMOQA" in page.title()
    assert main.is_main_title_visible()

def test_navigate_to_form(page):
    main = MainPage(page)
    main.open()
    main.go_to_practice_form()
    assert main.is_form_visible()