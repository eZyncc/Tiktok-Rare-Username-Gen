try:
    from pystyle import Colors, System, Colorate, Center
    import requests
    import time
    import randomword
    import json
except ImportError:
    print("Error, run 'modules.bat' in the 'install' case.")
System.Title("[ Rare Username Generator ] - [ PATCH ] - [ v2.0 ]")
banner = """

                                         ▄████████    ▄████████    ▄████████    ▄████████ 
                                        ███    ███   ███    ███   ███    ███   ███    ███ 
                                        ███    ███   ███    ███   ███    ███   ███    █▀  
                                        ▄███▄▄▄▄██▀   ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
                                        ▀▀███▀▀▀▀▀   ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
                                        ▀███████████   ███    ███ ▀███████████   ███    █▄  
                                          ███    ███   ███    ███   ███    ███   ███    ███ 
                                          ███    ███   ███    █▀    ███    ███   ██████████ 
                                          ███    ███                ███    ███              


"""
input(Center.XCenter("""


> """))
System.Clear()
print(Colorate.Vertical(Colors.cyan_to_blue, banner))
print(f"                                          [{Colors.cyan}!{Colors.reset}] Checking if https://tiktok.com is online...")
time.sleep(0.5)
url = "https://tiktok.com/"
re = requests.get(url)
if re.status_code == 200:
    print(f"                                          [{Colors.cyan}!{Colors.reset}] {url} is online !")
    pass
else:
    input(f"                                          [{Colors.cyan}!{Colors.reset}] {url} is offline, check your connection or check if tiktok is accesible.")
    quit()
print(f"                                          [{Colors.cyan}!{Colors.reset}] Recovering Data...")
time.sleep(1)
with open("config.json") as f:
    config = json.load(f)
f1 = config.get('valid_username_file')
f2 = config.get('invalid_username_file')
f.close()
file1 = open(f1, 'a')
file2 = open(f2, 'a')
print(f"                                          [{Colors.cyan}!{Colors.reset}] Done !")
while True:
    try:
        w = randomword.get_random_word()
        url = f"https://tiktok.com/@{w}"
        r = requests.get(url)
        if r.status_code == 200 or 302:
            print(f"                                          [{Colors.cyan}!{Colors.reset}] :( -> {w} has already been taken.")
            file2.write(w + "\n")
        elif r.status_code == 404:
            print(f"                                          [{Colors.cyan}!{Colors.reset}] :) -> {w} was not taken !")
            file1.write(w + "\n")
        else:
            print(r.status_code)
    except KeyboardInterrupt:
        file1.close()
        file2.close()
        input(f"                                          [{Colors.cyan}!{Colors.reset}] Checking stoped ! All saved in '{f1}' and '{f2}'")
        quit()