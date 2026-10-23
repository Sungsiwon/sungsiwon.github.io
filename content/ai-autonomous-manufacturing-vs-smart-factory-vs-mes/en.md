*Disclosure: I work at INTERX, a Korean manufacturing AI company (founded 2020). This article is my personal summary based on public sources such as Korean government documents and international standards; it does not represent my employer's official position.*

If you follow manufacturing technology in Korea, you have probably noticed a new phrase showing up in policy papers and trade press: **AI autonomous manufacturing** (AI 자율제조). It often appears next to two older terms, **smart factory** and **MES** (Manufacturing Execution System), and the three are easy to blur together.

They are not competing options, and none of them replaces the others. They describe different layers. The shortest way I can put it:

- **MES** is a *system* that records and manages production.
- A **smart factory** is a factory that *connects and visualizes* its data.
- **AI autonomous manufacturing** is a factory where *AI makes decisions and acts on them*, with people supervising.

<figure><img src="/assets/ai-autonomous-manufacturing-vs-smart-factory-vs-mes.jpg" alt="Diagram: MES records and manages, smart factory connects and visualizes, AI autonomous manufacturing decides and controls." width="1200" height="675" loading="lazy"><figcaption>MES (record &amp; manage) → Smart factory (connect &amp; visualize) → AI autonomous manufacturing (decide &amp; control)</figcaption></figure>

## At a glance

| | MES | Smart factory | AI autonomous manufacturing |
|---|---|---|---|
| What it is | A production execution system (software) | A way and level of running a factory (concept) | A way and level of running a factory (concept) |
| Purpose | Manage work orders, production results, and lot history | Improve efficiency by collecting, connecting, and visualizing data | Determine optimal conditions and operate autonomously |
| Main data | Work orders, production output, material history | Integrated MES, ERP, sensor, and equipment data | All of the above, plus training data such as process conditions and images |
| Who decides | People | People (based on data) | AI recommends or controls; people supervise |
| Example | Lot tracking, issuing work orders | Real-time monitoring dashboard | AI recommends and applies process settings; vision AI makes automatic pass/fail calls |

## The questions people actually ask

### What is AI autonomous manufacturing?

It is a way of manufacturing in which AI reads process data, makes judgments, and, combined with robots and equipment, pushes production toward higher sophistication and autonomy.

Korea's Ministry of Trade, Industry and Energy (MOTIE) defined it in its May 2024 *AI Autonomous Manufacturing Strategy 1.0* as, roughly, "a future manufacturing environment that achieves advanced and autonomous production by combining robots, equipment and the like with manufacturing processes on the basis of AI" (my translation of the Korean original).

The practical difference is where the loop closes. A smart factory can put a defect on a screen. AI autonomous manufacturing aims to go further: find the process condition likely causing the defect and change it.

### How is that different from a smart factory?

The two overlap, but they are not the same thing. "Smart factory" is a broad concept: using ICT to connect a plant and make it visible. AI autonomous manufacturing is closer to a stage built on top of that, where AI takes on judgment and control.

Korea's Ministry of SMEs and Startups describes smart factory maturity in four levels in its smart factory support program: **Basic** (checking and monitoring), **Intermediate 1** (analysis and control), **Intermediate 2** (optimization), and **Advanced** (autonomous operation). Seen through that lens, AI autonomous manufacturing is an effort to reach the "Advanced" end of the smart factory scale using AI.

### If we already have an MES, do we still need AI?

Yes, because they answer different questions. An MES tells you *what happened*. AI deals with *what is likely to happen and what should change*.

The international standard ISA-95 (IEC 62264) places MES at Level 3, manufacturing operations management, between business systems such as ERP (Level 4) and control layers such as PLCs and DCS (Level 2). The production and history data piling up in an MES is actually good training material for AI, which is why plants with a well-run MES tend to adopt AI faster. An MES is a starting point for AI, not a substitute.

### Do you need a full MES and smart factory before attempting AI autonomous manufacturing?

Not necessarily. What you do need is the data relevant to the problem you are trying to solve. For example, to reduce defects in injection molding, process conditions (temperature, pressure, time) need to be linked to the pass/fail results for each part.

### Where should a small or mid-sized manufacturer start?

Pick one problem whose impact is easy to measure in numbers, such as the defect rate on a specific line or unplanned stops on a specific machine. Then:

1. Define the problem and the target metric.
2. Check whether the data you need exists, and whether collection frequency and standards are consistent.
3. Run a small proof of concept (PoC).
4. If the effect holds up, expand to other lines.

In Korea, the government's smart factory level assessment is also a useful way to check where your plant stands before you begin.

## Korea's policy context

In May 2024, MOTIE announced its **AI Autonomous Manufacturing Strategy 1.0**, and in July 2024 it launched the **AI Autonomous Manufacturing Alliance**, stating a plan to pursue 200 leading projects by 2028. The alliance started with 153 companies and institutions across 12 industries. In May 2025, the ministry added the **Industrial Complex AX Caravan**, a program in which AI companies visit manufacturers in industrial complexes to provide consulting on AI transformation.

For readers outside Korea, the point is that "AI autonomous manufacturing" is not just a marketing label there. It is a named policy category with a government definition, which is one reason the term now appears so often in Korean industry discussions.

## Three differences to remember

1. **What it is.** MES is a system (software). Smart factory and AI autonomous manufacturing describe how, and how far, a factory is run.
2. **What happens to the data.** MES records it, a smart factory connects and displays it, and AI autonomous manufacturing uses it to decide what to change next.
3. **Who makes the call.** With MES and a smart factory, people decide based on data. In AI autonomous manufacturing, AI recommends or directly controls process conditions, and people supervise.

*The original, longer FAQ (in Korean) is on my blog: [AI 자율제조 vs 스마트팩토리 vs MES, 뭐가 다를까?](https://blog.naver.com/sangza40/224448962411)*

## Sources

- MOTIE, "Drawing the path for Korean industry in the AI era" (AI Autonomous Manufacturing Strategy 1.0, 2024-05-08), Korea Policy Briefing (Korean): https://m.korea.kr/briefing/pressReleaseView.do?newsId=156629475
- MOTIE, "Manufacturing AI adoption to expand to 40%; 200 leading projects" (launch of the AI Autonomous Manufacturing Alliance, 2024-07-22), Korea Policy Briefing (Korean): https://www.korea.kr/news/policyNewsView.do?newsId=148931737
- MOTIE, "On-site AI transformation support: Industrial Complex AX Caravan launched" (2025-05-20, Korean): https://www.motie.go.kr/kor/article/ATCL8764a1224/155118874/view
- Ministry of SMEs and Startups, Smart Factory program, "Introduction of Support Project" (definition and levels): https://www.smart-factory.kr/eng/smartFactory.do?menuId=03
- ISA, ISA-95 Standard: Enterprise-Control System Integration: https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard

*I work at INTERX, a Korean manufacturing AI company (founded 2020). Views are my own.*
