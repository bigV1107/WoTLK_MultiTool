# WoTLK_MultiTool
头盔移动
# 1. 先找有没有现成的控制骨骼（CRC == 987654321）
control_bone_id = get_control_bone_id(model_path)

# 2. 没有就找一根"空闲"的根骨骼
if control_bone_id is None:
    control_bone_id = search_valid_bone_id(...)

# 3. 还找不到才创建新的
if control_bone_id is None:
    control_bone_id = create_Control_Bone(...)

一般第一根空闲，代码的搜索逻辑恰好经常匹配到第一根，会写入值，看情况用。
