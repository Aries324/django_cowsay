from django.shortcuts import render,HttpResponseRedirect, reverse
from cowsay_project.forms import UserInputForm
from cowsay_project.models import UserTextInput
import subprocess



def index(request):
    new_form = UserInputForm()
    if request.method == 'POST':
        form = UserInputForm(request.POST)

        if form.is_valid():
            user_text = form.cleaned_data
            show_txt = subprocess.run(
                ['cowsay'] + user_text['text'].split(), capture_output=True
            ).stdout.decode()
            UserTextInput.objects.create(
                text=user_text['text']

            )
        return render(request, 'index.html', {'show_txt': show_txt, "form": new_form})

    form = UserInputForm()


    return render(request, 'index.html', {'form': form})



def history(request):
    text_history = UserTextInput.objects.order_by('-id')[:10]
    return render(request, 'history.html', {'text_history': text_history})


