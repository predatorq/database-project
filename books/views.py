from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from books.models import Book

def index(request):
    return render(request, "index.html")

def reg(request):
    if request.method == 'POST':
        action=request.POST.get('action')
        if action == "add":
            return HttpResponseRedirect("/add")
        if action == "delete":
            return HttpResponseRedirect("/delete")
        if action == "change":
            return HttpResponseRedirect("/change")
        if action == "check":
            return HttpResponseRedirect("/check")
    return render(request,'index.html')

def add(request):
    if request.method == 'POST':
        bid = request.POST.get('id')
        name = request.POST.get('name')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        price = request.POST.get('price')
        time = request.POST.get('time')
        new_book = Book(book_id = bid, book_name = name, book_isbn = isbn, book_author = author, book_publisher = publisher, book_price = price, interview_times = time)
        new_book.save()
        text = Book.objects.filter()
        cond = "add complete"
        return render(request, "add.html", {"books":text, "cond":cond})
    else:
        text = Book.objects.filter()
        cond = ""
        return render(request, "add.html", {"books":text, "cond":cond})

def delete(request):
    if request.method == 'POST':
        bid = request.POST.get('id')
        name = request.POST.get('name')
        if bid != '':
            book = Book.objects.get(book_id = bid)
            print(bid)
        if name != '':
            book = Book.objects.get(book_name = name)
        book.delete()
        text = Book.objects.filter()
        cond = "delete complete"
        return render(request, "delete.html", {"books":text, "cond":cond})
    else:
        text = Book.objects.filter()
        cond = ""
        return render(request, "delete.html", {"books":text, "cond":cond})

def change(request):
    if request.method == 'POST':
        oldid = request.POST.get('oldid')
        book = Book.objects.get(book_id = oldid)
        print(book)
        newid = request.POST.get('newid')
        if newid != '':
            book.book_id = newid
        name = request.POST.get('name')
        if name != '':
            book.book_name = name
        isbn = request.POST.get('isbn')
        if isbn != '':
            book.book_isbn = isbn
        author = request.POST.get('author')
        if author != '':
            book.book_author = author
        publisher = request.POST.get('publisher')
        if publisher != '':
            book.book_publisher = publisher
        price = request.POST.get('price')
        if price != '':
            book.book_price = price
        time = request.POST.get('time')
        if time != '':
            book.interview_times = time       
        book.save()
        text = Book.objects.filter()
        cond = "change complete"
        return render(request, "change.html", {"books":text, "cond":cond})
    else:
        text = Book.objects.filter()
        cond = ""
        return render(request, "change.html", {"books":text, "cond":cond})

def check(request):
    if request.method == 'POST':
        book = Book.objects.filter()
        bid = request.POST.get('id')
        if bid != '':
            book = book.filter(book_id = bid)
        name = request.POST.get('name')
        if name != '':
            book = book.filter(book_name = name)
        isbn = request.POST.get('isbn')
        if isbn != '':
            book = book.filter(book_isbn = isbn)
        author = request.POST.get('author')
        if author != '':
            book = book.filter(book_author = author)
        publisher = request.POST.get('publisher')
        if publisher != '':
            book = book.filter(book_publisher = publisher)
        price = request.POST.get('price')
        if price != '':
            book = book.filter(book_price = price)
        time = request.POST.get('time')
        if time != '':
            book = book.filter(interview_times = time)
        text = Book.objects.filter()
        cond = "check complete"
        return render(request, "check.html", {"books":text, "cond":cond, "checks":book})
    else:
        text = Book.objects.filter()
        cond = ""
        return render(request, "check.html", {"books":text, "cond":cond})
