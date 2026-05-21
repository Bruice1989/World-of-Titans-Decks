from pythonforandroid.recipe import CythonRecipe


class PygameCERecipe(CythonRecipe):
    version = '2.4.1'
    url = 'https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz'
    name = 'pygame_ce'
    depends = ['sdl2', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'python3']
    patches = []
    call_hostpython_via_targetpython = False
    install_in_hostpython = False


recipe = PygameCERecipe()
