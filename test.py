import tkinter as tk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# =========================================
# FUZZY LOGIC SYSTEM
# =========================================

traffic = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'traffic'
)

waiting = ctrl.Antecedent(
    np.arange(0, 61, 1),
    'waiting'
)

green_time = ctrl.Consequent(
    np.arange(5, 21, 1),
    'green_time'
)

# Traffic Density
traffic['low'] = fuzz.trimf(
    traffic.universe,
    [0, 0, 40]
)

traffic['medium'] = fuzz.trimf(
    traffic.universe,
    [20, 50, 80]
)

traffic['high'] = fuzz.trimf(
    traffic.universe,
    [60, 100, 100]
)

# Waiting Time
waiting['short'] = fuzz.trimf(
    waiting.universe,
    [0, 0, 20]
)

waiting['medium'] = fuzz.trimf(
    waiting.universe,
    [10, 30, 50]
)

waiting['long'] = fuzz.trimf(
    waiting.universe,
    [40, 60, 60]
)

# Green Signal Time
green_time['short'] = fuzz.trimf(
    green_time.universe,
    [5, 5, 8]
)

green_time['medium'] = fuzz.trimf(
    green_time.universe,
    [7, 10, 13]
)

green_time['long'] = fuzz.trimf(
    green_time.universe,
    [12, 20, 20]
)

# Rules
rules = [

    ctrl.Rule(
        traffic['low'] & waiting['short'],
        green_time['short']
    ),

    ctrl.Rule(
        traffic['low'] & waiting['medium'],
        green_time['short']
    ),

    ctrl.Rule(
        traffic['low'] & waiting['long'],
        green_time['medium']
    ),

    ctrl.Rule(
        traffic['medium'] & waiting['short'],
        green_time['medium']
    ),

    ctrl.Rule(
        traffic['medium'] & waiting['medium'],
        green_time['medium']
    ),

    ctrl.Rule(
        traffic['medium'] & waiting['long'],
        green_time['long']
    ),

    ctrl.Rule(
        traffic['high'] & waiting['short'],
        green_time['long']
    ),

    ctrl.Rule(
        traffic['high'] & waiting['medium'],
        green_time['long']
    ),

    ctrl.Rule(
        traffic['high'] & waiting['long'],
        green_time['long']
    ),
]

system = ctrl.ControlSystem(rules)

# =========================================
# COLORS
# =========================================

BG = "#0b1220"
ROAD = "#1e293b"

RED = "#ef4444"
YELLOW = "#facc15"
GREEN = "#22c55e"

OFF = "#1f2937"
TEXT = "#e5e7eb"

CARD = "#111827"
ACCENT = "#38bdf8"

# =========================================
# WINDOW
# =========================================

root = tk.Tk()

root.title(
    "Fuzzy Smart Traffic Control"
)

root.state("zoomed")

root.configure(bg=BG)

# =========================================
# TITLE
# =========================================

tk.Label(
    root,
    text="🚦 Fuzzy Logic Smart Traffic System",
    font=("Segoe UI", 24, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=10)

tk.Label(
    root,
    text="Adaptive Smart-City Traffic Controller",
    font=("Segoe UI", 11),
    bg=BG,
    fg="#94a3b8"
).pack()

# =========================================
# MAIN FRAME
# =========================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(pady=20)

# =========================================
# CANVAS
# =========================================

canvas = tk.Canvas(
    main,
    width=700,
    height=500,
    bg=BG,
    highlightthickness=0
)

canvas.grid(
    row=0,
    column=0,
    padx=20
)

# =========================================
# MAIN ROADS
# =========================================

canvas.create_rectangle(
    280, 0,
    420, 500,
    fill=ROAD,
    outline=""
)

canvas.create_rectangle(
    0, 180,
    700, 320,
    fill=ROAD,
    outline=""
)

# =========================================
# 4-SIDE EMERGENCY LANES
# =========================================

# TOP
canvas.create_rectangle(
    430, 0,
    490, 180,
    fill="#334155",
    outline=""
)

# BOTTOM
canvas.create_rectangle(
    430, 320,
    490, 500,
    fill="#334155",
    outline=""
)

# LEFT
canvas.create_rectangle(
    0, 330,
    280, 390,
    fill="#334155",
    outline=""
)

# RIGHT
canvas.create_rectangle(
    420, 330,
    700, 390,
    fill="#334155",
    outline=""
)

# Labels
canvas.create_text(
    460,
    20,
    text="EMERGENCY",
    fill="white",
    font=("Segoe UI", 9, "bold")
)

canvas.create_text(
    460,
    480,
    text="EMERGENCY",
    fill="white",
    font=("Segoe UI", 9, "bold")
)

canvas.create_text(
    70,
    360,
    text="EMERGENCY",
    fill="white",
    font=("Segoe UI", 9, "bold")
)

canvas.create_text(
    630,
    360,
    text="EMERGENCY",
    fill="white",
    font=("Segoe UI", 9, "bold")
)

# =========================================
# ROAD MARKINGS
# =========================================

for i in range(0, 500, 40):

    canvas.create_line(
        350, i,
        350, i+20,
        fill="white",
        width=2
    )

for i in range(0, 700, 40):

    canvas.create_line(
        i, 250,
        i+20, 250,
        fill="white",
        width=2
    )

# Emergency Markings

for i in range(0, 180, 30):

    canvas.create_line(
        460, i,
        460, i+15,
        fill="#f87171",
        width=3
    )

for i in range(320, 500, 30):

    canvas.create_line(
        460, i,
        460, i+15,
        fill="#f87171",
        width=3
    )

for i in range(0, 280, 30):

    canvas.create_line(
        i, 360,
        i+15, 360,
        fill="#f87171",
        width=3
    )

for i in range(420, 700, 30):

    canvas.create_line(
        i, 360,
        i+15, 360,
        fill="#f87171",
        width=3
    )

# =========================================
# SIGNALS
# =========================================

def create_signal(x, y):

    canvas.create_rectangle(
        x-10, y-10,
        x+40, y+110,
        fill="#0f172a",
        outline=""
    )

    return {

        "red": canvas.create_oval(
            x, y,
            x+30, y+30,
            fill=OFF
        ),

        "yellow": canvas.create_oval(
            x, y+35,
            x+30, y+65,
            fill=OFF
        ),

        "green": canvas.create_oval(
            x, y+70,
            x+30, y+100,
            fill=OFF
        )
    }

north_south = create_signal(320, 20)
east_west = create_signal(20, 220)

# =========================================
# STATUS PANEL
# =========================================

panel = tk.Frame(
    main,
    bg=CARD,
    width=280,
    height=500
)

panel.grid(
    row=0,
    column=1
)

panel.pack_propagate(False)

tk.Label(
    panel,
    text="SYSTEM STATUS",
    font=("Segoe UI", 16, "bold"),
    bg=CARD,
    fg=TEXT
).pack(pady=15)

mode_label = tk.Label(
    panel,
    text="NORTH-SOUTH ACTIVE",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=ACCENT
)

mode_label.pack(pady=10)

timer_label = tk.Label(
    panel,
    text="5",
    font=("Segoe UI", 42, "bold"),
    bg=CARD,
    fg=TEXT
)

timer_label.pack()

fuzzy_label = tk.Label(
    panel,
    text="FUZZY TIME : 5s",
    font=("Segoe UI", 12, "bold"),
    bg=CARD,
    fg=GREEN
)

fuzzy_label.pack(pady=10)

# =========================================
# PEDESTRIAN
# =========================================

tk.Label(
    panel,
    text="🚶 Pedestrian",
    font=("Segoe UI", 13, "bold"),
    bg=CARD,
    fg=TEXT
).pack(pady=(25, 5))

pedestrian_indicator = tk.Label(
    panel,
    text="WAIT",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg=RED,
    width=12,
    pady=8
)

pedestrian_indicator.pack()

# =========================================
# EMERGENCY
# =========================================

tk.Label(
    panel,
    text="🚑 Emergency",
    font=("Segoe UI", 13, "bold"),
    bg=CARD,
    fg=TEXT
).pack(pady=(25, 5))

emergency_indicator = tk.Label(
    panel,
    text="NORMAL",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg=GREEN,
    width=12,
    pady=8
)

emergency_indicator.pack()

# =========================================
# TRAFFIC INPUT
# =========================================

traffic_val = tk.IntVar(value=50)

tk.Scale(
    root,
    label="Traffic Density",
    from_=0,
    to=100,
    variable=traffic_val,
    orient="horizontal",
    bg=BG,
    fg="white",
    font=("Segoe UI", 11)
).pack(fill="x", padx=50)

# =========================================
# STATES
# =========================================

phase = 0
timer = 5

waiting_counter = 0

pedestrian_requested = False
pedestrian_active = False

emergency_active = False

# =========================================
# LIGHT FUNCTIONS
# =========================================

def reset_lights():

    for s in [north_south, east_west]:

        canvas.itemconfig(
            s["red"],
            fill=OFF
        )

        canvas.itemconfig(
            s["yellow"],
            fill=OFF
        )

        canvas.itemconfig(
            s["green"],
            fill=OFF
        )

def ns_green():

    reset_lights()

    canvas.itemconfig(
        north_south["green"],
        fill=GREEN
    )

    canvas.itemconfig(
        east_west["red"],
        fill=RED
    )

def ew_green():

    reset_lights()

    canvas.itemconfig(
        east_west["green"],
        fill=GREEN
    )

    canvas.itemconfig(
        north_south["red"],
        fill=RED
    )

def ns_yellow():

    reset_lights()

    canvas.itemconfig(
        north_south["yellow"],
        fill=YELLOW
    )

    canvas.itemconfig(
        east_west["red"],
        fill=RED
    )

def ew_yellow():

    reset_lights()

    canvas.itemconfig(
        east_west["yellow"],
        fill=YELLOW
    )

    canvas.itemconfig(
        north_south["red"],
        fill=RED
    )

def all_red():

    reset_lights()

    canvas.itemconfig(
        north_south["red"],
        fill=RED
    )

    canvas.itemconfig(
        east_west["red"],
        fill=RED
    )

# =========================================
# FUZZY TIME
# =========================================

def calculate_fuzzy_time():

    global waiting_counter

    sim = ctrl.ControlSystemSimulation(system)

    sim.input['traffic'] = traffic_val.get()

    sim.input['waiting'] = min(
        waiting_counter,
        60
    )

    sim.compute()

    if 'green_time' not in sim.output:

        value = 10

    else:

        value = int(
            sim.output['green_time']
        )

    fuzzy_label.config(
        text=f"FUZZY TIME : {value}s"
    )

    return max(5, value)

# =========================================
# MAIN LOOP
# =========================================

def system_loop():

    global timer
    global phase
    global pedestrian_active
    global pedestrian_requested
    global waiting_counter

    # Emergency
    if emergency_active:

        all_red()

        mode_label.config(
            text="EMERGENCY MODE",
            fg=RED
        )

        emergency_indicator.config(
            text="ACTIVE",
            fg=RED
        )

        timer_label.config(
            text="STOP"
        )

        root.after(
            1000,
            system_loop
        )

        return

    else:

        emergency_indicator.config(
            text="NORMAL",
            fg=GREEN
        )

    # Pedestrian
    if pedestrian_active:

        all_red()

        pedestrian_indicator.config(
            text="WALK",
            fg=GREEN
        )

        mode_label.config(
            text="PEDESTRIAN CROSSING",
            fg=YELLOW
        )

        timer_label.config(
            text=f"{timer}"
        )

        timer -= 1

        if timer <= 0:

            pedestrian_active = False

            waiting_counter = 0

            timer = calculate_fuzzy_time()

        root.after(
            1000,
            system_loop
        )

        return

    else:

        pedestrian_indicator.config(
            text="WAIT",
            fg=RED
        )

    timer_label.config(
        text=f"{timer}"
    )

    # North South
    if phase == 0:

        mode_label.config(
            text="NORTH-SOUTH ACTIVE",
            fg=ACCENT
        )

        if timer <= 2:
            ns_yellow()
        else:
            ns_green()

    # East West
    else:

        mode_label.config(
            text="EAST-WEST ACTIVE",
            fg=ACCENT
        )

        if timer <= 2:
            ew_yellow()
        else:
            ew_green()

    timer -= 1

    waiting_counter += 1

    # Switch Phase
    if timer <= 0:

        if pedestrian_requested:

            pedestrian_requested = False

            pedestrian_active = True

            timer = 5

        else:

            waiting_counter = 0

            phase = 1 - phase

            timer = calculate_fuzzy_time()

    root.after(
        1000,
        system_loop
    )

# =========================================
# BUTTON FUNCTIONS
# =========================================

def pedestrian_request():

    global pedestrian_requested

    pedestrian_requested = True

def emergency_toggle():

    global emergency_active

    if emergency_active:
        return

    emergency_active = True

    direction = np.random.choice([
        "TOP",
        "BOTTOM",
        "LEFT",
        "RIGHT"
    ])

    # TOP
    if direction == "TOP":

        ambulance = canvas.create_rectangle(
            440, -80,
            480, -20,
            fill="white",
            outline=""
        )

        ambulance_text = canvas.create_text(
            460,
            -50,
            text="🚑",
            font=("Segoe UI", 18)
        )

        dx = 0
        dy = 12

    # BOTTOM
    elif direction == "BOTTOM":

        ambulance = canvas.create_rectangle(
            440, 520,
            480, 580,
            fill="white",
            outline=""
        )

        ambulance_text = canvas.create_text(
            460,
            550,
            text="🚑",
            font=("Segoe UI", 18)
        )

        dx = 0
        dy = -12

    # LEFT
    elif direction == "LEFT":

        ambulance = canvas.create_rectangle(
            -80, 340,
            -20, 380,
            fill="white",
            outline=""
        )

        ambulance_text = canvas.create_text(
            -50,
            360,
            text="🚑",
            font=("Segoe UI", 18)
        )

        dx = 12
        dy = 0

    # RIGHT
    else:

        ambulance = canvas.create_rectangle(
            720, 340,
            780, 380,
            fill="white",
            outline=""
        )

        ambulance_text = canvas.create_text(
            750,
            360,
            text="🚑",
            font=("Segoe UI", 18)
        )

        dx = -12
        dy = 0

    def move_ambulance():

        global emergency_active

        canvas.move(
            ambulance,
            dx,
            dy
        )

        canvas.move(
            ambulance_text,
            dx,
            dy
        )

        x1, y1, x2, y2 = canvas.coords(
            ambulance
        )

        inside = (
            -100 < x1 < 800 and
            -100 < y1 < 600
        )

        if inside:

            root.after(
                40,
                move_ambulance
            )

        else:

            canvas.delete(ambulance)
            canvas.delete(ambulance_text)

            emergency_active = False

            emergency_indicator.config(
                text="NORMAL",
                fg=GREEN
            )

    move_ambulance()

# =========================================
# BUTTONS
# =========================================

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="🚶 Request Crossing",
    command=pedestrian_request,
    bg=YELLOW,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    padx=20,
    pady=10,
    bd=0
).grid(
    row=0,
    column=0,
    padx=10
)

tk.Button(
    button_frame,
    text="🚑 Emergency Alert",
    command=emergency_toggle,
    bg=RED,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=20,
    pady=10,
    bd=0
).grid(
    row=0,
    column=1,
    padx=10
)

# =========================================
# START
# =========================================

timer = calculate_fuzzy_time()

system_loop()

ns_green()

root.mainloop()