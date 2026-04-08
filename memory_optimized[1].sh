#!/system/bin/sh

# Ждём, пока система полностью загрузится
sleep 30

# =======================
# 1. zRAM
# =======================
/system/bin/toybox swapoff /dev/block/zram0 2>/dev/null
echo 1 > /sys/block/zram0/reset
echo 4294967296 > /sys/block/zram0/disksize   # 4 GB
/system/bin/toybox mkswap /dev/block/zram0
/system/bin/toybox swapon /dev/block/zram0

# =======================
# 2. swapfile
# =======================
if [ ! -f /data/swapfile ]; then
    dd if=/dev/zero of=/data/swapfile bs=1M count=2048
    chmod 600 /data/swapfile
    /system/bin/toybox mkswap /data/swapfile
fi
/system/bin/toybox swapon /data/swapfile

# =======================
# 3. swappiness
# =======================
echo 120 > /proc/sys/vm/swappiness

# =======================
# 4. LMK tuning
# =======================
# уменьшаем агрессивность Low Memory Killer
echo "1536,2048,4096,6144,8192,10240" > /sys/module/lowmemorykiller/parameters/minfree
