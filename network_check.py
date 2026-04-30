import os
import platform

def security_scan_simulation(target):
    print(f"--- BabiEat Network Security Audit ---")
    print(f"Targeting Server: {target}")
    
    
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {target}"
    
    print(f"Action: Sending a 'Security Ping' to ensure server availability...")
    response = os.system(command)
    
    if response == 0:
        print(f"Result: Server is UP. Path is clear for secure data.")
    else:
        print(f"Result: Server is DOWN or Blocking Pings. Potential security shield active.")
    
    
    print("\nAction: Identifying standard secure ports...")
    secure_ports = {
        80: "HTTP (Insecure - Should be redirected)",
        443: "HTTPS (Secure - BabiEat Standard)",
        22: "SSH (Management - Must be restricted)"
    }
    
    for port, description in secure_ports.items():
        print(f"Checking Port {port}: {description}")
    
    print("---------------------------------------")

if __name__ == "__main__":
    
    security_scan_simulation("8.8.8.8")