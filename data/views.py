from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import FileForm
from .models import Dataset
import os
from django.contrib.auth.decorators import login_required




@login_required(login_url="login")
def FileUploader(request):
    form = FileForm()
    if request.method == "POST":

        mydata = FileForm(request.POST, request.FILES)
        if mydata.is_valid():

            x = mydata.save(commit=False)

            x.user_name = request.user
            file = request.FILES["file"]
            x.file = file

            print(request.FILES["file"])
            x.save()
            # messages.success(request, "File Uploaded")

            return redirect("table")
    context = {"form": form}
    return render(request, "index.html", context)


@login_required(login_url="login")
def table(request):
    # messages.success(request, "Look at whats been uploaded.")

    try:
        public = Dataset.objects.filter(public=True)
        upload = Dataset.objects.filter(user_name=request.user)
        context = {"public": public, "upload": upload}
    except:
        context = {"public": "None", "upload": "None"}
    return render(request, "table.html", context)



@login_required(login_url="login")
def deletefiles(request, id):
    data = Dataset.objects.get(id=id)
    myfile = str(data.file.path)
    if os.path.exists(myfile):
        os.remove(myfile)
        data.delete()
        # messages.success(request, "File is Deleted!")
        return redirect("table")
    else:
        print("files does not exists")
        # messages.error(request, "File is Not Deleted!")
        return redirect("table")
    

@login_required(login_url="login")
def updatefiles(request, id):

    data = Dataset.objects.get(id=id)
    updateform = FileForm(request.POST or None, instance=data)
    if updateform.is_valid():
        updateform.save()
        # messages.success(request, "File Status is Updated!")
        return redirect("table")
    context = {"form": updateform}
    return render(request, "update.html", context)

