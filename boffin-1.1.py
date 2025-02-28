# THIS CODE IS BY Adko5558
# Works for "Boffin IV Coding" and "Elenco Snap Circuits; Explore Coding"


import asyncio
import sys
import time
import os
from bleak import BleakClient
import winrt.windows.foundation as wf

ADDRESS = "A1:5F:2C:03:F4:90"  # Replace with address of device
WRITE_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"  # Replace with UUID


# This will clear the console

if os.name == 'nt':  # Windows
    os.system('cls')
else:
    os.system('clear') # Linux/MacOS



ascii_art = """
\033[94m██████╗  ██████╗ ███████╗███████╗██╗███╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔════╝██╔════╝██║████╗  ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║█████╗  █████╗  ██║██╔██╗ ██║    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║     ██║     ██║██║ ╚████║    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[0m
                                                                                                  
"""


async def send_command(client, command, show_output=True):
    if client.is_connected:
        print("Connected to device!")
        await client.write_gatt_char(WRITE_UUID, command.encode())
    if show_output:
        print(f"Command '{command}' sent.")
        await asyncio.sleep(1)  # some time, so the device can't miss the signal
        response = await client.read_gatt_char(WRITE_UUID)
        print(f"Response from device (raw): {response}")
        print(f"Response from device (hex): {' '.join(f'{byte:02X}' for byte in response)}")

async def control_car(command):
    async with BleakClient(ADDRESS) as client:
        await send_command(client, command, show_output=True)

async def main():
    print(ascii_art)
    print("\033[91m Type '1' to go forward. Type '2' to simulate pressing A button. Type '3' to go Right. Type '4' to go Left. Type 'exit' to stop the process and quit.")
    user_input = input("Enter your choice (1, 2, 3, 4 or exit): ")
    
    async with BleakClient(ADDRESS) as client:
        
        
        if user_input == '1':
            await send_command(client, "AT+PIO71", show_output=True)
            await send_command(client, "AT+PIO41", show_output=True)
        
        
        elif user_input == '2':
                await send_command(client, "AT+PIO21", show_output=True)
                while True:
                    await asyncio.sleep(5)
                    await send_command(client, "AT+KEEPCONECTION", show_output=False) # This command does nothing, it's just for keeping connection alive between pc and device
                    
        
        elif user_input == '3':
                    await send_command(client, "AT+PIO71", show_output=True)

        elif user_input == '4':
                    await send_command(client, "AT+PIO41", show_output=True)
        elif user_input == 'exit':

            if os.name == 'nt':  # Windows
                os.system('cls')
            else:
                os.system('clear') # Linux/MacOS

            def loading(duration=5):
                loading_chars = ["|", "/", "-", "\\"]  
                start_time = time.time()
                sys.stdout.write("\033[93mClosing, do not quit process manually... ")  
                sys.stdout.flush()
                while time.time() - start_time < duration:
                    for char in loading_chars:
                        if time.time() - start_time >= duration:  
                            break
                        sys.stdout.write(f"\r\033[93mClosing, do not quit process manually... {char} ")  
                        sys.stdout.flush()  
                        time.sleep(0.2)
                sys.stdout.write("\033[93m\nDone with exit code: 1\n")  
                sys.stdout.flush()  # flush after writing to ensure it's displayed on a new line
            loading(5)
            print("\033[0mThank you for using our program :D")
            sys.exit()
        else:
            print("\033[93mInvalid input. Please enter 1, 2, 3, 4 or exit.")

if __name__ == "__main__":
    asyncio.run(main())



# COMMANDS:
#  AT+PIO71   ----> LEFT WHEELS     ||  Goes RIGHT
#  AT+PIO41   ----> RIGHT WHEELS    ||  Goes LEFT
#  AT+PIO21   ----> 'A' BUTTON      ||  Turns ON/OFF the output