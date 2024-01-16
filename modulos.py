
from mensajes import messageFormatter

print(messageFormatter("Error: Este mensaje es de error", "error"))

print(messageFormatter("Error: Este mensaje es de éxito", "success"))

print(messageFormatter("Error: Este mensaje es una advertencia", "warning"))

print(messageFormatter("Error: Este mensaje es informativo", "info"))

import mensajes
print(dir(mensajes))