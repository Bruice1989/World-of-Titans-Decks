[app]
title = World of Titans Decks
package.name = worldtitans
package.domain = org.bruice
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json,wav,mp3,ogg
source.include_patterns = images/*.png,images/*.jpg,images/*.jpeg,images/Icon/*.png,images/Icon/*.jpg,images/Icon/*.jpeg,images/essences/*.png,images/essences/*.jpg,images/World/*.png,images/World/*.jpg,images/super_humans/*.png,images/super_humans/*.jpg,images/arch_cards/*.png,images/arch_cards/*.jpg,images/titans/*.png,images/titans/*.jpg,images/tabs/*.png,images/tabs/*.jpg,music/*.mp3,music/*.ogg,music/*.wav,sounds/*.wav,sounds/*.ogg,sounds/*.mp3
source.exclude_dirs = dist,__pycache__,.buildozer,build,p4a-recipes
source.main = main.py
version = 0.2
requirements = python3==3.10.14,hostpython3==3.10.14,kivy,pygame==2.1.0,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf
orientation = landscape
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.logcat_filters = *:S python:D
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
p4a.bootstrap = sdl2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
