# =====================================================================
#  N5KWD Ham & Electronics Toolkit  -  TI-84 Plus CE Python / Evo
#  Free & open source (MIT).  More tools + the online versions:
#      https://n5kwd.com/tools
# ---------------------------------------------------------------------
#  This file is written to run under the calculator's Python app
#  (MicroPython).  It is also a teaching example: every calculation is
#  a few lines of plain Python you can read, change, and learn from.
#
#  Each tool echoes your inputs, shows the formula, then the answer.
# =====================================================================

VERSION = "1.0.0"

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
    print("\n-- Ohm's Law / Power --")
    print("(enter any two, blank the rest)")
    v = ask("V (V): ", True)
    i = ask("I (A): ", True)
    r = ask("R (ohm): ", True)
    p = ask("P (W): ", True)

    # Solve from whichever two were given, and show the formula each uses.
    if v is not None and i is not None:
        r, p = v / i, v * i
        print("Given V=%.4g, I=%.4g" % (v, i))
        print("R = V/I = %.4g ohm" % r)
        print("P = V*I = %.4g W" % p)
    elif v is not None and r is not None:
        i, p = v / r, v * v / r
        print("Given V=%.4g, R=%.4g" % (v, r))
        print("I = V/R = %.4g A" % i)
        print("P = V^2/R = %.4g W" % p)
    elif v is not None and p is not None:
        i, r = p / v, v * v / p
        print("Given V=%.4g, P=%.4g" % (v, p))
        print("I = P/V = %.4g A" % i)
        print("R = V^2/P = %.4g ohm" % r)
    elif i is not None and r is not None:
        v, p = i * r, i * i * r
        print("Given I=%.4g, R=%.4g" % (i, r))
        print("V = I*R = %.4g V" % v)
        print("P = I^2*R = %.4g W" % p)
    elif i is not None and p is not None:
        v, r = p / i, p / (i * i)
        print("Given I=%.4g, P=%.4g" % (i, p))
        print("V = P/I = %.4g V" % v)
        print("R = P/I^2 = %.4g ohm" % r)
    elif r is not None and p is not None:
        v, i = math.sqrt(p * r), math.sqrt(p / r)
        print("Given R=%.4g, P=%.4g" % (r, p))
        print("V = sqrt(P*R) = %.4g V" % v)
        print("I = sqrt(P/R) = %.4g A" % i)
    else:
        print("Enter exactly two values.")


# =====================================================================
# 2.  SERIES / PARALLEL RESISTORS
# =====================================================================
def resistors():
    print("\n-- Series / Parallel Resistors --")
    raw = input("Values (space separated): ").split()
    vals = [float(x) for x in raw if x]
    if not vals:
        print("No values entered."); return
    mode = input("(S)eries or (P)arallel? ").strip().lower()
    shown = " ".join("%g" % x for x in vals)
    if mode.startswith("p"):
        total = 1.0 / sum(1.0 / x for x in vals)   # parallel: reciprocal of the reciprocals
        print("Parallel: " + shown)
        print("R = 1/(1/R1+1/R2+..)")
        print("  = %.4g ohm" % total)
    else:
        print("Series: " + shown)
        print("R = R1+R2+..")
        print("  = %.4g ohm" % sum(vals))


# =====================================================================
# 3.  REACTANCE  (Xc / Xl)
#     Xc = 1 / (2*pi*f*C),  Xl = 2*pi*f*L
# =====================================================================
def reactance():
    print("\n-- Reactance --")
    fmhz = ask("Frequency (MHz): ")
    w = 2 * math.pi * fmhz * 1e6                 # angular frequency, omega
    c = ask("Capacitance (pF, 0 skip): ")
    l = ask("Inductance (uH, 0 skip): ")
    print("f=%g MHz" % fmhz)
    if c > 0:
        print("Xc = 1/(2*pi*f*C), C=%g pF" % c)
        print("   = %.4g ohm" % (1.0 / (w * c * 1e-12)))
    if l > 0:
        print("Xl = 2*pi*f*L, L=%g uH" % l)
        print("   = %.4g ohm" % (w * l * 1e-6))


# =====================================================================
# 4.  LC RESONANCE
#     f = 1 / (2*pi*sqrt(L*C))
# =====================================================================
def lc_resonance():
    print("\n-- LC Resonant Frequency --")
    lu = ask("Inductance (uH): ")
    cp = ask("Capacitance (pF): ")
    f = 1.0 / (2 * math.pi * math.sqrt(lu * 1e-6 * cp * 1e-12))
    print("L=%g uH, C=%g pF" % (lu, cp))
    print("f = 1/(2*pi*sqrt(L*C))")
    print("  = %.4f MHz" % (f / 1e6))


# =====================================================================
# 5.  ANTENNA LENGTHS
# =====================================================================
def antenna():
    print("\n-- Antenna Lengths --")
    f = ask("Frequency (MHz): ")
    print("f=%g MHz  (x0.3048 for m)" % f)
    print("wavelen  984/f = %.2f ft" % (984.0 / f))
    print("1/2 dipl 468/f = %.2f ft" % (468.0 / f))
    print("1/4 vert 234/f = %.2f ft" % (234.0 / f))
    print("5/8 vert 585/f = %.2f ft" % (585.0 / f))


# =====================================================================
# 6.  COAX LOSS
#     Matched loss from the cable's rated loss per 100 ft.
# =====================================================================
def coax_loss():
    print("\n-- Coax Loss --")
    per100 = ask("Loss (dB/100 ft): ")
    length = ask("Length (ft): ")
    pin = ask("Power W (0 skip): ")
    loss = per100 * length / 100.0
    print("loss = %g*%g/100" % (per100, length))
    print("     = %.2f dB" % loss)
    if pin > 0:
        pout = pin * 10 ** (-loss / 10.0)        # dB -> power ratio
        print("Pout = %g*10^(-loss/10)" % pin)
        print("     = %.2f W (%.0f%%)" % (pout, 100.0 * pout / pin))


# =====================================================================
# 7.  SWR  /  RETURN LOSS
# =====================================================================
def swr():
    print("\n-- SWR / Return Loss --")
    s = ask("SWR (e.g. 1.5): ")
    g = (s - 1) / (s + 1)                         # reflection coefficient
    print("SWR=%g" % s)
    print("gamma=(SWR-1)/(SWR+1)")
    print("     = %.4f" % g)
    if g != 0:
        print("RL = -20*log(gamma)")
        print("   = %.2f dB" % (-20 * math.log10(abs(g))))
    print("refl = gamma^2 = %.2f%%" % (g * g * 100))


# =====================================================================
# 8.  dBm  /  WATTS  /  MICROVOLTS
# =====================================================================
def dbm():
    print("\n-- dBm / Watts / uV (50 ohm) --")
    d = ask("Power (dBm): ")
    watts = 10 ** ((d - 30) / 10.0)               # dBm -> watts
    uv = math.sqrt(watts * 50.0) * 1e6            # P = V^2/R  ->  V, in microvolts
    print("%g dBm" % d)
    print("W = 10^((dBm-30)/10)")
    print("  = %.4g W" % watts)
    print("uV = sqrt(W*50)*1e6")
    print("   = %.4g uV" % uv)


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
        print("\n== N5KWD TOOLKIT v" + VERSION + " ==")
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
