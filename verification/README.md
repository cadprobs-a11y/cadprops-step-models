# Release validation — 2026-10-04

## Passed

- Thirty STEP models imported into Open CASCADE, each with valid geometry, at least one solid and positive volume.
- All thirty IGES exports reimported successfully and passed geometry validation. Maximum permitted envelope difference: 0.02 mm.
- All thirty STL exports loaded as triangle meshes. Maximum permitted envelope difference against source STEP: 0.15 mm.
- Thirty actual-geometry previews inspected. All metadata records contain source, author, license and original-file SHA-256. The 23 community STEP files preserve original bytes; the seven CADProps originals use CC0.
- The public GitHub README rendered with previews and download links. About website and topics saved; default branch is `main` and visibility is public.
- The full ZIP was downloaded by clicking the public GitHub README link in Chrome. All 180 part files matched the prepared SHA-256 list, including all 90 CAD files.
- Six category representatives downloaded from public GitHub URLs with HTTP 200 and matching SHA-256. These span STEP, STL and IGES.
- Seven linked CADProps tool, accuracy and privacy pages returned HTTP 200.

## Failed and not verified

The real CADProps workspace upload flow was attempted with the six representatives, retried, and attempted again with only the socket-head screw STEP after a reload. The page returned **“Upload verification failed.”** before conversion. The browser console reported **Cloudflare Turnstile error 300030**. No security check was bypassed.

Consequently, online rendering, online dimension comparison and a CADProps-generated CSV export are **not verified**. `browser-acceptance.csv` records expected dimensions from source geometry and the incomplete online result; it is an acceptance log, not a CADProps export. This does not change the successful local geometry checks or public download checks. A successful online run remains outstanding.

A GT2 16-tooth pulley candidate failed the IGES round-trip validity check during preparation and was replaced by the supplied 20-tooth pulley. The rejected candidate is not included.

## Evidence

- [Geometry/export checks](geometry-validation.csv)
- [SHA-256 manifest](SHA256SUMS.txt)
- [Public ZIP verification](public-download-validation.json)
- [Six representative download records](representative-downloads.json)
- [Browser acceptance log](browser-acceptance.csv)
- [CADProps link checks](website-links.json)
- [Published repository screenshot](screenshots/github-repository.jpg)
- [Rendered catalog screenshot](screenshots/github-catalog.jpg)
- [Workspace upload failure screenshot](screenshots/cadprops-upload-blocked.jpg)

## Repeat the browser acceptance

1. Download the complete ZIP from the root README and extract it. Compare the part files with `SHA256SUMS.txt`.
2. In the CADProps workspace, open the six files listed in `representative-downloads.json`, one at a time if necessary. Files are uploaded to the server for processing.
3. Confirm visible geometry, record source-axis X/Y/Z dimensions in millimetres, and compare with the expected envelopes. Use up to 0.02 mm for CAD imports and 0.15 mm for the STL mesh samples.
4. Capture each rendered model and its properties. Export the available properties CSV through the workspace UI and retain it separately from this acceptance log.
5. Mark online checks passed only after the six models render and the dimension comparisons succeed.

No CADProps application files were changed or deployed for this repository publication. No full application E2E suite was run.
