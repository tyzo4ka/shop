from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request, *args, **kwargs):
    products = Product.objects.filter(remainder__gt=0).order_by("category", "name")
    return render(request, "index.html", context={
        'products': products
    })


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })


def product_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', context={"form": form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product= Product.objects.create(
                name=form.cleaned_data["name"],
                desctiption=form.cleaned_data["description"],
                category=form.cleaned_data["category"],
                remainder=form.cleaned_data["remainder"],
                price=form.cleaned_data['price'])
            return redirect("product_detail_view", pk=product.pk)
        else:
            return render(request, "create.html", context={"form": form})
#
#
# def article_update_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         form = ArticleForm(data={
#             "title": article.title,
#             "author": article.title,
#             "text": article.text,
#             "category": article.category
#         })
#         return render(request, "update.html", context={"form": form, "article": article})
#     elif request.method == 'POST':
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article.title = form.cleaned_data["title"]
#             article.text = form.cleaned_data["text"]
#             article.author = form.cleaned_data["author"]
#             article.category = form.cleaned_data["category"]
#             article.save()
#             return redirect("article_view", pk=article.pk)
#         else:
#             return render(request, "update.html", context={"form": form, "article": article})
#
#
# def article_delete_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == "GET":
#         return render(request, "delete.html", context={"article": article})
#     elif request.method == "POST":
#         article.delete()
#         return redirect("index")
#
