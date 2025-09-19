from django.shortcuts import render,redirect
from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *

def loginpage(request):
    return render(request,'login.html')
def workpage(request):
    return render(request,'work.html')
def aboutpage(request):
    return render(request,'about.html')
def homepage(request):
    return render(request,'home.html')
def locationpage(request):
    return render(request,'location.html')
def recordpage(request):
    return render(request,'SWMS.html')
def newyopage(request):
    if request.method == "POST":
        form = SWMS_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS_Form()  
    else:
        form = SWMS_Form()

    context = {
        'Wrecord': form
    }

    return render(request, 'ny.html', context)
def rorapage(request):
   context = {
    "all_record": Steel_records.objects.all()
}
   return render(request, 'ny_ta.html', context)
def delete_page(request,id):
    selected_rec = Steel_records.objects.get(id=id)
    selected_rec.delete()
    return redirect('/SWMS/rora/')

def nj(request):
    if request.method == "POST":
        form = SWMS1_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS1_Form()  
    else:
        form = SWMS1_Form()

    context = {
        'W_record': form
    }

    return render(request, 'nj.html', context)
def nj_ta(request):
   context = {
    "all_record": Steel1_records.objects.all()
}
   return render(request, 'nj_ta.html', context)
def delete1_page(request,id):
    selected1_rec = Steel1_records.objects.get(id=id)
    selected1_rec.delete()
    return redirect('/SWMS/nj_ta/')

def nc(request):
    if request.method == "POST":
        form = SWMS2_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS2_Form()  
    else:
        form = SWMS2_Form()

    context = {
        'W_record1': form
    }

    return render(request, 'nc.html', context)
def nc_ta(request):
   context = {
    "all_record": Steel2_records.objects.all()
}
   return render(request, 'nc_ta.html', context)
def delete2_page(request,id):
    selected2_rec = Steel2_records.objects.get(id=id)
    selected2_rec.delete()
    return redirect('/SWMS/nc_ta/')

def tabas(request):
    if request.method == "POST":
        form = SWMS3_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS3_Form()  
    else:
        form = SWMS3_Form()

    context = {
        'W_record2': form
    }

    return render(request, 'tabas.html', context)
def taba_ta(request):
   context = {
    "all_record": Steel3_records.objects.all()
}
   return render(request, 'taba_ta.html', context)
def delete3_page(request,id):
    selected3_rec = Steel3_records.objects.get(id=id)
    selected3_rec.delete()
    return redirect('/SWMS/taba_ta/')

def avanna(request):
    if request.method == "POST":
        form = SWMS4_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS4_Form()  
    else:
        form = SWMS4_Form()

    context = {
        'W_record3': form
    }

    return render(request, 'avanna.html', context)
def avan_ta(request):
   context = {
    "all_record": Steel4_records.objects.all()
}
   return render(request, 'avan_ta.html', context)
def delete4_page(request,id):
    selected4_rec = Steel4_records.objects.get(id=id)
    selected4_rec.delete()
    return redirect('/SWMS/avan_ta/')

def losla(request):
    if request.method == "POST":
        form = SWMS5_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS5_Form()  
    else:
        form = SWMS5_Form()

    context = {
        'W_record4': form
    }

    return render(request, 'losla.html', context)
def los_ta(request):
   context = {
    "all_record": Steel5_records.objects.all()
}
   return render(request, 'los_ta.html', context)
def delete5_page(request,id):
    selected5_rec = Steel5_records.objects.get(id=id)
    selected5_rec.delete()
    return redirect('/SWMS/los_ta/')

def acre(request):
    if request.method == "POST":
        form = SWMS6_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS6_Form()  
    else:
        form = SWMS6_Form()

    context = {
        'W_record5': form
    }

    return render(request, 'acre.html', context)
def acre_ta(request):
   context = {
    "all_record": Steel6_records.objects.all()
}
   return render(request, 'acre_ta.html', context)
def delete6_page(request,id):
    selected6_rec = Steel6_records.objects.get(id=id)
    selected6_rec.delete()
    return redirect('/SWMS/acre_ta/')

def alag(request):
    if request.method == "POST":
        form = SWMS7_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS7_Form()  
    else:
        form = SWMS7_Form()

    context = {
        'W_record6': form
    }

    return render(request, 'alag.html', context)
def alg_ta(request):
   context = {
    "all_record": Steel7_records.objects.all()
}
   return render(request, 'alg_ta.html', context)
def delete7_page(request,id):
    selected7_rec = Steel7_records.objects.get(id=id)
    selected7_rec.delete()
    return redirect('/SWMS/alg_ta/')

def ban(request):
    if request.method == "POST":
        form = SWMS8_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS8_Form()  
    else:
        form = SWMS8_Form()

    context = {
        'W_record7': form
    }

    return render(request, 'ban.html', context)
def ban_ta(request):
   context = {
    "all_record": Steel8_records.objects.all()
}
   return render(request, 'ban_ta.html', context)
def delete8_page(request,id):
    selected8_rec = Steel8_records.objects.get(id=id)
    selected8_rec.delete()
    return redirect('/SWMS/ban_ta/')

def ind(request):
    if request.method == "POST":
        form = SWMS9_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS9_Form()  
    else:
        form = SWMS9_Form()

    context = {
        'W_record8': form
    }

    return render(request, 'ind.html', context)
def ind_ta(request):
   context = {
    "all_record": Steel9_records.objects.all()
}
   return render(request, 'ind_ta.html', context)
def delete9_page(request,id):
    selected9_rec = Steel9_records.objects.get(id=id)
    selected9_rec.delete()
    return redirect('/SWMS/ind_ta/')

def hong(request):
    if request.method == "POST":
        form = SWMS10_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS10_Form()  
    else:
        form = SWMS10_Form()

    context = {
        'W_record9': form
    }

    return render(request, 'hong.html', context)
def hong_ta(request):
   context = {
    "all_record": Steel10_records.objects.all()
}
   return render(request, 'hong_ta.html', context)
def delete10_page(request,id):
    selected10_rec = Steel10_records.objects.get(id=id)
    selected10_rec.delete()
    return redirect('/SWMS/hong_ta/')

def dor(request):
    if request.method == "POST":
        form = SWMS11_Form(request.POST)
        if form.is_valid():
            form.save()
            form = SWMS11_Form()  
    else:
        form = SWMS11_Form()

    context = {
        'W_record10': form
    }

    return render(request, 'dor.html', context)
def dor_ta(request):
   context = {
    "all_record": Steel11_records.objects.all()
}
   return render(request, 'dor_ta.html', context)
def delete11_page(request,id):
    selected11_rec = Steel11_records.objects.get(id=id)
    selected11_rec.delete()
    return redirect('/SWMS/dor_ta/')

def uy_rec(request):
    if request.method == "POST":
        form = was1_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was1_Form()  
    else:
        form = was1_Form()

    context = {
        'Wa_record1': form
    }

    return render(request, 'uy_re.html', context)
def uy_red(request):
   context = {
    "all_record": was_rec1.objects.all()
}
   return render(request, 'uy_red.html', context)
def van_page(request,id):
    sel1_rec = was_rec1.objects.get(id=id)
    sel1_rec.delete()
    return redirect('/SWMS/uy_red/')

def nc_rec(request):
    if request.method == "POST":
        form = was2_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was2_Form()  
    else:
        form = was2_Form()

    context = {
        'Wa_record2': form
    }

    return render(request, 'nc_re.html', context)
def nc_red(request):
   context = {
    "all_record": was_rec2.objects.all()
}
   return render(request, 'nc_red.html', context)
def van_page1(request,id):
    sel2_rec = was_rec2.objects.get(id=id)
    sel2_rec.delete()
    return redirect('/SWMS/nc_red/')

def nj_rec(request):
    if request.method == "POST":
        form = was3_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was3_Form()  
    else:
        form = was3_Form()

    context = {
        'Wa_record3': form
    }

    return render(request, 'nj_re.html', context)
def nj_red(request):
   context = {
    "all_record": was_rec3.objects.all()
}
   return render(request, 'nj_red.html', context)
def van_page2(request,id):
    sel3_rec = was_rec3.objects.get(id=id)
    sel3_rec.delete()
    return redirect('/SWMS/nj_red/')

def taba_rec(request):
    if request.method == "POST":
        form = was4_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was4_Form()  
    else:
        form = was4_Form()

    context = {
        'Wa_record4': form
    }

    return render(request, 'taba_re.html', context)
def taba_red(request):
   context = {
    "all_record": was_rec4.objects.all()
}
   return render(request, 'taba_red.html', context)
def van_page3(request,id):
    sel4_rec = was_rec4.objects.get(id=id)
    sel4_rec.delete()
    return redirect('/SWMS/taba_red/')

def avan_rec(request):
    if request.method == "POST":
        form = was5_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was5_Form()  
    else:
        form = was5_Form()

    context = {
        'Wa_record5': form
    }

    return render(request, 'avan_re.html', context)
def avan_red(request):
   context = {
    "all_record": was_rec5.objects.all()
}
   return render(request, 'avan_red.html', context)
def van_page4(request,id):
    sel5_rec = was_rec5.objects.get(id=id)
    sel5_rec.delete()
    return redirect('/SWMS/avan_red/')

def los_rec(request):
    if request.method == "POST":
        form = was6_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was6_Form()  
    else:
        form = was6_Form()

    context = {
        'Wa_record6': form
    }

    return render(request, 'los_re.html', context)
def los_red(request):
   context = {
    "all_record": was_rec6.objects.all()
}
   return render(request, 'los_red.html', context)
def van_page5(request,id):
    sel6_rec = was_rec6.objects.get(id=id)
    sel6_rec.delete()
    return redirect('/SWMS/los_red/')

def acre_rec(request):
    if request.method == "POST":
        form = was7_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was7_Form()  
    else:
        form = was7_Form()

    context = {
        'Wa_record7': form
    }

    return render(request, 'acre_re.html', context)
def acre_red(request):
   context = {
    "all_record": was_rec7.objects.all()
}
   return render(request, 'acre_red.html', context)
def van_page6(request,id):
    sel7_rec = was_rec7.objects.get(id=id)
    sel7_rec.delete()
    return redirect('/SWMS/acre_red/')

def alag_rec(request):
    if request.method == "POST":
        form = was8_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was8_Form()  
    else:
        form = was8_Form()

    context = {
        'Wa_record8': form
    }

    return render(request, 'alag_re.html', context)
def alag_red(request):
   context = {
    "all_record": was_rec8.objects.all()
}
   return render(request, 'alag_red.html', context)
def van_page7(request,id):
    sel8_rec = was_rec8.objects.get(id=id)
    sel8_rec.delete()
    return redirect('/SWMS/alag_red/')

def ban_rec(request):
    if request.method == "POST":
        form = was9_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was9_Form()  
    else:
        form = was9_Form()

    context = {
        'Wa_record9': form
    }

    return render(request, 'ban_re.html', context)
def ban_red(request):
   context = {
    "all_record": was_rec9.objects.all()
}
   return render(request, 'ban_red.html', context)
def van_page8(request,id):
    sel9_rec = was_rec9.objects.get(id=id)
    sel9_rec.delete()
    return redirect('/SWMS/ban_red/')

def ind_rec(request):
    if request.method == "POST":
        form = was10_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was10_Form()  
    else:
        form = was10_Form()

    context = {
        'Wa_record10': form
    }

    return render(request, 'ind_re.html', context)
def ind_red(request):
   context = {
    "all_record": was_rec10.objects.all()
}
   return render(request, 'ind_red.html', context)
def van_page9(request,id):
    sel10_rec = was_rec10.objects.get(id=id)
    sel10_rec.delete()
    return redirect('/SWMS/ind_red/')


def hong_rec(request):
    if request.method == "POST":
        form = was11_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was11_Form()  
    else:
        form = was11_Form()

    context = {
        'Wa_record11': form
    }

    return render(request, 'hong_re.html', context)
def hong_red(request):
   context = {
    "all_record": was_rec11.objects.all()
}
   return render(request, 'hong_red.html', context)
def van_page10(request,id):
    sel11_rec = was_rec11.objects.get(id=id)
    sel11_rec.delete()
    return redirect('/SWMS/hong_red/')

def dor_rec(request):
    if request.method == "POST":
        form = was12_Form(request.POST)
        if form.is_valid():
            form.save()
            form = was12_Form()  
    else:
        form = was12_Form()

    context = {
        'Wa_record12': form
    }

    return render(request, 'dor_re.html', context)
def dor_red(request):
   context = {
    "all_record": was_rec12.objects.all()
}
   return render(request, 'dor_red.html', context)
def van_page11(request,id):
    sel12_rec = was_rec12.objects.get(id=id)
    sel12_rec.delete()
    return redirect('/SWMS/dor_red/')




def uy_me(request):
    return render(request,'uy_me.html')
def nj_me(request):
    return render(request,'nj_me.html')
def nc_me(request):
    return render(request,'nc_me.html')
def tabas_me(request):
    return render(request,'tabas_me.html')
def avanna_me(request):
    return render(request,'avanna_me.html')
def losla_me(request):
    return render(request,'losla_me.html')
def acre_me(request):
    return render(request,'acre_me.html')
def alag_me(request):
    return render(request,'alag_me.html')
def ban_me(request):
    return render(request,'ban_me.html')
def ind_me(request):
    return render(request,'ind_me.html')
def hong_me(request):
    return render(request,'hong_me.html')
def dor_me(request):
    return render(request,'dor_me.html')
''''def newjerpage(request):
     

     context={
        'W_record':SWMS0_Form()
    }

     if request.method=="POST":
        W_record = SWMS0_Form(request.POST)
        if W_record.is_valid():
            W_record.save()
     return render(request,'nj.html',context)
def jalispage(request):
    context = {
       "all_record1":Waste1_records.objects.all()
   }
    return render(request,'nj_ta.html',context)
def newcapage(request):
    context={
        'W_record1':SWMS1_Form()
    }

    if request.method=="POST":
        W_record1 = SWMS1_Form(request.POST)
        if W_record1.is_valid():
            W_record1.save()
    return render(request,'nc.html',context)
def tunupage(request):
     context1 = {
       "all_record2":Waste2_records.objects.all()
   }
     return render(request,'nc_ta.html',context1)
def tabaspage(request):
    context={
        'W_record2':SWMS2_Form()
    }

    if request.method=="POST":
        W_record2 = SWMS2_Form(request.POST)
        if W_record2.is_valid():
            W_record2.save()
    return render(request,'tabas.html',context)
def chiapapage(request):
     context = {
       "all_record3":Waste3_records.objects.all()
   }
     return render(request,'taba_ta.html')
def avannapage(request):
     context={
        'W_record3':SWMS3_Form()
    }

     if request.method=="POST":
        W_record3 = SWMS3_Form(request.POST)
        if W_record3.is_valid():
            W_record3.save()
     return render(request,'avanna.html',context)
def kitapage(request):
     context = {
       "all_record4":Waste4_records.objects.all()
   }
     return render(request,'avan_ta.html',context)
def loslapage(request):
    context={
        'W_record4':SWMS2_Form()
    }

    if request.method=="POST":
        W_record4 = SWMS2_Form(request.POST)
        if W_record4.is_valid():
            W_record4.save()
    return render(request,'losla.html',context)
def manulpage(request):
    context = {
       "all_record5":Waste5_records.objects.all()
   }
    return render(request,'los_ta.html',context)
def biobpage(request):
    context = {
       "all_record6":Waste5_records.objects.all()
   }
    return render(request,'acre_ta.html',context)
def acrepage(request):
     context={
        'W_record5':SWMS2_Form()
    }

     if request.method=="POST":
        W_record5 = SWMS2_Form(request.POST)
        if W_record5.is_valid():
            W_record5.save()
     return render(request,'acre.html',context)
def alagpage(request):
    context={
        'W_record6':SWMS2_Form()
    }

    if request.method=="POST":
        W_record6 = SWMS2_Form(request.POST)
        if W_record6.is_valid():
            W_record6.save()
    return render(request,'alag.html',context)
def pe1page(request):
    context = {
       "all_record7":Waste6_records.objects.all()
   }
    return render(request,'alg_ta.html',context)
def pe2page(request):
    return render(request,'pe2.html')
def pe3page(request):
    return render(request,'pe3.html')
def mumpage(request):
    return render(request,'mum.html')
def bangapage(request):
    return render(request,'banga.html')
def chennaipage(request):
    return render(request,'chen.html')
def beijpage(request):
    return render(request,'beij.html')
def shangpage(request):
    return render(request,'shang.html')
def hongpage(request):
    return render(request,'hong.html')
def bulgpage(request):
    return render(request,'bulg.html')
def dornpage(request):
    return render(request,'dorn.html')
def orkhopage(request):
    return render(request,'orkh.html')
def monavilpage(request):
    return render(request,'monavil.html')
def montecarpage(request):
    return render(request,'montecar.html')
def laconpage(request):
    return render(request,'lacon.html')
def evangpage(request):
    return render(request,'evang.html')
def serravpage(request):
    return render(request,'serrav.html')
def faetpage(request):
    return render(request,'faet.html')
def capelpage(request):
    return render(request,'capel.html')
def merspage(request):
    return render(request,'mers.html')'''''