from django.http import JsonResponse

def greetings(request) -> str:
    message = 'Hello' + ' ' + 'Tanvir'
    return JsonResponse({'message': message})
    