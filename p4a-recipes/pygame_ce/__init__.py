from pythonforandroid.recipe import CythonRecipe
from os.path import join


class PygameCERecipe(CythonRecipe):
    version = '2.4.1'
    url = 'https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz'
    name = 'pygame_ce'
    depends = ['sdl2', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'python3']
    call_hostpython_via_targetpython = False
    install_in_hostpython = False
    setup_extra_args = ['--ignore-setup-py']

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        sdl2 = self.get_recipe('sdl2', self.ctx)
        env['SDL_ROOT'] = sdl2.get_build_dir(arch.arch)
        return env


recipe = PygameCERecipe()
