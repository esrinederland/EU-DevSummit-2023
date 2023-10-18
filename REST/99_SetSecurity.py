import keyring
import Settings

print("Setting password for: {}")
pwd = input("Enter the password:")

keyring.set_password(Settings.KeyringKeyword, Settings.Username, pwd)
print(f"Successfully saved password for {Settings.Username}") 
