from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save(self):
        self.save()

    def delete(self):
        self.delete()

    def update(self, update):
        self.name = update
        self.save()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save(self):
        self.save()

    def delete(self):
        self.delete()

    def update(self, update):
        self.name = update
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image_url =models.ImageField(upload_to='images/')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, name, description, image_url, location, category):
        update = cls.objects.filter(id=id).update(name=name, description=description, image_url=image_url, location=location, category=category)
        return update

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id).all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        loc = cls.object.filter(location__id = location)
        return loc

    @classmethod
    def search_by_category(cls, search_term):
        cat = cls.objects.filter(category__name__icontains = search_term)
        return cat