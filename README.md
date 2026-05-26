# FDA FSVP repository
The purpose of this repository is to keep track of all the FSVP records TrueTech Inc has established for suppliers that are in the Agroverse's transparent direct to consumer distribution network

## How it works
The suppliers folder has sub-folders. Each of them represents the repository of the FSVP records we have established on the supplier we have included in our Agroverse network

The regulations folder contains all the documentation of known USA FDA FSVP regulations that we should comply with regarding the FSVP records

## Machine-readable entity profiles (for LLMs / agents)

Start at **`entities.index.json`** at the repo root — a single index that points to every per-entity profile:

- `truetech_inc.entity.json` — TrueTech Inc, the US FSVP + CBP importer of record
- `suppliers/<name>/entity.json` — one profile per supplier (legal name, CNPJ/DUNS/FDA FFR, address, products, FSVP status, and an index of that folder's source documents)

These are derived from the committed PDF records. FDA registration PINs and any personal CPF are intentionally excluded.