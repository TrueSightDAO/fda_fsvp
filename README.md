# FDA FSVP repository
The purpose of this repository is to keep track of all the FSVP records TrueTech Inc has established for suppliers that are in the Agroverse's transparent direct to consumer distribution network

## How it works
The suppliers folder has sub-folders. Each of them represents the repository of the FSVP records we have established on the supplier we have included in our Agroverse network

The regulations folder contains all the documentation of known USA FDA FSVP regulations that we should comply with regarding the FSVP records

## Site inspection documents — signature rule (ALL future docs)

Every site inspection / site visit PDF filed in this repo MUST be signed off with the **official ink signature image** from the private `TrueSightDAO/signature_assets` repo:

- **Asset:** `gary_teh/gary_teh_signature_transparent.png` (transparent PNG, ink-only)
- **Where:** composited between "Sincerely," and the typed TrueTech block (Zhiwen Teh, President, TrueTech Inc)
- **Access:** read-only via the narrow-scope `GITHUB_READ_PAT` — NEVER copy the asset into this public repo, a public PR, or a shared chat/group
- A **plain typed name is NOT acceptable** on a site-visit PDF (rule adopted 2026-09-05, Fazenda Dona Rosa site visit)
- Full process: `agentic_ai_context/fsvp/SITE_VISIT_PROCESS.md`

## Site-visit PDF photos — EXIF orientation rule (learned 2026-09-10)

Site-visit PDFs must embed photos through **`tools/site_visit_images.py`** (`img_flow`),
never a raw reportlab `RLImage` with a hand-computed box.

Incident: on the Sítio Torres record, `IMG_9682.HEIC` rendered **rotated 90°** — Apple's
HEIC→JPEG export writes pixels *already upright* but leaves a **stale** EXIF Orientation
tag (e.g. `6`), and the ad-hoc converter applied `exif_transpose()` on top of that (rotating
upright pixels sideways) *and* resized every image to a fixed landscape box (squashing
portraits). reportlab's `RLImage` never consults EXIF and never rescales.

The helper enforces: **(1)** embed pixels AS-IS (no transpose) for Apple HEIC derivatives,
**(2)** downscale aspect-preserving and return the true pixel size so the layout box matches,
**(3)** strip the stale tag on write. Pass `respect_exif=True` only for raw sensor JPEGs whose
tag genuinely describes un-rotated pixels. See the module docstring for the full rationale.

## Machine-readable entity profiles (for LLMs / agents)

Start at **`entities.index.json`** at the repo root — a single index that points to every per-entity profile:

- `truetech_inc.entity.json` — TrueTech Inc, the US FSVP + CBP importer of record
- `suppliers/<name>/entity.json` — one profile per supplier (legal name, CNPJ/DUNS/FDA FFR, address, products, FSVP status, and an index of that folder's source documents)

These are derived from the committed PDF records. FDA registration PINs and any personal CPF are intentionally excluded.

## Farmer & plot onboarding guide (field tool for FSVP inspections)

For LLMs / agents: the bilingual (EN/PT) illustrated onboarding guide used by Jedielcio (facilitator)
to photograph a farm + plot and its bean-to-bar equipment with GPS for future FDA FSVP site inspections
lives in the **agentic_ai_context** repo (committed 2026-09-08):

- **Guide PDF (v6, 9 pp):** `agentic_ai_context/fsvp/FSVP_Onboarding_Guide_EN_PT.pdf`
- **Operating runbook + policies:** `agentic_ai_context/fsvp/ONBOARDING_GUIDE_EN_PT.md` (search terms that surface it: FSVP, onboarding guide, Jedielcio, melanger, WhatsApp photo protocol, farm onboarding, reforestation plot, CEPOTX site code)
- **Example photo assets:** `agentic_ai_context/fsvp/assets/` (incl. the Gary-supplied melanger photo, 2026-09-08)

WhatsApp send protocol (v4): the farmer opens the message with **Farm Name + CEPOTX site code** (e.g. La do Sítio — V-06-29) before photos, and sends photos as **documents (not image messages)** so GPS/EXIF survives. Site-code registry: `suppliers/cepotx/site_codes.md`.