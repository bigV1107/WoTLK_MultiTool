import dearpygui.dearpygui as dpg
import pyperclip

from position_scale import auto_fix_helm_offset, model_moving_pre, model_resize_pre


def paste_path():
    dpg.set_value("inp_model", pyperclip.paste().strip('"'))


def on_auto_fix():
    path = dpg.get_value("inp_model")
    if path:
        auto_fix_helm_offset(path)


def on_move():
    model_moving_pre()


def on_resize():
    model_resize_pre()


# GUI
dpg.create_context()
dpg.create_viewport(title="Helm Offset Tool", width=420, height=480, resizable=False)

with dpg.window(label="Main", tag="win_main", no_title_bar=True, no_resize=True):
    dpg.add_text("Model Path:")
    with dpg.group(horizontal=True):
        dpg.add_input_text(tag="inp_model", width=320, hint="Path to .m2 model")
        dpg.add_button(label="Paste", width=60, callback=paste_path)

    dpg.add_separator()
    dpg.add_spacer(height=5)
    dpg.add_button(label="AUTO FIX HELM OFFSET", width=390, height=30, callback=on_auto_fix)

    dpg.add_separator()
    dpg.add_spacer(height=5)
    dpg.add_text("Move Model (x / y / z)")
    with dpg.group(horizontal=True):
        dpg.add_input_float(tag="inp_x_position", default_value=0.0, format="%.3f", step=0.01, width=120, label="x")
        dpg.add_input_float(tag="inp_y_position", default_value=0.0, format="%.3f", step=0.01, width=120, label="y")
        dpg.add_input_float(tag="inp_z_position", default_value=0.0, format="%.3f", step=0.01, width=120, label="z")
    dpg.add_button(label="MOVE", width=390, height=25, callback=on_move)

    dpg.add_separator()
    dpg.add_spacer(height=5)
    dpg.add_text("Resize Model (%)")
    dpg.add_input_int(tag="inp_scale_modifier", default_value=0, width=120, step_fast=10)
    dpg.add_button(label="RESIZE", width=390, height=25, callback=on_resize)

    dpg.add_spacer(height=10)
    dpg.add_text("", tag="txt_info", color=[255, 255, 255])

dpg.setup_dearpygui()
dpg.set_primary_window("win_main", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
