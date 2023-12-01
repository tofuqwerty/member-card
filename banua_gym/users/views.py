from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QRCode
from .forms import MemberForm
import datetime
import base64



def memberList(request):  
    members = QRCode.objects.all()  
    # print(members)
    return render(request,"member_list.html",{'members':members})  


def memberCreate(request):  
    if request.method == "POST":  
        form = MemberForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('member_list')  
            except:  
                pass  
    else:  
        form = MemberForm()  
    return render(request,'member_create.html',{'form':form})  

def memberUpdate(request, id):  
    member = QRCode.objects.get(id=id)
    form = MemberForm(initial={'nama': member.title, 'alamat': member.alamat, 'nohp': member.nohp, 'join_member': member.join_member,  'habis_member': member.habis_member})
    if request.method == "POST":  
        form = MemberForm(request.POST, instance=QRCode)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/member_list')  
            except Exception as e: 
                pass    
    return render(request,'member_update.html',{'form':form})  

def memberDelete(request, id):
    member = QRCode.objects.get(id=id)
    try:
        member.delete()
    except:
        pass
    return redirect('member_list')


def user_profile(request, encode_name):
    # Retrieve the user profile using the username
    encoded_nama=base64.b64decode(encode_name.encode('utf-8')).decode('utf-8')
    user_profile = QRCode.objects.get(nama=encoded_nama)
    print("cek ",user_profile.foto.url)
    return render(request, 'user_profile.html', {'user_profile': user_profile})


# custom 404 view
def custom_404(request, exception):
    return render(request, 'eror_page.html', status=404)

# def geeks_view(request):
#     # fetch date and time
#     now = datetime.datetime.now()
#     # convert to string
#     html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)

    