from django.shortcuts import render, redirect
from .models import Threads, PostNumber, Message
from .forms import CreateNewThread, CreateNewPost
from .linkmanager import linkmanager


def frontpage(response):
    return render(response, 'main/frontpage.html', {})


def b(response):
    if response.method == 'POST' and response.FILES:
        img = response.FILES['media']
        head = response.POST.get('head')
        text = response.POST.get('text')
        PostNumber.objects.create()
        n = PostNumber.objects.latest('id')
        t = Threads(number=n, head=head, text=text, update=n.id, media=img)
        if response.POST.get('name') != '':
            t.name = response.POST.get('name')
        t.save()
        index = t.id
        linkmanager(response.f, n, t)
        t = Threads.objects.all().order_by('-update')
        if len(t) > 20:
            m = t[20:]
            for thr in m:
                thr.delete()
        return redirect('/b/thread/' + str(index))
    form = CreateNewThread()
    t = Threads.objects.all().order_by('-update')
    return render(response, 'main/b.html', {'t': t, 'form': form})


def thread(response, id):
    if response.method == 'POST':
        text = response.POST.get('text')
        PostNumber.objects.create()
        n = PostNumber.objects.latest('id')
        t = Threads.objects.get(id=id)
        if response.POST.get('sage') != 'on' and len(t.message_set.all()) <= 100:
            t.update = n.id
        t.save()
        if response.POST.get('sage') == 'on':
            sage = True
        else:
            sage = False
        m = Message(number=n, thread=t, text=text, sage=sage)
        if response.FILES:
            m.media = response.FILES['media']
        if response.POST.get('name') != '':
            m.name = response.POST.get('name')
        m.save()
        linkmanager(response.f, n, t)
    form = CreateNewPost()
    t = Threads.objects.get(id=id)
    return render(response, 'main/thread.html', {'form': form, 'id': id, 't': t})
