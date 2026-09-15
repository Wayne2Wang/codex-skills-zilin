# Technical and Editorial Review Protocol

Use this protocol for content audits of computer vision and robotics papers. Adapt depth to the user's requested scope, but use every section for a full submission audit.

## 1. Mathematical and notation audit

Create a symbol ledger with: symbol, first definition, mathematical type or tensor shape, domain/range, units, indices, time dependence, and later uses.

For every displayed equation, verify:

- all symbols are defined before or immediately after use;
- scalar, vector, matrix, tensor, set, function, distribution, and random-variable notation is distinguishable;
- dimensions and tensor shapes make every sum, product, norm, concatenation, and comparison valid;
- multiplication semantics are explicit where ambiguity matters: scalar-vector product, dot product, matrix product, Hadamard product, outer product, or cross product;
- indices, superscripts, subscripts, bounds, dummy variables, and time steps are consistent;
- sums combine the indexed term rather than accidentally repeating an unindexed term;
- losses and rewards are scalar; tuples, intervals, cases, indicators, maxima, clipping, and expectations are syntactically and semantically correct;
- domains and boundary cases are valid, including closed versus open intervals, division by zero, normalization, empty sets, and logarithms;
- probability expressions have valid conditioning and normalization;
- coordinate frames, transformations, units, signs, and reference points are consistent;
- prose, diagrams, algorithms, and supplementary definitions agree with the equation;
- equation numbering and references point to the intended expression.

Do not infer a missing definition from familiarity with the field. If implementation details would determine correctness, mark the item "Resolve before submission" and say exactly what must be confirmed.

## 2. Method and reproducibility audit

Check that a knowledgeable reader could reconstruct:

- observations, actions, commands, coordinate frames, control rates, and action interpretation;
- architecture inputs/outputs and trainable versus frozen components;
- complete objectives, signs, gates, schedules, weights, thresholds, and aggregation rules;
- training stages, data generation, randomization, optimization, seeds, and stopping criteria;
- evaluation protocols, sample counts, uncertainty/statistics, success criteria, and exclusion rules;
- metric definitions with units and time integration where needed;
- sim-to-sim and sim-to-real splits, hardware settings, safety constraints, and deployment assumptions;
- baseline implementation, tuning budget, training data, and comparison fairness.

Flag only omissions that affect interpretation, replication, or claim validity.

## 3. Claims and empirical consistency

Trace each major abstract, introduction, result, and conclusion claim to evidence. Check:

- values agree across prose, tables, figures, captions, and supplement;
- percentages distinguish relative change from percentage-point change;
- metric direction and labels agree with plotted values;
- error, signed error, reward, energy, power, work, and cost are not conflated;
- sample size and aggregation match what the caption claims;
- "transfer," "generalization," "zero-shot," "single policy," and similar terms match the actual training/evaluation setup;
- ablations isolate the claimed component;
- visual examples do not silently substitute for quantitative evidence;
- limitations do not contradict headline claims.

Treat overclaiming as a required fix only when the manuscript's own evidence contradicts it. Otherwise report it as a material reviewer risk and identify the evidentiary gap.

## 4. Strict language and formatting pass

Report definite problems only:

- grammar, agreement, articles, tense, malformed parallel constructions, fragments, and comma splices;
- typos, capitalization, spelling of method names, venue names, simulators, datasets, and robots;
- ambiguous antecedents that change technical meaning;
- inconsistent terminology or notation for the same object;
- broken citations, labels, panel references, captions, section references, and table/figure numbering;
- unexplained visual encodings, colors, arrows, or boxes;
- unreadable, clipped, overlapping, or rasterized text and equations;
- bibliography formatting or metadata defects.

Do not report a sentence merely because an alternative sounds smoother. Preserve the author's voice when the current wording is grammatical and technically clear.

## 5. Reviewer-style assessment

Judge the factors that commonly drive decisions at strong CV and robotics venues:

- technical soundness and internal consistency;
- novelty relative to the most relevant prior work;
- significance and scope of the contribution;
- experimental coverage, baselines, ablations, and statistical support;
- clarity and reproducibility;
- real-robot or deployment evidence where central to the claim;
- ethical, safety, and limitation disclosures where applicable.

Separate direct evidence from inference. Rank only the few issues likely to affect the decision; do not manufacture a balanced list of weaknesses.

## Finding record

For every actionable finding capture:

- severity and classification;
- PDF page and section, equation, figure, table, or reference number;
- exact anchor text or symbol;
- why it is wrong or risky;
- exact correction when determinable;
- evidence or cross-reference used to reach the conclusion.

Consolidate recurring typographic defects into one finding with all affected locations.
