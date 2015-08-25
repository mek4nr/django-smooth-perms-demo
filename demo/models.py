from django.db import models
from smooth_perms.models import GlobalPermissionMixin, ModelPermission
from smooth_perms.managers import GlobalPermissionManager
from django.utils.translation import ugettext_lazy, ugettext as _


# Custom perms
class ContinentPermissionManager(GlobalPermissionManager):
    foreign_key = 'continent'


class ContinentPermission(GlobalPermissionMixin):
    continent = models.ForeignKey('Continent')

    PERMISSIONS = ('change_country',)

    can_change_country = models.BooleanField(_("can change country"), default=False)

    objects = ContinentPermissionManager()


class Continent(ModelPermission):
    name = models.CharField(max_length=1000)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}' . format(self.name)

    permissions = ContinentPermission


class Country(ModelPermission):
    continent = models.ForeignKey(Continent)
    name = models.CharField(max_length=1000)
    citizen = models.PositiveIntegerField()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}' . format(self.name)


# Normal perms
class CarPermissionManager(GlobalPermissionManager):
    foreign_key = 'car'


class CarPermission(GlobalPermissionMixin):
    car = models.ForeignKey('Car')

    objects = CarPermissionManager()


class Car(ModelPermission):
    name = models.CharField(max_length=1000)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}' . format(self.name)

    permissions = CarPermission