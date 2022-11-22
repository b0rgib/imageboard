from .models import Threads, Message


def linkmanager(f, n, t):
    f = set(f)
    if '>>' + str(n.id) in f:
        f.remove('>>' + str(n.id))
    for k in f:
        if int(k[2:]) in list(Threads.objects.all().values_list('number', flat=True)):
            tr = Threads.objects.get(number=int(k[2:]))
            update = tr.ref + ', <a href="/b/thread/' + \
                str(t.id) + '#' + str(n.id) + '">' + \
                '>>' + str(n.id) + '</a>'
            tr.ref = update
            tr.save()
        elif int(k[2:]) in list(Message.objects.all().values_list('number', flat=True)):
            ms = Message.objects.get(number=int(k[2:]))
            update = ms.ref + ', <a href="/b/thread/' + \
                str(t.id) + '#' + str(n.id) + '">' + \
                '>>' + str(n.id) + '</a>'
            ms.ref = update
            ms.save()
