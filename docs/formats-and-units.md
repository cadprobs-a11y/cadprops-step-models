# STEP, STL, IGES and units

## STEP

STEP stores CAD boundary-representation geometry. Community STEP files are supplied unchanged. The catalog’s envelope and property values are calculated after Open CASCADE normalizes the loaded geometry to millimetres. CADProps originals are written in millimetres.

## STL

STL is a triangle mesh generated from the STEP geometry. Coordinates use millimetres, but STL itself does not declare a length unit. Select millimetres when importing into your slicer or mesh editor. These meshes use a 0.05 mm linear tessellation deflection and a 0.15 radian angular setting; they are not a substitute for the original CAD surface definition. Tessellation settings are not a certified manufacturing tolerance.

## IGES

IGES files are exported from the loaded STEP B-Rep using Open CASCADE’s B-Rep mode, in millimetres. Names, assembly hierarchy, colors and topology may differ across applications. Check the import report; CAD-property availability depends on whether your application recognizes suitable closed solids.

## Verify scale and suitability

Each part README lists the X × Y × Z geometry envelope. Orientation affects those extents. Compare a known dimension after import and read geometry warnings before relying on area or volume. A recognized format or plausible preview does not certify a part for manufacture.

The source catalog retains upstream standard and product names for identification. Dimensions are model measurements, not a guarantee of conformity to those standards or a manufacturer specification.

## Save a file from GitHub

A STEP or IGES link may open as text in your browser. Use **Save As** to save the original file with its `.step` or `.iges` extension. Alternatively, download the whole repository as ZIP from the catalog and extract the part files. STL is often handled as a download directly.
