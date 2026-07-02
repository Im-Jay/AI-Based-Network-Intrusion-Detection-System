import socket
import time
try:
    from scapy.all import IP, TCP, send
except ImportError:
    print("scapy is not installed. Please run 'pip install scapy'")
    exit()

# Instead of targeting our own machine, we target an external IP (Google) 
# so the packets are forced to travel OUT of the Wi-Fi adapter where Npcap can capture them!
target_ip = "8.8.8.8"

print(f"Targeting External Machine: {target_ip} to force packets through Wi-Fi...")
print("Starting simulated DoS Flood Attack...")

# Create a packet pointing out to the internet
malicious_packet = IP(dst=target_ip) / TCP(dport=80, flags="S")

# Send 40 packets very fast to trigger the Flood Detection!
for i in range(40):
    send(malicious_packet, verbose=False)
    time.sleep(0.2)

print("Simulated Attack Finished! Check your script.py sniffer.")
