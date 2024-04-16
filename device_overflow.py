# name=Overflow test
# supportedDevices=Test
"""
device_overflow.py

Simple MIDI controller script to test overflow messages
"""
try:
    from fl_classes import FlMidiMsg
except ImportError:
    pass
import device


def send_msg(data_length: int):
    """
    Send a sysex message with the given length.
    """
    SYSEX_HEADER = [
        0xF0,
        0x7D,  # non-commercial byte
    ]

    msg = bytes([
        *SYSEX_HEADER,
        *([0x42] * (data_length - len(SYSEX_HEADER) - 1)),
        0xF7,
    ])

    device.midiOutSysex(msg)


def OnSysEx(msg: 'FlMidiMsg'):
    print("Received sysex message")
    print(f"Length: {len(msg.sysex)}")
    print(f"Ends with 0xF7: {msg.sysex[-1] == 0xF7}")
    print()
    msg.handled = True


def OnInit():
    print("\nCall send_msg(data_length) to send a sysex message\n\n")
