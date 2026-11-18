*Disclosure: I work as a principal researcher (service planning) at INTERX, a Korean manufacturing AI company founded in 2020. This article is my personal summary based on public sources such as Korean government surveys and international standards; it does not represent my employer's official position.*

If you run or support a small or mid-sized manufacturer and someone asks, "How do we start with AI?", the most useful answer is not a model name. It is this: **pick one problem, then check whether five kinds of data exist for it and can be linked to the same product.** Buying new sensors or software can come later.

Here are the five:

- **The problem and its baseline.** One line, one metric, and today's number for it (for example, the defect rate of a specific line over the last three months).
- **Process conditions.** The values machines and sensors record: temperature, pressure, speed, load.
- **Quality outcomes.** The "answers" AI will learn to predict: pass/fail, defect type, measured dimensions.
- **Linking keys.** Lot or serial numbers, machine codes, and timestamps that tie a specific outcome to the conditions under which that part was made.
- **Definitions and shop-floor records.** What each variable means, its unit and valid range, plus human-logged events such as tool changes, mold changes, or material switches.

<figure><img src="/assets/ai-data-readiness-small-manufacturers.jpg" alt="A worker arranges five boxes of data on a shelf while an AI helper picks them up and links them." width="1200" height="675" loading="lazy"><figcaption>Five kinds of data to prepare before AI: problem &amp; baseline, process conditions, quality outcomes, linking keys, definitions &amp; shop-floor records</figcaption></figure>

## A five-step check on the shop floor

1. Write down one problem and its baseline number, with a date range.
2. Note where each process condition is recorded, and how often.
3. Confirm that the quality outcome is written down, not just remembered.
4. Pick one defective part and try to retrieve the process conditions under which it was made.
5. Keep a variable dictionary and shop-floor event records (tool or mold changes) next to the dataset.

If step 4 breaks, fix the linking key before you pick a model.

## Why data, and why now

Korea offers an unusually clear snapshot of the gap. In April 2025, the Ministry of SMEs and Startups (MSS) published its first Smart Manufacturing Innovation Survey. It covered small, medium, and mid-sized manufacturers that own a factory, using a sample of 5,000 firms interviewed in person between October 2024 and January 2025. Among the findings:

- **60.8%** of firms collect manufacturing data, but only 52.1% of those actually analyze it.
- Among firms that have adopted a smart factory, 92.4% collect data and 74.0% of those analyze it.
- Only **0.1%** of firms have adopted manufacturing AI, and another 1.6% plan to.
- Just 0.8% have a dedicated department or staff for manufacturing data and AI.
- 75.5% of the smart factories in place are at the basic level.

In other words, collection is common, analysis is less common, and AI is rare. In my reading, the step that is most often missing in between is data preparation: making the data that already exists usable together.

## The questions people actually ask

### "We don't have much data. Can we still use AI?"

Connection matters more than volume at the start. If you have lots of sensor readings but the pass/fail result for each part lives in a separate notebook, a model has nothing to learn from. That is why linking keys are on the list. A useful first test: pick one defective part and try to retrieve the process conditions under which it was made. If you can, you have the core of a dataset. If you cannot, you know exactly where the chain breaks.

### "Do we need to buy new sensors first?"

Not necessarily. Start by listing where data already lives: PLCs, inspection-station PCs, MES or ERP, and spreadsheets or paper logs. Public examples show that mixed collection is normal. One machining (MCT) dataset description published on KAMP, the Korea AI Manufacturing Platform run under MSS, describes:

- machine conditions collected from the PLC and temperature sensors every 5 seconds,
- 3D and vision measurements collected automatically when each inspection finishes, and
- tool-change intervals entered by operators after checking.

The same document lists each variable with its unit, valid range, and the OK/NG rule used for pass/fail, which is a good model for the "definitions" item above.

### "How do we judge whether our data is good enough?"

The international standard **ISO/IEC 25012** offers a ready-made checklist. It defines data quality through 15 characteristics. Five of them describe the data itself: accuracy, completeness, consistency, credibility, and currentness. On a shop floor these translate into plain questions:

| Criterion | Source | Shop-floor question |
|---|---|---|
| Accuracy | ISO/IEC 25012 | Do the recorded values match what actually happened? |
| Completeness | ISO/IEC 25012 | Are fields or lots missing? |
| Consistency | ISO/IEC 25012 | Do lines and machines use the same units and formats? |
| Credibility | ISO/IEC 25012 | Can we trust where the value came from? |
| Currentness | ISO/IEC 25012 | Is this the value from the right moment, or a stale one? |
| Connectivity (linking) | A shop-floor check, not an ISO/IEC 25012 characteristic name | Can one defective part be linked to the conditions under which it was made? |

If the data will be used for analytics or machine learning, a later series builds on ISO/IEC 25012: **ISO/IEC 5259**. Part 1 was published in July 2024 and Part 2 in November 2024. They address how to define and measure data quality for analytics and ML. The official number is ISO/IEC 5259 (not a look-alike number sometimes seen in secondary summaries).

### "Is there data we can practice on before ours is ready?"

Yes. KAMP offers free manufacturing AI datasets for small manufacturers. A list published on Korea's public data portal by the Korea Technology and Information Promotion Agency for SMEs (TIPA) shows 50 datasets as of December 31, 2024, organized by industry, purpose, and process. As of this draft (18 November 2026, Asia/Seoul), that "as-of" date on the public list has not been updated. Even if you never train on them, they are useful templates for how to structure your own variables.

### "How big should the first project be?"

Small: one line, one problem, one metric. Define the problem and target, check the five kinds of data for that problem, run a small proof of concept, and expand only if the effect holds. Record the baseline before you start, or you will not be able to show the effect later.

### "We only have Excel files and paper logs. Can we still start?"

Yes, provided you can list where each record lives and join process conditions to quality outcomes for the same product. If a lot number or a timestamp ties a defect to the conditions under which it was made, you already have the seed of a small proof of concept. Buying new sensors can wait until you know which records are missing. The public machining dataset above also mixes automatic collection with operator-entered events.

## Korea's policy context

On October 24, 2025, MSS announced its **AI-based Smart Manufacturing Innovation 3.0 Strategy**. According to the ministry's briefing, the targets for 2030 include deploying 12,000 AI-centered smart factories and raising AI adoption among small manufacturers to 10%. Two of the listed tasks are directly about data: standardizing manufacturing data based on international standards, and securing 1,000 high-quality manufacturing datasets generated during smart factory projects. The ministry also plans a consolidated one-stop support platform called "Manufacturing AI 24."

In 2026 that work moved from plan to execution. In April 2026 MSS invited organizations to develop reference models for its manufacturing-data standardization program. At a 1 July 2026 kickoff briefing, MSS and TIPA said they had selected five consortia (17 organizations) to develop Asset Administration Shell (AAS) reference models, with a goal of 500 models by year-end. In a 20 February 2026 press explanation, MSS also said it would complete an information-strategy plan (ISP) in 2026 to upgrade KAMP into "Manufacturing AI 24," with actual build-out planned for 2027.

For readers outside Korea, the takeaway is that the policy debate has moved from "deploy more smart factories" to "make factory data usable for AI." That shift matches what the survey numbers suggest.

## A five-line checklist to keep

1. Can we state one problem and its current number, with a date range?
2. Do we know where each process value is recorded and how often?
3. Is the outcome (pass/fail, defect type) written down, not just remembered?
4. Can one defective part be linked to its process conditions?
5. Could a newcomer read our variable list and understand every column?

*The original post (in Korean), with a checklist table and FAQs, is on my blog: https://blog.naver.com/sangza40/224451245938*

Related: [AI Autonomous Manufacturing vs Smart Factory vs MES](/ko/ai-autonomous-manufacturing-vs-smart-factory-vs-mes/) (Korean FAQ; [English version](/en/ai-autonomous-manufacturing-vs-smart-factory-vs-mes/)).

## Sources

- Ministry of SMEs and Startups, "Results of the 2024 Smart Manufacturing Innovation Survey" (2025-04-28), Korea Policy Briefing (Korean): https://www.korea.kr/briefing/pressReleaseView.do?newsId=156686561
- Ministry of SMEs and Startups, "AI-based Smart Manufacturing Innovation 3.0 Strategy" briefing (2025-10-24), Korea Policy Briefing (Korean): https://www.korea.kr/news/policyNewsView.do?newsId=156722205
- Ministry of SMEs and Startups, press explanation on upgrading KAMP to Manufacturing AI 24 (2026-02-20, Korean): https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1065703&cbIdx=87
- Ministry of SMEs and Startups, 2026 call for manufacturing-data standardization reference-model developers (2026-04-06, Korean): https://www.mss.go.kr/site/smba/ex/bbs/View.do?bcIdx=1067009&cbIdx=310
- Yonhap News, kickoff of the AAS reference-model program (2026-07-01, Korean): https://www.yna.co.kr/view/AKR20260701154400030
- TIPA, "Manufacturing AI datasets (50)" (as of 2024-12-31), Public Data Portal (Korean): https://www.data.go.kr/data/15089213/fileData.do
- KAMP, Korea AI Manufacturing Platform: https://www.kamp-ai.kr/
- KAMP, MCT machining and inspection dataset description (PDF, Korean): https://aisquare.kamp-ai.kr/upload_data/mainImg/95d6c6ca-96ee-4dfb-ad98-dbe0c6676420.pdf
- ISO/IEC 25012:2008, Data quality model: https://www.iso.org/standard/35736.html
- ISO 25000 portal, ISO/IEC 25012 characteristics: https://iso25000.com/index.php/en/iso-25000-standards/iso-25012
- ISO/IEC 5259-1:2024: https://www.iso.org/standard/81088.html
- ISO/IEC 5259-2:2024: https://www.iso.org/standard/81860.html

*I work as a principal researcher (service planning) at INTERX, a Korean manufacturing AI company founded in 2020. Views are my own.*
