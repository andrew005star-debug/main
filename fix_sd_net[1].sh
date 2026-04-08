#!/system/bin/sh

# ждём, пока система и SD полностью поднимутся
sleep 60

echo "=== SD NET FIX START ==="

# получаем список пакетов с путями
pm list packages -f | while read line; do

    # пропускаем приложения во внутренней памяти
    echo "$line" | grep -q "/data/app/" && continue

    # извлекаем имя пакета
    pkg=${line##*=}

    # получаем UID (надёжный способ)
    uid=$(cmd package list packages -U | grep "^package:$pkg " | grep -oE 'uid:[0-9]+' | cut -d: -f2)

    # если UID найден — применяем фикс
    if [ -n "$uid" ]; then
        echo "Fixing $pkg (UID=$uid)"

        cmd netpolicy add restrict-background-whitelist $uid
        sleep 1
        cmd netpolicy remove restrict-background-whitelist $uid
    fi

done

echo "=== SD NET FIX DONE ==="