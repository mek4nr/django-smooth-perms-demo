from django.contrib import admin
from smooth_perms.admin import SmoothPermInlineTabularAdmin, SmoothPermAdmin
from demo.models import Car, CarPermission, Continent, ContinentPermission, Country
from smooth_perms.admin import smooth_registry
from smooth_perms.admin import SmoothGroupAdmin, SmoothGroupForm, SmoothGroup, SmoothUser, SmoothPermTabularInline
from django import forms
from django.utils.translation import ugettext_lazy, ugettext as _


class CarPermissionInline(SmoothPermInlineTabularAdmin):
    model = CarPermission


class CarAdmin(SmoothPermAdmin):
    inline_perm_model = CarPermissionInline
    fields = ['name', 'color']

admin.site.register(Car, CarAdmin)


class ContinentPermissionInline(SmoothPermInlineTabularAdmin):
    model = ContinentPermission


class CountryInline(SmoothPermTabularInline):
    model = Country

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


class ContinentAdmin(SmoothPermAdmin):
    inline_perm_model = ContinentPermissionInline
    inlines = [CountryInline]
    fields = ['name', 'color']

    smooth_perm_field = {
        'change_country': {
            SmoothPermAdmin.INLINE: [
                CountryInline
            ]
        }
    }


admin.site.register(Continent, ContinentAdmin)
admin.site.register(SmoothUser)

smooth_registry.register(Car)
smooth_registry.register(Continent)


class MyGroupForm(SmoothGroupForm):
    can_add_car = forms.BooleanField(label=_('Add'), required=False)
    can_change_car = forms.BooleanField(label=_('Change'), required=False)
    can_delete_car = forms.BooleanField(label=_('Delete'), required=False)

    can_add_continent = forms.BooleanField(label=_('Add'), required=False)
    can_change_continent = forms.BooleanField(label=_('Change'), required=False)
    can_delete_continent = forms.BooleanField(label=_('Delete'), required=False)


class MyGroup(SmoothGroupAdmin):
    form = MyGroupForm

admin.site.register(SmoothGroup, MyGroup)