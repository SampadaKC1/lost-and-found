from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item
from .forms import ItemForm


def home(request):
    query = request.GET.get("q", "")
    status = request.GET.get("status", "")

    # Get all items ordered by newest first
    items = Item.objects.all().order_by("-created_at")

    # Search functionality
    if query:
        items = items.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(location__icontains=query)
        )

    # Filter by status (Lost/Found)
    if status:
        items = items.filter(status=status)

    # Dashboard statistics
    total_items = Item.objects.count()
    lost_items = Item.objects.filter(status="Lost").count()
    found_items = Item.objects.filter(status="Found").count()

    context = {
        "items": items,
        "query": query,
        "status": status,
        "total_items": total_items,
        "lost_items": lost_items,
        "found_items": found_items,
    }

    return render(request, "home.html", context)


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    return render(request, "item_detail.html", {
        "item": item,
    })


@login_required
def my_items(request):
    items = Item.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "my_items.html", {
        "items": items,
    })


@login_required
def report_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            return redirect("home")

    else:
        form = ItemForm()

    return render(request, "report_item.html", {
        "form": form,
    })

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect("my_items")
    else:
        form = ItemForm(instance=item)

    return render(request, "report_item.html", {
        "form": form,
    })


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)

    if request.method == "POST":
        item.delete()
        return redirect("my_items")

    return render(request, "delete_item.html", {
        "item": item,
    })