#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FSOCIETY SIMULATOR - Mr. Robot inspired security tool simulation
Ninguna herramienta realiza acciones reales, solo efectos visuales.
Uso educativo y de entretenimiento.
"""

import time
import random
import sys
from threading import Thread  # Solo para simular concurrencia en DDoS

# ==================== EFECTOS VISUALES ====================

def type_writer(text, speed=0.002, color=""):
    """Efecto máquina de escribir."""
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def glitch_text(text, times=3):
    """Efecto glitch hacker."""
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    for _ in range(times):
        fake = ''.join(
            random.choice(chars) if c != ' ' else ' '
            for c in text
        )

        sys.stdout.write(f"\r\033[91m{fake}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

    sys.stdout.write(f"\r\033[92m{text}\033[0m\n")
    sys.stdout.flush()

def loading_spinner(duration=2, text="Inicializando"):
    """Spinner animado."""
    spinner = ['|', '/', '-', '\\']
    start = time.time()

    i = 0

    while time.time() - start < duration:
        sys.stdout.write(
            f"\r\033[93m{text} {spinner[i % len(spinner)]}\033[0m"
        )

        sys.stdout.flush()
        time.sleep(0.1)

        i += 1

    print("\r\033[92mSistema listo.          \033[0m")

def matrix_rain(lines=15, width=60):
    """Mini lluvia Matrix."""
    chars = "01アイウエオカサタナハマヤラワ"

    for _ in range(lines):
        line = ''.join(
            random.choice(chars)
            for _ in range(width)
        )

        print(f"\033[92m{line}\033[0m")

        time.sleep(0.03)

# ==================== ICONIC FSOCIETY LOGO ====================
def show_logo():
    print("\033c", end="")  # limpia pantalla

    loading_spinner(2, "Conectando con FSOCIETY")
    
    time.sleep(0.5)

    matrix_rain(8, 70)

    logo = r"""
⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛
⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀⠀⠀
"""

    # Escribe el logo lentamente
    for line in logo.splitlines():
        type_writer(line, speed=0.0008, color="\033[91m")

    print()

    glitch_text("FSOCIETY ACCESS GRANTED")
    
    time.sleep(0.4)

    type_writer("="*60, 0.001, "\033[91m")
    type_writer("Bienvenido al simulador de herramientas FSOCIETY", 0.01, "\033[93m")
    type_writer("Ninguna acción es real. Solo efectos visuales.", 0.01, "\033[91m")
    type_writer("="*60, 0.001, "\033[91m")

    print("\n")
# ==================== FUNCIONES SIMULADAS ====================

def simulate_progress(seconds=2, steps=10, description="Procesando"):
    """Barra de progreso simulada."""
    print(f"\033[94m{description}:\033[0m")
    for i in range(steps + 1):
        percent = i * 100 // steps
        bar = "#" * i + "-" * (steps - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(seconds / steps)
    print("\n\033[92mCompletado.\033[0m\n")
    time.sleep(0.5)

def fake_scan_output(target, open_ports=None):
    """Simula salida de escaneo."""
    if open_ports is None:
        open_ports = [22, 80, 443, 8080]
    print(f"\033[96m[+] Escaneando objetivo: {target}\033[0m")
    for port in open_ports:
        time.sleep(random.uniform(0.2, 0.5))
        print(f"\033[92m    Puerto {port}: ABIERTO\033[0m")
    print("\n")

# ==================== HERRAMIENTAS (24 simulaciones) ====================

def tool_password_breaker():
    print("\n\033[91m[Password Breaker Simulado]\033[0m")
    target = input("Ingrese objetivo (ej. usuario@dominio): ")
    print(f"\033[93mIniciando ataque de diccionario contra {target}...\033[0m")
    simulate_progress(2, 15, "Probando combinaciones")
    passwords = ["123456", "password", "admin", "root", "letmein"]
    found = random.choice([True, False])
    if found:
        pwd = random.choice(passwords)
        print(f"\033[92m¡Contraseña encontrada! -> {pwd}\033[0m")
    else:
        print("\033[91mNo se encontró contraseña en el diccionario.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_brute_force():
    print("\n\033[91m[Brute Force Simulado]\033[0m")
    target = input("Ingrese objetivo (IP/URL): ")
    print(f"\033[93mIniciando fuerza bruta contra {target}...\033[0m")
    simulate_progress(3, 20, "Probando todas las combinaciones")
    success = random.choice([True, False])
    if success:
        print("\033[92mAcceso concedido. Credenciales: admin/rockyou\033[0m")
    else:
        print("\033[91mFallo: límite de intentos alcanzado.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_ddos():
    print("\n\033[91m[DDoS Attack Simulado]\033[0m")
    target = input("Ingrese IP/URL objetivo: ")
    print(f"\033[93mLanzando DDoS contra {target}...\033[0m")
    print("\033[93mCreando hilos zombies... (simulación)\033[0m")
    for i in range(5):
        print(f"\033[91mEnviando paquetes desde zombie {i+1}...\033[0m")
        time.sleep(0.3)
    simulate_progress(2, 10, "Saturando objetivo")
    print("\033[92mAtaque completado (simulado). El servidor no sufrió daño real.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_ip_scanner():
    print("\n\033[91m[IP Scanner Simulado]\033[0m")
    subnet = input("Ingrese red (ej. 192.168.1.0/24): ")
    print(f"\033[93mEscaneando {subnet}...\033[0m")
    hosts = [f"192.168.1.{i}" for i in range(1, 255, 30)]  # Muestra algunos
    for ip in hosts:
        time.sleep(0.2)
        print(f"\033[92mHost activo: {ip}\033[0m")
    print("\033[93mEscaneo finalizado.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_port_scanner():
    print("\n\033[91m[Port Scanner Simulado]\033[0m")
    target = input("Ingrese IP objetivo: ")
    fake_scan_output(target, [21, 22, 23, 80, 443, 3306, 8080])
    input("\nPresione Enter para continuar...")

def tool_wifi_deauth():
    print("\n\033[91m[WiFi Deauth Simulado]\033[0m")
    ssid = input("Nombre de red WiFi objetivo: ")
    print(f"\033[93mDesautenticando clientes de {ssid}...\033[0m")
    simulate_progress(1.5, 8, "Enviando paquetes de deauth")
    print("\033[92mAtaque de deauth simulado. Ningún cliente fue afectado realmente.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_keylogger():
    print("\n\033[91m[Keylogger Simulado]\033[0m")
    print("\033[93mSimulando captura de teclas en segundo plano...\033[0m")
    simulate_progress(1, 5, "Registrando pulsaciones (demo)")
    print("\033[92mTeclas capturadas (simulación): 'secreto', 'password123'...\033[0m")
    print("\033[91m[!] Esto es solo una demo, no se registró nada real.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_ransomware():
    print("\n\033[91m[Ransomware Simulado]\033[0m")
    print("\033[93mCifrando archivos en /Documentos (simulación)...\033[0m")
    simulate_progress(3, 15, "Encriptando datos")
    print("\033[92m(Simulación) Archivos encriptados. Clave de rescate: 1234-FSOC-5678\033[0m")
    print("\033[93mNingún archivo real fue modificado.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_exploit_finder():
    print("\n\033[91m[Exploit Finder]\033[0m")
    target = input("Ingrese IP/dominio: ")
    print(f"\033[93mBuscando vulnerabilidades conocidas en {target}...\033[0m")
    exploits = ["CVE-2024-1234 (RCE)", "CVE-2023-5678 (SQLi)", "CVE-2025-0001 (LFI)"]
    for e in exploits:
        time.sleep(0.8)
        print(f"\033[91m[+] Posible exploit: {e}\033[0m")
    print("\033[92mEscaneo completado.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_reverse_shell():
    print("\n\033[91m[Reverse Shell Simulado]\033[0m")
    lhost = input("LHOST (tu IP): ")
    lport = input("LPORT: ")
    print(f"\033[93mGenerando payload para conectar a {lhost}:{lport}...\033[0m")
    simulate_progress(1, 8, "Estableciendo conexión inversa")
    print("\033[92mConexión inversa establecida (simulada). Shell interactiva fake.\033[0m")
    print("\033[93mPara salir escriba 'exit'.\033[0m")
    # Simular shell simple
    while True:
        cmd = input("shell> ")
        if cmd.lower() == "exit":
            break
        print(f"\033[90mComando '{cmd}' ejecutado (simulación)\033[0m")
    input("\nPresione Enter para continuar...")

def tool_packet_sniffer():
    print("\n\033[91m[Packet Sniffer Simulado]\033[0m")
    interface = input("Interfaz de red (ej. eth0): ")
    print(f"\033[93mCapturando paquetes en {interface}... (Ctrl+C para detener)\033[0m")
    for i in range(5):
        time.sleep(0.5)
        src = f"192.168.1.{random.randint(2,254)}"
        dst = f"10.0.0.{random.randint(1,254)}"
        print(f"\033[92m{src}:{random.randint(1024,65535)} -> {dst}:80 [TCP]\033[0m")
    print("\033[93mCaptura detenida.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_arp_spoof():
    print("\n\033[91m[ARP Spoof Simulado]\033[0m")
    target = input("IP víctima: ")
    gateway = input("IP gateway: ")
    print(f"\033[93mEnvenenando ARP: {target} <-> {gateway} ...\033[0m")
    simulate_progress(2, 10, "Redirigiendo tráfico")
    print("\033[92mAtaque MITM iniciado (simulado). Los paquetes no fueron interceptados realmente.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_hash_cracker():
    print("\n\033[91m[Hash Cracker Simulado]\033[0m")
    hash_type = input("Tipo de hash (MD5, SHA1): ")
    hash_value = input("Hash a crackear: ")
    print(f"\033[93mRompiendo {hash_type}:{hash_value} con rainbow tables...\033[0m")
    simulate_progress(2.5, 12, "Probando hashes")
    cracked = random.choice(["password123", "admin", "qwerty"])
    print(f"\033[92mHash crackeado: {cracked}\033[0m")
    input("\nPresione Enter para continuar...")

def tool_steganography():
    print("\n\033[91m[Steganography Tool]\033[0m")
    print("1. Ocultar mensaje en imagen")
    print("2. Extraer mensaje de imagen")
    op = input("Seleccione: ")
    if op == "1":
        img = input("Imagen portadora: ")
        msg = input("Mensaje secreto: ")
        print(f"\033[93mOcultando '{msg}' en {img}...\033[0m")
        simulate_progress(1, 6, "Codificando")
        print("\033[92mMensaje oculto exitosamente (simulado).\033[0m")
    else:
        img = input("Imagen con mensaje oculto: ")
        print(f"\033[93mExtrayendo datos de {img}...\033[0m")
        simulate_progress(1, 5, "Decodificando")
        print("\033[92mMensaje extraído: 'Este es un mensaje secreto simulado'\033[0m")
    input("\nPresione Enter para continuar...")

def tool_network_mapper():
    print("\n\033[91m[Network Mapper]\033[0m")
    target = input("Rango IP (ej. 192.168.1.0/24): ")
    print(f"\033[93mMapeando red {target}...\033[0m")
    fake_scan_output(target, [22, 80, 445, 3389])
    print("\033[92mTopología de red simulada.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_vuln_scanner():
    print("\n\033[91m[Vulnerability Scanner]\033[0m")
    target = input("URL/IP: ")
    print(f"\033[93mAnalizando {target} en busca de CVEs...\033[0m")
    vulns = ["CVE-2021-44228 (Log4Shell)", "CVE-2017-0144 (EternalBlue)", "CVE-2019-0708 (BlueKeep)"]
    for v in vulns:
        time.sleep(0.7)
        print(f"\033[91m[CRÍTICA] {v}\033[0m")
    print("\033[93mSe encontraron 3 vulnerabilidades críticas (simulación).\033[0m")
    input("\nPresione Enter para continuar...")

def tool_log_cleaner():
    print("\n\033[91m[Log Cleaner]\033[0m")
    target = input("Ruta de logs (ej. /var/log/auth.log): ")
    print(f"\033[93mLimpiando evidencia en {target}...\033[0m")
    simulate_progress(1.2, 10, "Eliminando entradas sospechosas")
    print("\033[92mLogs limpiados correctamente (simulado).\033[0m")
    input("\nPresione Enter para continuar...")

def tool_backdoor_creator():
    print("\n\033[91m[Backdoor Creator]\033[0m")
    port = input("Puerto de escucha: ")
    print(f"\033[93mGenerando backdoor en puerto {port}...\033[0m")
    simulate_progress(2, 8, "Compilando payload")
    print("\033[92mBackdoor creado: backdoor.exe (no funcional, solo simulación)\033[0m")
    input("\nPresione Enter para continuar...")

def tool_rootkit_installer():
    print("\n\033[91m[Rootkit Installer Simulado]\033[0m")
    print("\033[93mInstalando rootkit en el sistema...\033[0m")
    simulate_progress(2, 12, "Ocultando procesos")
    print("\033[92mRootkit instalado (simulado). El sistema sigue limpio.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_mitm():
    print("\n\033[91m[Man-in-the-Middle Simulado]\033[0m")
    victim = input("IP víctima: ")
    print(f"\033[93mInterceptando tráfico entre {victim} y gateway...\033[0m")
    simulate_progress(2, 8, "Capturando paquetes")
    print("\033[92mContraseñas capturadas (simulación): user=admin, pass=12345\033[0m")
    input("\nPresione Enter para continuar...")

def tool_honeypot():
    print("\n\033[91m[Honeypot Creator]\033[0m")
    port = input("Puerto a simular (ej. 22): ")
    print(f"\033[93mCreando honeypot en puerto {port}...\033[0m")
    simulate_progress(1, 6, "Configurando señuelo")
    print("\033[92mHoneypot activo. Se registrarán intentos de conexión (simulado).\033[0m")
    input("\nPresione Enter para continuar...")

def tool_payload_generator():
    print("\n\033[91m[Payload Generator]\033[0m")
    lhost = input("LHOST: ")
    lport = input("LPORT: ")
    print(f"\033[93mGenerando payload reverse shell para {lhost}:{lport}...\033[0m")
    simulate_progress(1.5, 7, "Ofuscando código")
    print("\033[92mPayload generado (simulación): python -c 'import socket;...'\033[0m")
    input("\nPresione Enter para continuar...")

def tool_social_engineering():
    print("\n\033[91m[Social Engineering Toolkit]\033[0m")
    print("1. Clonación de página de login")
    print("2. Generador de phishing")
    op = input("Seleccione: ")
    if op == "1":
        url = input("URL a clonar: ")
        print(f"\033[93mClonando {url}...\033[0m")
    else:
        print("\033[93mGenerando correo falso de phishing...\033[0m")
    simulate_progress(2, 10, "Creando señuelo")
    print("\033[92mAtaque de ingeniería social simulado. No se envió ningún correo.\033[0m")
    input("\nPresione Enter para continuar...")

def tool_crypto_miner():
    print("\n\033[91m[Crypto Miner Simulado]\033[0m")
    print("\033[93mIniciando minero de Monero (simulación)...\033[0m")
    simulate_progress(3, 15, "Minando bloques")
    print("\033[92mHashrate: 12.5 KH/s (simulado). No se minó ninguna criptomoneda real.\033[0m")
    input("\nPresione Enter para continuar...")

# ==================== MENÚ PRINCIPAL ====================

def main():
    while True:
        show_logo()
        print("\033[96m" + "="*50 + "\033[0m")
        print("\033[93m[ MENÚ FSOCIETY - SIMULACIÓN ]\033[0m")
        print("\033[96m" + "="*50 + "\033[0m")
        print("1. Password Breaker (Ataque diccionario)")
        print("2. Brute Force (Fuerza bruta)")
        print("3. DDoS Attack (Ataque de denegación)")
        print("4. IP Scanner (Escáner de hosts)")
        print("5. Port Scanner")
        print("6. WiFi Deauth Simulator")
        print("7. Keylogger Simulator")
        print("8. Ransomware Simulator")
        print("9. Exploit Finder")
        print("10. Reverse Shell Simulator")
        print("11. Packet Sniffer")
        print("12. ARP Spoof Simulator")
        print("13. Hash Cracker")
        print("14. Steganography Tool")
        print("15. Network Mapper")
        print("16. Vulnerability Scanner")
        print("17. Log Cleaner")
        print("18. Backdoor Creator")
        print("19. Rootkit Installer")
        print("20. MITM Simulator")
        print("21. Honeypot Creator")
        print("22. Payload Generator")
        print("23. Social Engineering Toolkit")
        print("24. Crypto Miner Simulator")
        print("0. Salir")
        print("\033[96m" + "="*50 + "\033[0m")
        
        choice = input("\033[93mSeleccione una herramienta [0-24]: \033[0m")
        
        if choice == "0":
            print("\033[91mSaliendo de FSOCIETY... Hasta luego, hacker.\033[0m")
            sys.exit(0)
        elif choice == "1":
            tool_password_breaker()
        elif choice == "2":
            tool_brute_force()
        elif choice == "3":
            tool_ddos()
        elif choice == "4":
            tool_ip_scanner()
        elif choice == "5":
            tool_port_scanner()
        elif choice == "6":
            tool_wifi_deauth()
        elif choice == "7":
            tool_keylogger()
        elif choice == "8":
            tool_ransomware()
        elif choice == "9":
            tool_exploit_finder()
        elif choice == "10":
            tool_reverse_shell()
        elif choice == "11":
            tool_packet_sniffer()
        elif choice == "12":
            tool_arp_spoof()
        elif choice == "13":
            tool_hash_cracker()
        elif choice == "14":
            tool_steganography()
        elif choice == "15":
            tool_network_mapper()
        elif choice == "16":
            tool_vuln_scanner()
        elif choice == "17":
            tool_log_cleaner()
        elif choice == "18":
            tool_backdoor_creator()
        elif choice == "19":
            tool_rootkit_installer()
        elif choice == "20":
            tool_mitm()
        elif choice == "21":
            tool_honeypot()
        elif choice == "22":
            tool_payload_generator()
        elif choice == "23":
            tool_social_engineering()
        elif choice == "24":
            tool_crypto_miner()
        else:
            print("\033[91mOpción inválida. Presione Enter para continuar.\033[0m")
            input()
        
        # Limpiar pantalla opcional
        print("\033c", end="")  # Limpia consola (ANSI)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91mInterrupción detectada. Saliendo...\033[0m")
        sys.exit(0)
