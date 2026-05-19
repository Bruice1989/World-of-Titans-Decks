def pre_build(ctx):
    import shutil, os
    pygame_path = os.path.join(
        ctx.python_installs_dir, 
        "worldtitans/arm64-v8a/pygame"
    )
    if os.path.exists(pygame_path):
        shutil.rmtree(pygame_path)
        print("Видалено старий pygame!")
