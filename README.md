# barn53 kicad library
## Contains self-constructed symbols, footprints and models

----
# KiCad Path

Define the following path in the KiCad path configuration:

```${BARN53_KICAD_DIR} = <...>/barn53-kicad-library/```

## Add the symbol- and the footprint libraries

- Symbol Library

    ```${BARN53_KICAD_DIR}/library/barn53-kicad.lib```

- Footprint Library

    ```${BARN53_KICAD_DIR}/footprints/barn53-kicad.pretty```
-----

# KiCad External AutoRouter FreeRouting

https://github.com/freerouting/freerouting


-----
# Also add the digikey library

https://github.com/Digi-Key/digikey-kicad-library


------

# JLCPCB SMT Assembly

## Generate BOM with
`plugins/bom_jlcpcb.xsl`

## Position File

https://support.jlcpcb.com/article/84-how-to-generate-the-bom-and-centroid-file-from-kicad

Position file column names  must be renamed as follows:

Designator|Val|Package|Mid X|Mid Y|Rotation|Layer
---|---|---|---|---|---|---


