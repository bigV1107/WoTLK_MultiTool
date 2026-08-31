# -*- mode: python ; coding: utf-8 -*-
# WoTLK_MultiTool 单文件 EXE 打包配置
# 修复：collect_all 结果直接传给 Analysis，避免 TOC 格式冲突

from PyInstaller.utils.hooks import collect_all

# 预先收集第三方库的二进制/数据资源（必须在 Analysis 之前）
dpg_datas, dpg_binaries, dpg_hiddenimports = collect_all('dearpygui')
pwa_datas, pwa_binaries, pwa_hiddenimports = collect_all('pywinauto')
comtypes_datas, comtypes_binaries, comtypes_hiddenimports = collect_all('comtypes')

block_cipher = None

a = Analysis(
    ['WoTLK_MultiTool.py'],
    pathex=['.'],
    # 直接在这里传入 collect_all 的结果，避免手动 += 到 TOC
    binaries=dpg_binaries + pwa_binaries + comtypes_binaries,
    datas=dpg_datas + pwa_datas + comtypes_datas,
    hiddenimports=[
        # DearPyGui
        'dearpygui',
        'dearpygui.dearpygui',
        # 本地业务模块
        'arrays_keyframes',
        'color_calculator',
        'convert_autotexture',
        'csv_editor',
        'particle_cloner',
        'position_scale',
        'texture_components',
        # utils 包
        'utils',
        'utils.async_manager',
        'utils.binary',
        'utils.config',
        'utils.miscellaneous',
        'utils.offsets',
        'utils.registry',
        'utils.statusbar',
        # 第三方依赖
        'keyboard',
        'pyperclip',
        'requests',
        'pywinauto',
        'pywinauto.application',
        'comtypes',
        'comtypes.client',
        # Windows 专属标准库
        'winreg',
        'winsound',
        'asyncio',
        'threading',
    ] + dpg_hiddenimports + pwa_hiddenimports + comtypes_hiddenimports,
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
    name='WoTLK_MultiTool',
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
