from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404

#Create your views here

@login_required
def edit_entry(request, entry_id):
    """edit the selected entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    #make sure the topic is associated with user
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #save modified entry
        form = EntryForm(instance=entry)
    else:
        #to revise entered text
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def new_entry(request, topic_id):
    """add a new entry for the associated entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #create a blank form because no data was submitted
        form = EntryForm()
    else:
        #process the data because POST data was submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    #display an invalid form if request,method != POST
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #no submitted data so create a blank form
        form = TopicForm()
    else:
        #post data is submitted so you process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()            
            return redirect('learning_logs:topics')
    
    #diplay invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def index(request):
    """larning logs home page"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """show topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """show a topic and all queries"""
    topic = Topic.objects.get(id=topic_id)

    #make sure the topic is associated with user
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)



