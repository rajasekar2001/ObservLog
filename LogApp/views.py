import json
from django.http import JsonResponse
from django.conf import settings
import os

def process_log_files(request):
    log_file_path = os.path.join(settings.BASE_DIR, 'LogApp', 'static', 'data', 'D:\\PYTHON\\ObservLog\\LogApp\\static\\data\\log.json')
    
    try:
        with open(log_file_path, 'r') as file:
            log_data = json.load(file)
        next_file_name = log_data.get('next_file', 'D:\\PYTHON\\ObservLog\\LogApp\\static\\data\\logDTO.json')
        next_file_path = os.path.join(settings.BASE_DIR, 'LogApp', 'static', 'data', next_file_name)
        
        # Open and read the next file
        with open(next_file_path, 'r') as file:
            next_file_data = json.load(file)
        
        # Return the contents of the next file as a JsonResponse
        return JsonResponse(next_file_data)
    
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except KeyError:
        return JsonResponse({'error': 'Expected data not found in log.json'}, status=500)

