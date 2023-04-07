def test_scratch(set_browser):
    browser = set_browser
    browser.get('https://google.com/')
    assert "Google" in browser.title
