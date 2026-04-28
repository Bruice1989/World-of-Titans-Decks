[app]
title = World of Titans Decks
package.name = worldtitans
package.domain = org.bruice
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json,wav,mp3
source.main = main.py
version = 0.1

# Додано Cython версії 0.29.33, це важливо для Pygame
requirements = python3,pygame==2.5.2,cython==0.29.33

orientation = landscape
fullscreen = 1
android.permissions = INTERNET

# Версії Android
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
