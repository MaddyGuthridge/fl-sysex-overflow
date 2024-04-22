"""
send.py

Send a sysex message that is long enough to seemingly cause an overflow in FL
Studio.
"""
import mido
from mido import Message

available_ports = mido.get_output_names()

print(f"Available ports: {available_ports}")

port_name = input("Enter port name: ")

print(f"Connecting to MIDI port '{port_name}'...")

port = mido.open_output(name=port_name)


def main():
    data_length = int(input("Enter length of message to send: "))


    SYSEX_HEADER = [
        # 0xF0,  # added by mido
        0x7D,  # non-commercial byte
    ]
    # Closing 0xF7 byte is added by mido too

    bytes_added_by_mido = 2


    # Create message
    msg = bytes([
        *SYSEX_HEADER,
        *([0x42] * (data_length - bytes_added_by_mido - len(SYSEX_HEADER)))
    ])

    print(f"Sending message with length {len(msg) + bytes_added_by_mido}...")

    port.send(Message("sysex", data=msg))

    print("Message sent...")


try:
    print("Press Ctrl+C to exit")
    while True:
        main()
except KeyboardInterrupt:
    print("Goodbye")
