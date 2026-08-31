# -*- mode: python ; coding: utf-8 -*-
# Helm Offset Tool 极简打包配置
# 只保留 helm offset + move/resize 功能，去掉所有重型依赖

from PyInstaller.utils.hooks import collect_all

dpg_datas, dpg_binaries, dpg_hiddenimports = collect_all('dearpygui')

block_cipher = None

a = Analysis(
    ['helm_tool.py'],
    pathex=['.'],
    binaries=dpg_binaries,
    datas=dpg_datas,
    hiddenimports=[
        # DearPyGui
        'dearpygui',
        'dearpygui.dearpygui',
        # 本地模块
        'position_scale',
        'utils',
        'utils.async_manager',
        'utils.binary',
        'utils.config',
        'utils.miscellaneous',
        'utils.offsets',
        'utils.registry',
        'utils.statusbar',
        # 第三方（miscellaneous/statusbar 间接需要）
        'pyperclip',
        'pywinauto',
        'pywinauto.application',
        'comtypes',
        'comtypes.client',
        'requests',
        # Windows 标准库
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
        'tkinter',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        # 明确排除之前那堆重型依赖
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
