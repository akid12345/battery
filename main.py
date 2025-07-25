import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor('black')  
ax.set_facecolor('black')        
ax.set_xlim(0, 13)
ax.set_ylim(0, 6)
ax.axis('off')


# === LABELS ===
ax.text(2.5, 5.5, "Lithium-Ion Battery", ha='center', fontsize=12, weight='bold')
ax.text(10.0, 5.5, "Solid-State Battery", ha='center', fontsize=12, weight='bold')

# === Li-ion Battery ===
liion_body = patches.Rectangle((0, 1), 6, 3, edgecolor='white', facecolor='lightblue')
liion_sep = patches.Rectangle((2.9, 0.99), 0.2, 2.98, facecolor='peachpuff')
liion_anode = patches.Rectangle((0, 1), 0.2, 3, facecolor='gray')
liion_cathode = patches.Rectangle((5.8, 1), 0.2, 3, facecolor='darkblue')
ax.add_patch(liion_body)
ax.add_patch(liion_sep)
ax.add_patch(liion_anode)
ax.add_patch(liion_cathode)
ax.text(1.5, 0.5, "Anode (-)", ha='center', color='white', fontsize=10)
ax.text(4.5, 0.5, "Cathode (+)", ha='center', color='white', fontsize=10)
ax.text(3, 0.5, "Separator", ha='center', color='white', fontsize=10)
ax.text(1, 4.5, "Anode", ha='center', color='white', fontsize=10)
ax.text(1, 4.3, "Electrical Contact", ha='center', color='white', fontsize=10)
ax.text(5, 4.5, "Cathode", ha='center', color='white', fontsize=10)
ax.text(5, 4.3, "Electrical Contact", ha='center', color='white', fontsize=10)

# === Solid-State Battery ===
ssb_body = patches.Rectangle((8, 1), 5, 3, edgecolor='white', facecolor='white')
ssb_sep = patches.Rectangle((11, 0.99), 0.5, 2.98, facecolor='peachpuff')
ssb_anodecont = patches.Rectangle((12.8, 1), 0.2, 3, facecolor='gray')
ssb_cathodecont = patches.Rectangle((8, 1), 0.2, 3, facecolor='darkblue')
ssb_lithium_anode = patches.Rectangle((11.5, 1), 1.5, 3, edgecolor='white', facecolor='red', alpha=0.3)
ax.add_patch(ssb_body)
ax.add_patch(ssb_sep)
ax.add_patch(ssb_anodecont)
ax.add_patch(ssb_cathodecont)
ax.add_patch(ssb_lithium_anode)
ax.text(9.5, 0.5, "Cathode (+)", ha='center', color='white', fontsize=10)
ax.text(11.25, 0.5, "Solid-State", ha='center', color='white', fontsize=10)
ax.text(11.25, 0.3, "Ceramic Separator", ha='center', color='white', fontsize=10)
ax.text(12, 4.5, "Anode", ha='center', color='white', fontsize=10)
ax.text(12, 4.3, "Electrical Contact", ha='center', color='white', fontsize=10)
ax.text(9, 4.5, "Cathode", ha='center', color='white', fontsize=10)
ax.text(9, 4.3, "Electrical Contact", ha='center', color='white', fontsize=10)
ax.text(12.5, 0.5, "Lithium", ha='center', color='white', fontsize=10)
ax.text(12.5, 0.3, "Anode", ha='center', color='white', fontsize=10)

# === Lithium Ions with velocity for lionbat ===
liion_ions = []
liion_vels = []
for _ in range(15):
    x, y = np.random.uniform(1.2, 4.8), np.random.uniform(1.2, 3.7)
    liion_ions.append(plt.Circle((x, y), 0.1, color='orange'))
    angle = np.random.uniform(0, 2 * np.pi)
    speed = 0.03
    liion_vels.append((speed * np.cos(angle), speed * np.sin(angle)))

for ion in liion_ions:
    ax.add_patch(ion)

# === External Circuit for Li-ion Battery ===
wire_up_left = patches.FancyArrow(0.1, 4, 0, 1, width=0.02, head_width=0, color='white')
wire_across_top = patches.FancyArrow(0.1, 5, 5.8, 0, width=0.02, head_width=0, color='white')
wire_down_right = patches.FancyArrow(5.9, 4, 0, 1, width=0.02, head_width=0, color='white')
ax.add_patch(wire_up_left)
ax.add_patch(wire_across_top)
ax.add_patch(wire_down_right)

# Electrons in external circuit
electron_path = [(0.1, 4), (0.1, 5), (5.9, 5), (5.9, 4)]
electron_count = 35
electron_radius = 0.07
liion_electrons = [plt.Circle(electron_path[0], electron_radius, color='gold')
for _ in range(electron_count)]
for e in liion_electrons:
    ax.add_patch(e)

# === Migrating Ions for Solid-State Battery ===
migrating_ions = []
for _ in range(60):
    x, y = np.random.uniform(8.2, 10.8), np.random.uniform(1.2, 3.7)
    ion = plt.Circle((x, y), 0.1, color='orange')
    migrating_ions.append(ion)
    ax.add_patch(ion)


ssb_targets_reached = [False for _ in migrating_ions]


# === Animation Function ===
def animate(frame):
    for i, ion in enumerate(liion_ions):
        x, y = ion.center
        vx, vy = liion_vels[i]
        x_new = x + vx
        y_new = y + vy

        if not (0.2 < x_new < 5.8):
            vx = -vx
            x_new = x + vx
        if not (1.1 < y_new < 3.9):
            vy = -vy
            y_new = y + vy

        ion.center = (x_new, y_new)
        liion_vels[i] = (vx, vy)
    
    for i, ion in enumerate(migrating_ions):
        x, y = ion.center
        target_x = np.random.uniform(11.6, 12.9)
        dx = (target_x - x) * 0.02
        dy = np.random.uniform(-0.01, 0.01)

        new_x = x + dx
        new_y = y + dy

        if not ssb_targets_reached[i]:
            if 12.25 < new_x < 13.0 and 1.1 < new_y < 3.9:
                ssb_targets_reached[i] = True
            ion.center = (new_x, new_y)

        else:
            jitter_x = np.random.uniform(-0.02, 0.02)
            jitter_y = np.random.uniform(-0.02, 0.02)
            x_new = x + jitter_x
            y_new = y + jitter_y

            if 11.5 < x_new < 13.0 and 1.1 < y_new < 3.9:
                ion.center = (x_new, y_new)


    for i, e in enumerate(liion_electrons):
        seg_len = 50 
        t = (frame + i * 10) % (seg_len * len(electron_path))
        seg = t // seg_len
        frac = (t % seg_len) / seg_len

        x0, y0 = electron_path[seg]
        x1, y1 = electron_path[(seg + 1) % len(electron_path)]
        e.center = (x0 + frac * (x1 - x0), y0 + frac * (y1 - y0))

        if seg == 3: 
            e.set_radius(0)
        elif seg == 0 and frac == 0: 
            e.set_radius(0.07)
            
# === Run Animation ===
ani = FuncAnimation(fig, animate, frames=500, interval=60)
plt.show()
