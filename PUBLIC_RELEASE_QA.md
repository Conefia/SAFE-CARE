# Public release QA

- Clean-package confidentiality scan: **PASS**.
- Scanned for the client case-study name, client app name, private source labels, and generated stamp text across Markdown, metadata, DOCX XML, and extracted PDF text.
- Ten clean branded DOCX files and ten matching PDFs were rendered and visually reviewed for clipping, overlap, broken glyphs, table overflow, headers, and footers.
- The framework executive overview renders correctly and is complete; it is a short multi-page summary, not a single page.
- All document titles use SAFE-CARE™ on the first prominent use; subsequent framework references are plain SAFE-CARE.
- Every branded document includes the authorship line, v1.0 date, licensing, citation placeholder, trademark legend, copyright, and Conefia letterhead.
- GitHub Markdown was regenerated with clean headings, separate tables, readable references, and the README opening line required by the editor instructions.
- Machine-readable JSON and YAML files were syntax-validated.
- Private tracked-change review copies are stored outside the clean package because tracked deletions retain source strings. **Do not publish the redline ZIP.**

## Pending publisher actions

1. Obtain written client approval.
2. Publish the clean package to GitHub.
3. Enable GitHub-Zenodo integration and create release `v1.0.0`.
4. Insert the minted DOI and repository URL into all citation metadata and branded assets.
5. Re-export, rerun QA, and preserve the immutable release evidence for the petition exhibit.
