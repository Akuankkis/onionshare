# -*- mode: python -*-

import platform
system = platform.system()

version = open('resources/version.txt').read().strip()

block_cipher = None

a = Analysis(
    ['scripts/onionshare-gui'],
    pathex=['.'],
    binaries=None,
    datas=[
        ('../resources/images/*', 'images'),
        ('../resources/locale/*', 'locale'),
        ('../resources/html/*', 'html'),
        ('../resources/version.txt', '.'),
        ('../resources/wordlist.txt', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher)

pyz = PYZ(
    a.pure, a.zipped_data,
    cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='onionshare',
    debug=False,
    strip=False,
    upx=True,
    console=False)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='onionshare')

if system == 'Darwin':
    app = BUNDLE(
        coll,
        name='OnionShare.app',
        icon='install/onionshare.icns',
        bundle_identifier='com.micahflee.onionshare',
        info_plist={
            'CFBundleShortVersionString': version,
            'NSHighResolutionCapable': 'True'
        }
    )
