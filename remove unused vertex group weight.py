import bpy

# ambil semua object yang dipilih
for obj in bpy.context.selected_objects:
    if obj.type != 'MESH':
        continue

    vgroups = obj.vertex_groups
    to_remove = []

    # cek tiap group
    for vg in vgroups:
        has_weight = False
        for v in obj.data.vertices:
            try:
                w = vg.weight(v.index)
                if w > 1e-6:  # ada bobot non-zero
                    has_weight = True
                    break
            except RuntimeError:
                # vertex tidak ada di group ini
                continue
        if not has_weight:
            to_remove.append(vg)

    # hapus group yang kosong
    for vg in to_remove:
        print("Removing group:", vg.name, "from object:", obj.name)
        obj.vertex_groups.remove(vg)

print("Done. Removed empty groups from selected meshes.")
