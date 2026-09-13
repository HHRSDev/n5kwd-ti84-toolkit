# N5KWD Ham &amp; Electronics Toolkit for TI-84

Free, open-source ham radio and electronics **calculator programs that run on the calculator** — the
TI-84 that lives in a lot of shacks and nearly every US classroom. It ports the online tools at
**[n5kwd.com/tools](https://n5kwd.com/tools)** to an offline, in-the-field form, in **two languages**:

- **`N5KWD.py`** — Python (for the TI-84 Plus CE Python and the new Evo). Heavily commented, so it doubles
  as a *learn-Python-by-real-uses* example.
- **`NKWD.8xp.txt`** — TI-BASIC source listing (runs on **every** TI-84 Plus, and TI-83 Plus for the math).

> **License:** MIT · **Guide:** how to load & use it, and the same tools online, at
> **[n5kwd.com/tools](https://n5kwd.com/tools)**

## The tools

One menu, eight of the most-used calculators:

| # | Tool | Online version |
|---|------|----------------|
| 1 | Ohm's Law / Power | [ohmslawcalculator](https://n5kwd.com/ohmslawcalculator) |
| 2 | Series / Parallel Resistors | [resistorcombinationcalculator](https://n5kwd.com/resistorcombinationcalculator) |
| 3 | Reactance (Xc / Xl) | [reactancecalculator](https://n5kwd.com/reactancecalculator) |
| 4 | LC Resonance | [lcresonance](https://n5kwd.com/lcresonance) |
| 5 | Antenna Lengths | [dipolecalculator](https://n5kwd.com/dipolecalculator) |
| 6 | Coax Loss | [coaxlosscalculator](https://n5kwd.com/coaxlosscalculator) |
| 7 | SWR / Return Loss | [swrcalculator](https://n5kwd.com/swrcalculator) |
| 8 | dBm / Watts / µV | [dbmconverter](https://n5kwd.com/dbmconverter) |

## Try the Python version now (desktop)

```
python N5KWD.py
```

It runs anywhere Python does. On the calculator, send `N5KWD.py` with TI Connect CE (it becomes a `.8xv`),
then open the **Python App** and Run it.

## Getting it onto a calculator

Full, beginner-friendly, step-by-step instructions — TI Connect CE for a real calculator, or the free CEmu
emulator — are here: **[How to Load &amp; Use](https://n5kwd.com/tools)**. In short:

- **TI-BASIC (`.8xp`):** send it with TI Connect CE, then `[prgm]` → `NKWD` → `[enter]`.
- **Python (`.py`):** send it with TI Connect CE (it converts to `.8xv`), then `[apps]` → **Python** →
  File Manager → **Run**.

## Works on

TI-84 Plus CE · TI-84 Plus CE Python · TI-84 Plus CE **Evo** · older TI-83/84 Plus (TI-BASIC math). Python
requires the CE Python or Evo. No calculator? Run it on the free **[CEmu](https://ce-programming.github.io/CEmu/)**
emulator (it needs a ROM copied from your own calculator).

## Contributing

Pull requests welcome — add a tool, fix a formula, or improve the comments. Keep programs numeric (no
diagrams on a calculator screen) and keep the header link back to n5kwd.com. Only original code, please —
no third-party programs.

## Roadmap

This is the starter set. Next: the rest of the site's diagram-free calculators (time constant, filter cutoff,
E-series, wire gauge, grid distance, CW timing, and more), grouped download files, and a CEmu demo video.

## License

[MIT](LICENSE) — free to use, change, and share. Built by David C. Taylor, **N5KWD**.
