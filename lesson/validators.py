import os
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect,redirect


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')




def validate_document_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.docx','.doc','.xml','.xlsx','.rar']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg','.png','.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
