def post_build_arch(ctx, arch):
    import shutil, os
    # Видаляємо старий pygame з python-installs після збірки
    pygame_path = os.path.join(
        ctx.build_dir,
        "python-installs",
        "worldtitans",
        arch.arch,
        "pygame"
    )
    if os.path.exists(pygame_path):
        shutil.rmtree(pygame_path)
        print(f">>> Видалено старий pygame з python-installs: {pygame_path}")
