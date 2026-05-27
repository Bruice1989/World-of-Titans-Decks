from pythonforandroid.recipe import CythonRecipe
from os.path import join
import os
import glob


class PygameCERecipe(CythonRecipe):
    version = '2.4.1'
    url = 'https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz'
    name = 'pygame_ce'
    depends = ['sdl2', 'sdl2_image', 'sdl2_mixer', 'sdl2_ttf', 'python3']
    call_hostpython_via_targetpython = False
    install_in_hostpython = False

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        # Встановлюємо Cython саме в hostpython
        hostpython = self.ctx.hostpython
        self.run_hostpython(hostpython, '-m', 'pip', 'install',
                            'cython==0.29.37', '--user')

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

        # Додаємо шлях до cython у hostpython
        hostpython_dir = join(self.ctx.build_dir,
                              'other_builds', 'hostpython3', 'desktop',
                              'hostpython3', 'native-build', 'root',
                              'usr', 'local', 'bin')
        env['PATH'] = hostpython_dir + ':' + env.get('PATH', '')

        return env

    def prepare_build_dir(self, arch):
        super().prepare_build_dir(arch)
        self._patch_build_dir(arch)

    def _patch_build_dir(self, arch):
        build_dir = self.get_build_dir(arch)
        print(f'Патчимо pygame_ce в {build_dir}')

        for f in glob.glob(join(build_dir, 'src_c', 'scrap*.c')):
            os.remove(f)
            print(f'Видалено: {f}')

        setup_py = join(build_dir, 'setup.py')
        if os.path.exists(setup_py):
            with open(setup_py, 'r') as f:
                content = f.read()
            lines = [l for l in content.split('\n') if 'scrap' not in l.lower()]
            with open(setup_py, 'w') as f:
                f.write('\n'.join(lines))
            print('setup.py патч застосовано!')


recipe = PygameCERecipe()
