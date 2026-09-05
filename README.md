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

## Machine-readable entity profiles (for LLMs / agents)

Start at **`entities.index.json`** at the repo root — a single index that points to every per-entity profile:

- `truetech_inc.entity.json` — TrueTech Inc, the US FSVP + CBP importer of record
- `suppliers/<name>/entity.json` — one profile per supplier (legal name, CNPJ/DUNS/FDA FFR, address, products, FSVP status, and an index of that folder's source documents)

These are derived from the committed PDF records. FDA registration PINs and any personal CPF are intentionally excluded.