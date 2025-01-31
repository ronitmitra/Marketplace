from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item,Category
from .forms import AdditemForm,EdititemForm
# Create your views here.
@login_required
def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('Category',0)
    categories= Category.objects.all()
    item = Item.objects.filter(is_sold=False)

    if query:
        item = item.filter(Q(name__icontains = query)| Q(description__icontains=query))

    if category_id:
        item = item.filter(Category_id = category_id)

    return render(request,'items/items.html',{
        'items':item,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })

def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    
    related_item = Item.objects.filter(Category = item.Category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'items/detail.html',{
        'item':item,
        'related_item':related_item
    })
@login_required
def newItem(request):
    if request.method == 'POST':
        form = AdditemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit = False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail',pk=item.id)
    else:        
        form = AdditemForm()

    return render(request,'items/form.html',{
        'form':form,
        'title':'Add Item'
    })
@login_required

def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required

def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)

    if request.method == 'POST':
        form = EdititemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()

            return redirect('items:detail',pk=item.id)

    else:
        form = EdititemForm(instance=item)

    return render(request,'items/form.html',{
        'form':form,
        'title':'Edit Form'
    })