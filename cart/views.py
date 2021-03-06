from django.shortcuts import render, HttpResponse, get_object_or_404
import uuid
from order.forms import CustomProductForm
from django.contrib import messages
from checkout.models import Category


def view_cart(request):
    """ Returns the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add item to the cart page """
    id = str(uuid.uuid4())
    item_type = request.POST.get('category')
    complexity = request.POST.get('complexity')
    variations = request.POST.get('variations')
    user_description = request.POST.get('user_description')
    fast_delivery = request.POST.get('fast_delivery')

    cart_product = {
      "category": item_type, "complexity": complexity,
      "variations": variations, "user_description": user_description,
      "fast_delivery": fast_delivery}

    cart = request.session.get('cart', {})
    cart.__setitem__(id, cart_product)
    request.session['cart'] = cart
    form = CustomProductForm()

    message_item_type = ""
    message_item_complexity = ""
    if item_type == "1":
        message_item_type = "Logo"
    elif item_type == "2":
        message_item_type = "Poster"
    elif item_type == "3":
        message_item_type = "Icon"
    elif item_type == "4":
        message_item_type = "Banner"

    if complexity == "1.0":
        message_item_complexity = "Standard"
    elif complexity == "1.25":
        message_item_complexity = "Advanced"
    elif complexity == "1.5":
        message_item_complexity = "Complex"

    messages.success(request, f'<strong>{message_item_complexity} \
        {message_item_type} added to cart.</strong>')

    context = {
        'form': form
    }

    return render(request, 'order/order.html', context)


def remove_from_cart(request):
    """ Returns item from the cart page """
    id = request.POST.get('id')
    cart = request.session.get('cart', {})
    name_part_1 = ""
    name_part_2 = ""
    for item in cart.items():
        category = get_object_or_404(Category, pk=int(item[1]["category"]))
        if item[0] == id:
            complexty = item[1]["complexity"]
            if complexty == "1.0":
                name_part_1 = "Standard"
            elif complexty == "1.25":
                name_part_1 = "Advanced"
            elif complexty == "1.5":
                name_part_1 = "Complex"
        name_part_2 = category.name.title()
    try:
        del cart[id]
        request.session['cart'] = cart
        messages.success(request, f"<strong>{name_part_1} {name_part_2} \
                             removed from your cart</strong>")
        return render(request, 'cart/cart.html')

    except Exception as e:
        messages.error(request, f'Error occured. When removing \
                       {name_part_1} {name_part_2} from your cart: {e}')
        return HttpResponse(status=500)
