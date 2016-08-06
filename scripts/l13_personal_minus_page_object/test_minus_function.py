from pages.index_page import IndexPage

def test_minus_function(driver):
    first_arg = 10
    second_arg = 2

    index_page = IndexPage(driver)
    index_page.calculate_minus(str(first_arg), str(second_arg))
    assert index_page.minus_result.text == str(first_arg - second_arg)
