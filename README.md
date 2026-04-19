# Adoptable Storage Network Fix (Magisk) "fix_sd_net[1].sh"

Fixes a critical Android bug where apps installed on adoptable storage (SD card) lose internet access after reboot.

## Problem

On some devices (especially with custom ROMs like LineageOS):

- Apps on SD card launch normally
- But have **no internet access after reboot**
- Other apps work fine
- Moving app to internal storage fixes it temporarily

## Root Cause

Android fails to restore proper **network binding (UID → network)**  
for apps on adoptable storage after system boot.

## Solution

Force re-binding using `netpolicy`:

- Triggers system to reprocess UID network rules
- No need to move apps or re-download data

## Installation

1. Install Magisk
2. Download file: fix_sd_net.sh and paste to: /data/adb/service.d/
3. Set permissions by Termux or ADB: chmod 755 /data/adb/service.d/fix_sd_net.sh
4. Reboot

## Notes
Works without moving apps
No data loss
Supports large apps (e.g. 50GB+)

## Tested on
LineageOS 23
Android 16
Devices with adoptable storage

## Credits

Discovered and debugged through real-world testing and system-level analysis.

# Memory Optimized Android Tuning Script

Low-level Android/Linux memory optimization script focused on improving system stability under low RAM conditions (2–4 GB devices).

The script tunes virtual memory behavior, swap usage, and memory management policies to reduce OOM kills and improve background process retention.

---

## 📌 Overview

Modern Android devices with limited RAM often suffer from:

- Aggressive background app killing
- UI stutters under memory pressure
- Frequent OOM (Out Of Memory) events
- Poor multitasking stability

This project implements a lightweight system-level tuning layer using shell scripting and Linux kernel interfaces exposed via `/proc` and `/sys`.

---

## ⚙️ Features

### Memory Management
- zRAM activation and configuration
- Optional swapfile support
- Swappiness tuning for better memory pressure handling

### Kernel Tuning
- LMK (Low Memory Killer) parameter optimization (legacy devices)
- lmkd-aware configurations for modern Android versions
- Reduced background process eviction aggressiveness

### Stability Improvements
- Reduced app cold-killing under load
- Improved multitasking retention
- Better behavior under memory pressure scenarios

---

## 🧩 Technical Implementation

The script operates at system boot or via root shell:

- Configures `/sys/block/zram0`
- Sets `/proc/sys/vm/*` parameters
- Applies LMK thresholds via sysfs (if available)
- Creates and activates swapfile if required

Example:

```sh
echo 1 > /sys/block/zram0/reset
echo 2147483648 > /sys/block/zram0/disksize
mkswap /dev/block/zram0
swapon /dev/block/zram0

echo 120 > /proc/sys/vm/swappiness
