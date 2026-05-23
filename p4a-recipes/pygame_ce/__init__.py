from pythonforandroid.recipe import CythonRecipe
from os.path import join
import os


class PygameCERecipe(CythonRecipe):
    version = '2.4.1'
    url = 'https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz'
    name = 'pygame_ce'
    depends = ['sdl2', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'python3']
    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        sdl2_recipe = self.get_recipe('sdl2', self.ctx)
        sdl2_dir = sdl2_recipe.get_build_dir(arch.arch)
        sdl2_include = join(sdl2_dir, 'include')
        env['SDL_CONFIG'] = 'true'
        env['CFLAGS'] += f' -I{sdl2_include}'
        env['PYGAME_SDL2_PREFIX'] = sdl2_dir
        return env

    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        env = self.get_recipe_env(arch)
        # Пропускаємо config і компілюємо напряму
        env['PYGAME_CROSS_COMPILE'] = '1'
        super().build_arch(arch)


recipe = PygameCERecipe()
