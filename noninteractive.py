import os
import subprocess
import shutil
import json
import secrets
import string
import urllib.request

# Clear the screen
os.system("clear")

# LEAVE CREDITS
print("""
#######################################################################################
#
#                                  Foxytoux
#
#                           Copyright (C) 2023 - 2024
#
#
#######################################################################################
""")

# Ask the user for the Minecraft server script URL
server_url = input("Please enter the URL of the Minecraft server script (press Enter to use the default URL): ")
server_url = server_url or "https://piston-data.mojang.com/v1/objects/5b868151bd02b41319f54c8d4061b8cae84e665c/server.jar"

# Download the Minecraft server script
urllib.request.urlretrieve(server_url, "server.jar")

# Download openjdk-17-jdk
subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "install", "openjdk-17-jdk", "-y"])

# Ask the user if they accept the Minecraft EULA
eula_acceptance = input("Do you accept the Minecraft EULA? (Type 'yes' or 'y' to accept): ")

# Check if the user accepted the EULA
if eula_acceptance.lower() in ['yes', 'y']:
    # Ask the user for the amount of RAM to allocate
    ram_amount = input("How much RAM would you like to allocate to the Minecraft server (in GB)? ")

    # Modify the Java command with the user's response
    java_command = f"java -Xms{ram_amount}G -Xmx{ram_amount}G -jar server.jar nogui"

    # Launch the Minecraft server
    subprocess.run(java_command, shell=True)

    # Modify the eula.txt file to set 'true'
    with open("eula.txt", "w") as eula_file:
        eula_file.write("eula=true")

    # Restart the Minecraft server with the new configurations
    subprocess.run(java_command, shell=True)
else:
    print("You must accept the Minecraft EULA to proceed. Aborting.")
