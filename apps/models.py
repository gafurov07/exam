from django.db import models


# class Product(models.Model):
#     name = models.CharField(max_length=25, verbose_name='nomi')
#     price = models.IntegerField(verbose_name='narxi')
#
#     def __str__(self):
#         return self.name
#
#
# class Order(models.Model):
#     class Status(models.TextChoices):
#         NEW = 'yangi', 'Yangi'
#         IN_PROGRESS = 'tayyorlanmoqda', 'Tayyorlanmoqda'
#         CANCEL = 'atkaz', 'Atkaz'
#         COMPLETED = 'bajarilgan', 'Bajarilgan'
#
#     product = models.ForeignKey('apps.Product', models.CASCADE)
#     user = models.ForeignKey('auth.User', models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     status = models.CharField(max_length=25, choices=Status.choices, default=Status.NEW)


# class Humans(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     image = models.ImageField()
#     username = models.CharField(max_length=50)
#     website = models.URLField(max_length=255)
#     wallets_balance = models.IntegerField()
#     income_amounts = models.IntegerField()
#     total_transactions = models.IntegerField()


# class Category(models.Model):
#     name = models.CharField(max_length=25)


class Product(models.Model):
    # category = models.ForeignKey('apps.Category', models.CASCADE)
    name = models.CharField(max_length=55)
    description = models.TextField()
    price = models.IntegerField()


class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    image = models.ImageField()

