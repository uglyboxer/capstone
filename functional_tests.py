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
        assert 'Finnegan' in self.browser.title, "Browser title was " +\
                                                  self.browser.title

        # User sees "Finnegan" in header text
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Finnegan', header_text)

        # A window on the right side of the screen shows a handwritten
        # number.
        input_window = self.browser.find_element_by_tag_name('canvas').text
        self.assertIn('4', input_window)

        # A button to submit 'nothing' is presented on the left side
        sub_button = self.browser.find_element_by_id('sub_button')
        self.assertEqual(sub_button.get_attribute('value'), 'Submit')

        self.fail('Finish the tests!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')