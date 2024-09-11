#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

playtone(329, 0.21)
playtone(698, 0.21)
playtone(329, 0.21)
playtone(698, 0.21)
playtone(329, 0.21)
playtone(698, 0.21)

playtone(293, 0.21)
playtone(659, 0.21)
playtone(293, 0.21)
playtone(659, 0.21)
playtone(293, 0.21)
playtone(659, 0.21)

playtone(261, 0.21)
playtone(587, 0.21)
playtone(261, 0.21)
playtone(587, 0.21)
playtone(261, 0.21)
playtone(587, 0.21)

playtone(493, 0.21)
playtone(880, 0.21)

playtone(415, 0.5)
playtone(164, 0.5)

playtone(493, 0.5)
playtone(323, 0.5)
playtone(987, 0.5)
playtone(660, 0.5)
playtone(987, 0.5)

# Turn off the PWM
quiet()
