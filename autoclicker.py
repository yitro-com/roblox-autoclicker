#!/usr/bin/env python3
import time
import threading
import sys
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode

# ==================== KONFIGURASI ====================
# Kecepatan Super Cepat
INTERVAL = 0.01      # Jeda antar klik dalam detik (0.01 = ~50-80 klik per detik)
HOLD_TIME = 0.005    # Durasi penahanan klik (5 milidetik agar input terbaca oleh Roblox)
BUTTON = Button.left

START_STOP_KEY = KeyCode(char='s')  # 's' untuk Mulai / Jeda
EXIT_KEY = KeyCode(char='e')        # 'e' untuk Keluar
# =====================================================


class UltraFastClicker(threading.Thread):
    def __init__(self, interval, hold_time, button):
        super().__init__()
        self.interval = interval
        self.hold_time = hold_time
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        mouse = MouseController()
        while self.program_running:
            while self.running:
                mouse.press(self.button)
                time.sleep(self.hold_time)
                mouse.release(self.button)
                time.sleep(self.interval)
            time.sleep(0.02)


clicker = UltraFastClicker(INTERVAL, HOLD_TIME, BUTTON)
clicker.start()


def on_press(key):
    if key == START_STOP_KEY:
        if clicker.running:
            clicker.stop_clicking()
            print("[STATUS] Auto Clicker: JEDA (Paused)")
        else:
            clicker.start_clicking()
            print("[STATUS] Auto Clicker: AKTIF (Mode Super Cepat)")
    elif key == EXIT_KEY:
        clicker.exit()
        listener.stop()
        print("[STATUS] Program dimatikan.")
        sys.exit(0)


print("=" * 45)
print("    ROBLOX AUTO CLICKER (MODE ULTRA CEPAT)")
print("=" * 45)
print(" Kecepatan : ~50 - 80 Klik per Detik (CPS)")
print(" Kontrol   :")
print("   Tekan 's' -> Mulai / Jeda (Start/Pause)")
print("   Tekan 'e' -> Keluar dari program (Exit)")
print("=" * 45)
print("Status: Siap. Arahkan kursor lalu tekan 's'.\n")

with Listener(on_press=on_press) as listener:
    listener.join()
