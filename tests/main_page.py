def test_open_prices(main_page):
    price_page = main_page.open_prices_page()
    assert price_page.get_current_url() == price_page._page_url


def test_scrolling(main_page):
    main_page.scroll_to_footer()
    main_page.scroll_to_header()
    main_page.scroll_to_element(main_page._locators.price_section)


def test_current_url(main_page):
    assert main_page._page_url == main_page.get_current_url()


def test_title(main_page):
    assert main_page._page_title == main_page.get_title()
