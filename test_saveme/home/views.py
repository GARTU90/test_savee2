from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RespuestaForm
from . import procesador  # importa tu archivo
import json

def index(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save()

            # Llamar al analizador de texto con la descripción ingresada
            resultados = procesador.procesar_respuesta(
                respuesta.seguro,
                respuesta.problema
            )

            return render(request, 'gracias.html', {
                'resultados': resultados,
                'nombre_seguro': respuesta.seguro,
                'descripcion': respuesta.problema,
            })
    else:
        form = RespuestaForm()
    return render(request, 'index.html', {'form': form})


# 🆕 View que recibe los resultados de Denue desde el JS
@csrf_exempt
def procesar_datos_denue(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)

            # ✅ Puedes imprimir o guardar o procesar
            print("✅ Datos Denue recibidos:")
            for i, est in enumerate(datos):
                print(f"[{i+1}] {est.get('Nombre')} - {est.get('Clase_actividad')}")

            # 🔥 Llama a tu procesador si quieres
            resultado_clasificado = procesador.procesar_datos_denue(datos)


            return JsonResponse({'estado': 'ok', 'mensaje': 'Procesado correctamente'})
        except Exception as e:
            print("❌ Error:", e)
            return JsonResponse({'estado': 'error', 'mensaje': str(e)}, status=400)
    else:
        return JsonResponse({'estado': 'error', 'mensaje': 'Método no permitido'}, status=405)
