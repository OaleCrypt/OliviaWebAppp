from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re 
from .utils import view_passwords, add_password

@csrf_exempt
def password_terminal(request):
    if request.method == 'POST':
        command = json.loads(request.body).get('command', '').strip()
        current_step = request.session.get('step', 'welcome')

        if current_step == 'welcome':
            request.session['step'] = 'username'
            output = (
                "Welcome to the Password Manager Terminal!\n"
                "This is just a project to showcase password encryptions.\n"
                "Follow the instructions to begin ....\n"
                "Enter a username:"
            )
        elif current_step == 'username':
            if re.match("^[A-Za-z0-9]+$", command):  # Username must be letters and/or numbers
                request.session['username'] = command
                request.session['step'] = 'password'
                output = f"Username entered: {command}\nEnter a password:"
            else:
                output = "Please enter a valid username (letters and numbers only):"
        elif current_step == 'password':
            if command:
                request.session['password'] = command
                add_password(request.session['username'], command)
                request.session['step'] = 'command'
                output = (
                    f"Password entered for {request.session['username']}.\n"
                    "Do you want to view your encrypted password, add a new username & password, or exit?"
                )
            else:
                output = "Please enter a valid password:"
        elif current_step == 'command':
            if command.lower() == 'view':
                passwords = view_passwords(request.session['username'])
                if passwords:
                    output = "\n".join([f"{user}: {pwd}" for user, pwd in passwords])
                else:
                    output = "No passwords found for this user."
                output += "\nDo you want to view your encrypted password, add a new username & password, or exit?"
            elif command.lower() == 'add':
                request.session['step'] = 'username'
                request.session['username'] = ''
                request.session['password'] = ''
                output = "Enter a new username:"
            elif command.lower() == 'exit':
                request.session.flush()
                output = "Session ended. Thank you for using the Password Manager Terminal!"
            else:
                output = "Unknown command. Please enter view, add, or exit."
        else:
            output = "Invalid state. Restarting session."
            request.session.flush()
            request.session['step'] = 'welcome'

        return JsonResponse({'output': output})

    return render(request, 'password_manager/terminal.html')
