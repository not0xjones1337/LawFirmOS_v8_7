# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('core', 'core'),
        ('services', 'services'),
        ('gui', 'gui'),
        ('app', 'app'),
        ('data', 'data'),
    ],
    hiddenimports=[
        'core.bootstrap',
        'services.ingestion_service',
        'services.qdrant_service',
        'qdrant_client',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='launcher',
    debug=False,
    strip=False,
    upx=True,
    console=True
)

