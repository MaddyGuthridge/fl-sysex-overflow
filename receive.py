"""
receive.py

Simple script to connect to a MIDI port and listen for incoming MIDI messages.
"""
import mido
from mido import Message
from mido.ports import BaseInput

available_ports = mido.get_input_names()

print(f"Available ports: {available_ports}")

port_name = input("Enter port name: ")

print(f"Connecting to MIDI port '{port_name}'...")

port: BaseInput = mido.open_input(name=port_name)


def recv():
    msg: Message | None = port.receive(block=False)

    if msg is None:
        return

    print("Received response message")
    print(f"Message length: {len(msg.bytes())}")
    print()


print("Connected! Press Ctrl+C to stop listening")
try:
    while True:
        recv()
except KeyboardInterrupt:
    print("Goodbye")
