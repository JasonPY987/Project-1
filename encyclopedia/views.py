import random
from django import forms
from django.shortcuts import render, redirect
from markdown2 import Markdown
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


def entry(request, entry):
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
        })
