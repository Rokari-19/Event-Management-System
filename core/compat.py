
import json  

from django.contrib.auth import get_user_model
User = get_user_model()  

from django.utils.encoding import smart_str 


from django.utils.encoding import force_bytes as force_bytes_or_smart_bytes
