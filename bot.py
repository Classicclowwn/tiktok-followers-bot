# Modules
import time
import json

# Load config.json
with open("config.json") as f:
    config = json.load(f)

# Mock classes (since tiktok, proxies, creator, account are not real modules)
class TikTokAccount:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
        self.banned = False
        self.followers = 0
    
    def change_avatar(self, avatar_source):
        print(f"[+] Avatar changed from {avatar_source}")
    
    def sub_to(self, target):
        if not self.banned:
            self.followers += 1
            print(f"[+] Subscribed to {target}. Total followers: {self.followers}")
        else:
            print("[-] Account banned, cannot subscribe.")


# Example usage
def account_creator(email, password, username):
    acc = TikTokAccount(email, password, username)
    acc.change_avatar("RandomPictureNet")
    acc.sub_to("MostFolloweds")
    return acc


def sub_bot(account):
    if account.banned:
        print("[-] Account is banned")
    else:
        account.sub_to(config.get("acc", "default_account"))


# Demo
if __name__ == "__main__":
    # Replace with values from config.json
    email = "test@example.com"
    password = "mypassword"
    username = "myuser"

    acc = account_creator(email, password, username)
    sub_bot(acc)
