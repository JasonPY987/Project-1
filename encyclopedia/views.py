import random
import markdown2
from django import forms 
from django.shortcuts import render, redirect


from django.shortcuts import render

from . import util


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
        return render(request,"encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
        })