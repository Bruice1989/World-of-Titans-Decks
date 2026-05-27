[app]
title = World of Titans Decks
package.name = worldtitans
package.domain = org.bruice
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json,wav,mp3,ogg
source.exclude_dirs = dist,__pycache__,.buildozer,build,p4a-recipes
source.main = main.py
version = 0.2
requirements = python3==3.10.14,hostpython3==3.10.14,pygame_ce==2.1.3,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf
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
p4a.local_recipes = ./p4a-recipes

[buildozer]
log_level = 2
warn_on_root = 1
