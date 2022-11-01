################### INFORMACION (EDITA ESTO) #########################
lista_canales = ["id1", "id2"] #las ids de los canales de spam, puedes agregar infinitas usando una , y las ids entre comillas.

mensaje = """
""" # aqui va la plantilla de tu servidor, la que se enviara a los canales.

token = "" #el token de tu cuenta, ten cuidado con este, tu token no se usara para otra cosa mas que para el proposito de la herramienta
#evita compartir el codigo con tu token ya añadido o mostrar el codigo.

################## CODIGO (NO EDITAR) #########################

import discum   
import time  
from colorama import Fore
bot = discum.Client(token=token, log=False)

print("""
8888888b.  d8b                                       888 8888888b.           888      888 d8b          
888  "Y88b Y8P                                       888 888   Y88b          888      888 Y8P          
888    888                                           888 888    888          888      888              
888    888 888 .d8888b   .d8888b .d88b.  888d888 .d88888 888   d88P 888  888 88888b.  888 888  .d8888b 
888    888 888 88K      d88P"   d88""88b 888P"  d88" 888 8888888P"  888  888 888 "88b 888 888 d88P"    
888    888 888 "Y8888b. 888     888  888 888    888  888 888        888  888 888  888 888 888 888      
888  .d88P 888      X88 Y88b.   Y88..88P 888    Y88b 888 888        Y88b 888 888 d88P 888 888 Y88b.    
8888888P"  888  88888P'  "Y8888P "Y88P"  888     "Y88888 888         "Y88888 88888P"  888 888  "Y8888P 
""")
print("""\n
|                                                                                                   |
|         Envia tu servidor en servidores de spam facilmente y sin parecer un bot!                  |
|         Puedes seguir usando tu cuenta y dejar en segundo plano el proceso                        |
|         Desarrollado por: Katast666                                                               |
|                                                                                                   |
""")
print(Fore.RED + "\nUSALO BAJO TU PROPIO RIESGO" + Fore.WHITE)

@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:
        print(f"Cliente {Fore.RED}(DISCORD_PUBLIC){Fore.WHITE} iniciado en el token dado.")
        time.sleep(3)
        while True:
            print("Publicando Servidores.")
            for canal in lista_canales:
                try:
                    bot.sendMessage(canal, mensaje)
                    print(f"    [ {Fore.GREEN}ENVIADO{Fore.WHITE} ] " + canal)
                except:
                    print(f"    [ {Fore.RED}NO ENVIADO{Fore.WHITE} ] " + canal)
                time.sleep(0.5)
            print("Los mensajes se volveran a enviar en 2400s (40min)")
            time.sleep(2400)


        
try:
    bot.gateway.run(auto_reconnect=True)
except:
    print(f"[ {Fore.RED}ERROR{Fore.WHITE} ] El token que especificaste es invalido o fue destruido por discord.")