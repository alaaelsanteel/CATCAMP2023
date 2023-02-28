from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def usd_to_egp(request):
    context = {
        'usd_to_egp': 30,
    }
    return render(request, 'app/usd-to-egp.html', context=context)

# psst, yes, you'll write code here :)
def live_indomie_price(request):
    context = {
        'indomie_price' : 8, 
    }
    return render(request,'app/live-indomie-price.html',content=context)