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

        fake_sdl2_config = join(self.ctx.build_dir, 'fake_sdl2_config')
        with open(fake_sdl2_config, 'w') as f:
            f.write('#!/bin/sh\n')
            f.write('case "$1" in\n')
            f.write('  --version) echo "2.0.20" ;;\n')
            f.write(f'  --cflags) echo "-I{sdl2_include}" ;;\n')
            f.write('  --libs) echo "-lSDL2" ;;\n')
            f.write('esac\n')
        os.chmod(fake_sdl2_config, 0o755)

        env['SDL_CONFIG'] = fake_sdl2_config
        env['CFLAGS'] += f' -I{sdl2_include}'
        # Вимикаємо модулі які потребують X11
        env['PYGAME_SCRAP'] = 'no'
        env['PYGAME_FREESANS'] = 'no'
        return env

    def build_arch(self, arch):
        build_dir = self.get_build_dir(arch.arch)
        # Патчимо setup.py щоб виключити scrap
        setup_py = join(build_dir, 'setup.py')
        if os.path.exists(setup_py):
            with open(setup_py, 'r') as f:
                content = f.read()
            content = content.replace(
                "'scrap'",
                "'scrap_disabled'"
            )
            with open(setup_py, 'w') as f:
                f.write(content)
        super().build_arch(arch)


recipe = PygameCERecipe()
