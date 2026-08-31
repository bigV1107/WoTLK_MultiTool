# -*- mode: python ; coding: utf-8 -*-
# WoTLK_MultiTool 单文件 EXE 打包配置
# 基于 WoTLK_MultiTool.py 的实际导入生成

block_cipher = None

a = Analysis(
    ['WoTLK_MultiTool.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # 如果有图标文件，取消注释并确保 multitool.ico 在仓库根目录
        # ('multitool.ico', '.'),
    ],
    hiddenimports=[
        # DearPyGui
        'dearpygui',
        'dearpygui.dearpygui',
        # 本地业务模块（WoTLK_MultiTool.py 直接导入的）
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
    ],
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

# DearPyGui 内嵌了 GLFW 渲染器和字体，必须全量收集
from PyInstaller.utils.hooks import collect_all
dpg_datas, dpg_binaries, dpg_hiddenimports = collect_all('dearpygui')
a.datas += dpg_datas
a.binaries += dpg_binaries
a.hiddenimports += dpg_hiddenimports

# pywinauto 也建议全量收集，避免缺后台 DLL
pwa_datas, pwa_binaries, pwa_hiddenimports = collect_all('pywinauto')
a.datas += pwa_datas
a.binaries += pwa_binaries
a.hiddenimports += pwa_hiddenimports

# comtypes 生成缓存目录处理
comtypes_datas, comtypes_binaries, comtypes_hiddenimports = collect_all('comtypes')
a.datas += comtypes_datas
a.binaries += comtypes_binaries
a.hiddenimports += comtypes_hiddenimports

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
    console=False,         # ← 隐藏控制台黑框
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
