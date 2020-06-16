import time
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_is_displayed(browser):
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary"))
    assert button > 0, "Button is not found"


        
            

    
           

    