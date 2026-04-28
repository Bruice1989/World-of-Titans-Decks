[app]
title = World of Titans Decks
package.name = worldtitans
package.domain = org.bruice

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json,wav,mp3
source.main = main.py

version = 0.1

requirements = python3,pygame==2.1.3,sdl2,sdl2_ttf,sdl2_image,sdl2_mixer

orientation = landscape
fullscreen = 1

android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
