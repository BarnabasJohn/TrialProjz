from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Conversations
from .forms import ConversationMessageForm


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, id=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversations.objects.filter(item=item).filter(members=request.user.id)

    if conversations:
        pass  # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversations.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {'form': form})


@login_required
def inbox(request):
    conversations = Conversations.objects.filter(members=request.user.id)
    return render(request, 'conversation/inbox.html', {'conversations': conversations})


@login_required
def detail(request, pk):
    conversation = Conversations.objects.filter(members=request.user.id).get(id=pk)

    return render(request, 'conversation/detail.html', {'conversation': conversation})
