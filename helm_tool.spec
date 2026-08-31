# -*- mode: python ; coding: utf-8 -*-
# Helm Offset Tool 打包配置（含 tkinter 文件夹对话框）

from PyInstaller.utils.hooks import collect_all

dpg_datas, dpg_binaries, dpg_hiddenimports = collect_all('dearpygui')

block_cipher = None

a = Analysis(
    ['helm_tool.py'],
    pathex=['.'],
    binaries=dpg_binaries,
    datas=dpg_datas,
    hiddenimports=[
        'dearpygui',
        'dearpygui.dearpygui',
        'position_scale',
        'utils',
        'utils.async_manager',
        'utils.binary',
        'utils.config',
        'utils.miscellaneous',
        'utils.offsets',
        'utils.registry',
        'utils.statusbar',
        'pyperclip',
        'pywinauto',
        'pywinauto.application',
        'comtypes',
        'comtypes.client',
        'requests',
        'tkinter',                 # ← 新增：文件夹对话框需要
        'tkinter.filedialog',      # ← 新增
        'winreg',
        'winsound',
        'asyncio',
        'threading',
    ] + dpg_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'PIL',
        'unittest',
        'pytest',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'pyautogui',
        'dbcpy',
        'keyboard',
    ],
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
    name='HelmOffsetTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
