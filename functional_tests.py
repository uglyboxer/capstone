from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_page_view(self):
        # User navigates to site
        self.browser.get('http://localhost:8000')

        # User sees "Finnegan" in title bar
        assert 'Finnegan' in self.browser.title

        # User sees "Finnegan" in header text

        # A window on the right side of the screen shows a handwritten
        # number.

        # A button to submit 'nothing' is presented on the left side

if __name__ == '__main__':
    unittest.main(warnings='ignore')