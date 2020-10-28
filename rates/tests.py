from django.test import TestCase
from .models import Profile,Project
from django.contrib.auth.models import User




class ProfileTest(TestCase):
    def setUp(self):
        self.peris = User(username = 'Peris',email = 'peris@gmail.com')
        self.peris = Profile(user = Self.peris,user_id = 1,bio = 'my awwards',profile_pic = 'image.jpg',date_craeted='Oct,12.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.peris,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.peris.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Project(title = 'project',image = 'trial.jpg',description = 'I like your pic',user = peris,link = 'https://trial.com',date_craeted='Oct,12.2020')


    def test_save_image(self):
        self.picture.save_image()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_image(self):
        self.picture.save_image()
        self.picture.delete_image()
        picture_list = Image.objects.all()
        self.assertTrue(len(image)==0)

    def test_get_all_images(self):
       
        self.picture.save_image()
        all_pictures = Image.get_all_images()
        self.assertTrue(len(all_pictures) < 1)

    def test_get_one_image(self):
        self.food.save_image()
        one_pic = Image.get_one_image(self.food.id)
        self.assertTrue(one_pic.name == self.picture.name)