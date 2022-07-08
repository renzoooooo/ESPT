from django.test import TestCase
from esportscentresys.views import MainPage
from .models import Contactesports

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'Renzo',
	 		'email': 'renzo.mendiola@gsfe.tupcavite.edu.ph',
	 		'number': '09152141030',
	 		'message': 'Nice!'})
		self.assertEqual(Contactesports.objects.count(),1)
		inputData = Contactesports.objects.first()
		self.assertEqual(inputData.uname, 'Renzo')
		self.assertEqual(inputData.uemail, 'renzo.mendiola@gsfe.tupcavite.edu.ph')
		self.assertEqual(inputData.unumber, '09152141030')
		self.assertEqual(inputData.umessage, 'Nice!')

	def test_POST_redirect(self):
		response = self.client.post('/', {'name' :'Renzo',
	 		'email': 'renzo.mendiola@gsfe.tupcavite.edu.ph',
	 		'number': '09152141030',
	 		'message': 'Nice!'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


class ORMTEST(TestCase):
	def test_saving_retrive(self):
		Contactesports_page = Contactesports()
		Contactesports_page.uname = 'Renzo'
		Contactesports_page.uemail = 'renzo.mendiola@gsfe.tupcavite.edu.ph'
		Contactesports_page.unumber = '09152141030'
		Contactesports_page.umessage = 'Nice!'
		Contactesports_page.save()

		Contactesports_page2 = Contactesports()
		Contactesports_page2.uname = 'Mendiola Renzo'
		Contactesports_page2.uemail = 'mendiolarenzoo@gmail.com'
		Contactesports_page2.unumber = '09150545426'
		Contactesports_page2.umessage = 'Nice Game!'
		Contactesports_page2.save()

		ContactesportsPoll = Contactesports.objects.all()
		self.assertEqual(ContactesportsPoll.count(), 2)

		User1 = ContactesportsPoll[0]
		User2 = ContactesportsPoll[1]

		self.assertEqual(User1.uname, 'Renzo')
		self.assertEqual(User1.uemail, 'renzo.mendiola@gsfe.tupcavite.edu.ph')
		self.assertEqual(User1.unumber, '09152141030')
		self.assertEqual(User1.umessage, 'Nice!')

		self.assertEqual(User2.uname, 'Mendiola Renzo')
		self.assertEqual(User2.uemail, 'mendiolarenzoo@gmail.com')
		self.assertEqual(User2.unumber, '09150545426')
		self.assertEqual(User2.umessage, 'Nice Game!')


	def test_template_display_list(self):
		Contactesports.objects.create(uname = 'Ren Zo',
			uemail = 'mendrengaming@gmail.com',
			unumber = '09266777018',
			umessage = 'Love the Game!')

		Contactesports.objects.create(uname = 'Zo Ren',
			uemail = 'ZoRen@gmail.com',
			unumber = '09150545426',
			umessage = 'Nice Wan!')

		response = self.client.get('/')
		self.assertIn('Entry 1: Ren Zo, mendrengaming@gmail.com, 09266777018, Love the Game!', response.content.decode())
		self.assertIn('Entry 2: Zo Ren, ZoRen@gmail.com, 09150545426, Nice Wan!', response.content.decode())