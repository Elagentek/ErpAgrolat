from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  


def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('registro:registro')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('registro:registro')

        user = User.objects.create_user(username=usuario, email=email, password=password)
        user.first_name = nombre
        user.save()

        messages.success(request, "Usuario creado exitosamente. Inicia sesión.", extra_tags='alert-success')
        return redirect('login')  # 🔁 Redirige al login directamente

    return render(request, 'Registro/registro_usuarios.html')
