from Mensajes.formatter import messageFormatter

print(messageFormatter("Error: Este mensaje es de error", "error"))
print()
print(messageFormatter("Éxito: Este mensaje es de éxito", "success"))
print()
print(messageFormatter("Advertencia: Este mensaje es una advertencia", "warning"))
print()
print(messageFormatter("Información: Este mensaje es informativo", "info"))

#Para ver las funciones disponibles que tiene el archivo mensajes.py
import Mensajes.formatter as formatter
print(dir(formatter))

import builtins
print(dir(builtins))