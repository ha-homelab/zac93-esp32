#!/usr/bin/env python3
"""Generate the repository's original SVG illustrations (standard library only)."""

from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / "assets/diagrams"
OUT.mkdir(parents=True, exist_ok=True)


def start(w, h, title):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto-start-reverse" markerUnits="strokeWidth"><path d="M0,0 L0,6 L8,3 z" fill="context-stroke"/></marker></defs>',
        f'<rect width="{w}" height="{h}" rx="22" fill="#f4f7fb"/>',
    ]


def text(s, x, y, value, size=22, color="#142c47", weight="normal", anchor="start"):
    s.append(
        f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-family="Arial,Helvetica,sans-serif" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'
    )


def rect(s, x, y, w, h, fill="white", stroke="#d8e2ee", r=16):
    s.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    )


def line(s, x1, y1, x2, y2, color="#4a647e", width=4, arrow=False):
    a = ' marker-end="url(#arrow)"' if arrow else ""
    s.append(
        f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"{a}/>'
    )


def save(s, name):
    (OUT / name).write_text("\n".join(s + ["</svg>"]) + "\n")


for variant, title, tx, rx, caveat in [
    (
        "wroom",
        "ESP32-WROOM-32 / DevKit",
        17,
        16,
        "WROOM only: GPIO16/17 may be reserved on WROVER modules.",
    ),
    (
        "s3",
        "ESP32-S3 / DevKitC-1",
        17,
        18,
        "S3 baseline: N8 / 8 MB flash. Confirm the actual module and header labels.",
    ),
]:
    s = start(1200, 710, title + " to Zooz ZAC93 wiring")
    text(s, 48, 56, title + " + ZAC93", 34, weight="bold")
    text(s, 48, 94, "Four wires • 3.3 V logic • UART 115200 / 8N1", 23)
    rect(s, 48, 130, 325, 410, "#173d63", "#173d63")
    rect(s, 785, 130, 367, 410, "#fff5d9", "#dfbf69")
    text(s, 75, 174, "ESP32 board", 26, "white", "bold")
    text(s, 812, 174, "ZAC93 module", 26, weight="bold")
    specs = [
        ("3V3", "Pin 1 · 3V3", 230, "#c74042", "POWER", False),
        ("GND", "Pin 6 · GND", 307, "#34404c", "COMMON GROUND", False),
        (f"GPIO{tx} · TX", "Pin 8 · RX", 384, "#a66b00", "ESP32 → ZAC93", True),
        (f"GPIO{rx} · RX", "Pin 10 · TX", 461, "#087d89", "ZAC93 → ESP32", True),
    ]
    for src, dst, y, col, label, arr in specs:
        text(s, 75, y + 8, src, 24, "white", "bold")
        text(s, 812, y + 8, dst, 24, weight="bold")
        text(s, 578, y - 13, label, 16, col, "bold", "middle")
        if "ZAC93 →" in label:
            line(s, 780, y, 380, y, col, 5, arr)
        else:
            line(s, 380, y, 780, y, col, 5, arr)
        for x in (373, 785):
            s.append(
                f'<circle cx="{x}" cy="{y}" r="7" fill="{col}" stroke="white" stroke-width="2"/>'
            )
    text(s, 75, 515, "USB powers this board", 18, "#cfdeed")
    text(s, 812, 515, "Leave all other pins open", 18)
    rect(s, 48, 566, 1104, 104, "#e5edf6", "#d8e2ee")
    text(
        s,
        70,
        601,
        "Disconnect USB before wiring. Never connect 5 V to ZAC93.",
        23,
        weight="bold",
    )
    text(s, 70, 635, caveat, 18)
    text(
        s,
        48,
        693,
        "Electrical diagram, not a scale drawing. Match signals and pin numbers, not board orientation.",
        16,
    )
    save(s, "wiring-" + variant + ".svg")

s = start(1200, 550, "ZAC93 connector signal map")
text(s, 48, 56, "ZAC93 · identify signals before connecting", 32, weight="bold")
text(s, 48, 97, "Logical pin map based on the Raspberry Pi 1–10 header numbering", 22)
text(
    s,
    48,
    129,
    "This grid is not a mating-side view. Use the board silkscreen and the reference photographs.",
    18,
)
labels = [
    [
        (1, "3V3"),
        (3, "SDA / unused"),
        (5, "SCL / unused"),
        (7, "RESET / unused"),
        (9, "GND"),
    ],
    [(2, "NC"), (4, "NC"), (6, "GND"), (8, "RX to ZAC93"), (10, "TX from ZAC93")],
]
for row, items in enumerate(labels):
    for col, (num, label) in enumerate(items):
        x = 48 + col * 225
        y = 175 + row * 135
        fill = "#fff0c1" if num in (1, 6, 8, 10) else "#e7edf4"
        rect(s, x, y, 205, 110, fill)
        text(s, x + 18, y + 38, str(num), 30, weight="bold")
        text(s, x + 18, y + 78, label, 19)
text(
    s,
    48,
    471,
    "Our four wires use pins 1, 6, 8 and 10. Pin 9 is another ground; leave it unused.",
    20,
    weight="bold",
)
text(
    s,
    48,
    509,
    "Hardware v2 connects pin 7 to reset. This project does not drive pin 7.",
    19,
)
save(s, "zac93-header.svg")

s = start(1200, 590, "Z-Wave to Home Assistant system architecture")
text(
    s, 48, 60, "One radio. One Z-Wave driver. Two firmware domains.", 32, weight="bold"
)
items = [
    (48, "Z-Wave device", ["PIR • switch • sensor", "US/CA/MX variant"]),
    (335, "ZAC93", ["Zooz radio firmware", "Serial API controller"]),
    (622, "ESP32", ["ESPHome zwave_proxy", "Wi-Fi network bridge"]),
    (909, "Z-Wave JS", ["Driver + network keys", "Home Assistant client"]),
]
for x, title, lines in items:
    rect(s, x, 180, 243, 200, "white")
    text(s, x + 20, 229, title, 25, weight="bold")
    for n, t in enumerate(lines):
        text(s, x + 20, 282 + n * 30, t, 17)
for x, label in [(295, "RF"), (582, "UART"), (869, "API")]:
    line(s, x, 255, x + 32, 255, "#087d89", 3, True)
    text(s, x + 15, 157, label, 17, anchor="middle")
rect(s, 48, 420, 1104, 123, "#173d63", "#173d63")
text(
    s,
    73,
    461,
    "ESPHome runs on ESP32. The ZAC93 keeps its Zooz firmware.",
    26,
    "white",
    "bold",
)
text(
    s,
    73,
    500,
    "Z-Wave devices appear through the Z-Wave integration; ESPHome exposes bridge diagnostics.",
    20,
    "#d7e5f2",
)
save(s, "architecture.svg")

s = start(1200, 870, "Diagnostic sequence for a ZAC93 ESPHome bridge")
text(s, 48, 58, "Diagnose in order", 34, weight="bold")
text(
    s,
    48,
    96,
    "An online ESP32 does not prove that the Z-Wave radio is communicating.",
    22,
)
rows = [
    (
        "1",
        "POWER",
        "3.3 V at ZAC93; shared ground; no hot or loose connections.",
        "#b0343b",
    ),
    (
        "2",
        "NETWORK",
        "DHCP address + TCP 6053 reachable from the driver host.",
        "#8b6300",
    ),
    (
        "3",
        "API",
        "Correct encrypted esphome:// URL; ESPHome logs available.",
        "#007a89",
    ),
    (
        "4",
        "RADIO",
        "Z-Wave JS reports controller identity, firmware and Home ID.",
        "#235aab",
    ),
    (
        "5",
        "DEVICE",
        "Inclusion completes; PIR events and battery reports arrive.",
        "#227348",
    ),
]
for i, (num, title, desc, col) in enumerate(rows):
    y = 137 + i * 131
    rect(s, 48, y, 1104, 104)
    s.append(f'<circle cx="100" cy="{y + 52}" r="28" fill="{col}"/>')
    text(s, 100, y + 62, num, 28, "white", "bold", "middle")
    text(s, 150, y + 37, title, 22, col, "bold")
    text(s, 150, y + 74, desc, 20)
    if i < 4:
        line(s, 100, y + 105, 100, y + 128, "#91a5b9", 3, True)
text(
    s,
    48,
    836,
    "Stop at the first failing layer. Do not reset or re-pair a network to fix a transport problem.",
    21,
    weight="bold",
)
save(s, "diagnostic-ladder.svg")

s = start(1200, 540, "Two different connection URLs used by the system")
text(s, 48, 59, "Use the right URL in the right application", 32, weight="bold")
for y, title, url, desc in [
    (
        110,
        "Z-Wave JS UI → Settings → Z-Wave → Serial Port",
        "esphome://zac93-wroom.local:6053?key=ENCODED_KEY",
        "Connects the driver to the ESP32. The key is private; encode + / =.",
    ),
    (
        300,
        "Home Assistant → Z-Wave → server URL",
        "ws://zwave-js-ui:3000",
        "Connects Home Assistant to the driver, not directly to the ESP32.",
    ),
]:
    rect(s, 48, y, 1104, 160)
    text(s, 75, y + 38, title, 24, weight="bold")
    text(s, 75, y + 84, url, 26, "#087d89")
    text(s, 75, y + 127, desc, 19)
text(
    s,
    48,
    507,
    "Illustration of fields, not a screenshot. Hostnames are examples. The web UI itself uses port 8091.",
    18,
)
save(s, "connection-fields.svg")
print("Generated six original SVG diagrams.")
