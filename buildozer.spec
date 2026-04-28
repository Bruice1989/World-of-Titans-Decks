[app]
# Назва вашої гри
title = World of Titans Decks

# Назва пакету (без пробілів)
package.name = world_of_titans

# Домен
package.domain = org.bruice

# КРИТИЧНО: Директорія з вихідним кодом (крапка означає поточну папку)
source.dir = .

# Файли, які треба включити
source.include_exts = py,png,jpg,jpeg,ttf,json

# Головний файл
source.main = main.py

# ВЕРСІЯ ТА ЗАЛЕЖНОСТІ
version = 0.1
# Додаємо kivi, навіть якщо ви на pygame, це іноді допомагає buildozer правильно налаштувати середовище
requirements = python3,pygame

# Орієнтація екрану
orientation = landscape

# Дозволи
android.permissions = INTERNET

# Налаштування для Android
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
