from django.shortcuts import render
from .forms import FileUploadForm
import os
from django.conf import settings

def welcome(request):
    return render(request, 'FileUploader/welcome.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name
            file_extension = file_name.split('.')[-1].lower()
            
            # Determine the folder to save the file based on extension
            if file_extension == 'pdf':
                folder = 'pdf'
            elif file_extension == 'docx':
                folder = 'doc'
            elif file_extension in ['jpg', 'png']:
                folder = 'images'
            else:
                folder = 'others'  # Default folder for unsupported file types

            # Define the full file path
            file_path = os.path.join(settings.MEDIA_ROOT, folder, file_name)

            # Create the folder if it does not exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Save the file to the determined folder
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return render(request, 'FileUploader/upload_success.html')
    else:
        form = FileUploadForm()
    return render(request, 'FileUploader/upload_form.html', {'form': form})
