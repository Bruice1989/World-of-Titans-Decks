def pre_build(ctx):
    import shutil, os, glob
    # Шукаємо pygame в усіх можливих місцях
    base = ctx.build_dir
    patterns = [
        os.path.join(base, "python-installs", "*", "*", "pygame"),
        os.path.join(base, "other_builds", "pygame*"),
    ]
    for pattern in patterns:
        for path in glob.glob(pattern):
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Видалено: {path}")
