from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from cat_sim.cat import Cat
import random

cat = Cat()


def main_view(request: WSGIRequest):
    return render(request, 'index.html')


def cat_view(request: WSGIRequest):
    if request.POST.get('name') is None:
        cat.name = cat.name
    else:
        cat.name = request.POST.get('name')
    print(f"Действие {request.POST.get('action')}")
    if request.POST.get('action') == "Поиграть":
        rage = random.randint(1, 9)
        if cat.sleep == 1:
            cat.happy -= 5
            cat.sleep = 0
        cat.happy += 15
        cat.satiety -= 10
        if rage > 6:
            print(f"Кот {cat.name} в ярости ")
            cat.happy = 0
    if request.POST.get('action') == "Покормить":
        if cat.sleep == 1:
            print("Нельзя кормить спящего кота")
        if cat.sleep == 0:
            cat.happy += 5
            cat.satiety += 15
    if request.POST.get('action') == "Уложить спать":
        cat.sleep = 1
    cat.check_stat()
    cat.avatar = cat.set_avatar()
    context = {
        "name": cat.name,
        "age": cat.age,
        "happy": cat.happy,
        "satiety": cat.satiety,
        "sleep": cat.sleep,
        "avatar": cat.avatar
    }
    return render(request, "cat_stat.html", context)