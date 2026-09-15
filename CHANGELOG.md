# Changelog

All notable changes to the **N5KWD Ham & Electronics Toolkit for TI-84**.

Versioning (semver): on every change, bump `VERSION` in `N5KWD.py` **and** the
menu title in `NKWD.8xp.txt`, add an entry here, rebuild the download zip, then
commit and tag `vX.Y.Z`.

## v1.0.1 &mdash; 2026-09-15

Packaging fix.

- **The v1.0.0 download zip shipped the wrong `N5KWD.py`** &mdash; the pre-fix
  file, without the after-each-tool pause and without the `VERSION` line. On a
  real calculator the result scrolled off before the menu redrew, so tools
  looked like they returned "no result." Rebuilt the zip from the correct
  sources; the pause and input/formula/result echo are now actually in the
  download.
- The download zip now also includes `CHANGELOG.md`.
- Version bumped to 1.0.1 in both the Python and TI-BASIC menu headers.

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
