# THIS CODE IS BY Adko5558
# Works for "Boffin IV Coding" and "Elenco Snap Circuits; Explore Coding"


import asyncio
from bleak import BleakClient

ADDRESS = "A1:5F:2C:03:F4:90"  # Replace with address of device
WRITE_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"  # Replace with UUID

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

async def main():
    command = "AT+PIO71"
    async with BleakClient(ADDRESS) as client:
#        await send_command(client, command, show_output=True)

        await send_command(client, "AT+PIO71", show_output=True)
        await send_command(client, "AT+PIO41", show_output=True)
        await send_command(client, "AT+PIO21", show_output=True)


        # while True:
            # await asyncio.sleep(5)
            # await send_command(client, "AT+KEEPCONECTION", show_output=False) # This command do nothing, it's just for keeping connection alive between pc and device

asyncio.run(main())



# COMMANDS:
#  AT+PIO71   ----> LEFT WHEELS     ||  Goes RIGHT
#  AT+PIO41   ----> RIGHT WHEELS    ||  Goes LEFT
#  AT+PIO21   ----> 'A' BUTTON      ||  Turns ON/OFF the output
