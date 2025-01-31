from django.shortcuts import render,get_object_or_404,redirect

from items.models import Item
from .models import Conversation
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Item,pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversation = Conversation.objects.filter(item = item).filter(member__in= [request.user.id])
    
    if conversation:
        return redirect('conversation:detail',pk=conversation.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.member.add(request.user)
            conversation.member.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('items:detail',pk=item_pk)
    else:
        form = MessageForm()

    return render(request,'conversation/new.html',{
        'form':form
        })

@login_required
def inbox(request):
    print("Current user:", request.user) 
    conversation = Conversation.objects.filter(member__in = [request.user.id])

    return render(request,'conversation/inbox.html',{
        'conversations':conversation
    })

@login_required
def con_detail(request,pk):
    conversation = Conversation.objects.filter(member__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detail',pk=pk)

    else:
        form = MessageForm()

    return render(request,'conversation/detail.html',{
        'conversations':conversation,
        'form':form
    })

