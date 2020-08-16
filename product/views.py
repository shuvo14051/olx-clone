from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q


def productlist(request, category_slug = None):
    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products = Count('product'))

    if category_slug:
        category = Category.objects.get(slug = category_slug)
        productlist = productlist.filter(category = category)

    search_query = request.GET.get('q')
    if search_query:
        productlist = productlist.filter(
            Q(name__iscontains) =  
        )

    paginator = Paginator(productlist, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    productlist = paginator.get_page(page)


    context = {
        'productlist':productlist,
        'categorylist':categorylist,
        'category': category,
    }

    return render(request, 'product/product_list.html', context)


def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    context = {
        'productdetail': productdetail,
        'productimages': productimages,
    }
    return render(request, 'product/product_detail.html', context)

