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




"""def entry(request, entry):
    markdowner = Markdown(entry)
    entryPage = util.get_entry(entry)
    if entryPage is none:
        return render(request, "encyclopedia/NoEntryHere.html", {
            "entryTitle": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
        })"""