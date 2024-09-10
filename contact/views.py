from django.http import HttpResponse
# Create your views here.
 

def contact_me(request):
    return HttpResponse("Questions or comments? Get in touch and we'll be happy to help.")