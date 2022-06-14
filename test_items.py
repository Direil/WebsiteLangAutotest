from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket, "Кнопка добавления в корзину не была найдена."
