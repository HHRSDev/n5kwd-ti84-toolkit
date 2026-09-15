# =====================================================================
#  N5KWD Ham & Electronics Toolkit  -  TI-84 Plus CE Python / Evo
#  Free & open source (MIT).  More tools + the online versions:
#      https://n5kwd.com/tools
# ---------------------------------------------------------------------
#  This file is written to run under the calculator's Python app
#  (MicroPython).  It is also a teaching example: every calculation is
#  a few lines of plain Python you can read, change, and learn from.
# =====================================================================

import math

# The speed of light gives us the two constants every antenna formula
# uses.  In free space a half-wave dipole is 468 / f (feet) and a
# quarter-wave is 234 / f, where f is the frequency in megahertz.
# (The 468, not 492, already allows for real-wire "end effect".)
C_FT = 984.0        # feet per wavelength * MHz  (one full wavelength = 984 / f ft)


# ---------------------------------------------------------------------
# Small helper: ask for a number, and allow a blank entry to mean
# "unknown" (returns None) so one routine can solve for the missing one.
# ---------------------------------------------------------------------
def ask(prompt, blank_ok=False):
    while True:
        s = input(prompt).strip()
        if s == "" and blank_ok:
            return None
        try:
            return float(s)
        except ValueError:
            print("  Please enter a number.")


# =====================================================================
# 1.  OHM'S LAW  &  POWER
#     Enter any TWO of V, I, R, P (leave the others blank) - solve the rest.
# =====================================================================
def ohms_law():
    print("\n-- Ohm's Law / Power --  (blank = unknown)")
    v = ask("Voltage V (V): ", True)
    i = ask("Current I (A): ", True)
    r = ask("Resistance R (ohm): ", True)
    p = ask("Power P (W): ", True)

    # Fill in V, I, R, P from whichever two the user supplied.
    if v is not None and i is not None:
        r, p = v / i, v * i
    elif v is not None and r is not None:
        i, p = v / r, v * v / r
    elif v is not None and p is not None:
        i, r = p / v, v * v / p
    elif i is not None and r is not None:
        v, p = i * r, i * i * r
    elif i is not None and p is not None:
        v, r = p / i, p / (i * i)
    elif r is not None and p is not None:
        v, i = math.sqrt(p * r), math.sqrt(p / r)
    else:
        print("  Enter exactly two values."); return

    print("  V = %.4g V" % v)
    print("  I = %.4g A" % i)
    print("  R = %.4g ohm" % r)
    print("  P = %.4g W" % p)


# =====================================================================
# 2.  SERIES / PARALLEL RESISTORS
#     Enter values separated by spaces; pick the connection.
# =====================================================================
def resistors():
    print("\n-- Series / Parallel Resistors --")
    raw = input("Resistor values (space separated): ").split()
    vals = [float(x) for x in raw if x]
    if not vals:
        print("  No values entered."); return
    mode = input("(S)eries or (P)arallel? ").strip().lower()
    if mode.startswith("p"):
        total = 1.0 / sum(1.0 / r for r in vals)   # parallel: reciprocal of the sum of reciprocals
        print("  Parallel total = %.4g ohm" % total)
    else:
        print("  Series total = %.4g ohm" % sum(vals))   # series: just add them up


# =====================================================================
# 3.  REACTANCE  (Xc / Xl)
#     Xc = 1 / (2*pi*f*C),  Xl = 2*pi*f*L
# =====================================================================
def reactance():
    print("\n-- Reactance --")
    f = ask("Frequency (MHz): ") * 1e6          # work in hertz internally
    w = 2 * math.pi * f                          # angular frequency, omega
    c = ask("Capacitance (pF, 0 to skip): ")
    l = ask("Inductance (uH, 0 to skip): ")
    if c > 0:
        print("  Xc = %.4g ohm" % (1.0 / (w * c * 1e-12)))
    if l > 0:
        print("  Xl = %.4g ohm" % (w * l * 1e-6))


# =====================================================================
# 4.  LC RESONANCE
#     f = 1 / (2*pi*sqrt(L*C))
# =====================================================================
def lc_resonance():
    print("\n-- LC Resonant Frequency --")
    l = ask("Inductance (uH): ") * 1e-6
    c = ask("Capacitance (pF): ") * 1e-12
    f = 1.0 / (2 * math.pi * math.sqrt(l * c))
    print("  f = %.4f MHz" % (f / 1e6))


# =====================================================================
# 5.  ANTENNA LENGTHS
#     From the frequency: wavelength and the common cut lengths.
# =====================================================================
def antenna():
    print("\n-- Antenna Lengths --")
    f = ask("Frequency (MHz): ")
    wl = C_FT / f                                # full wavelength in feet
    print("  Wavelength    = %.2f ft (%.2f m)" % (wl, wl * 0.3048))
    print("  1/2 dipole    = %.2f ft (%.2f m)" % (468.0 / f, 468.0 / f * 0.3048))
    print("  1/4 vertical  = %.2f ft (%.2f m)" % (234.0 / f, 234.0 / f * 0.3048))
    print("  5/8 vertical  = %.2f ft" % (585.0 / f))


# =====================================================================
# 6.  COAX LOSS
#     Matched loss from the cable's rated loss per 100 ft.
# =====================================================================
def coax_loss():
    print("\n-- Coax Loss --")
    per100 = ask("Cable loss (dB / 100 ft): ")
    length = ask("Run length (ft): ")
    pin = ask("Input power (W, 0 to skip): ")
    loss = per100 * length / 100.0
    print("  Total loss = %.2f dB" % loss)
    if pin > 0:
        pout = pin * 10 ** (-loss / 10.0)        # dB -> power ratio
        print("  Power out  = %.2f W (%.0f%% delivered)" % (pout, 100.0 * pout / pin))


# =====================================================================
# 7.  SWR  /  RETURN LOSS
#     Enter SWR to get return loss and reflected power.
# =====================================================================
def swr():
    print("\n-- SWR / Return Loss --")
    s = ask("SWR (e.g. 1.5): ")
    gamma = (s - 1) / (s + 1)                     # reflection coefficient
    rl = -20 * math.log10(abs(gamma)) if gamma != 0 else float("inf")
    print("  Reflection coeff = %.4f" % gamma)
    print("  Return loss      = %.2f dB" % rl)
    print("  Power reflected  = %.2f %%" % (gamma * gamma * 100))


# =====================================================================
# 8.  dBm  /  WATTS  /  MICROVOLTS
#     Convert a power level between the units hams use.
# =====================================================================
def dbm():
    print("\n-- dBm / Watts / uV (50 ohm) --")
    d = ask("Power (dBm): ")
    watts = 10 ** ((d - 30) / 10.0)               # dBm -> watts
    uv = math.sqrt(watts * 50.0) * 1e6            # P = V^2/R  ->  V, in microvolts
    print("  %.2f dBm = %.4g W" % (d, watts))
    print("  = %.4g uV into 50 ohm" % uv)


# ---------------------------------------------------------------------
# The menu.  On the calculator this loops until you pick 0 to quit.
# ---------------------------------------------------------------------
TOOLS = [
    ("Ohm's Law / Power", ohms_law),
    ("Series/Parallel R", resistors),
    ("Reactance Xc/Xl", reactance),
    ("LC Resonance", lc_resonance),
    ("Antenna Lengths", antenna),
    ("Coax Loss", coax_loss),
    ("SWR / Return Loss", swr),
    ("dBm / Watts / uV", dbm),
]


def main():
    while True:
        print("\n===== N5KWD TOOLKIT =====")
        for n, (name, _) in enumerate(TOOLS, 1):
            print("%d. %s" % (n, name))
        print("0. Quit")
        choice = input("Choose: ").strip()
        if choice == "0" or choice == "":
            print("73!  -  n5kwd.com/tools")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(TOOLS):
            TOOLS[int(choice) - 1][1]()
            # Pause so the answer stays on the calculator's small screen until
            # you're ready - without this, redrawing the menu scrolls it away.
            input("\n[enter for menu] ")
        else:
            print("  Pick a number from the menu.")


main()
