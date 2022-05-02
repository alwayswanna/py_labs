import os
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render
import json

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DATA_FILE = open(os.path.join(BASE_DIR, 'resources/university_data.json'), encoding='utf8')
DATA = json.load(JSON_DATA_FILE)


# Sample, returning value without html - template.
def index(request):
    return HttpResponse("Hello world!")


# Easy sample of rendering page.
def index_render(request):
    return render(request, 'index.html', {})


# Information about university.
def university_info(request):
    un_info_from_json = DATA['university_info']
    return render(request, 'university_info.html', {'info': un_info_from_json})


# Information about discipline.
def discipline_info(request):
    dis_info_from_json = DATA['current_subject']
    return render(request, 'discipline_info.html', {'info': dis_info_from_json})


# Information about groups of students.
def groups_info(request):
    groups_info_from_json = DATA['group_info']
    return render(request, 'groups_info.html', {'info': groups_info_from_json})


# Information about university structure.
def university_structure(request):
    un_structure_data = DATA['university_structure']
    return render(request, 'university_structure.html', {'info': un_structure_data})

# end
# 2022-05-02
# Created: https://github.com/alwayswanna
