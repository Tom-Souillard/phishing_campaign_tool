from scapy.all import send, IP, TCP
from typing import Any


def send_phishing_packet(target_ip: str, target_port: int, payload: str) -> None:
    """Send a phishing packet to a target IP and port using Scapy.

    Args:
        target_ip (str): The target IP address.
        target_port (int): The target port number.
        payload (str): The payload to send.
    """
    packet = IP(dst=target_ip) / TCP(dport=target_port) / payload
    send(packet)
    print(f"Phishing packet sent to {target_ip}:{target_port}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python scapy_phishing.py <target_ip> <target_port> <payload>")
    else:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
        payload = sys.argv[3]

        send_phishing_packet(target_ip, target_port, payload)
