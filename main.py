import time
import pytest
from selenium import webdriver
import bin.api_functions as api_f
import bin.factorial_page as fp


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\pospelov_i\PycharmProjects\factorial_check\bin\chromedriver.exe")
    yield driver
    driver.quit()


def test_1():
    assert api_f.calculate(0, 1, 200) == True


def test_2():
    assert api_f.calculate(1, 1, 200) == True


def test_3():
    assert api_f.calculate(9, 362880, 200) == True


def test_4():
    assert api_f.calculate(2147483647, "Inf", 200) == True


def test_5():
    assert api_f.calculate(-1, "invalid value", 200) == True


def test_6():
    assert api_f.calculate(0.2, "invalid value", 200) == True


def test_7():
    assert api_f.calculate("0,2", "invalid value", 200) == True


def test_8():
    assert api_f.calculate("%s", "invalid value", 200) == True


def test_9():
    assert api_f.calculate("%d", "invalid value", 200) == True


def test_10():
    assert api_f.calculate("00", "invalid value", 200) == True


def test_11():
    assert api_f.calculate("", "invalid value", 200) == True


def test_12():
    assert api_f.calculate(" ", "invalid value", 200) == True


def test_13():
    assert api_f.calculate("[1-9]", "invalid value", 200) == True


def test_14():
    assert api_f.calculate("test", "invalid value", 200) == True


def test_15(browser):
    f_page = fp.MainPage(browser)
    f_page.go_to_site()
    f_page.input_value("12")
    f_page.click()
    time.sleep(5)
    assert "479001600" in f_page.get_result_value()


def test_16(browser):
    f_page = fp.MainPage(browser)
    f_page.go_to_site()
    f_page.input_value("test")
    f_page.click()
    assert "Please enter an integer" in f_page.get_result_value()

