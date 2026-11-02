*Disclosure: I work at INTERX, a Korean manufacturing AI company. This article is my personal summary of public sources (peer-reviewed papers and Korean government documents) and does not represent my employer's official position.*

Injection molding looks simple from the outside: melt plastic, fill a mold, hold pressure, cool, eject. The difficulty is in the details. A 2022 review in *The International Journal of Advanced Manufacturing Technology* identifies warpage and shrinkage as the most common quality problems in plastic injection molding, and explains that the effects of process parameters such as mold temperature, melt temperature, injection rate, injection pressure, holding pressure, and holding and cooling time are coupled with each other. That coupling is why parameter setting has relied so heavily on the long experience of skilled operators.

It is also why "AI for defect root cause analysis" is a reasonable idea and why it needs careful reading. Below is how the published research breaks the problem down.

<figure><img src="/assets/injection-molding-defect-ai.jpg" alt="Cartoon of a molding machine with a sensor graph, a camera, and a magnifying glass, connected by dotted lines to a small robot with a clipboard." width="1280" height="720" loading="lazy"><figcaption>Three clues for finding the cause of a molding defect: sensor signals, vision inspection, and process settings</figcaption></figure>

## The short answer

AI approaches to injection molding defects fall into three groups, defined by the data they use:

- **Process-to-quality models** learn the relationship between machine settings and measured quality. They answer: *with these settings, will the part be good?*
- **Sensor anomaly detection** learns what a normal cycle looks like in signals such as cavity pressure or melt cushion. It answers: *is this shot different from usual?*
- **Vision inspection** finds defects in images of the part. It answers: *where is the defect, and what does it look like?*

None of these, on its own, tells you *why*. Getting closer to a cause requires an interpretation layer, usually called explainable AI (XAI), and then a confirmation step on the machine.

## Approach 1: Process-to-quality models, plus explainability

The idea is to collect, for each cycle, the settings and actual values from the machine together with a quality result (pass/fail, weight, dimensions), then train a model that maps one to the other.

A 2025 study in the *Journal of Manufacturing Processes*, "Explainable AI for Correct Root Cause Analysis of Product Quality in Injection Moulding," is a useful example because it tests the interpretation step directly. The researchers varied six settings (cooling time, injection speed, melt temperature, mold temperature, packing pressure, and packing time) across 77 combinations, repeating each 20 times for 1,540 cycles. Machine data and part weights were joined using cycle numbers marked on the parts.

Two findings matter for practitioners:

- The settings interacted. Melt temperature, for instance, changed how much packing pressure and packing time affected part weight.
- The choice of explanation method changed the "root cause." One method (ICE) pointed to packing time as the main cause no matter which setting had actually been changed. Another (SHAP) pointed to the setting that had really been changed.

In other words, a model can predict well and still lead an operator to adjust the wrong knob if the explanation method ignores interactions.

## Approach 2: Anomaly detection on sensor time series

Instead of predicting quality from settings, this approach watches the signals each cycle produces.

- A 2022 paper in *Sensors*, "Machine Learning in Injection Molding: An Industry 4.0 Method of Quality Prediction," classified part quality using features extracted from in-mold pressure curves. A decision tree classifier reached average accuracy above 90 percent even with only one to three training samples per class. It was one mold under controlled settings, so the result should not be generalized carelessly, but it shows how informative cavity pressure can be.
- A 2024 paper in *IEEE Access* combined an LSTM autoencoder with a statistical process control chart to monitor melt cushion. The autoencoder's reconstruction error set extra thresholds alongside the usual control limits, so the system could flag not only values outside the limits but also gradual upward and downward trends that classic control-chart rules can miss.

Anomaly detection does not name a cause either, but it tells you *when* something started drifting and *which* signal moved, which is where most root cause investigations begin.

## Approach 3: Vision inspection

Cameras see the result rather than the process. A 2024 study in *The International Journal of Advanced Manufacturing Technology* proposed a semi-supervised training strategy for a U-Net to segment flash defects on molded parts at the pixel level, reporting 89.40 percent mIoU and 94.95 percent recall. It used defect-free samples to reduce the need for labeled data and released an open dataset of flash defects. The authors frame the output as decision support for adjusting molding machine parameters, which is the honest way to describe vision inspection: precise about *what* and *where*, silent about *why* unless linked to process data.

## How they fit together

A practical sequence looks like this:

1. **Detect**: flag cycles whose sensor signals leave the normal pattern.
2. **Predict**: model how settings relate to quality for the defect you care about.
3. **Interpret**: use an explanation method that accounts for interactions to rank likely causes.
4. **Verify**: change the suspected setting deliberately and confirm the effect, then feed the result back as data.

Vision inspection supplies the quality labels and defect locations that steps 2 and 3 depend on.

## Korea's policy context

In South Korea, injection molding sits inside industrial policy. A December 2021 amendment to the enforcement decree of Korea's Root Industry Act expanded the list of "root technologies" from six to fourteen, adding injection molding and press forming among the new categories (effective December 16, 2021). Then, on January 22, 2025, the Ministry of Trade, Industry and Energy announced ten priority tasks for spreading industrial AI. In the accompanying expert recommendations, the predictive maintenance and quality management task listed data quality and integration difficulties as key problems and named explainable AI among the technologies expected to develop.

That combination, a foundational process plus a stated policy interest in explainability, is a big part of why root cause analysis for molding defects gets so much attention in Korea right now.

## What to take away

- Start with one costly defect and make sure settings, sensor values, and inspection results are linked by cycle.
- Treat AI output as a ranked list of candidate causes, not a verdict.
- Check how your explanation method handles interactions between settings.
- Confirm on the machine before you change the standard recipe.

*The original Korean FAQ (six questions, with a comparison table): [sungsiwon.github.io/ko/injection-molding-defect-ai](https://sungsiwon.github.io/ko/injection-molding-defect-ai/)*

## Sources

- Zhao N. et al., "Recent progress in minimizing the warpage and shrinkage deformations by the optimization of process parameters in plastic injection molding: a review," *The International Journal of Advanced Manufacturing Technology* (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC8831005/
- Muaz M. et al., "Explainable AI for Correct Root Cause Analysis of Product Quality in Injection Moulding," *Journal of Manufacturing Processes* (2025), preprint: https://arxiv.org/abs/2505.01445
- Párizs R. D. et al., "Machine Learning in Injection Molding: An Industry 4.0 Method of Quality Prediction," *Sensors* 22(7), 2704 (published 2022-03-31): https://www.mdpi.com/1424-8220/22/7/2704
- Tayalati F. et al., "Hybrid Approach Integrating Deep Learning-Autoencoder With Statistical Process Control Chart for Anomaly Detection: Case Study in Injection Molding Process," *IEEE Access* (2024): https://doi.org/10.1109/ACCESS.2024.3425582
- Yu Z. et al., "Semi-supervised auxiliary learning for surface defect detection and segmentation of injection-molded products from small image datasets," *The International Journal of Advanced Manufacturing Technology* (published 2024-03-04): https://link.springer.com/article/10.1007/s00170-024-13275-7
- Ministry of Trade, Industry and Energy, press release on ten priority tasks for industrial AI (2025-01-22, Korean): https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/170072/view
- Yonhap News, report on the expansion of root technologies from 6 to 14 (2021-12-14, Korean): https://www.yna.co.kr/view/AKR20211213151400003

*I work at INTERX, a Korean manufacturing AI company. Views are my own.*
