import random
from django import forms
from django.shortcuts import render, redirect
import markdown
from django.shortcuts import render
from . import util


def convert_MKDWN_to_HTML(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request, title):
    html_content = convert_MKDWN_to_HTML(title)
    if html_content == None:
        return render(request, "encyclopedia/NoEntryHere.html", {
            "message": "this entry does not exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_MKDWN_to_HTML(entry_search)
        
        entries = util.list_entries()
        if entry_search in entries:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "entryTitle": html_content
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
        return render(request, "encyclopedia/search.html", {
            "recommendation": recommendation 
        })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        if request.method == 'POST':
    
            input_title = request.POST['title']
            input_text = request.POST['text']
        entries = util.list_entries()
        if input_title in entries:
            return render(request, "encyclopedia/NoEntryHere.html")
        else:
            util.save_entry(input_title, input_text)
            html = convert_MKDWN_to_HTML(input_title)
            return render(request, "encyclopedia/entry.html", {
                "entry": html,
                "entryTitle": input_title
            })

def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

'''def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_MKDWN_to_HTML(title)
        return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content 
            })'''

def save_edit(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        input_text = request.POST['text']
        util.save_entry(input_title, input_text)
        html = convert_MKDWN_to_HTML(input_title)
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": input_title
        })