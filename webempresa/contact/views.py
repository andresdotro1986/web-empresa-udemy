from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from  django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form=ContactForm()

    if request.method == "POST":
        contact_form= ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            # Enviamos el correo y redireccionamos
            email=EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email, content),
                "no-contestar@inbox.mailtrap.io",
                ["andresdotro@gmail.com,"],
                reply_to=[email]

                # asunto,
                # cuerpo,
                # email_origen,
                # email_destino,
                # reply_to=[email]
            )
            try:
                email.send()
                # todo fue bien
                return redirect(reverse ('contact')+"?ok")
                print("nada")
            except:
                # Algo salio mal
                return redirect(reverse ('contact')+"?fail")
            
        
    return render (request,'contact/contact.html',{'form':contact_form})


