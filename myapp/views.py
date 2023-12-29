from django.shortcuts import render
import random
import os
import google.generativeai as genai
from google.cloud import storage
import PIL.Image


def authenticate_implicit_with_adc(project_id="yourprojectidgoeshere"):
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")
API='apigoeshere'

genai.configure(api_key=API)
from django.core.files.storage import FileSystemStorage

def test(request):
    context={}
    if request.method=='POST':
        CH=request.POST.get('input')
        uploaded_file = request.FILES.get('file')
        if uploaded_file is None:
            model = genai.GenerativeModel('gemini-pro')
            chat = model .start_chat(history=[])
            response = chat.send_message(CH)
            context['bot']=response.text
            context['ch']=CH
            return render(request,"test.html",context)
        else:
            vision_model = genai.GenerativeModel('gemini-pro-vision')
            fl=uploaded_file
            fs = FileSystemStorage()
            filename1 = fs.save(fl.name, fl)
            image = PIL.Image.open(filename1)
            response = vision_model.generate_content([CH,image])
            context['bot']=response.text
            context['ch']=CH
            return render(request,"test.html",context)
    return render(request,"test.html")