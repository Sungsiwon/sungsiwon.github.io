*Disclosure: I work at INTERX, a Korean manufacturing AI company (founded 2020). This article is my personal summary of an international standard, a NIST-affiliated paper, and Korean government surveys; it does not represent my employer's official position.*

You can only see the impact of manufacturing AI **against a baseline measured before deployment, using the same definitions**. Choose the metrics from ISO 22400, the international standard that defines KPIs for manufacturing operations management. A practical pattern is to pair one or two KPIs that the AI acts on directly with one composite KPI that shows the whole picture.

Three things to know first:

- **ISO 22400-2** defines 34 KPIs at the manufacturing operations management level (roughly, the MES level), each with a formula, unit, and intended audience.
- **OEE** (overall equipment effectiveness) = Availability × Effectiveness × Quality ratio.
- **A baseline** is the same KPI, defined the same way, recorded before the AI goes live. Without it, there is no "impact" to report.

<figure><img src="/assets/manufacturing-ai-kpi-oee.jpg" alt="A small robot in a factory pointing at three gauges of different colors, with a tape measure and a stopwatch nearby" width="1280" height="720" loading="lazy"><figcaption>Impact is not a single "after" number. It is the difference measured with the same ruler before and after</figcaption></figure>

## The OEE formula, as the standard defines it

ISO 22400-2:2014 defines the OEE index as Availability × Effectiveness × Quality ratio, where:

- **Availability** = actual production time (APT) ÷ planned busy time (PBT)
- **Effectiveness** = planned run time per item (PRI) × produced quantity (PQ) ÷ APT
- **Quality ratio** = good quantity (GQ) ÷ PQ

A worked example, using illustrative numbers for one shift:

- Planned busy time 480 min, actual production time 400 min → Availability **83.3%**
- Planned run time 0.5 min per item, 720 items produced → Effectiveness 0.5 × 720 ÷ 400 = **90.0%**
- 698 good items → Quality ratio **96.9%**
- OEE ≈ 0.833 × 0.900 × 0.969 ≈ **72.7%**

Now suppose a quality AI raises good items to 712 with nothing else changed. The quality ratio becomes 98.9% and OEE about 74.2%. That is a modest 1.5-point rise, yet scrap and rework fell from 22 items to 8. The composite KPI understates what changed, which is why you need the direct KPIs alongside it.

The standard adds a warning that is easy to skip. Before benchmarking with OEE, check that the work units being compared are actually comparable.

## Why one composite KPI is not enough

A 2016 paper in the *International Journal of Production Research* (Kang et al., with NIST co-authorship) organizes the 34 ISO 22400 KPIs into three layers. At the bottom are supporting elements, such as times and quantities. Above them are basic KPIs, such as availability, effectiveness, quality ratio, scrap ratio, and rework ratio. At the top are comprehensive KPIs, such as OEE and NEE. NEE, net equipment effectiveness, is similar to OEE but folds setup time into availability. The paper's point is that KPIs share elements and depend on each other, so you can read a change in a composite KPI only by looking at the basic KPIs underneath.

A practical pairing, using the standard's KPI names (my own mapping):

- **Quality inspection or root-cause AI:** scrap ratio, rework ratio, and quality ratio, with OEE
- **Process-parameter optimization:** effectiveness and quality ratio, with OEE
- **Scheduling or dispatch support:** availability and throughput rate, with OEE or NEE

## Where the data comes from

ISO 22400-2 places these KPIs at Level 3 of the IEC 62264 hierarchy, manufacturing operations management. It notes they may need parameters from Levels 1 and 2, the control and equipment layers. In practice, that means MES and machine logs. The first job is to collect the time elements (planned busy time, actual production time, downtime) and the quantity elements (produced, good, scrap, rework) in the same units, against the same clock.

## Measuring "impact" fairly

Three habits make an impact claim credible:

1. **Baseline:** record the KPIs for several weeks or more before go-live, using the final definitions.
2. **Like for like:** do not compare periods with very different product mix, shifts, or volumes.
3. **A comparison:** where possible, track a line or period without the AI alongside the one with it.

Public evaluations show why this matters. In March 2019, Korea's Ministry of SMEs and Startups reported that a survey of 5,003 companies that had adopted smart factories found productivity up 30%, defect rates down 43.5%, costs down 15.9%, and delivery times down 15.5%. The announcement was also a response to a newspaper report that most adopters felt the program had no effect. The same program can be judged very differently depending on what is measured and how.

## Where Korean manufacturers stand

Korea's 2024 Smart Manufacturing Innovation Survey, released on 28 April 2025, covered 163,273 small and mid-sized companies that own factories. It found that 0.1% had adopted manufacturing AI and 1.6% planned to. Among smart-factory adopters, 5.2% had adopted or planned to adopt it. As adoption grows, agreeing on how to measure results before a project starts will matter more.

## Where to start

Pick one process where AI will be applied. Start logging the three OEE components and the scrap ratio daily, using one fixed method. Then write down, in numbers, what change would count as success. If you choose the metric after deployment, it is tempting to pick whichever number looks best.

The full KPI pairing table and FAQ are in the [Korean version of this post](/ko/manufacturing-ai-kpi-oee/).

## Sources
- ISO 22400-2:2014, KPIs for manufacturing operations management, Part 2: Definitions and descriptions (overview and sample pages): https://standards.iteh.ai/catalog/standards/iso/8a9efc01-6c74-42a2-ad8f-ec19e84b48f0/iso-22400-2-2014
- Kang, Zhao, Li, Horst, "A Hierarchical structure of key performance indicators for operation management and continuous improvement in production systems," *Int J Prod Res* 54(21) (2016), author manuscript: https://pmc.ncbi.nlm.nih.gov/articles/PMC5795624/
- Ministry of SMEs and Startups, "SMEs adopting smart factories see productivity gains" (2019-03-08, Korean): https://www.korea.kr/news/policyNewsView.do?newsId=148858991
- Ministry of SMEs and Startups, 2024 Smart Manufacturing Innovation Survey (summary via KDI, Korean): https://eiec.kdi.re.kr/policy/materialView.do?num=266057

*I work at INTERX, a Korean manufacturing AI company (founded 2020). Views are my own.*
