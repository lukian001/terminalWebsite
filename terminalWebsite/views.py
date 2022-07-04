from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import os

from . import settings
from . import models


def get_all_images():
    image_list = []

    for dir in settings.STATICFILES_DIRS:
        for file in os.listdir(dir):
            image_list.append(file)

    return image_list


def homepage(request):
    images = get_all_images()
    enum = models.Commands.list()
    commands = []
    for en in enum:
        commands.append(en.name)
    return render(request, 'homepage.html', {'images': images,
                                             'commands': commands,
                                             })


@csrf_exempt
def verify(request):
    enum = models.Commands.list()
    commands = []
    for en in enum:
        commands.append(en.name)
    command = request.POST.get('command', None)

    if command and command in commands:
        if command == 'help':
            template = render_to_string('help.html', {
                'commands': enum
            })
        elif command == 'social':
            template = render_to_string('social.html', {
                'socials': models.Socials.list()
            })
        else:
            template = render_to_string(command + '.html')
    else:
        template = render_to_string('command_doesnt_exists.html')

    return JsonResponse(template, safe=False)
