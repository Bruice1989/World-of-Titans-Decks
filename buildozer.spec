[app]

# (str) Title of your application
title = World of Titans Decks

# (str) Package name
package.name = world_of_titans

# (str) Package domain (needed for android packaging)
package.domain = org.bruice

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,json,wav,mp3

# (str) Main python file name
source.main = main.py

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Залишаємо базовий набір для стабільності
requirements = python3,pygame==2.5.2

# (str) Supported orientation (landscape, portrait or all)
orientation = landscape

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use (31 - найбільш стабільна для GitHub)
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path = 

# (list) The Android architectures to build for
# Використовуємо одну для уникнення конфліктів при першій збірці
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1

[buildozer]

# (str) Path to build artifact storage, cache and configuration
build_dir = ./.buildozer

# (str) Path to bin directory where the APK will be stored
bin_dir = ./bin
