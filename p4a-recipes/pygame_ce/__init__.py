from pythonforandroid.recipes.pygame import PygameRecipe


class PygameCERecipe(PygameRecipe):
    version = '2.4.1'
    url = 'https://github.com/pygame-community/pygame-ce/archive/refs/tags/{version}.tar.gz'
    name = 'pygame_ce'


recipe = PygameCERecipe()
