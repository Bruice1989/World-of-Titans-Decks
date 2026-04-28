[app]
# Назва вашої гри
title = World of Titans Decks
# Назва пакету (без пробілів)
package.name = world_of_titans
# Домен (можна залишити такий)
package.domain = org.bruice
# Файли, які треба включити (py, png, jpg тощо)
source.include_exts = py,png,jpg,jpeg,ttf,json
# Головний файл
source.main = main.py

# ВЕРСІЯ ТА ЗАЛЕЖНОСТІ
version = 0.1
requirements = python3,pygame

# Орієнтація екрану (landscape - горизонтальна, portrait - вертикальна)
orientation = landscape

# Дозволи
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (Опціонально) Іконка гри
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
