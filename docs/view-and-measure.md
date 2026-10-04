# View and measure a downloaded part

1. Choose a part in the [catalog](../README.md) and download its STEP file.
2. Open the [STEP viewer](https://www.cadprops.com/tools/step-viewer/) and select the downloaded file. Selection starts an upload to the processing server.
3. Wait for processing and the visible model. Check any geometry or missing-component warning.
4. Use Fit, rotation and the structure panel to inspect the loaded bodies.
5. Read X, Y and Z dimensions in Properties. Compare them with the part README’s millimetre envelope, using the original axes.
6. For valid closed solids, inspect volume and area. Export a properties CSV to keep the values and warnings together.

## A useful first sample

The [electronics tray](../parts/enclosures-and-plates/electronics-tray/README.md) is a CADProps original: 80 × 60 × 24 mm. Its walls and base are nominally 3 mm. The tray is an open container made from a closed solid wall, so it has a material volume despite having no lid.

## Compare model revisions

Keep source coordinates consistent before using the [CAD comparison tool](https://www.cadprops.com/tools/compare-cad-files/). Different parts in this catalog are not automatically aligned mating pairs. Display changes such as hiding a part do not change the original geometry or overall property totals.

## Read results in context

CAD solid volume and approximate STL mesh volume are different methods. Assembly totals sum occurrences without subtracting overlaps. Material density is a user assumption, not a material certification stored in these models. See [formats and units](formats-and-units.md).
