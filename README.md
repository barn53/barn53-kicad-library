# barn53 kicad library
Contains self-constructed symbols, footprints and models

# KiCad Path

Define the following path in the KiCad path configuration:

```${BARN53_KICAD_DIR} = <...>/barn53-kicad-library/```

## Add the symbol- and the footprint libraries

- Symbol Library

    ```${BARN53_KICAD_DIR}/library/barn53-kicad.lib```

- Footprint Library

    ```${BARN53_KICAD_DIR}/footprints/barn53-kicad.pretty```

# KiCad External AutoRouter FreeRouting

https://layouteditor.com/#download

- Look for file ```freeRouting.jar``` in the bundle
  start it with: ```> java -jar freeRouting.jar```
