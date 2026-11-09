*Disclosure: I work at INTERX, a Korean manufacturing AI company (founded 2020). This article is my personal summary of public research papers and a Korean government survey; it does not represent my employer's official position, and it does not recommend or compare any specific product.*

When you evaluate an AI visual inspection system, the most useful question is not "How accurate is it?" It is **"How many real defects does it miss, and how many good parts does it reject, on images from our own line that it has never seen?"** Research on industrial inspection keeps returning to the same point: on factory data where defects are rare, a single accuracy figure says very little.

Here is a short list of seven criteria you can put to every vendor in the same words:

- **Defect definition:** can the system use your defect types and your acceptance limits?
- **Metrics:** does the vendor report misses and false rejects separately?
- **Validation:** was it tested on your images, held out from training?
- **Data burden:** how many defect images, and who labels them?
- **Speed:** does a decision fit inside your takt time?
- **Change handling:** what happens when lighting, product variant, or camera changes?
- **Operations:** does it show why it flagged a part, and can you feed back wrong calls?

<figure><img src="/assets/ai-vision-inspection-criteria.jpg" alt="Cute small robot inspecting pastel parts on a conveyor with a camera and magnifying glass, holding a clipboard with check marks" width="1280" height="720" loading="lazy"><figcaption>Start with what the inspection AI misses, not how often it is right</figcaption></figure>


## Why "99% accuracy" is not enough

A January 2024 survey in *Applied System Innovation*, "Deep Learning for Automated Visual Inspection in Manufacturing and Maintenance: A Survey of Open-Access Papers" (Hütten et al.), reviewed 196 open-access papers. Accuracy was the most commonly reported metric, yet the authors note that it describes performance poorly when classes are imbalanced. That is the normal situation on a production line. If 1% of parts are defective, a system that calls everything "good" scores 99%.

A 2023 review of visual defect detection benchmarks (Carvalho et al., arXiv:2305.13261) makes the same argument and recommends looking at the **false negative rate** (defects passed as good) and the **false positive rate** (good parts rejected) instead. It adds a subtler warning. Summary metrics such as AUROC describe a whole family of decision thresholds, while a real line runs on one threshold. Ask for the numbers at the threshold you will actually use.

Which error matters more depends on the process. For a safety-critical part, a single escaped defect can be very costly. Where every false reject sends a part to manual re-inspection, false rejects drive labor cost. Hütten et al. list this choice between false positives and false negatives as a requirement that differs from one application to the next.

## Validation: whose images, and were they held out?

Carvalho et al. recommend separating training, validation, and test data, giving roughly 50–70%, 15–30%, and 15–30% as an example split, and evaluating on real-world data where possible. In procurement terms, ask three things. Where did the test images come from? Were any of them used in training? Over what period were they collected?

Public benchmark scores are a starting point, not evidence for your line. A 2023 survey of industrial image anomaly detection (Liu et al., arXiv:2301.11514) observes that most public datasets create anomalies on defect-free products instead of collecting defects from actual production lines. A demo that looks excellent on such data may behave differently under your lighting and on your parts.

## Data burden: supervised or "normal-only"?

According to Hütten et al., 97% of the papers they analyzed used supervised learning, which needs labeled examples of defects. If a vendor's approach is supervised, ask how many defect images it needs per defect type and who will label them.

Liu et al. describe unsupervised anomaly detection methods that train on normal images only and flag anything that looks different. This suits lines where defects are rare and hard to collect. The trade-off is that "different from normal" is not the same as "a scratch" or "a dent", so classifying defect types needs a separate design.

## The shop-floor conditions that decide long-term cost

Hütten et al. list the requirements industrial users raise most often. These include real-time processing, hardware constraints, scarce labeled data, consistent labels, generalization to changing conditions such as lighting, and explainability. Two of these are easy to forget during a pilot and expensive afterward:

1. **Change handling.** Ask what has to be redone when you add a product variant or move a camera, and how long it takes.
2. **Explainability and feedback.** Ask whether operators can see why a part was flagged and how wrong calls get back into the model.

## People still matter

Inspection by people is not perfect either. Citing earlier studies, Hütten et al. note that human error rates in complex visual inspection can reach 20–30%. They also estimate that methods take about three years on average to move from research to industrial use. A practical first phase is to run AI decisions and human decisions side by side and collect the cases where they disagree.

## What to prepare before talking to vendors

Two assets make every comparison fairer:

- **A defect definition sheet:** photos of each defect type and the limit where a part is still acceptable.
- **A held-out image set from your own line,** kept away from any training, so every candidate is tested the same way.

In Korea, quality is one of the main reasons factories invest in smart manufacturing. In the Ministry of SMEs and Startups' 2024 smart manufacturing survey (released 28 April 2025), 37.1% of adopters named improving quality control as a goal, second only to production efficiency (56.5%).

The full comparison template, with a column for each candidate, is in the original Korean post: [sungsiwon.github.io/ko/ai-vision-inspection-criteria/](https://sungsiwon.github.io/ko/ai-vision-inspection-criteria/)

## Sources
- Hütten et al., "Deep Learning for Automated Visual Inspection in Manufacturing and Maintenance: A Survey of Open-Access Papers," *Applied System Innovation* 7(1):11 (2024): https://www.mdpi.com/2571-5577/7/1/11
- Carvalho et al., "A Review of Benchmarks for Visual Defect Detection in the Manufacturing Industry," arXiv:2305.13261 (2023): https://arxiv.org/abs/2305.13261
- Liu et al., "Deep Industrial Image Anomaly Detection: A Survey," arXiv:2301.11514 (2023): https://arxiv.org/abs/2301.11514
- Ministry of SMEs and Startups, "2024 Smart Manufacturing Innovation Survey results" (2025-04-28, Korean): https://www.korea.kr/briefing/pressReleaseView.do?newsId=156686561

*I work at INTERX, a Korean manufacturing AI company (founded 2020). Views are my own.*
