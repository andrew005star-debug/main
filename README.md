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
