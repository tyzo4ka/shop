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


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            "name": product.name,
            "description": product.description,
            "category": product.category,
            "remainder": product.remainder,
            "price": product.price
        })
        return render(request, "update.html", context={"form": form, "product": product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data["name"]
            product.description = form.cleaned_data["description"]
            product.category = form.cleaned_data["category"]
            product.remainder = form.cleaned_data['remainder']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect("product_detail", pk=product.pk)
        else:
            return render(request, "update.html", context={"form": form, "product": product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", context={"product": product})
    elif request.method == "POST":
        product.delete()
        return redirect("index")

