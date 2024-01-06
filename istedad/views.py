from django.shortcuts import render
from istedad.models import Muellim, Tedbirler, Serhler, EsasSehife, Saygac, Struktur, Kurslar, Sinaqlar, \
    Buraxilis11, AsagiSinif, Blok11, Blok9_10, Buraxilis9
from django.http.response import HttpResponse


# Create your views here.

def index(request):
    context = {
        "esassehife": EsasSehife.objects.filter(is_active=True),
        "serhler": Serhler.objects.filter(is_active=True),
        "saygac": Saygac.objects.filter(is_active=True),
        "kurslar": Kurslar.objects.filter(is_active=True),
        "tedbirler": Tedbirler.objects.filter(is_active=True),
    }
    return render(request, "index.html", context)


def haqqimizda(request):
    context = {
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "haqqimizda.html", context)


def struktur(request):
    context = {
        "struktur": Struktur.objects.filter(is_active=True),
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "struktur.html", context)


def filiallar(request):
    context = {
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "filiallar.html", context)


def muellimler(request):
    context = {
        "muellim": Muellim.objects.filter(is_active=True),
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "muellimler.html", context)


def kurslar(request):
    context = {
        "kurslar": Kurslar.objects.filter(is_active=True)
    }
    return render(request, "kurslar.html", context)


def kurs_details(request, slug):
    kurs = Kurslar.objects.get(slug=slug)
    return render(request, "kurs-details.html", {
        "kurs": kurs,
        "kurslar": Kurslar.objects.filter(is_active=True),
    })


def xeber_details(request, slug):
    xeber = Tedbirler.objects.get(slug=slug)
    return render(request, "xeber-details.html", {
        "xeber": xeber,
        "kurslar": Kurslar.objects.filter(is_active=True)
    })


def tedbirler(request):
    context = {
        "tedbirler": Tedbirler.objects.filter(is_active=True),
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "tedbirler.html", context)


def elaqe(request):
    context = {
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "qeydiyyat/elaqe.html", context)


def qeydiyyatt(request):
    context = {
        "kurslar": Kurslar.objects.filter(is_active=True),
    }
    return render(request, "qeydiyyat/qeydiyyat.html", context)


def sinaqlar(request):
    context = {
        "sinaqs": Sinaqlar.objects.all(),
    }
    return render(request, "sinaqnetice.html", context)


def sinaq_details(request, id):
    sinaq = Sinaqlar.objects.get(id=id)
    return render(request, "sinaq_details.html", {
        "sinaq": sinaq,
    })


def sinaqcavab(request):
    isno_input = request.GET.get('search')
    id_input = request.GET.get('id')
    sinaq = Sinaqlar.objects.get(id=id_input, is_active=True)

    if sinaq.sinaq_nov == 'buraxilis10' or sinaq.sinaq_nov == 'buraxilis11':
        try:
            students_ordered = Buraxilis11.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)

            student_index = list(students_ordered).index(student) + 1

            return render(request, "11buraxilis/ferdi.html", {"student": student, "student_index": student_index})

        except Buraxilis11.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')

    elif sinaq.sinaq_nov == 'buraxilis9':
        try:
            students_ordered = Buraxilis9.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)

            student_index = list(students_ordered).index(student) + 1

            return render(request, "9buraxilis/ferdi.html", {"student": student, "student_index": student_index})

        except Buraxilis9.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')

    elif sinaq.sinaq_nov == 'blok11':
        try:
            students_ordered = Blok11.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)
            student_index = list(students_ordered).index(student) + 1
            return render(request, "11blok/ferdi.html", {
                "student": student,
                "student_index": student_index,
                "tarix": sinaq.sinaq_tarix
            })
        except Blok11.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')

    elif sinaq.sinaq_nov == 'blok9_10':
        try:
            students_ordered = Blok9_10.objects.filter(sinaq_no=id_input).order_by('-cem')
            student = students_ordered.get(is_no=isno_input)
            student_index = list(students_ordered).index(student) + 1
            return render(request, "9_10blok/ferdi.html", {
                "student": student,
                "student_index": student_index,
                "tarix": sinaq.sinaq_tarix
            })
        except Blok9_10.DoesNotExist:
            return HttpResponse('İş nömrəsi tapılmadı')


def adminsinaqcavab(request):
    id_input = request.GET.get('id')
    karne_input = request.GET.get('sinaqtipi')
    sinaq = Sinaqlar.objects.get(id=id_input)

    if sinaq.sinaq_nov == 'buraxilis10' or sinaq.sinaq_nov == 'buraxilis11':
        students = Buraxilis11.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "11buraxilis/karneumumi.html", {
                "students": students
            })
        elif karne_input == 'Siyahi':
            return render(request, "11buraxilis/list.html", {
                "students": students,
                "sinaq": sinaq
            })

    elif sinaq.sinaq_nov == 'buraxilis9':
        students = Buraxilis9.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "9buraxilis/karneumumi.html", {
                "students": students
            })
        elif karne_input == 'Siyahi':
            return render(request, "9buraxilis/list.html", {
                "students": students,
                "sinaq": sinaq
            })

    elif sinaq.sinaq_nov == 'asagisinif':
        students = AsagiSinif.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "5-8sinif/karneumumi.html", {
                "students": students
            })
        elif karne_input == 'Siyahi':
            return render(request, "5-8sinif/list.html", {
                "students": students,
            })

    elif sinaq.sinaq_nov == 'blok11':
        students = Blok11.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "11blok/karneumumi.html", {
                "students": students,
                "tarix": sinaq.sinaq_tarix
            })
        elif karne_input == 'Siyahi':
            return render(request, "11blok/list.html", {
                "students": students
            })

    elif sinaq.sinaq_nov == 'blok9_10':
        students = Blok9_10.objects.filter(sinaq_no=id_input)

        if karne_input == 'Karne':
            return render(request, "9_10blok/karneumumi.html", {
                "students": students,
                "tarix": sinaq.sinaq_tarix
            })
        elif karne_input == 'Siyahi':
            return render(request, "9_10blok/list.html", {
                "students": students
            })
