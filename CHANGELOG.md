# Changelog

All notable changes to the **N5KWD Ham & Electronics Toolkit for TI-84**.

Versioning (semver): on every change, bump `VERSION` in `N5KWD.py` **and** the
menu title in `NKWD.8xp.txt`, add an entry here, rebuild the download zip, then
commit and tag `vX.Y.Z`.

## v1.0.0 &mdash; 2026-09-15

First tagged release.

- Eight tools in one menu: Ohm's Law / Power, Series/Parallel Resistors,
  Reactance (Xc/Xl), LC Resonance, Antenna Lengths, Coax Loss, SWR / Return Loss,
  dBm / Watts / µV.
- Two versions: **Python** (`N5KWD.py`, for CE Python & Evo) and **TI-BASIC**
  (`NKWD.8xp.txt` listing, for every TI-84 Plus).
- Each tool now **echoes your inputs, shows the formula, then the result** &mdash;
  self-documenting and a teaching aid.
- Python **pauses after each tool** (`[enter for menu]`) so the answer stays on
  the calculator's small screen instead of scrolling off when the menu redraws.
- Version shown in the menu header of both versions.
