from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login/")
def index(response, id):
    #getting the list if list exists and you are the user who made the list
    try: 
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
         return HttpResponseRedirect("/")
    except ls.user != response.user:
        return HttpResponseRedirect("/")


    if response.method == "POST":
        if response.POST.get("save") or response.POST.get("newItem"):
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+ str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            txt = response.POST.get("newItemText")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else: 
                pass
        elif response.POST.get("delete"):
            print("test")
            for item in ls.item_set.all():
                if response.POST.get("d"+ str(item.id)) == "delete":
                    item.delete()

        elif response.POST.get("deleteTable"):
            ls.delete()
            return HttpResponseRedirect("/")

    return render(response, "main/list.html", {"ls":ls})
    

# go to home page
def home(response):
    return render(response, "main/home.html", {})


#creating a new list
@login_required(login_url="/login/")
def create(response):
    if response.method == "POST":

        #only possible to have 5 tables per account
        if response.user.todolist.all().count() < 5:

            form = CreateNewList(response.POST)

            if form.is_valid():
                n = form.cleaned_data["name"]
                t = ToDoList(name=n, user=response.user)
                t.save()
                return HttpResponseRedirect("/%i" %t.id)
            
        else:
            return HttpResponse("You have too many items in your list. Please delete some and try again.")
        
    form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
        


#showing all your tables
@login_required(login_url="/login/")
def showAll(response):
    
    return render(response, "main/all.html", {})





