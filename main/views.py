from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList




def index(response, id):
    try: 
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("<h1>Object not found</h1>", {NameError: "Object not found"})
    
    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+ str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("newItemText")
            
            if len(txt) > 2:
                
                ls.item_set.create(text=txt, complete=False)
            else: 
                pass

    return render(response, "main/list.html", {"ls":ls})
    

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
        
    return render(response, "main/create.html", {"form":form})



    
def showAll(response):
    
    return render(response, "main/all.html", {"lists": ToDoList.objects.all()})





