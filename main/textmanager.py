from lxml.html import fromstring
from .models import Threads, Message


def textmanager(get_response):
    def middleware(request):
        if request.method == 'POST':
            text = request.POST.get('text')
            text = str(fromstring(text).text_content())
            f = []
            for i in range(len(text)):
                if i + 2 == len(text):
                    break
                else:
                    if text[i:i + 2] == '>>' and text[i + 2] != '>':
                        t = '>>'
                        j = i + 2
                        while text[j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            t += text[j]
                            j += 1
                            if j == len(text):
                                break
                        f.append(t)
            for k in f:
                if int(k[2:]) in list(Threads.objects.all().values_list('number', flat=True)):
                    id = str(Threads.objects.get(number=int(k[2:])).id)
                    text = text.replace(k, '<a href="/b/thread/' +
                                        id + '#' + k[2:] + '">' + k + '</a>')
                elif int(k[2:]) in list(Message.objects.all().values_list('number', flat=True)):
                    ms = Message.objects.get(number=int(k[2:]))
                    tr = ms.thread
                    id = str(tr.id)
                    text = text.replace(k, '<a href="/b/thread/' +
                                        id + '#' + k[2:] + '">' + k + '</a>')
            request.POST = request.POST.copy()
            request.POST['text'] = text
            request.f = f
        response = get_response(request)
        return response
    return middleware
