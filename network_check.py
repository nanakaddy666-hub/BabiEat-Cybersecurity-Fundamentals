

import os
import platform
import subprocess

def ping_server(ip_address):
    """
    Sends a ping to check if a server is alive.
    This is NOT a real security tool — just for learning availability.
    """
    print(f"\n[1] Checking if server {ip_address} is alive...")
    
   
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip_address]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"    ✅ Server {ip_address} is UP (responded to ping)")
            return True
        else:
            print(f"    ❌ Server {ip_address} is DOWN or blocking pings")
            return False
    except:
        print(f"    ❌ Timeout — server {ip_address} did not respond")
        return False

def explain_babieat_ports():
    """
    Lists which ports BabiEat should have open or closed.
    """
    print("\n[2] BabiEat Port Security Checklist")
    print("-" * 50)
    
    ports = {
        20: "FTP (Data) — Plain text file transfer",
        21: "FTP (Control) — Also plain text, insecure",
        22: "SSH — Secure remote admin access",
        23: "Telnet — Old, insecure, never use",
        80: "HTTP — Plain text web traffic",
        443: "HTTPS — Encrypted web traffic (BabiEat's main door)",
        3306: "MySQL Database — Should be internal only",
        3389: "RDP — Remote Desktop, high risk if exposed",
    }
    
    for port, description in ports.items():
        if port == 443:
            print(f"    Port {port} ({description[:30]}...) → ✅ SHOULD BE OPEN")
        elif port in [22, 3306]:
            print(f"    Port {port} ({description[:30]}...) → ⚠️ SHOULD BE RESTRICTED")
        else:
            print(f"    Port {port} ({description[:30]}...) → 🔒 SHOULD BE CLOSED")
    
    print("-" * 50)
    print("💡 Why this matters: Every open port is a potential entrance for attackers.")

def simulate_nmap_scan(target="scanme.nmap.org"):
    """
    Simulates what an Nmap scan would show.
    In a real audit, you would run: nmap -p 20,21,22,80,443,3389 <target>
    """
    print(f"\n[3] Simulated Nmap Scan Against: {target}")
    print("-" * 50)
    
    # This is SIMULATED output — based on what Nmap would actually show
    simulated_results = {
        20: "closed",
        21: "closed", 
        22: "open",
        80: "open",
        443: "open",
        3389: "filtered",
    }
    
    print("PORT     STATE    SERVICE")
    print("-----    -----    -------")
    for port, state in simulated_results.items():
        state_symbol = "🟢" if state == "open" else "🔴" if state == "closed" else "🟡"
        print(f"{port}/tcp   {state:<8} {state_symbol}")
    
    print("-" * 50)
    print("🟢 open = Door is unlocked (expected for HTTPS port 443)")
    print("🔴 closed = Door is locked (good)")
    print("🟡 filtered = Firewall is hiding the port (also good)")
    
    print("\n📌 Real Nmap command I would run:")
    print(f'    nmap -p 20,21,22,80,443,3389 {target}')

def think_like_an_attacker():
    """
    Demonstrates the adversarial mindset.
    """
    print("\n[4] Thinking Like an Attacker (Ethically!)")
    print("-" * 50)
    print("If I were attacking BabiEat's servers, I would ask:")
    print("    1. Is port 22 (SSH) open? If yes, can I brute force the password?")
    print("    2. Is port 80 (HTTP) open? If yes, can I intercept plain text traffic?")
    print("    3. Is there a database port (3306, 5432, 27017) exposed to the internet?")
    print("    4. Does the server respond to ping? If yes, it's alive and findable.")
    print("\n✅ That's why BabiEat should run regular Nmap scans on its own infrastructure.")

# ========== RUN THE DEMO ==========
if __name__ == "__main__":
    print("=" * 50)
    print("   BabiEat Network Security Audit")
    print("   Student: Norma")
    print(f"   Date: May 2026")
    print("=" * 50)
    
    # Test with a safe private IP (not a real BabiEat server)
    ping_server("10.0.0.5")
    
    explain_babieat_ports()
    
    simulate_nmap_scan()
    
    think_like_an_attacker()
    
    print("\n" + "=" * 50)
    print("   Audit Complete. Stay secure, BabiEat!")
    print("=" * 50)
