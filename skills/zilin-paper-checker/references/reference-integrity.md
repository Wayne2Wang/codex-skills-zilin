# Exhaustive Reference-Integrity Protocol

Use this protocol for every full paper audit. The goal is to detect fabricated, conflated, retracted, incomplete, and materially miscited references without falsely accusing authors when records are merely hard to access.

## Required coverage

Inventory every bibliography entry and every in-text citation. Reconcile these counts:

- total bibliography entries;
- unique cite keys or reference numbers;
- citations with no bibliography entry;
- bibliography entries never cited;
- duplicate or near-duplicate entries;
- entries verified, verified with corrections, unresolved, withdrawn/retracted, or likely fabricated.

Do not sample. If tool, access, or time limits prevent exhaustive verification, state exactly which entries remain unchecked and do not claim completion.

## Authoritative evidence hierarchy

Prefer records in this order:

1. Official publisher or proceedings page, such as IEEE Xplore, ACM Digital Library, Springer proceedings, CVF Open Access, PMLR, official NeurIPS proceedings, OpenReview venue pages, or official RSS proceedings.
2. DOI registry metadata and a resolving DOI.
3. The official arXiv abstract record for a preprint, including version and withdrawal status.
4. An institutional or author publication page when no canonical proceedings record exists.

Search engines, Google Scholar, Semantic Scholar, DBLP, and citation aggregators are discovery aids. Do not use a search-result snippet or an aggregator alone as final proof that a suspicious work exists.

## Per-entry verification

For each reference:

1. Parse the claimed title, authors, venue or repository, year, volume/issue/pages, DOI, arXiv identifier, and URL.
2. Resolve identifiers directly. Normalize DOI and arXiv forms before comparing.
3. Search the exact title, then a normalized distinctive title phrase plus first author, then author/venue/year combinations.
4. Open an authoritative record and compare:
   - title, allowing punctuation and capitalization differences;
   - core author identity and order;
   - publication venue or preprint status;
   - year, volume, issue, pages or article number;
   - DOI/arXiv identifier and URL destination;
   - correction, withdrawal, or retraction status.
5. Inspect the abstract or paper when needed to determine whether the work supports the nearby in-text claim. A real paper cited for an unrelated claim is a citation-support problem, not a hallucinated reference.
6. Record a direct evidence link and any discrepancy. Use the canonical metadata in the proposed repair.

For references to software, datasets, videos, technical reports, project pages, or corporate releases, verify the resource at its official owner page and ensure the entry identifies its type and date adequately.

## Status vocabulary

Assign exactly one primary status to every entry:

- **Verified:** an authoritative record matches the identity and the bibliography contains adequate metadata.
- **Verified - metadata fix required:** the work exists, but one or more material fields are wrong or incomplete.
- **Verified preprint/non-archival:** the work exists, but the entry or prose incorrectly implies peer review or archival publication.
- **Duplicate:** the same work appears more than once; identify the canonical entry.
- **Withdrawn/retracted/corrected:** the canonical source carries this status; explain the submission risk.
- **Unresolved:** no conclusive authoritative record was found, access was blocked, or multiple works could match. Specify the searches performed and what the author must supply.
- **Likely fabricated or conflated:** use only after the escalation procedure below produces no credible matching record or shows that fields from different works were combined.

Never equate an incomplete citation with a hallucination. Never infer fabrication solely from a future year, an unusual author list, a dead URL, a title typo, or absence from one index.

## Escalation before a fabrication finding

Before using **Likely fabricated or conflated**:

1. Try the supplied DOI, arXiv ID, and URL.
2. Search at least two materially different title/author queries.
3. Search the claimed venue's official proceedings for the claimed year when available.
4. Search at least one independent canonical registry or repository, such as Crossref or arXiv.
5. Check for title changes between preprint and publication and for workshop/main-conference variants.
6. Document the negative search path and distinguish "not found" from "source inaccessible."

If access remains inconclusive, use **Unresolved**, not **Likely fabricated**. Recommend removing or replacing an entry only when the evidence supports that action.

## Citation-support check

Map each in-text citation occurrence to its surrounding claim. Check for:

- cited work whose abstract or method does not support the claim;
- one citation range containing unrelated works;
- attribution to the wrong paper in a same-author series;
- claims of first, state of the art, publication venue, or publication year contradicted by the canonical record;
- primary technical claims supported only by secondary surveys when a primary source is available.

Classify support problems separately from metadata problems.

## Required report table

Produce one row per bibliography entry with:

| Ref/cite key | Status | Canonical identity | Evidence | Discrepancy or required action | Claim support |
|---|---|---|---|---|---|

Use direct links to authoritative records. For large bibliographies, place the exhaustive table in a separate artifact if that keeps the main report readable, but still summarize counts and all non-verified entries in the main response.

## Completion test

The number of status rows must equal the number of unique bibliography entries after explicitly accounting for duplicates. Spot-checking, checking only suspicious-looking citations, or reporting only failures does not satisfy an exhaustive reference audit.
