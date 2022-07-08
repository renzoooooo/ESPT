from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('esportscentre', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		

		IngameName = self.browser.find_element_by_id('Username')
		self.assertEqual(IngameName.get_attribute('placeholder'),'Name')
		IngameName.send_keys('Renzo Mendiola')
		time.sleep(1)

		IngameEmail = self.browser.find_element_by_id('Useremail')
		self.assertEqual(IngameEmail.get_attribute('placeholder'),'Email')
		IngameEmail.send_keys('renzo.mendiola@gsfe.tupcavite.edu.ph')
		time.sleep(1)

		IngameNumber = self.browser.find_element_by_id('Usernumber')
		self.assertEqual(IngameNumber.get_attribute('placeholder'),'Mobile Number')
		IngameNumber.send_keys('09152141030')
		time.sleep(1)

		IngameReview = self.browser.find_element_by_id('Usermessage')
		self.assertEqual(IngameReview.get_attribute('placeholder'),'Message')
		IngameReview.send_keys('Nice!')
		time.sleep(1)

		btnSend = self.browser.find_element_by_id('btnSend')
		btnSend.click()
		time.sleep(1)

		# self.browser.get(self.live_server_url)
		# self.assertIn('esportscentre', self.browser.title)
		# headerText = self.browser.find_element_by_tag_name('h1').text
		# self.assertIn('Contact Us', headerText)

		# IngameName = self.browser.find_element_by_id('Username')
		# self.assertEqual(IngameName.get_attribute('placeholder'),'Name')
		# IngameName.send_keys('Mendiola Renzo')
		# time.sleep(1)

		# IngameEmail = self.browser.find_element_by_id('Useremail')
		# self.assertEqual(IngameEmail.get_attribute('placeholder'),'Email')
		# IngameEmail.send_keys('mendiolarenzoo@gmail.com')
		# time.sleep(1)

		# IngameNumber = self.browser.find_element_by_id('Usernumber')
		# self.assertEqual(IngameNumber.get_attribute('placeholder'),'Mobile Number')
		# selectIngameNumber = Select(IngameNumber)
		# selectIngameNumber.select_by_visible_text('09266777018')
		# time.sleep(1)

		# IngameReview = self.browser.find_element_by_id('Usermessage')
		# self.assertEqual(IngameReview.get_attribute('placeholder'),'Message')
		# IngameReview.send_keys('Nice Game')
		# time.sleep(1)

		# btnSend = self.browser.find_element_by_id('btnSend')
		# btnSend.click()
		# time.sleep(1)

		self.browser.get(self.live_server_url)
		self.assertIn('esportscentre', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		IngameName = self.browser.find_element_by_id('Username')
		self.assertEqual(IngameName.get_attribute('placeholder'),'Name')
		IngameName.send_keys('Ren Zo')
		time.sleep(1)

		IngameEmail = self.browser.find_element_by_id('Useremail')
		self.assertEqual(IngameEmail.get_attribute('placeholder'),'Email')
		IngameEmail.send_keys('mendrengaming@gmail.com')
		time.sleep(1)

		IngameNumber = self.browser.find_element_by_id('Usernumber')
		self.assertEqual(IngameNumber.get_attribute('placeholder'),'Mobile Number')
		IngameNumber.send_keys('09150545426')
		time.sleep(1)

		IngameReview = self.browser.find_element_by_id('Usermessage')
		self.assertEqual(IngameReview.get_attribute('placeholder'),'Message')
		IngameReview.send_keys('Love the Game')
		time.sleep(1)

		btnSend = self.browser.find_element_by_id('btnSend')
		btnSend.click()
		time.sleep(1)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('Entry 1: Renzo Mendiola, renzo.mendiola@gsfe.tupcavite.edu.ph, 09152141030, Nice!', [row.text for row in row_data])
		self.assertIn('Entry 2: Ren Zo, mendrengaming@gmail.com, 09150545426, Love the Game', [row.text for row in row_data])