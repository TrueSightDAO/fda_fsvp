# FDA Product Codes (PNSI) — durable reference

**Purpose:** a single, view-anytime lookup mapping our cacao/Agroverse products to the
**FDA product codes** required on a US Prior Notice (PNSI). Before this file, the codes
existed only inside past PN PDFs in `suppliers/<name>/`, so every filing meant re-deriving
them by hand. Keep this file current as new products/codes are filed.

Maintained by: TrueSight DAO Autopilot (Sophia Truesight). Questions → thread 10800.

---

## Product → code mapping

| FDA Product Code | Product | Category note | Provenance |
|---|---|---|---|
| `34BGN04` | Cacao Nibs | ground/processed cocoa nibs | filed-PN precedent (2024–25) |
| `34BDN05` | Cacao Mass / Liquor | cocoa paste/liquor, bars & mass | filed-PN precedent (2024–25) |
| `34YGO99` | Cacao Molasses | molasses | filed-PN precedent (2024) |
| `34AHN99` | Cacao Almonds (**beans**) | cocoa BEANS (PT *amêndoas de cacau*), incl. Pará samples | governor-endorsed 2026-10-07 |
| `34BHN05` | Ceremonial Cacao | ceremonial cacao mass/paste, pouches | governor-endorsed 2026-10-07 |
| `34BHN04` | Cacao Tea | cacao tea (herbal) | governor-endorsed 2026-10-07 |
| `34BHN03` | Cacao Butter | cocoa butter | governor-endorsed 2026-10-07 |

> ⚠️ **"Cacao Almonds" = cocoa BEANS** — Portuguese *amêndoas de cacau* is the cacao
> **seed/bean**, **not** tree nuts. File under the cocoa-bean code (`34AHN99`), never a nut/allergen code.

> ℹ️ FDA product codes are distinct from Brazilian **NCM** codes. NCM is the customs/tax
> classification (e.g. 1801.00.00 cocoa beans); the FDA product code is the PNSI artifact class.

---

## Filed Prior Notice — F26X30142399 (Black King → TrueTech, SFO air)

- **Envelope / PN №:** `F26X30142399` · **Entry Identifier:** `###-4317322-5` · **Entry Type:** Consumption
- **Port:** San Francisco Airport, CA (2801) · **Arrival:** 10/08/2026 14:30 · **Mode:** Air
- **Carrier:** TAP Portugal, flight `TP237` · **AWB Master/House:** `04731753223`
- **Submitter/Importer:** TrueTech Inc · **Manufacturer (all 9):** MATHEUS REIS PEREIRA (Brazil)
- **Filed:** 10/06/2026, PN v15.0.0 · PDF: `suppliers/black_king/20261006_fda_prior_notice_cacao_9_articles_sfo_air.pdf`

| # | Product Name (as filed) | Packaging (units × unit size) | Qty | Net kg | FDA Product Code |
|---|---|---|---|---|---|
| 0001 | Cacao Nibs Kraft Pouch 8oz | 129 × 8oz pouch (≈0.227 kg) | 129 UN | 29.26 | `34BGN04` |
| 0002 | Cacao Mass Bar 500g | 37 × 500 g bar | 37 UN | 18.50 | `34BDN05` |
| 0003 | Cacao Nibs 10KG | 8 × 10 KG bag | 80 KG | 80.00 | `34BGN04` |
| 0004 | Cacao Almonds | 1 × 10 KG bag | 10 KG | 10.00 | `34AHN99` |
| 0005 | Ceremonial Cacao Kraft Pouch 200g | 169 × 200 g pouch | 169 UN | 33.80 | `34BHN05` |
| 0006 | Cacao Nibs (KG) | 10 × 10 KG bag | 100 units-KG (net 99.50) | 99.50 | `34BGN04` |
| 0007 | Cacao Tea KG | 2 × 10.5 KG bag | 21 KG | 21.00 | `34BHN04` |
| 0008 | Cacao Butter | 1 × 5 KG block | 5 KG | 5.00 | `34BHN03` |
| 0009 | Cacao Almonds samples from Para | 1 × 5 KG bag | 5 KG | 5.00 | `34AHN99` |
| | **TOTAL** | | | **302.06** | |

> **Note (article 0006):** packed as **10 × 10 KG** bags (nominal 100 KG) but the declared **net weight is 99.50 KG** — a fill/top-limit variance. Packaging shown as supplied by the governor; net weight is authoritative as filed on the PN.
