from django.contrib import admin
from .models import Muellim, Tedbirler, Serhler, EsasSehife, Saygac, Struktur, Media, Kurslar, Sinaqlar, Buraxilis11, AsagiSinif, Blok11, Blok9_10


def make_media_active(queryset):
    queryset.update(is_active=True)


make_media_active.short_description = "Secilmisleri aktiv et"


class IstedadAdminEsasSehife(admin.ModelAdmin):
    list_display = ("basliq", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("basliq", "elave", "elave1",)


class IstedadAdminSaygac(admin.ModelAdmin):
    list_display = ("basliq", "is_active",)
    list_editable = ("is_active",)


class IstedadAdminStruktur(admin.ModelAdmin):
    list_display = ("ad_soyad", "vezife", "is_active",)
    list_editable = ("is_active",)


class IstedadAdminMuellimler(admin.ModelAdmin):
    list_display = ("ad", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("ad", "fenn",)
    readonly_fields = ("slug",)


class IstedadAdminKurslar(admin.ModelAdmin):
    list_display = ("kurs_adi", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("kurs_adi", "genis_melumat",)
    readonly_fields = ("slug",)


class IstedadAdminTedbirler(admin.ModelAdmin):
    list_display = ("basliq", "is_active", "tarix",)
    list_editable = ("is_active",)
    search_fields = ("basliq", "aciqlama", "tarix",)
    readonly_fields = ("slug",)


class IstedadAdminSerhler(admin.ModelAdmin):
    list_display = ("ad_soyad", "basliq", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("ad_soyad", "basliq", "aciqlama",)
    readonly_fields = ("slug",)


class IstedadAdminMedia(admin.ModelAdmin):
    list_display = ("sekilgoster", "sekil_adi", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("sekil_adi",)
    actions = [make_media_active]


class IstedadAdminSinaqlar(admin.ModelAdmin):
    list_display = ("sinaq_adi", "sinaq_tarix", "is_active", "counter")
    list_editable = ("is_active", "counter")
    search_fields = ("sinaq_adi", "sinaq_tarix")
    readonly_fields = ("slug",)


class IstedadAdminBuraxilis11(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "f1_a4", "f1_a5", "f1_a6", "f1_a27", "f1_a28", "f1_a29", "f1_a30", "f2_a46", "f2_a47", "f2_a48", "f2_a49", "f2_a50", "f2_a56", "f2_a57", "f2_a58", "f2_a59", "f2_a60", "f3_a79", "f3_a80", "f3_a81", "f3_a82", "f3_a83", "f3_a84", "f3_a85", "cem")
    list_editable = ("f1_a4", "f1_a5", "f1_a6", "f1_a27", "f1_a28", "f1_a29", "f1_a30", "f2_a46", "f2_a47", "f2_a48", "f2_a49", "f2_a50", "f2_a56", "f2_a57", "f2_a58", "f2_a59", "f2_a60", "f3_a79", "f3_a80", "f3_a81", "f3_a82", "f3_a83", "f3_a84", "f3_a85")
    list_filter = ("sinaq_no", "aad", "soyad", "sinif")


class IstedadAdminBlok11(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "blok", "f1_28", "f1_29", "f1_30", "f2_28", "f2_29", "f2_30", "f3_28", "f3_29", "f3_30", "cem" )
    list_editable = ("f1_28", "f1_29", "f1_30", "f2_28", "f2_29", "f2_30", "f3_28", "f3_29", "f3_30",)

class IstedadAdminBlok9_10(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "blok", "cem" )

class IstedadAdminAsagiSinif(admin.ModelAdmin):
    list_display = ("sinaq_no", "aad", "soyad", "sinif", "f1_d", "f1_s", "f1_c", "f2_d", "f2_s", "f2_c", "f3_d", "f3_s", "f3_c", "cem")

admin.site.register(EsasSehife, IstedadAdminEsasSehife)
admin.site.register(Muellim, IstedadAdminMuellimler)
admin.site.register(Tedbirler, IstedadAdminTedbirler)
admin.site.register(Serhler, IstedadAdminSerhler)
admin.site.register(Saygac, IstedadAdminSaygac)
admin.site.register(Struktur, IstedadAdminStruktur)
admin.site.register(Media, IstedadAdminMedia)
admin.site.register(Kurslar, IstedadAdminKurslar)
admin.site.register(Sinaqlar, IstedadAdminSinaqlar)
admin.site.register(Buraxilis11, IstedadAdminBuraxilis11)
admin.site.register(AsagiSinif, IstedadAdminAsagiSinif)
admin.site.register(Blok11, IstedadAdminBlok11)
admin.site.register(Blok9_10, IstedadAdminBlok9_10)