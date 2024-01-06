from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from . import custom_static_func

sinaqmodel = (
    ("asagisinif", "Aşağı siniflər"),
    ("blok9_10", "Blok 9 və 10-cu siniflər"),
    ("blok11", "Blok 11-ci sinif"),
    ("buraxilis9", "Buraxılış 9-cu sinif"),
    ("buraxilis10", "Buraxılış 10"),
    ("buraxilis11", "Buraxılış 11"),
)


class EsasSehife(models.Model):
    basliq = RichTextField(blank=True, max_length=200)
    elave = RichTextField(blank=True, max_length=100)
    elave1 = RichTextField(blank=True, max_length=100)
    sekil = models.ImageField(null=False, upload_to="istedad_images/giris/")
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.elave}"


class Saygac(models.Model):
    basliq = models.CharField(max_length=50)
    cem = models.IntegerField()
    suret = models.IntegerField()
    interval = models.IntegerField()
    icon = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.basliq}"


class Struktur(models.Model):
    vezife = models.CharField(max_length=50)
    ad_soyad = models.CharField(max_length=50)
    elave = models.CharField(max_length=100)
    sekil = models.ImageField(null=False, upload_to="istedad_images/struktur/")
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.ad_soyad}"


class Muellim(models.Model):
    ad = models.CharField(max_length=50)
    fenn = models.CharField(max_length=50)
    aciqlama = RichTextField(blank=True)
    sekil = models.ImageField(upload_to="istedad_images/muellim/")
    is_active = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.ad}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.ad)
        super().save(*args, **kwargs)


class Kurslar(models.Model):
    kurs_adi = models.CharField(max_length=50)
    genis_melumat = RichTextField()
    is_active = models.BooleanField()
    sekil = models.ImageField(upload_to="istedad_images/kurslar/")
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.kurs_adi}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.kurs_adi)
        super().save(*args, **kwargs)


class Tedbirler(models.Model):
    tarix = models.DateField(auto_now_add=True)
    basliq = models.CharField(max_length=100)
    sekil = models.ImageField(upload_to="istedad_images/xeberler/")
    aciqlama = RichTextField()
    is_active = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.basliq}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.basliq)
        super().save(*args, **kwargs)


class Serhler(models.Model):
    ad_soyad = models.CharField(max_length=50)
    yuksek_netice = models.CharField(max_length=50)
    basliq = models.CharField(max_length=100)
    aciqlama = models.TextField()
    sekil = models.ImageField(null=True, upload_to="istedad_images/serhler/")
    is_active = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.ad_soyad}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.ad_soyad)
        super().save(*args, **kwargs)


class Media(models.Model):
    sekil_adi = models.CharField(max_length=50, blank=True)
    sekil = models.ImageField(upload_to="istedad_images/media/")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sekil_adi}"

    def sekilgoster(self):  # new
        return mark_safe(f'<img src = "{self.sekil.url}" width = "300"/>')


class Sinaqlar(models.Model):
    sinaq_adi = models.CharField(max_length=50, verbose_name="Sınaq adı")
    sinaq_tarix = models.DateField(auto_now_add=True)
    sinaq_nov = models.CharField(choices=sinaqmodel, max_length=100, null=True)
    sinaq_duzgun_cvb = models.TextField(blank=True, null=True)
    sinaq_sagird_cvb = models.TextField(blank=True, null=True)
    sinaq_sekil = models.ImageField(upload_to="istedad_images/sinaq/", null=True)
    is_active = models.BooleanField()
    counter = models.IntegerField(default=0)

    letter_replacements = [('c', 'Ç'), ('e', 'Ə'), ('g', 'Ğ'), ('i', 'İ'), ('o', 'Ö'), ('s', "Ş"), ('u', 'Ü')]

    @staticmethod
    def replace_letters(input_str, replacements):
        for old_char, new_char in replacements:
            input_str = input_str.replace(old_char, new_char)
        return input_str

    def hesabla(self):
        sinaqs = Sinaqlar.objects.filter(is_active=True)
        for sinaq in sinaqs:
            if (sinaq.sinaq_nov == 'buraxilis10' and sinaq.counter == 0) or (sinaq.sinaq_nov == 'buraxilis11' and sinaq.counter == 0):
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][26:32]
                    sinif = all_text[row_number][33:34]
                    x_dil = all_text[row_number][43:44]
                    kod = all_text[row_number][45:48]
                    if sinif == 'a':
                        sinif = 10
                    elif sinif == 'b':
                        sinif = 11
                    f1_q = all_text[row_number][53:76]
                    f2_q = all_text[row_number][77:97]
                    f3_q = all_text[row_number][98:111]
                    f3_k_a = all_text[row_number][112:147]

                    if x_dil == "I":
                        d1_q = right_answer[0:23]
                    elif x_dil == "F":
                        d1_q = right_answer[98:121]
                    elif x_dil == "A":
                        d1_q = right_answer[123:146]
                    elif x_dil == "R":
                        d1_q = right_answer[148:171]
                    else:
                        d1_q = right_answer[0:23]
                    d2_q = right_answer[25:45]
                    d3_q = right_answer[47:60]
                    d3_k = right_answer[61:95]

                    if Buraxilis11.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Buraxilis11.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.sinif = sinif
                        person.kod = kod
                        person.xarici_dil = x_dil
                        person.f1_q = f1_q
                        person.f2_q = f2_q
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d2_q = d2_q
                        person.d3_q = d3_q
                        person.d3_k = d3_k
                        person.save()
                    else:
                        person = Buraxilis11.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, sinif=sinif,
                                                            is_no=is_no, kod=kod, xarici_dil=x_dil,
                                                            f1_q=f1_q, f2_q=f2_q, f3_q=f3_q, f3_k_a=f3_k_a, d1_q=d1_q,
                                                            d2_q=d2_q, d3_q=d3_q, d3_k=d3_k)
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
            elif sinaq.sinaq_nov == 'buraxilis9' and sinaq.counter == 0:
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][26:32]
                    sinif = all_text[row_number][33:34]
                    x_dil = all_text[row_number][43:44]
                    kod = all_text[row_number][45:48]

                    f1_q = all_text[row_number][53:79]
                    f2_q = all_text[row_number][80:106]
                    f3_q = all_text[row_number][107:122]
                    f3_k_a = all_text[row_number][123:164]

                    if x_dil == "I":
                        d1_q = right_answer[0:26]
                    elif x_dil == "F":
                        d1_q = right_answer[116:142]
                    elif x_dil == "A":
                        d1_q = right_answer[144:170]
                    elif x_dil == "R":
                        d1_q = right_answer[172:198]
                    else:
                        d1_q = right_answer[0:26]

                    d2_q = right_answer[28:54]
                    d3_q = right_answer[56:71]
                    d3_k_a = right_answer[72:113]

                    if Buraxilis9.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Buraxilis9.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.sinif = sinif
                        person.xarici_dil = x_dil
                        person.kod = kod
                        person.f1_q = f1_q
                        person.f2_q = f2_q
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d2_q = d2_q
                        person.d3_q = d3_q
                        person.d3_k_a = d3_k_a
                        person.save()
                    else:
                        person = Buraxilis9.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, is_no=is_no,
                                                           sinif=sinif, kod=kod, xarici_dil=x_dil,
                                                           f1_q=f1_q, f2_q=f2_q, f3_q=f3_q, f3_k_a=f3_k_a, d1_q=d1_q,
                                                           d2_q=d2_q, d3_q=d3_q, d3_k_a=d3_k_a)
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
            elif sinaq.sinaq_nov == 'asagisinif' and sinaq.counter == 0:
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb
                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][26:33]
                    ata_adi = all_text[row_number][37:49]
                    sinif = all_text[row_number][58:59]
                    f1_q = all_text[row_number][64:89]
                    f2_q = all_text[row_number][89:114]
                    f3_q = all_text[row_number][114:134]
                    d1_q = right_answer[0:25]
                    d2_q = right_answer[27:52]
                    d3_q = right_answer[54:74]
                    if AsagiSinif.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = AsagiSinif.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.ata_adi = ata_adi
                        person.sinif = sinif
                        person.f1_q = f1_q
                        person.f2_q = f2_q
                        person.f3_q = f3_q
                        person.d1_q = d1_q
                        person.d2_q = d2_q
                        person.d3_q = d3_q
                        person.save()
                    else:
                        person = AsagiSinif.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, ata_adi=ata_adi,
                                                           is_no=is_no, sinif=sinif, f1_q=f1_q, f2_q=f2_q, f3_q=f3_q,
                                                           d1_q=d1_q, d2_q=d2_q, d3_q=d3_q)
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
            elif sinaq.sinaq_nov == 'blok11' and sinaq.counter == 0:
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    is_no = all_text[row_number][42:49]
                    sinif = all_text[row_number][26:27]
                    if sinif == '1':
                        sinif = '11'
                    blok = all_text[row_number][28:29]
                    fenn3 = all_text[row_number][30:31]

                    f1_q = all_text[row_number][53:75]
                    f1_k_a = all_text[row_number][76:121]
                    f2_q = all_text[row_number][122:144]
                    f2_k_a = all_text[row_number][145:190]
                    f3_q = all_text[row_number][191:213]
                    f3_k_a = all_text[row_number][214:259]
                    if blok == '1':
                        d1_q = right_answer[0:22]
                        d1_k_a = right_answer[23:68]
                        d2_q = right_answer[69:91]
                        d2_k_a = right_answer[92:137]
                        if fenn3 == 'I':
                            d3_q = right_answer[836:858]
                            d3_k_a = right_answer[859:904]
                        else:
                            d3_q = right_answer[138:160]
                            d3_k_a = right_answer[161:206]
                    elif blok == '2':
                        d1_q = right_answer[209:231]
                        d1_k_a = right_answer[232:277]
                        d2_q = right_answer[278:300]
                        d2_k_a = right_answer[301:346]
                        d3_q = right_answer[347:369]
                        d3_k_a = right_answer[370:415]
                    elif blok == '3':
                        d1_q = right_answer[418:440]
                        d1_k_a = right_answer[441:486]
                        d2_q = right_answer[487:509]
                        d2_k_a = right_answer[510:555]
                        d3_q = right_answer[556:578]
                        d3_k_a = right_answer[579:624]
                    elif blok == '4':
                        d1_q = right_answer[627:649]
                        d1_k_a = right_answer[650:695]
                        d2_q = right_answer[696:718]
                        d2_k_a = right_answer[719:764]
                        d3_q = right_answer[765:787]
                        d3_k_a = right_answer[788:833]
                    else:
                        pass

                    if Blok11.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Blok11.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.sinif = sinif
                        person.blok = blok
                        person.fenn3 = fenn3
                        person.f1_q = f1_q
                        person.f1_k_a = f1_k_a
                        person.f2_q = f2_q
                        person.f2_k_a = f2_k_a
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d1_k_a = d1_k_a
                        person.d2_q = d2_q
                        person.d2_k_a = d2_k_a
                        person.d3_q = d3_q
                        person.d3_k_a = d3_k_a
                        person.save()
                    else:
                        person = Blok11.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, is_no=is_no, sinif=sinif,
                                                       blok=blok, fenn3=fenn3,
                                                       f1_q=f1_q, f2_q=f2_q, f3_q=f3_q,
                                                       f1_k_a=f1_k_a, f2_k_a=f2_k_a, f3_k_a=f3_k_a,
                                                       d1_q=d1_q, d1_k_a=d1_k_a, d2_q=d2_q, d2_k_a=d2_k_a, d3_q=d3_q,
                                                       d3_k_a=d3_k_a, )
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
            elif sinaq.sinaq_nov == 'blok9_10' and sinaq.counter == 0:
                all_text = sinaq.sinaq_sagird_cvb.split("\n")
                all_text = [self.replace_letters(x, self.letter_replacements) for x in all_text]
                right_answer = sinaq.sinaq_duzgun_cvb

                for row_number in range(len(all_text)):
                    ad = all_text[row_number][0:12]
                    soyad = all_text[row_number][13:25]
                    ata_adi = all_text[row_number][26:38]
                    is_no = all_text[row_number][43:50]
                    sinif = all_text[row_number][56:57]
                    if sinif == '0':
                        sinif = '10'
                    blok = all_text[row_number][58:59]
                    fenn3 = all_text[row_number][60:61]

                    f1_q = all_text[row_number][66:88]
                    f1_k_a = all_text[row_number][89:155]
                    f2_q = all_text[row_number][156:178]
                    f2_k_a = all_text[row_number][179:245]
                    f3_q = all_text[row_number][246:268]
                    f3_k_a = all_text[row_number][269:335]
                    if blok == '1':
                        d1_q = right_answer[0:22]
                        d1_k_a = right_answer[23:89]
                        d2_q = right_answer[90:112]
                        d2_k_a = right_answer[113:179]
                        if fenn3 == 'I':
                            d3_q = right_answer[1088:1110]
                            d3_k_a = right_answer[1111:1177]
                        else:
                            d3_q = right_answer[180:202]
                            d3_k_a = right_answer[203:269]
                    elif blok == '2':
                        d1_q = right_answer[272:294]
                        d1_k_a = right_answer[295:361]
                        d2_q = right_answer[362:384]
                        d2_k_a = right_answer[385:451]
                        d3_q = right_answer[452:474]
                        d3_k_a = right_answer[475:541]
                    elif blok == '3':
                        d1_q = right_answer[544:566]
                        d1_k_a = right_answer[567:633]
                        d2_q = right_answer[634:656]
                        d2_k_a = right_answer[657:723]
                        d3_q = right_answer[724:746]
                        d3_k_a = right_answer[747:813]
                    elif blok == '4':
                        d1_q = right_answer[816:838]
                        d1_k_a = right_answer[839:905]
                        d2_q = right_answer[906:928]
                        d2_k_a = right_answer[929:995]
                        d3_q = right_answer[996:1018]
                        d3_k_a = right_answer[1019:1085]
                    else:
                        pass

                    if Blok9_10.objects.filter(is_no=is_no, sinaq_no=sinaq.id):
                        person = Blok9_10.objects.get(is_no=is_no, sinaq_no=sinaq.id)
                        person.aad = ad
                        person.soyad = soyad
                        person.ata_adi = ata_adi
                        person.sinif = sinif
                        person.blok = blok
                        person.fenn3 = fenn3
                        person.f1_q = f1_q
                        person.f1_k_a = f1_k_a
                        person.f2_q = f2_q
                        person.f2_k_a = f2_k_a
                        person.f3_q = f3_q
                        person.f3_k_a = f3_k_a
                        person.d1_q = d1_q
                        person.d1_k_a = d1_k_a
                        person.d2_q = d2_q
                        person.d2_k_a = d2_k_a
                        person.d3_q = d3_q
                        person.d3_k_a = d3_k_a
                        person.save()
                    else:
                        person = Blok9_10.objects.create(sinaq_no=sinaq.id, aad=ad, soyad=soyad, ata_adi=ata_adi,
                                                         is_no=is_no, sinif=sinif,
                                                         blok=blok, fenn3=fenn3,
                                                         f1_q=f1_q, f2_q=f2_q, f3_q=f3_q,
                                                         f1_k_a=f1_k_a, f2_k_a=f2_k_a, f3_k_a=f3_k_a,
                                                         d1_q=d1_q, d1_k_a=d1_k_a, d2_q=d2_q, d2_k_a=d2_k_a, d3_q=d3_q,
                                                         d3_k_a=d3_k_a, )
                        person.save()
                else:
                    new_counter = 1
                    return new_counter
        return self.counter

    @property
    def percent_f1_cem(self):
        buraxilis11_instances = Buraxilis11.objects.filter(sinaq_no=self.id)
        count = Buraxilis11.objects.filter(sinaq_no=self.id).count()
        return round(sum(instance.f1_cem for instance in buraxilis11_instances) / count, 2)

    @property
    def percent_f2_cem(self):
        buraxilis11_instances = Buraxilis11.objects.filter(sinaq_no=self.id)
        count = Buraxilis11.objects.filter(sinaq_no=self.id).count()
        return round(sum(instance.f2_cem for instance in buraxilis11_instances) / count, 2)

    @property
    def percent_f3_cem(self):
        buraxilis11_instances = Buraxilis11.objects.filter(sinaq_no=self.id)
        count = Buraxilis11.objects.filter(sinaq_no=self.id).count()
        return round(sum(instance.f3_cem for instance in buraxilis11_instances) / count, 2)

    def __str__(self):
        return f"{self.sinaq_adi}"

    def save(self, *args, **kwargs):
        self.counter = self.hesabla()
        return super(Sinaqlar, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class Buraxilis11(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    kod = models.CharField(max_length=3)
    xarici_dil = models.CharField(max_length=1, null=True, blank=True)
    d1_q = models.CharField(max_length=23)  # -----------
    f1_q = models.CharField(max_length=23)
    f1_a4 = models.FloatField(default=0)
    f1_a5 = models.FloatField(default=0)
    f1_a6 = models.FloatField(default=0)
    f1_a27 = models.FloatField(default=0)
    f1_a28 = models.FloatField(default=0)
    f1_a29 = models.FloatField(default=0)
    f1_a30 = models.FloatField(default=0)
    d2_q = models.CharField(max_length=20)  # ----------------
    f2_q = models.CharField(max_length=20)
    f2_a46 = models.FloatField(default=0)
    f2_a47 = models.FloatField(default=0)
    f2_a48 = models.FloatField(default=0)
    f2_a49 = models.FloatField(default=0)
    f2_a50 = models.FloatField(default=0)
    f2_a56 = models.FloatField(default=0)
    f2_a57 = models.FloatField(default=0)
    f2_a58 = models.FloatField(default=0)
    f2_a59 = models.FloatField(default=0)
    f2_a60 = models.FloatField(default=0)
    d3_q = models.CharField(max_length=13)  # ---------------
    d3_k = models.CharField(max_length=30)
    f3_q = models.CharField(max_length=13)
    f3_k_a = models.CharField(max_length=34)
    f3_a79 = models.FloatField(default=0)
    f3_a80 = models.FloatField(default=0)
    f3_a81 = models.FloatField(default=0)
    f3_a82 = models.FloatField(default=0)
    f3_a83 = models.FloatField(default=0)
    f3_a84 = models.FloatField(default=0)
    f3_a85 = models.FloatField(default=0)
    cem = models.FloatField()

    def __str__(self):
        return f"{self.sinaq_no}"

    @property
    def x_dil(self):
        return custom_static_func.xarici_dil(self.xarici_dil)

    @property
    def d1_qq(self):
        return custom_static_func.part_of_question(self.d1_q, 3)

    @property
    def d2_qq(self):
        return custom_static_func.part_of_question(self.d2_q, 15)

    @property
    def f1_qq(self):
        return custom_static_func.part_of_question(self.f1_q, 3)

    @property
    def f2_qq(self):
        return custom_static_func.part_of_question(self.f2_q, 15)

    @property
    def f1_d_q(self):
        return custom_static_func.qapali_duz(self.f1_q, self.d1_q, 23)

    @property
    def f2_d_q(self):
        return custom_static_func.qapali_duz(self.f2_q, self.d2_q, 20)

    @property
    def f3_d_q(self):
        return custom_static_func.qapali_duz(self.f3_q, self.d3_q, 13)

    @property
    def f1_d_a(self):
        return round(sum([self.f1_a4, self.f1_a5, self.f1_a6, self.f1_a27, self.f1_a28, self.f1_a29, self.f1_a30]),
                     1) * 2

    @property
    def f2_d_a(self):
        return round(
            sum([self.f2_a46, self.f2_a47, self.f2_a48, self.f2_a49, self.f2_a50, self.f2_a56, self.f2_a57, self.f2_a58,
                 self.f2_a59, self.f2_a60]), 1) * 2

    @property
    def f3_d_a(self):
        return round(sum([self.f3_a79, self.f3_a80, self.f3_a81, self.f3_a82, self.f3_a83, self.f3_a84, self.f3_a85]),
                     1) * 2

    @property
    def f3_k_aa(self):
        return custom_static_func.convert_to_list(self.f3_k_a)

    @property
    def d3_k_aa(self):
        return custom_static_func.convert_to_list(self.d3_k)

    @property
    def f3_d_k(self):
        return custom_static_func.aciq_duz(self.f3_k_aa, self.d3_k_aa)

    @property
    def f1_cem(self):
        return round(((100 * sum([self.f1_d_a, self.f1_d_q])) / 37), 2)

    @property
    def f2_cem(self):
        return round(((5 * sum([self.f2_d_a, self.f2_d_q])) / 2), 2)

    @property
    def f3_cem(self):
        return round((25 * sum([self.f3_d_a, self.f3_d_q, self.f3_d_k])) / 8, 2)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Buraxilis11, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']


class Buraxilis9(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    xarici_dil = models.CharField(max_length=1, null=True, blank=True)
    kod = models.CharField(max_length=3)
    d1_q = models.CharField(max_length=26)  # -----------
    f1_q = models.CharField(max_length=26)
    f1_a6 = models.FloatField(default=0)
    f1_a28 = models.FloatField(default=0)
    f1_a29 = models.FloatField(default=0)
    f1_a30 = models.FloatField(default=0)
    d2_q = models.CharField(max_length=26)  # ----------------
    f2_q = models.CharField(max_length=26)
    f2_a49 = models.FloatField(default=0)
    f2_a50 = models.FloatField(default=0)
    f2_a59 = models.FloatField(default=0)
    f2_a60 = models.FloatField(default=0)
    d3_q = models.CharField(max_length=15)  # ---------------
    d3_k_a = models.CharField(max_length=50)
    f3_q = models.CharField(max_length=15)
    f3_k_a = models.CharField(max_length=50)
    f3_a82 = models.FloatField(default=0)
    f3_a83 = models.FloatField(default=0)
    f3_a84 = models.FloatField(default=0)
    f3_a85 = models.FloatField(default=0)
    cem = models.FloatField()

    def __str__(self):
        return f"{self.sinaq_no}"

    @property
    def x_dil(self):
        return custom_static_func.xarici_dil(self.xarici_dil)

    @property
    def f1_qq(self):
        return custom_static_func.part_of_question(self.f1_q, 5)

    @property
    def f2_qq(self):
        return custom_static_func.part_of_question(self.f2_q, 18)

    @property
    def f3_qq(self):
        return self.f3_q.replace(" ", "&nbsp;")

    @property
    def d1_qq(self):
        return custom_static_func.part_of_question(self.d1_q, 5)

    @property
    def d2_qq(self):
        return custom_static_func.part_of_question(self.d2_q, 18)

    @property
    def f1_d_q(self):
        return custom_static_func.qapali_duz(self.f1_q, self.d1_q, 26)

    @property
    def f2_d_q(self):
        return custom_static_func.qapali_duz(self.f2_q, self.d2_q, 26)

    @property
    def f3_d_q(self):
        return custom_static_func.qapali_duz(self.f3_q, self.d3_q, 15)

    @property
    def f1_d_a(self):
        return round(sum([self.f1_a6, self.f1_a28, self.f1_a29, self.f1_a30]), 1) * 2

    @property
    def f2_d_a(self):
        return round(
            sum([self.f2_a49, self.f2_a50, self.f2_a59, self.f2_a60]), 1) * 2

    @property
    def f3_d_a(self):
        return round(sum([self.f3_a82, self.f3_a83, self.f3_a84, self.f3_a85]), 1) * 2

    @property
    def f3_k_aa(self):
        return custom_static_func.convert_to_list(self.f3_k_a)

    @property
    def d3_k_aa(self):
        return custom_static_func.convert_to_list(self.d3_k_a)

    @property
    def f3_d_k(self):
        return custom_static_func.aciq_duz(self.f3_k_aa, self.d3_k_aa)

    @property
    def f1_cem(self):
        return round(((100 * sum([self.f1_d_a, self.f1_d_q])) / 34), 2)

    @property
    def f2_cem(self):
        return round(((100 * sum([self.f2_d_a, self.f2_d_q])) / 34), 2)

    @property
    def f3_cem(self):
        return round((100 * sum([self.f3_d_a, self.f3_d_q, self.f3_d_k])) / 29, 2)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Buraxilis9, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']


class AsagiSinif(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    ata_adi = models.CharField(max_length=12)
    is_no = models.CharField(max_length=7)
    sinif = models.CharField(max_length=2)
    d1_q = models.CharField(max_length=30)  # -----------
    f1_q = models.CharField(max_length=30)
    d2_q = models.CharField(max_length=30)  # ----------------
    f2_q = models.CharField(max_length=30)
    d3_q = models.CharField(max_length=30)  # ---------------
    f3_q = models.CharField(max_length=30)
    cem = models.FloatField(default=0)

    def __str__(self):
        return f"{self.sinaq_no}"

    @staticmethod
    def space_html(f_q):
        return f_q.replace(" ", "&nbsp;")

    @staticmethod
    def duz_say(araliq, f1, d1):
        x = 0
        for number in range(araliq):
            if f1[number] == d1[number] or d1[number] == '*':
                x += 1
        return x

    @staticmethod
    def sehv_say(araliq, f1, d1):
        x = 0
        for number in range(araliq):
            if f1[number] == ' ':
                continue
            elif f1[number] != d1[number]:
                x += 1
            else:
                pass

        return x

    @staticmethod
    def f_cem(d, s):
        cem = round(((d - s / 3) * 10), 2)
        if cem < 0:
            cem = 0
        return cem

    @property
    def f1_d(self):
        return self.duz_say(25, self.f1_q, self.d1_q)

    @property
    def f2_d(self):
        return self.duz_say(25, self.f2_q, self.d2_q)

    @property
    def f3_d(self):
        return self.duz_say(20, self.f3_q, self.d3_q)

    @property
    def f1_s(self):
        return self.sehv_say(25, self.f1_q, self.d1_q)

    @property
    def f2_s(self):
        return self.sehv_say(25, self.f2_q, self.d2_q)

    @property
    def f3_s(self):
        return self.sehv_say(20, self.f3_q, self.d3_q)

    @property
    def f1_c(self):
        return self.f_cem(self.f1_d, self.f1_s)

    @property
    def f2_c(self):
        return self.f_cem(self.f2_d, self.f2_s)

    @property
    def f3_c(self):
        return self.f_cem(self.f3_d, self.f3_s)

    def cem_func(self):
        return round(sum([self.f1_c, self.f2_c, self.f3_c]), 2)

    @property
    def f1_qq(self):
        return self.space_html(self.f1_q)

    @property
    def f2_qq(self):
        return self.space_html(self.f2_q)

    @property
    def f3_qq(self):
        return self.space_html(self.f3_q)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(AsagiSinif, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']


class Blok11(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    blok = models.CharField(max_length=1)
    fenn3 = models.CharField(max_length=1, null=True)
    f1_q = models.CharField(max_length=22)
    f2_q = models.CharField(max_length=22)
    f3_q = models.CharField(max_length=22)
    f1_k_a = models.CharField(max_length=45)
    f2_k_a = models.CharField(max_length=45)
    f3_k_a = models.CharField(max_length=45)
    d1_q = models.CharField(max_length=22)
    d2_q = models.CharField(max_length=22)
    d3_q = models.CharField(max_length=22)
    d1_k_a = models.CharField(max_length=45)
    d2_k_a = models.CharField(max_length=45)
    d3_k_a = models.CharField(max_length=45)
    f1_28 = models.IntegerField(default=0)
    f1_29 = models.IntegerField(default=0)
    f1_30 = models.IntegerField(default=0)
    f2_28 = models.IntegerField(default=0)
    f2_29 = models.IntegerField(default=0)
    f2_30 = models.IntegerField(default=0)
    f3_28 = models.IntegerField(default=0)
    f3_29 = models.IntegerField(default=0)
    f3_30 = models.IntegerField(default=0)
    cem = models.FloatField(default=0)

    def __str__(self):
        return f'{self.sinaq_no}'

    @property
    def fennler(self):
        fennler = []
        if self.blok == "1":
            if self.fenn3 == 'I':
                fennler = ["Riyaziyyat", "Fizika", "İnformatika"]
            else:
                fennler = ["Riyaziyyat", "Fizika", "Kimya"]
        elif self.blok == "2":
            fennler = ["Riyaziyyat", "Coğrafiya", "Tarix"]
        elif self.blok == "3":
            fennler = ["Azərbaycan dili", "Tarix", "Ədəbiyyat"]
        elif self.blok == "4":
            fennler = ["Biologiya", "Kimya", "Fizika"]
        else:
            pass
        return fennler

    @staticmethod
    def qapali_duz(f_q, d_q, number):
        duz = 0
        for i in range(number):
            if f_q[i] == d_q[i] or d_q[i] == '*':
                duz += 1
        return duz

    @property
    def f1_d_q(self):
        return self.qapali_duz(self.f1_q, self.d1_q, 22)

    @property
    def f2_d_q(self):
        return self.qapali_duz(self.f2_q, self.d2_q, 22)

    @property
    def f3_d_q(self):
        return self.qapali_duz(self.f3_q, self.d3_q, 22)

    @staticmethod
    def qapali_sehv(f_q, d_q, number):
        sehv = 0
        for i in range(number):
            if f_q[i] == ' ' or d_q[i] == '*':
                continue
            elif f_q[i] != d_q[i]:
                sehv += 1

        return sehv

    @property
    def f1_d_s(self):
        return self.qapali_sehv(self.f1_q, self.d1_q, 22)

    @property
    def f2_d_s(self):
        return self.qapali_sehv(self.f2_q, self.d2_q, 22)

    @property
    def f3_d_s(self):
        return self.qapali_sehv(self.f3_q, self.d3_q, 22)

    @staticmethod
    def convert_to_list(string):
        my_list = string.split(',')
        my_list = [element.strip() for element in my_list]
        return my_list

    @property
    def f1_k_aa(self):
        return self.convert_to_list(self.f1_k_a)

    @property
    def f2_k_aa(self):
        return self.convert_to_list(self.f2_k_a)

    @property
    def f3_k_aa(self):
        return self.convert_to_list(self.f3_k_a)

    @property
    def d1_k_aa(self):
        return self.convert_to_list(self.d1_k_a)

    @property
    def d2_k_aa(self):
        return self.convert_to_list(self.d2_k_a)

    @property
    def d3_k_aa(self):
        return self.convert_to_list(self.d3_k_a)

    @staticmethod
    def aciq_duz(f_a, d_a, ):
        duz = 0
        for i in range(4):
            if f_a[i] == d_a[i] or d_a[i] == '*':
                duz += 1
            else:
                continue
        if f_a[4:] == d_a[4:] or d_a[4] == '*':
            duz += 1

        return duz

    @property
    def f1_d_a(self):
        return self.aciq_duz(self.f1_k_aa, self.d1_k_aa)

    @property
    def f2_d_a(self):
        return self.aciq_duz(self.f2_k_aa, self.d2_k_aa)

    @property
    def f3_d_a(self):
        return self.aciq_duz(self.f3_k_aa, self.d3_k_aa)

    @staticmethod
    def uygunluq(f_k_a):
        last_three_elements = f_k_a[-3:]
        # Remove spaces between letters in the last three elements
        new_list = [element.replace(' ', '') for element in last_three_elements]
        return new_list

    @property
    def f1_uyg(self):
        return self.uygunluq(self.f1_k_aa)

    @property
    def f2_uyg(self):
        return self.uygunluq(self.f2_k_aa)

    @property
    def f3_uyg(self):
        return self.uygunluq(self.f3_k_aa)

    @property
    def d1_uyg(self):
        return self.uygunluq(self.d1_k_aa)

    @property
    def d2_uyg(self):
        return self.uygunluq(self.d2_k_aa)

    @property
    def d3_uyg(self):
        return self.uygunluq(self.d3_k_aa)

    @property
    def f1_sit(self):
        return sum([self.f1_28, self.f1_29, self.f1_30])

    @property
    def f2_sit(self):
        return sum([self.f2_28, self.f2_29, self.f2_30])

    @property
    def f3_sit(self):
        return sum([self.f3_28, self.f3_29, self.f3_30])

    @staticmethod
    def f_cem(qapali_duz, qapali_sehv, aciq_duz, f_sit, emsal=1.0):
        qapali_nisbi = qapali_duz - qapali_sehv * 0.25
        aciq_nisbi = (aciq_duz + f_sit)
        nisbi = qapali_nisbi + aciq_nisbi
        f_cem = nisbi * emsal * 100 / 33
        f_cem = round(f_cem, 1)
        if f_cem < 0:
            f_cem = 0
        return f_cem

    @property
    def f1_cem(self):
        return self.f_cem(self.f1_d_q, self.f1_d_s, self.f1_d_a, self.f1_sit, 1.5)

    @property
    def f2_cem(self):
        return self.f_cem(self.f2_d_q, self.f2_d_s, self.f2_d_a, self.f2_sit, 1.5)

    @property
    def f3_cem(self):
        return self.f_cem(self.f3_d_q, self.f3_d_s, self.f3_d_a, self.f3_sit, )

    @staticmethod
    def space_html(f_q):
        return f_q.replace(" ", "&nbsp;")

    @property
    def f1_qq(self):
        return self.space_html(self.f1_q)

    @property
    def f2_qq(self):
        return self.space_html(self.f2_q)

    @property
    def f3_qq(self):
        return self.space_html(self.f3_q)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Blok11, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']


class Blok9_10(models.Model):
    sinaq_no = models.CharField(max_length=100)
    aad = models.CharField(max_length=12)
    soyad = models.CharField(max_length=12)
    ata_adi = models.CharField(max_length=12)
    is_no = models.CharField(max_length=6)
    sinif = models.CharField(max_length=2)
    blok = models.CharField(max_length=1)
    fenn3 = models.CharField(max_length=1, null=True)
    f1_q = models.CharField(max_length=22)
    f2_q = models.CharField(max_length=22)
    f3_q = models.CharField(max_length=22)
    f1_k_a = models.CharField(max_length=45)
    f2_k_a = models.CharField(max_length=45)
    f3_k_a = models.CharField(max_length=45)
    d1_q = models.CharField(max_length=22)
    d2_q = models.CharField(max_length=22)
    d3_q = models.CharField(max_length=22)
    d1_k_a = models.CharField(max_length=45)
    d2_k_a = models.CharField(max_length=45)
    d3_k_a = models.CharField(max_length=45)
    cem = models.FloatField(default=0)

    def __str__(self):
        return f'{self.sinaq_no}'

    @property
    def fennler(self):
        fennler = []
        if self.blok == "1":
            if self.fenn3 == 'I':
                fennler = ["Riyaziyyat", "Fizika", "İnformatika"]
            else:
                fennler = ["Riyaziyyat", "Fizika", "Kimya"]
        elif self.blok == "2":
            fennler = ["Riyaziyyat", "Coğrafiya", "Tarix"]
        elif self.blok == "3":
            fennler = ["Azərbaycan dili", "Tarix", "Ədəbiyyat"]
        elif self.blok == "4":
            fennler = ["Biologiya", "Kimya", "Fizika"]
        else:
            pass
        return fennler

    @staticmethod
    def qapali_duz(f_q, d_q, number):
        duz = 0
        for i in range(number):
            if f_q[i] == d_q[i] or d_q[i] == '*':
                duz += 1
        return duz

    @property
    def f1_d_q(self):
        return self.qapali_duz(self.f1_q, self.d1_q, 22)

    @property
    def f2_d_q(self):
        return self.qapali_duz(self.f2_q, self.d2_q, 22)

    @property
    def f3_d_q(self):
        return self.qapali_duz(self.f3_q, self.d3_q, 22)

    @staticmethod
    def qapali_sehv(f_q, d_q, number):
        sehv = 0
        for i in range(number):
            if f_q[i] == ' ' or d_q[i] == '*':
                continue
            elif f_q[i] != d_q[i]:
                sehv += 1
        return sehv

    @property
    def f1_d_s(self):
        return self.qapali_sehv(self.f1_q, self.d1_q, 22)

    @property
    def f2_d_s(self):
        return self.qapali_sehv(self.f2_q, self.d2_q, 22)

    @property
    def f3_d_s(self):
        return self.qapali_sehv(self.f3_q, self.d3_q, 22)

    @staticmethod
    def convert_to_list(string):
        my_list = string.split(',')
        my_list = [element.strip() for element in my_list]
        return my_list

    @property
    def f1_k_aa(self):
        return self.convert_to_list(self.f1_k_a)

    @property
    def f2_k_aa(self):
        return self.convert_to_list(self.f2_k_a)

    @property
    def f3_k_aa(self):
        return self.convert_to_list(self.f3_k_a)

    @property
    def d1_k_aa(self):
        return self.convert_to_list(self.d1_k_a)

    @property
    def d2_k_aa(self):
        return self.convert_to_list(self.d2_k_a)

    @property
    def d3_k_aa(self):
        return self.convert_to_list(self.d3_k_a)

    @staticmethod
    def aciq_duz(f_a, d_a, ):
        duz = 0
        nisbi = 0
        for i in range(4):
            if f_a[i] == d_a[i] or d_a[i] == '*':
                duz += 1
                nisbi += 1
            else:
                continue
        for i in range(4, 7):
            if f_a[i] == d_a[i] or d_a[i] == '*':
                duz += 1
                nisbi += 2
            else:
                continue
        if f_a[7:] == d_a[7:]:
            duz += 1
            nisbi += 1
        return duz, nisbi

    @property
    def f1_d_a(self):
        return self.aciq_duz(self.f1_k_aa, self.d1_k_aa)

    @property
    def f2_d_a(self):
        return self.aciq_duz(self.f2_k_aa, self.d2_k_aa)

    @property
    def f3_d_a(self):
        return self.aciq_duz(self.f3_k_aa, self.d3_k_aa)

    @staticmethod
    def uygunluq(f_k_a):
        last_three_elements = f_k_a[-3:]
        # Remove spaces between letters in the last three elements
        new_list = [element.replace(' ', '') for element in last_three_elements]
        return new_list

    @property
    def f1_uyg(self):
        return self.uygunluq(self.f1_k_aa)

    @property
    def f2_uyg(self):
        return self.uygunluq(self.f2_k_aa)

    @property
    def f3_uyg(self):
        return self.uygunluq(self.f3_k_aa)

    @property
    def d1_uyg(self):
        return self.uygunluq(self.d1_k_aa)

    @property
    def d2_uyg(self):
        return self.uygunluq(self.d2_k_aa)

    @property
    def d3_uyg(self):
        return self.uygunluq(self.d3_k_aa)

    @staticmethod
    def f_cem(qapali_duz, qapali_sehv, aciq_duz, emsal=1.0):
        qapali_nisbi = ((qapali_duz - qapali_sehv * 0.25) * 100) / 33
        aciq_nisbi = aciq_duz * 100 / 33
        nisbi = qapali_nisbi + aciq_nisbi
        f_cem = nisbi * emsal
        f_cem = round(f_cem, 1)
        if f_cem < 0:
            f_cem = 0
        return f_cem

    @property
    def f1_cem(self):
        return self.f_cem(self.f1_d_q, self.f1_d_s, self.f1_d_a[1], 1.5)

    @property
    def f2_cem(self):
        return self.f_cem(self.f2_d_q, self.f2_d_s, self.f2_d_a[1], 1.5)

    @property
    def f3_cem(self):
        return self.f_cem(self.f3_d_q, self.f3_d_s, self.f3_d_a[1])

    @staticmethod
    def space_html(f_q):
        return f_q.replace(" ", "&nbsp;")

    @property
    def f1_qq(self):
        return self.space_html(self.f1_q)

    @property
    def f2_qq(self):
        return self.space_html(self.f2_q)

    @property
    def f3_qq(self):
        return self.space_html(self.f3_q)

    def cem_func(self):
        return round(sum([self.f1_cem, self.f2_cem, self.f3_cem]), 2)

    def save(self, *args, **kwargs):
        self.cem = self.cem_func()
        return super(Blok9_10, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-cem']
