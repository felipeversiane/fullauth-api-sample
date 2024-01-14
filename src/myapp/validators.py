import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone
import re
from django.core.exceptions import ValidationError

#Regex 
PHONE_REGEX = r"^\d{11}$"
ZIPCODE_REGEX = r"^\d{5}-\d{3}$"
DATE_REGEX = r'(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$'

MAX_SIZE_AUDIO = 20000000 
MAX_SIZE_IMAGE = 10000000

def validate_first_letter(str):    
    if str[0].isdigit():        
        raise ValidationError(_("First letter cannot be a number."))

def validate_letters(name):    
    if not re.match(r'^[A-Za-z ]+$', name):      
        raise ValidationError(_("Only letters and spaces allowed."))
        
def validate_phone(phone):
    if not re.match(PHONE_REGEX, phone):
        raise ValidationError(_("Invalid phone number format.")) 

def validate_value(value):
    if value <= 0:
        raise ValidationError(_("Value must be positive."))
        
def validate_date(date): 
    if date < timezone.now().date():  
        raise ValidationError(_("Invalid date."))
        
def validate_time(time):       
    if time < timezone.now().time():   
        raise ValidationError(_("Invalid time."))   

def validate_zipcode(zipcode):    
    if not re.match(ZIPCODE_REGEX, zipcode):    
        raise ValidationError(_("Invalid zipcode format."))
    
def validate_audio_file(value):
    import os
    ext = os.path.splitext(value.name)[1]  
    if not ext.lower() in ['.wav','.mp3','.ogg']:
        raise ValidationError(_("Only audio files are allowed."))
    

def validate_size_audio(value):
    ...
    filesize = value.file.size
    if filesize > MAX_SIZE_AUDIO:
        raise ValidationError(_("File too large. Maximum size is 20MB."))
    
def validate_size_image(value):
    ...
    filesize = value.file.size
    if filesize > MAX_SIZE_IMAGE:
        raise ValidationError(_("File too large. Maximum size is 20MB."))
    
def validate_birth_date(value):
    if not re.match(DATE_REGEX, value):
         raise ValidationError(_("Invalid date of birth."))