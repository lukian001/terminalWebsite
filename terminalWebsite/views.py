from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import os

from . import settings
from . import Models


def get_all_images():
    image_list = []

    for dir in settings.STATICFILES_DIRS:
        for file in os.listdir(dir):
            image_list.append(file)

    return image_list


def homepage(request):
    images = get_all_images()
    enum = Models.Commands.list()
    return render(request, 'homepage.html', {'images': images,
                                             'commands': enum,
                                             })


@csrf_exempt
def verify(request):
    enum = Models.Commands.list()
    command = request.POST.get('command', None)

    if command and command in enum:
        template = render_to_string(command + '.html')
    else:
        template = render_to_string('clear.html')

    return JsonResponse(template, safe=False)
