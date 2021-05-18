from django.test import TestCase
from .models import Image, Category, Location


# Create your tests here.
class CategoryTest(TestCase):

    # set up method
    def setUp(self):
        self.new_category = Category(name='newCategory')

    # tear down method
    def tearDown(self):
        Category.objects.all().delete()

    # testing instance
    def test_instance(self):
        self.assertTrue(self.new_category, Category)

    # testing saving image category
    def test_save_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # testing deleting a category
    def test_delete_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories) < 1)


class LocationTest(TestCase):

    # set up method
    def setUp(self):
        self.new_location = Location(name='canada')

    # tear down method
    def tearDown(self):
        Location.objects.all().delete()

    # testing instance
    def test_instance(self):
        self.assertTrue(self.new_location, Location)

    # testing saving image location
    def test_save_location(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # testing deleting a location
    def test_delete_location(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.new_location.delete_location()
        self.assertTrue(len(locations) < 1)


class ImageTest(TestCase):

    # set up method
    def setUp(self):
        # creating a new image category and saving
        self.new_category = Category(name='newCategory')
        self.new_category.save()

        # creating aa new image location and saving
        self.new_location = Location(name='Canada')
        self.new_location.save()

        # creating a new image
        self.new_image = Image(image_url='building.png', name='building', description='Image of building taken at sunset', location=self.new_location, category=self.new_category)
        self.new_image.save()

    # tear down method
    def tearDown(self):
       Category.objects.all().delete()
       Location.objects.all().delete()
       Image.objects.all().delete()

    # testing saving an image
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # testing saving multiple images
    def test_save_multiple_images(self):
        self.new_image.save_image()
        image2 = Image(image_url='building2.png', name='building2', description='Image of building taken at sunrise', location=self.new_location, category=self.new_category)
        image2.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 1)

    # testing deleting an image
    def test_delete_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images) < 1)

