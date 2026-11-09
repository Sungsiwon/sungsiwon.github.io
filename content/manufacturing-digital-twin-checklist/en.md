*Disclosure: I work at INTERX, a Korean manufacturing AI company. This is my personal summary of public sources (international standards, NIST publications, and Korean government documents) and does not represent my employer's official position.*

"Let's build a digital twin" is an easy sentence to say in a planning meeting and a hard one to act on. The standards community has spent the last few years making the term more precise, and that precision turns out to be the most useful planning tool available.

## Start with the definition

ISO/IEC 30173:2023, the cross-industry standard on digital twin concepts and terminology, defines a digital twin as a digital representation of a target entity with data connections that enable convergence between the physical and digital states at an appropriate rate of synchronization. The manufacturing-specific framework, ISO 23247, describes it as a *fit for purpose* digital representation of an observable manufacturing element, synchronized with that element. According to NIST's explanation of the framework, an observable manufacturing element can be personnel, equipment, material, a process, a facility, the environment, a product, or a supporting document.

Two words carry most of the weight: **purpose** and **synchronization**. Everything in the checklist below follows from them.

<figure><img src="/assets/manufacturing-digital-twin-checklist.jpg" alt="Cartoon of a small factory and its translucent digital twin connected by dotted data lines, with a robot holding a checklist." width="1280" height="720" loading="lazy"><figcaption>What connects a real factory to its digital twin is data and synchronization. Start with the checklist.</figcaption></figure>

## The checklist, in three phases

### Planning: what and why

1. **One use case.** NIST's *Use Case Scenarios for Digital Twin Implementation Based on ISO 23247* (NIST AMS 400-2, May 2021) states plainly that no single digital twin can provide all the solutions for a manufacturing system. It lists typical applications (analytics, real-time control, equipment health, scheduling and routing, virtual commissioning, predictive maintenance, product twins) and works through three of them in detail: machine health, scheduling and routing, and virtual commissioning. Pick one.
2. **The target.** Decide which element you are twinning. ISO/IEC 30173 distinguishes component, asset, system, and process twins, and the right choice depends on the use case.
3. **Fidelity.** "Fit for purpose" means as detailed as the use case needs, and no more. A machine-health twin may not need geometry at all; a virtual commissioning twin may need a lot.

### Data: how it stays connected

4. **Data collection.** The first step in NIST's procedure for applying ISO 23247 is selecting data standards, sensor interfaces, and processing tools for collecting data from the shop floor.
5. **Synchronization rate.** ISO/IEC 30173 speaks of an "appropriate" rate, and NIST describes it as a rate defined by the application. Real-time, per-cycle, and daily are all legitimate answers, depending on the decision the twin supports.
6. **Read-only or control.** The ISO 23247 reference architecture has a dedicated data collection and device control domain, and ISO/IEC 30173 defines the control loop in which the digital entity sends data back to modify the physical entity's behavior. Decide early whether your twin only observes or also acts.
7. **Representation and identifiers.** Per NIST's summary of ISO 23247-3, existing standards should be used to represent manufacturing elements whenever possible, and each element should use an enterprise-unique identifier if possible. For asset data, the Asset Administration Shell structure is now an IEC standard (IEC 63278-1, published December 2023).

### Operation: how you trust it

8. **Integration with existing systems.** In the ISO 23247 reference architecture, the user domain includes not just people but enterprise applications such as MES and ERP, and other digital twins. Plan the interfaces up front.
9. **Security and trust.** NIST IR 8356, *Security and Trust Considerations for Digital Twin Technology* (February 14, 2025), identifies five features that need special cybersecurity attention: massive instrumentation of objects (usually via IoT), centralization of measurements, visualization of object operation, remote control of objects, and standards that allow universal access and control. If you answered "control" in item 6, this item gets heavier.
10. **Verification and metrics.** Decide how you will confirm the twin tracks reality and which KPIs will show value. ISO/IEC 30173 includes verification and validation among its defined terms, and NIST AMS 400-2 lists benefits such as detecting anomalous equipment performance in real time using KPIs.

## The architecture behind the checklist

NIST's report summarizes the ISO 23247-2 reference architecture as four domains:

- **Observable manufacturing domain**: the real equipment, materials, and processes, outside the twin itself.
- **Data collection and device control domain**: links those elements to their twins by collecting sensor data and, where needed, actuating devices.
- **Core domain**: operates and manages the twin and hosts analytics, simulation, and optimization services.
- **User domain**: people, enterprise applications, and other twins that use the results.

Items 4 to 7 fill in the middle two domains. Items 8 to 10 govern how the whole stack is used.

## When one twin becomes many

Most plants will eventually have several twins built by different teams or suppliers. ISO 23247-6, published in July 2026, addresses exactly this. It defines three kinds of composition (integrated, unified, and federated) and gives step-by-step guidance for making twins from different parties interoperate. It is a good reason to design a first, small twin with identifiers and interfaces that can be joined later.

## Korea's policy context

South Korea's Ministry of Science and ICT announced a Digital Twin Activation Strategy in 2021, which included applying digital twins to major industries to improve production and operational efficiency. On January 22, 2025, the Ministry of Trade, Industry and Energy published ten priority tasks for industrial AI, including developing AI agents linked with digital twins as part of its autonomous manufacturing lead projects. Korea's smart factory level framework, run by the Ministry of SMEs and Startups, describes Level 4 (optimization) as the stage where advance response through process operation simulation becomes possible, and lists AR/VR and cyber-physical systems as main tools at Level 5.

For a small or mid-sized manufacturer, the practical reading is that the twin sits on top of basic data collection and monitoring. NIST AMS 400-2 notes that SMEs in particular struggle because definitions vary, terminology is inconsistent, and there are no standardized procedures, which is the gap the standards above try to close.

## The short version

- Pick one use case and one target.
- Decide fidelity, synchronization rate, and whether the twin may control anything.
- Use existing data standards and unique identifiers.
- Plan MES and ERP integration, security, and verification before the first screen is designed.

## Sources

- ISO/IEC 30173:2023, Digital twin — Concepts and terminology (Edition 1.0, 2023-11): https://www.iso.org/standard/81442.html
- ISO 23247-1:2021, Digital twin framework for manufacturing — Part 1 (2021-10): https://www.iso.org/standard/75066.html
- ISO 23247-6:2026, Digital twin framework for manufacturing — Part 6: Digital twin composition (2026-07): https://www.iso.org/standard/87426.html
- Shao G., *Use Case Scenarios for Digital Twin Implementation Based on ISO 23247*, NIST AMS 400-2 (May 2021): https://doi.org/10.6028/NIST.AMS.400-2
- NIST IR 8356, *Security and Trust Considerations for Digital Twin Technology* (2025-02-14): https://www.nist.gov/news-events/news/2025/02/security-and-trust-considerations-digital-twin-technology-nist-releases-ir
- IEC 63278-1:2023, Asset Administration Shell for industrial applications — Part 1 (2023-12): https://webstore.iec.ch/en/publication/65628
- Ministry of SMEs and Startups, Smart Factory program, "Introduction of Support Project": https://www.smart-factory.kr/eng/smartFactory.do?menuId=03
- Ministry of Science and ICT, Digital Twin Activation Strategy summary, Korea Policy Briefing (2021-10-15, Korean): https://www.korea.kr/news/policyFocusView.do?newsId=148894352
- Ministry of Trade, Industry and Energy, ten priority tasks for industrial AI (2025-01-22, Korean): https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/170072/view

*I work at INTERX, a Korean manufacturing AI company. Views are my own.*
