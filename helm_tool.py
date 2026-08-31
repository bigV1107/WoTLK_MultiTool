import dearpygui.dearpygui as dpg
import os
import pyperclip
from tkinter import filedialog
from tkinter import Tk

from position_scale import auto_fix_helm_offset, model_moving_pre, model_resize_pre


def browse_folder():
    """弹出 Windows 文件夹选择对话框"""
    root = Tk()
    root.withdraw()           # 隐藏 tkinter 主窗口
    root.wm_attributes('-topmost', 1)  # 置顶
    folder = filedialog.askdirectory()
    root.destroy()
    if folder:
        dpg.set_value("inp_folder", folder)
        update_m2_count()


def update_m2_count():
    """更新检测到的 .m2 文件数量"""
    folder = dpg.get_value("inp_folder")
    if folder and os.path.isdir(folder):
        count = len([f for f in os.listdir(folder) if f.lower().endswith('.m2')])
        dpg.set_value("txt_m2_count", f"Found: {count} .m2 file(s)")
        dpg.configure_item("txt_m2_count", color=[150, 255, 150])
    else:
        dpg.set_value("txt_m2_count", "Found: 0 .m2 file(s)")
        dpg.configure_item("txt_m2_count", color=[150, 150, 150])


def fix_all_helmets():
    """遍历文件夹内所有 .m2，按种族自动修正头盔偏移"""
    folder = dpg.get_value("inp_folder")
    if not folder or not os.path.isdir(folder):
        dpg.set_value("txt_info", "ERROR: Select a valid folder", color=[255, 10, 0])
        return

    files = [f for f in os.listdir(folder) if f.lower().endswith('.m2')]
    if not files:
        dpg.set_value("txt_info", "ERROR: No .m2 files found", color=[255, 10, 0])
        return

    total = len(files)
    fixed = 0
    failed = 0

    for i, name in enumerate(files, 1):
        path = os.path.join(folder, name)
        dpg.set_value("txt_info", f"Processing {i}/{total}: {name}...")
        dpg.configure_item("txt_info", color=[255, 255, 255])
        dpg.render_dearpygui_frame()  # 强制刷新 UI
        try:
            auto_fix_helm_offset(path)
            fixed += 1
        except Exception as e:
            failed += 1

    if failed:
        dpg.set_value("txt_info", f"Done: {fixed} OK, {failed} failed")
        dpg.configure_item("txt_info", color=[255, 200, 0])
    else:
        dpg.set_value("txt_info", f"Done: {fixed}/{total} helmets fixed")
        dpg.configure_item("txt_info", color=[10, 255, 0])


def paste_path():
    dpg.set_value("inp_model", pyperclip.paste().strip('"'))


# GUI 布局
dpg.create_context()
dpg.create_viewport(title="Helm Offset Tool", width=460, height=400, resizable=False)

with dpg.window(label="Main", tag="win_main", no_title_bar=True, no_resize=True):

    # ===== 批量处理区域 =====
    dpg.add_text("Batch Fix Helmets", color=[0, 240, 255])
    with dpg.group(horizontal=True):
        dpg.add_input_text(tag="inp_folder", width=320, hint="Select folder with .m2 files", callback=update_m2_count)
        dpg.add_button(label="Browse", width=70, callback=browse_folder)

    dpg.add_text("Found: 0 .m2 file(s)", tag="txt_m2_count", color=[150, 150, 150])
    dpg.add_button(label="AUTO FIX ALL HELMETS IN FOLDER", width=400, height=35, callback=fix_all_helmets)

    dpg.add_separator()
    dpg.add_spacer(height=5)

    # ===== 单文件微调（保留） =====
    dpg.add_text("Single File Tools", color=[0, 240, 255])
    with dpg.group(horizontal=True):
        dpg.add_input_text(tag="inp_model", width=320, hint="Path to single .m2 model")
        dpg.add_button(label="Paste", width=70, callback=paste_path)

    with dpg.group(horizontal=True):
        dpg.add_input_float(tag="inp_x_position", default_value=0.0, format="%.3f", step=0.01, width=125, label="x")
        dpg.add_input_float(tag="inp_y_position", default_value=0.0, format="%.3f", step=0.01, width=125, label="y")
        dpg.add_input_float(tag="inp_z_position", default_value=0.0, format="%.3f", step=0.01, width=125, label="z")
    dpg.add_button(label="MOVE", width=400, height=25, callback=model_moving_pre)

    dpg.add_spacer(height=5)
    dpg.add_input_int(tag="inp_scale_modifier", default_value=0, width=120, label="%")
    dpg.add_button(label="RESIZE", width=400, height=25, callback=model_resize_pre)

    # 状态栏
    dpg.add_spacer(height=10)
    dpg.add_text("", tag="txt_info", color=[255, 255, 255])

dpg.setup_dearpygui()
dpg.set_primary_window("win_main", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
