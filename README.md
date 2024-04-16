# Sysex overflow test

Code for testing overflows with sending/receiving sysex messages in FL Studio.

## Setup

1. Create a virtual MIDI port by using a tool such as
   [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)

2. `git clone` the project

3. [Install the Poetry build system](https://python-poetry.org/docs/#installing-with-the-official-installer)
   to install project dependencies.

4. Install dependencies by running `poetry install`

5. Install the FL Studio script by running `poetry run python install_script.py`

6. Launch FL Studio and assign a port.

7. Launch the sender script by running `poetry run python send.py`

8. In another terminal, launch the receiver script by running
   `poetry run python receive.py`.

## Usage

Enter the name of your virtual MIDI port (including the number from the
displayed port names) to connect to the port.

Follow the prompts to send messages from the send script.

Whenever a message is sent on the port, it will be reported in both the script
output and the receiver script.

To send a message from FL Studio, call `send_msg(data_length)`.

## Findings

* Messages with a length `<= 1024` bytes work correctly.

* Messages with a length `> 1024` bytes are split into two messages by FL
  Studio, and are not displayed by the receive script (possibly a similar bug
  in the `rtmidi` library? Will investigate).

* Messages with a length that is too large cause FL Studio to either freeze
  or immediately crash. A length of 1500 did this for me, but I couldn't find a
  specific value where it starts happening.
