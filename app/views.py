from django.shortcuts import render
from django.http import HttpResponse
from cus_details.models import customer
#from orders.models import orders
# Create your views here.
cus=[]
def home(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        gmail=request.POST["gmail"]
        tableno=request.POST["tableno"]
        cus.append(name)
        cus.append(tableno)
        var=customer(name=name,phone=phone,gmail=gmail,tableno=tableno)
        var.save()
        return render(request,"signin.html")
    return render(request,"index.html")
def signin(request):
    if request.method=="POST":
        #Starters
        spinach=request.POST["spinach"]
        crockpot=request.POST["crockpot"]
        fruitdip=request.POST["fruitdip"]
        meatballs=request.POST["meatballs"]
        hormelchilidip=request.POST["hormelchilidip"]
        macandcheesebites=request.POST["macandcheesebites"]
        mozzarellasticks=request.POST["mozzarellasticks"]
        brioche=request.POST["brioche"]
        #Lunch
        pulledbbqpork=request.POST["pulledbbqpork"]
        meatloaf=request.POST["meatloaf"]
        wildalaskasalmon=request.POST["wildalaskasalmon"]
        bakedbeans=request.POST["bakedbeans"]
        macaroniandcheese=request.POST["macaroniandcheese"]
        cioppino=request.POST["cioppino"]
        chickenfriedsteaks=request.POST["chickenfriedsteaks"]
        scallions=request.POST["scallions"]
        #Beverages
        syrah=request.POST["syrah"]
        zinfandel=request.POST["zinfandel"]
        southerncomfort=request.POST["southerncomfort"]
        tennesseewhiskey=request.POST["tennesseewhiskey"]
        winecooler=request.POST["winecooler"]
        #Done
        l1={"spinach":spinach,"crockpot":crockpot,"fruitdip":fruitdip,"meatballs":meatballs,"hormelchilidip":hormelchilidip,"macandcheesebites":macandcheesebites,"mozzarellasticks":mozzarellasticks,"brioche":brioche}
        d1={}
        for i in l1:
            if l1[i]!='0':
                d1[i]=l1[i]
        l2={"pulledbbqpork":pulledbbqpork,"meatloaf":meatloaf,"wildalaskasalmon":wildalaskasalmon,"bakedbeans":bakedbeans,"macaroniandcheese":macaroniandcheese,"cioppino":cioppino,"chickenfriedsteaks":chickenfriedsteaks,"scallions":scallions}
        d2={}
        for j in l2:
            if l2[j]!='0':
                d2[j]=l2[j]
        l3={"syrah":syrah,"zinfandel":zinfandel,"southerncomfort":southerncomfort,"tennesseewhiskey":tennesseewhiskey,"winecooler":winecooler}        
        d3={}
        for k in l3:
            if l3[k]!='0':
                d3[k]=l3[k]
        #obj=orders(customer=cus[-2],tableno=cus[-1],starters=d1,lunch=d2,beverages=d3)
        #obj.save()
        return render(request,"success.html")
    return render(request,"signin.html")
