import pytest
from selenium import webdriver

'''
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', /
                     help="Choose Your Hero(language): us,ru,fr")
'''


@pytest.fixture(scope="session")
def browser(request):
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    '''
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    '''
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()



