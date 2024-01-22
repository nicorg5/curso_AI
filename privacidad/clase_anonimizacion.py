# Librerías a importar
import hashlib
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class AnonimizadorCifrador():
    def __init__(self):
        load_dotenv()
        self.salt = os.environ.get("SALT").encode()
        self.clave_fernet = Fernet.generate_key()
        self.clave_publica, self.clave_privada = self.generar_par_claves()


    def hash_nombre_apellido(self, nombre, apellido):
        # Concatenar nombre y apellido
        nombre_completo = nombre + " " + apellido
        # Codificar el nombre completo para prepararlo para el hashing 
        nombre_completo_codificado = nombre_completo.encode()
        # Crear el hash usando SHA-256
        hash_objeto = hashlib.sha256(nombre_completo_codificado)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_objeto.hexdigest()
        return hash_hex
    
    def hash_md5nombre_apellido(self, nombre, apellido):
        # Concatenar nombre y apellido
        nombre_completo = nombre + " " + apellido
        # Codificar el nombre completo para prepararlo para el hashing 
        nombre_completo_codificado = nombre_completo.encode()
        # md5
        hash_objeto_md5 = hashlib.md5(nombre_completo_codificado)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_objeto_md5.hexdigest()
        return hash_hex
    
    def hash_con_salt(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()
        # Combinar el nombre completo codificado con el salt 
        entrada_con_salt = nombre_completo_codificado + self.salt
        # Crear el hash
        hash_objeto = hashlib.sha256(entrada_con_salt) 
        hash_hex = hash_objeto.hexdigest()
        return hash_hex

    def generar_salt(self, longitud=16):
        # Retorna un salt aleatorio con la longitud especificada 
        return os.urandom(longitud) 

    def hash_con_salt_aleatoria(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()
        salt = self.generar_salt()
        # Combinar el nombre completo codificado con el salt 
        entrada_con_salt = nombre_completo_codificado + salt
        # Crear el hash
        hash_objeto = hashlib.sha256(entrada_con_salt) 
        hash_hex = hash_objeto.hexdigest()
        return hash_hex     
    
    def cifrar_nombre(self, nombre):
        # Crear una instancia de Fernet con la clave proporcionada 
        f = Fernet(self.clave_fernet)
        # Codificar el nombre y cifrarlo
        nombre_codificado = nombre.encode()
        nombre_cifrado = f.encrypt(nombre_codificado)
        return nombre_cifrado
    
    def descifrar_nombre(self, nombre_cifrado):
        # Crear una instancia de Fernet con la clave proporcionada 
        f = Fernet(self.clave_fernet)
        # Descifrar y decodificar el nombre
        nombre_descifrado = f.decrypt(nombre_cifrado)
        nombre_original = nombre_descifrado.decode()
        return nombre_original
    
    def generar_par_claves(self):
        # Generar una clave privada
        clave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        # Generar la clave pública correspondiente
        clave_publica = clave_privada.public_key()
        return clave_publica, clave_privada
    
    def cifrar_nombre_asimetrico(self, nombre):
        nombre_codificado = nombre.encode()
        nombre_cifrado = self.clave_publica.encrypt(
            nombre_codificado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_cifrado
    
    def descifrar_nombre_asimetrico(self, nombre_cifrado):
        nombre_descifrado = self.clave_privada.decrypt(
            nombre_cifrado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_descifrado.decode()
    

# Ejemplos de uso
anonimizador_cifrador = AnonimizadorCifrador()

#ejemplo de uso de hash_nombre_apellido
hash_nombre_apellido_resultado = anonimizador_cifrador.hash_nombre_apellido("Nicolás", "Rodríguez")
print(f"Hash del nombre y del apellido Nicolás Rodríguez: {hash_nombre_apellido_resultado}")

#ejemplo de uso de hash_md5nombre_apellido
hash_md5nombre_apellido_resultado = anonimizador_cifrador.hash_md5nombre_apellido("Nicolás", "Rodríguez")
print(f"Hash md5 del nombre y del apellido Nicolás Rodríguez: {hash_md5nombre_apellido_resultado}")

#ejemplo de uso de hash_con_salt
hash_con_salt_resultado = anonimizador_cifrador.hash_con_salt("Nicolás", "Rodríguez")
print(f"Hash con salt del nombre y del apellido Nicolás Rodríguez: {hash_con_salt_resultado}")

#ejemplo de uso de hash_con_salt_aleatoria
hash_con_salt_aleatoria_resultado = anonimizador_cifrador.hash_con_salt_aleatoria("Nicolás", "Rodríguez")
print(f"Hash con salt aleatoria del nombre y del apellido Nicolás Rodríguez: {hash_con_salt_aleatoria_resultado}")

#ejemplo de uso de cifrar_nombre
cifrar_nombre_resultado = anonimizador_cifrador.cifrar_nombre("Nicolás")
print(f"El nombre cifrado: {cifrar_nombre_resultado}")

#ejemplo de uso de descifrar_nombre
nombre_original = anonimizador_cifrador.descifrar_nombre(cifrar_nombre_resultado)
print(f"Nombre original descifrado: {nombre_original}")

#ejemplo de uso de cifrar_nombre_asimetrico
cifrar_nombre_asimetrico_resultado = anonimizador_cifrador.cifrar_nombre_asimetrico("Nicolás")
print(f"Nombre cifrado asimétrico: {cifrar_nombre_asimetrico_resultado}")

#ejemplo de uso de descifrar_nombre_asimetrico
descifrar_nombre_asimetrico_resultado = anonimizador_cifrador.descifrar_nombre_asimetrico(cifrar_nombre_asimetrico_resultado)
print(f"Nombre original descifrado asimétrico: {descifrar_nombre_asimetrico_resultado}")