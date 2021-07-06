from django.shortcuts import render
from math import ceil
from .models import Images


# def index(request):
    # info = Images.objects.all()
    # a = {
    #     "images": info
    # }
    # # n = len(info)
    # # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'images': info}
    # return render(request, "imgsite.html", a)

def index(request):
    # products= Images.objects.all()
    # print(products)
    allProds=[]
    catprods= Images.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Images.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"imgsite.html", params)

# def index(request):
#     products= Images.objects.all()
#     n= len(products)
#     nSlides= n//4 + ceil((n/4)-(n//4))
#     allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
#     params={'allProds':allProds }
#     return render(request,"imgsite.html", params)


def contact(request):
    return render(request, "imgdetails.html")
