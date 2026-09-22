"""Build the thesis-style business research report PDF."""
from PIL import Image as PILImage
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (Paragraph, Spacer, PageBreak, Image, Table,
                                TableStyle, KeepTogether, NextPageTemplate)
from reportlab.platypus.tableofcontents import TableOfContents
from rstyle import *
from rcharts import *

story = []

# ============================================================ COVER
story.append(P("BUSINESS MODEL &amp; FEASIBILITY STUDY", CHAP_LABEL))
story.append(Spacer(1, 26 * mm))
story.append(P("Destination-Based EV Charging Infrastructure in India", TITLE))
story.append(P("A Business Model and Feasibility Study for Converting Existing "
               "Destination Parking into Distributed EV Charging Infrastructure", SUBTITLE))
story.append(Spacer(1, 8 * mm))

pil = PILImage.open("assets/cover.jpg")
cw, ch = pil.size
story.append(Image("assets/cover.jpg", width=W * 0.92, height=W * 0.92 * ch / cw))
story.append(P("Cover: electric vehicles charging in destination parking during a routine visit. "
               "Source: commissioned illustration for this report.", CAPTION))

meta = [
    [P("<b>RESEARCH QUESTION</b>", CELL_H),
     P("Under what conditions can existing destination parking be converted into "
       "economically viable EV charging infrastructure in India?", CELL)],
    [P("<b>METHOD</b>", CELL_H),
     P("Secondary market research \u00b7 Unit-economics modelling \u00b7 Scenario &amp; sensitivity "
       "analysis (no primary data collected)", CELL)],
    [P("<b>DATE</b>", CELL_H), P("September 2026", CELL)],
    [P("<b>VERSION</b>", CELL_H), P("1.0", CELL)],
]
story.append(styled_table(
    [[P("<b>ITEM</b>", CELL_H), P("<b>DETAIL</b>", CELL_H)]] +
    [[r[0], r[1]] for r in meta], [52 * mm, W - 52 * mm]))
story.append(Spacer(1, 4 * mm))
story.append(P("This document is an academic business research report \u2014 a feasibility "
               "investigation, not a validated business plan. It does not constitute financial "
               "advice or an investment recommendation. All economic models are directional and "
               "contain clearly labelled assumptions requiring empirical validation.", FOOTNOTE))
story.append(NextPageTemplate("FrontA"))
story.append(PageBreak())

# ============================================================ ABSTRACT
story.append(P("ABSTRACT", CHAP_LABEL))
story.append(P("Abstract \u2014 Research Summary", H1))
story.append(P("<b>Background.</b> India\u2019s electric vehicle market set new records in 2025. "
               "Total EV retail sales reached 2.27 million units, up 16% year-on-year (Autocar "
               "Professional, 2026), and electric passenger vehicle sales grew 77% to 176,538 units "
               "(Autocar Professional, 2026). Public charging infrastructure expanded nearly "
               "sixfold in three years to 29,277 stations by August 2025 (Ministry of Power, 2025). "
               "Yet the charger-to-EV ratio stands at roughly 1:235 against a global benchmark of "
               "1:6 to 1:20 (The Economic Times, 2025), and only 22,753 of 27,737 installed stations "
               "were operational as of March 2026 \u2014 an 18% non-functional rate (MMCM, 2026)."))
story.append(P("<b>Problem.</b> Dedicated charging sites face land costs, capital intensity and "
               "grid-connection constraints; premium urban leases can absorb up to 40% of project "
               "budgets (Mordor Intelligence, 2025). Meanwhile, thousands of commercial "
               "destinations \u2014 malls, hotels, hospitals, offices, universities \u2014 already own "
               "parking, customer dwell time, footfall and electricity connections. Whether these "
               "existing assets can be integrated into a viable destination-charging model is the "
               "central problem this study investigates."))
story.append(P("<b>Research objective.</b> To determine the conditions under which existing "
               "destination parking can be converted into economically viable EV charging "
               "infrastructure in India \u2014 evaluating the model critically, separating what is "
               "supported by evidence from what remains assumption or hypothesis."))
story.append(P("<b>Methodology.</b> The study combines secondary market research (regulatory data, "
               "Vahan registrations, industry reports) with original unit-economics modelling, "
               "scenario analysis and sensitivity testing. No customer interviews, host negotiations "
               "or pilot data have been collected; this absence is disclosed throughout and every "
               "major claim is classified as FACT, ESTIMATE, ASSUMPTION or HYPOTHESIS."))
story.append(P("<b>Major findings.</b> The market opportunity is real but narrow: the addressable "
               "pool is concentrated among urban EV owners without reliable home charging, "
               "directionally estimated at 100,000\u2013150,000 passenger EVs. At reference-case "
               "inputs (Rs.12/kWh price, Rs.9/kWh tariff, 20% host share), a charging bay cannot "
               "break even at any plausible utilisation \u2014 the operator retains only Rs.0.60/kWh, "
               "implying a breakeven of ~30 sessions/day. Viability emerges only under stricter "
               "parameters (Rs.15 price, Rs.8 tariff, 15% share), where breakeven falls to ~3.4 "
               "sessions/bay/day with ~5.5-year payback. Site utilisation as low as 5% has been "
               "observed at deployed public stations (MMCM, 2026), and large operators \u2014 Tata "
               "Power, Jio-bp, Statiq, Bolt.Earth \u2014 are expanding aggressively."))
story.append(P("<b>Business implications.</b> The destination model structurally avoids land-"
               "acquisition cost and is aligned with Ministry of Power hosting guidelines. It is "
               "conditionally viable: site selection, tariff discipline and utilisation above ~3.5 "
               "sessions/bay/day are non-negotiable. A structured 3\u20135 site pilot is the "
               "recommended next step before any scaling commitment."))
story.append(P("<b>Key limitations.</b> Driver willingness to use destination charging, host "
               "willingness to allocate parking, and any incremental host spending uplift are all "
               "unvalidated hypotheses. All financial figures are directional modelling, not forecasts."))
story.append(NextPageTemplate("FrontC"))
story.append(PageBreak())

# ============================================================ CONTENTS
story.append(P("CONTENTS", CHAP_LABEL))
story.append(P("Contents", H1NT))
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle("TOC0", fontName="DV-B", fontSize=10, leading=16, textColor=TEXT,
                   leftIndent=0, firstLineIndent=0, spaceBefore=4),
    ParagraphStyle("TOC1", fontName="DV", fontSize=9, leading=14, textColor=SECOND,
                   leftIndent=14, firstLineIndent=0, spaceBefore=1),
]
toc.dotsMinLevel = 0
story.append(toc)
story.append(Spacer(1, 6 * mm))
story.append(P("<b>Evidence classification.</b> Throughout this report all major claims are "
               "classified as: {} \u2014 sourced from verifiable data; {} \u2014 derived from "
               "available evidence; {} \u2014 modelling input requiring validation; {} \u2014 "
               "proposition requiring empirical testing."
               .format(badge("FACT"), badge("ESTIMATE"), badge("ASSUMPTION"), badge("HYPOTHESIS")),
               BODY_S))
story.append(P("<b>Reading guide.</b> Chapters 1\u20132 establish context and the research gap. "
               "Chapters 3\u20134 define the business model and the customer. Chapter 5 contains the "
               "core economic analysis, including a corrected reference case and a viability "
               "frontier. Chapters 6\u20137 cover strategy, validation and risk. Chapter 8 states "
               "what is proven, what is not, and what must be tested next.", BODY_S))
story.append(NextPageTemplate("Ch1"))
story.append(PageBreak())

# ============================================================ CHAPTER 1
story.append(P("CHAPTER 01", CHAP_LABEL))
story.append(P("01 \u2014 Introduction", H1))

story.append(P("1.1 Background", H2))
story.append(P("{} India\u2019s EV industry crossed the 2-million annual sales milestone for the "
               "first time in November 2025 and closed CY2025 at 2.27 million units, up 16% on "
               "CY2024\u2019s 1.95 million (Autocar Professional, 2026). Electric passenger vehicles "
               "posted their strongest year on record: 176,538 units, up 77% year-on-year, with 11 "
               "months above 11,000 units and a festive peak of 19,161 units in October (Autocar "
               "Professional, 2026). The last three calendar years account for the large majority "
               "of all EVs ever sold in India, indicating accelerating \u2014 not linear \u2014 adoption "
               "momentum. {}" .format(badge("FACT"), badge("ESTIMATE"))))
story.append(P("{} Public charging infrastructure has grown nearly sixfold in three years: from "
               "5,151 stations in December 2022 to 25,202 in December 2024 and 29,277 by August "
               "2025, operated by 83 charge point operators (Ministry of Power, 2025, via ORF, "
               "2025). Yet scale remains the binding constraint. India has roughly one public "
               "station per 235 EVs versus a global benchmark of one per 6\u201320 (The Economic "
               "Times, 2025), and reaching the government\u2019s 30% EV penetration ambition for 2030 "
               "would require an estimated 1.32 million public stations \u2014 more than 40 times the "
               "current base (ORF, 2025)." .format(badge("FACT"))))
story.append(P("{} Policy direction is explicitly supportive. Setting up charging stations is a "
               "de-licensed activity under Ministry of Power guidelines; the PM E-DRIVE scheme "
               "allocates Rs.2,000 crore toward 72,300 public chargers; and official guidance "
               "identifies malls, workplaces, fuel stations and residential complexes as preferred "
               "hosting sites (Avaada, 2026; Bolt.Earth, 2025). The destination-charging model "
               "evaluated here sits directly inside this policy corridor." .format(badge("FACT"))))

story.append(P("1.2 Problem Statement", H2))
story.append(P("Vehicle growth and usable charging supply are diverging. Dedicated charging "
               "infrastructure must be located where charging is useful, but commercially "
               "attractive urban land is expensive \u2014 business-district leases in Mumbai consume up "
               "to 40% of project budgets and extend payback periods (Mordor Intelligence, 2025) "
               "\u2014 while grid-connection upgrades add further capital and delay. Operational "
               "quality compounds the problem: an 18% national non-functional rate, up to 60% on "
               "the worst networks, and site utilisation as low as 5% at many deployed stations "
               "(MMCM, 2026)."))
story.append(P("Simultaneously, thousands of destination businesses already possess the three "
               "assets a charging operator must otherwise buy or build: parking inventory, customer "
               "dwell time, and electricity connections \u2014 plus existing footfall. The underlying "
               "problem is therefore allocative: whether these dormant assets can be integrated "
               "into a destination-charging network that is economically sustainable at the level of "
               "the individual site, not merely attractive in aggregate market statistics."))

story.append(P("1.3 Research Objectives", H2))
for o in ["<b>O1.</b> To assess the scale and composition of India\u2019s EV market relevant to destination charging.",
          "<b>O2.</b> To define the criteria that make a destination site suitable for EV charging conversion.",
          "<b>O3.</b> To model the unit economics of a single destination-charging bay under multiple utilisation scenarios.",
          "<b>O4.</b> To evaluate whether host businesses can receive sufficient economic incentive to allocate parking.",
          "<b>O5.</b> To identify the assumptions and hypotheses requiring empirical validation before any scaling commitment."]:
    story.append(P(o, BULLET, bulletText="\u2014"))

story.append(P("1.4 Research Questions", H2))
rq = [[P("<b>NO.</b>", CELL_H), P("<b>RESEARCH QUESTION</b>", CELL_H)]]
for n, q in [("RQ1", "What portion of India\u2019s EV market is behaviourally and technically relevant to destination charging?"),
             ("RQ2", "What destination characteristics \u2014 dwell time, parking, electricity capacity, EV density \u2014 determine site suitability?"),
             ("RQ3", "At what utilisation rate does a destination-charging bay break even, and how sensitive is this to price, tariff and revenue share?"),
             ("RQ4", "Can host businesses receive sufficient economic value to justify allocating parking bays to EV charging?"),
             ("RQ5", "What hypotheses must be validated through primary research and a pilot before the model can be responsibly scaled?")]:
    rq.append([P("<b>" + n + "</b>", CELL), P(q, CELL)])
story.append(styled_table(rq, [16 * mm, W - 16 * mm]))

story.append(P("1.5 Scope", H2))
scope = [[P("<b>WITHIN SCOPE</b>", CELL_H), P("<b>OUTSIDE SCOPE</b>", CELL_H)],
         [P("Passenger EV segment (four-wheelers)<br/>Urban and Tier-1 Indian markets<br/>AC destination chargers (7\u201322 kW)<br/>Commercial destination categories<br/>Operator\u2013host partnership model<br/>Unit economics and scenario modelling", CELL),
          P("Highway DC fast charging<br/>Two- and three-wheeler charging<br/>Rural / Tier-3 markets<br/>Battery swapping infrastructure<br/>Fleet depot charging<br/>Primary interviews (proposed, not conducted)", CELL)]]
story.append(styled_table(scope, [W / 2, W / 2]))
story.append(NextPageTemplate("Ch2"))
story.append(PageBreak())

# ============================================================ CHAPTER 2
story.append(P("CHAPTER 02", CHAP_LABEL))
story.append(P("02 \u2014 Market &amp; Literature Review", H1))

story.append(P("2.1 Indian EV Market", H2))
story.append(stat_row([
    ("2.27", "M", "Total EV retail sales, CY2025<br/>+16% YoY (Autocar Pro, 2026)"),
    ("176.5", "K", "Electric passenger vehicles, CY2025<br/>+77% YoY (Autocar Pro, 2026)"),
    ("30", "%", "Govt EV penetration ambition, 2030<br/>vs ~8% today (MMCM, 2026)"),
]))
story.append(P("{} Two-wheelers dominate volumes with a 56% share (~1.28 million units in CY2025), "
               "followed by three-wheelers at ~35%; together they account for 91% of EV sales "
               "(Autocar Professional, 2026). Passenger four-wheelers are the smallest segment by "
               "units but among the fastest-growing in percentage terms, and \u2014 critically for "
               "this study \u2014 the segment whose range, charge duration and destination dwell "
               "patterns align best with AC destination charging." .format(badge("FACT"))))
story.append(ev_composition())
story.append(P("Source: Autocar Professional analysis of Vahan data, January 2026. "
               "Note: CY2025 figures; e-2W 56%, e-3W ~35%, e-PV ~7.8%.", CAPTION))
story.append(P("{} Tata Motors remains the largest player in the electric passenger vehicle "
               "segment (Cornell University, 2025). The segment\u2019s trajectory \u2014 99,693 units in "
               "CY2024 to 176,538 in CY2025 \u2014 implies that a destination-charging operator entering "
               "today builds ahead of mass adoption: an early-mover timing opportunity paired with "
               "early-period utilisation risk." .format(badge("FACT"))))

story.append(P("2.2 EV Charging Behaviour", H2))
story.append(P("Charging behaviour decomposes into five location types with distinct economics:"))
beh = [[P("<b>LOCATION</b>", CELL_H), P("<b>USER TYPE</b>", CELL_H), P("<b>ECONOMICS</b>", CELL_H), P("<b>RELEVANCE TO THIS MODEL</b>", CELL_H)],
       [P("<b>Home</b>", CELL), P("Owners with parking", CELL), P("Cheapest per kWh; slow", CELL), P("Low \u2014 self-sufficient", CELL)],
       [P("<b>Workplace</b>", CELL), P("Employees", CELL), P("Often subsidised; long dwell", CELL), P("Medium \u2014 offices are viable hosts", CELL)],
       [P("<b>Fleet / depot</b>", CELL), P("Fleets, ride-hailing", CELL), P("High volume, managed", CELL), P("Medium \u2014 utilisation anchor", CELL)],
       [P("<b>Public fast (DC)</b>", CELL), P("En-route travellers", CELL), P("Premium price, fast turn", CELL), P("Low \u2014 different model", CELL)],
       [P("<b>Destination (AC)</b>", CELL), P("Shoppers, diners, guests", CELL), P("Value aligned with dwell", CELL), P("High \u2014 this study\u2019s subject", CELL)]]
story.append(styled_table(beh, [28 * mm, 36 * mm, 52 * mm, W - 116 * mm]))
story.append(P("{} Home charging dominates energy delivery wherever it is available, at Rs.5\u20138/kWh "
               "versus Rs.15\u201330/kWh on public networks (EVBlogs, 2025). The addressable pool for "
               "destination charging is therefore concentrated among owners who <i>cannot</i> reliably "
               "charge at home \u2014 apartment dwellers, households without dedicated parking, "
               "ride-hailing drivers and long-trip urban drivers. Fleet size must never be conflated "
               "with public-charging demand." .format(badge("FACT"))))

story.append(P("2.3 Destination Charging \u2014 Definition and Rationale", H2))
story.append(P("Destination charging is infrastructure installed where users arrive for a primary "
               "purpose other than charging \u2014 shopping, dining, medical care, work, overnight "
               "stay. The session is incidental to the visit; the charger monetises time the user "
               "would have spent at the location regardless. Its economics rest on <i>dwell-time "
               "alignment</i>: a 7\u201322 kW AC charger can add 30\u201350 km of range over a 2\u20133 hour "
               "visit, sufficient for most urban use cases."))
story.append(P("The model is structurally distinct from both home charging (cheapest, private) and "
               "highway fast charging (premium, throughput-driven). It competes on convenience and "
               "routine integration \u2014 charging that requires no detour, no wait and no dedicated "
               "trip. That convenience must be worth the premium over home tariffs; whether drivers "
               "agree is Hypothesis H1 (Chapter 7)."))
pil2 = PILImage.open("assets/parking.jpg")
pw, ph = pil2.size
story.append(Image("assets/parking.jpg", width=W, height=W * ph / pw))
story.append(P("Figure 2.4 \u2014 Destination parking as convertible infrastructure: marked bays, "
               "existing electrical access and captive dwell time. Source: commissioned "
               "illustration for this report.", CAPTION))

story.append(P("2.4 Existing Research / Industry Evidence", H2))
ev2 = [[P("<b>INFRASTRUCTURE EXPANSION</b>", CELL_H), P("<b>OPERATIONAL PERFORMANCE</b>", CELL_H)],
       [P("{} Stations grew 5,151 (Dec 2022) \u2192 25,202 (Dec 2024) \u2192 29,277 (Aug 2025) across 83 CPOs (Ministry of Power, 2025).<br/><br/>{} Concentration is severe: five states hold ~60% of stations; Bengaluru alone reports ~5,880 (ORF, 2025; Avaada, 2026).<br/><br/>{} Including semi-public points, the count crosses ~39,500 chargers by late 2025 (Bolt.Earth, 2026)." .format(badge("FACT"), badge("FACT"), badge("FACT")), CELL),
        P("{} Of 27,737 stations reported to Parliament, only 22,753 were operational \u2014 18% non-functional; BPCL at 60%; utilisation as low as 5% at many sites (MMCM, 2026).<br/><br/>{} Premium urban leases consume up to 40% of project budgets (Mordor Intelligence, 2025).<br/><br/>{} Policy favours land-sharing: malls, workplaces and fuel stations are designated preferred hosts (Bolt.Earth, 2025)." .format(badge("FACT"), badge("FACT"), badge("FACT")), CELL)]]
story.append(styled_table(ev2, [W / 2, W / 2]))
story.append(pcs_growth())
story.append(P("Source: Ministry of Power (2025) via ORF (2025); 2030 requirement per ORF. "
               "The 2030 bar is 45\u00d7 the current base and shown as annotation, not to scale.", CAPTION))

story.append(P("2.5 Research Gap", H2))
story.append(finding_block(
    "Market data establishes EV and infrastructure growth. It does not establish whether "
    "individual destination sites can achieve economically sustainable utilisation.",
    "Published utilisation spans from below 5% at weak sites to far higher at mature ones; "
    "the distribution is unknown. Site-level session volume requires primary data absent "
    "from existing literature."))
story.append(P("This gap defines the study\u2019s contribution: it translates macro demand signals "
               "into site-level economics, identifies the exact thresholds that must hold, and "
               "specifies how each threshold will be tested \u2014 rather than asserting viability from "
               "aggregate growth rates."))

story.append(P("2.6 Conceptual Framework", H2))
story.append(P("The analytical framework connects macro EV demand through the site-selection "
               "filter to session-level economics:"))
story.append(framework_flow())
story.append(P("Source: author\u2019s conceptual framework. Each arrow is a hypothesis: demand must "
               "convert to arrivals, arrivals to sessions, sessions to host value, and host value "
               "to sustainable operator margin.", CAPTION))
story.append(NextPageTemplate("Ch3"))
story.append(PageBreak())

# ============================================================ CHAPTER 3
story.append(P("CHAPTER 03", CHAP_LABEL))
story.append(P("03 \u2014 Proposed Business Model", H1))

story.append(P("3.1 Concept", H2))
story.append(P("An independent charging operator partners with commercial destination businesses. "
               "The operator supplies, installs, operates and maintains AC charging equipment in "
               "selected bays of the host\u2019s existing parking; the host provides land, electricity "
               "access and footfall. Charging revenue is shared under a pre-agreed commercial "
               "structure. The core insight is asset synthesis: the operator gains location access "
               "without land acquisition; the host monetises underutilised parking without "
               "operational complexity. Neither party captures the full value alone."))
story.append(P("The model targets AC charging (7\u201322 kW) because destination dwell times of 45 "
               "minutes to several hours match AC charge curves, equipment and grid-connection "
               "costs are an order of magnitude below DC fast charging, and most urban top-up needs "
               "are satisfied within a single visit."))

story.append(P("3.2 Stakeholders", H2))
story.append(stakeholder())
story.append(P("Source: author\u2019s framework. The operator is the commercial hub: it contracts "
               "with drivers for energy and with hosts for site access.", CAPTION))
story.append(P("Three contracts define the system: driver\u2013operator (price per kWh, payment, "
               "reliability expectation), operator\u2013host (revenue share or access fee, bay "
               "availability, contract term, branding), and the implicit driver\u2013host relationship "
               "(the visit itself). Failure in any one contract \u2014 distrusted chargers, defecting "
               "hosts, absent drivers \u2014 collapses site economics."))

story.append(P("3.3 Three-Sided Value Model", H2))
vm = [[P("<b>EV DRIVER</b>", CELL_H), P("<b>HOST BUSINESS</b>", CELL_H), P("<b>OPERATOR</b>", CELL_H)],
      [P("Charges during existing visit \u2014 no detour<br/>Predictable location in daily routine<br/>Reduced urban range anxiety<br/>AC speed matched to dwell<br/><br/>{} Range anxiety is a documented adoption barrier" .format(badge("FACT")), CELL),
       P("Revenue share per session<br/>No capital or operational burden<br/>Better use of selected bays<br/>EV-friendly differentiation<br/><br/>{} Incremental customer spend requires validation" .format(badge("ASSUMPTION")), CELL),
       P("Session revenue<br/>Location access without land cost<br/>Network scale via partnerships<br/>Software and data value<br/><br/>{} Scale creates a defensible position" .format(badge("HYPOTHESIS")), CELL)]]
story.append(styled_table(vm, [W / 3, W / 3, W / 3]))
story.append(P("Each column\u2019s evidence status differs deliberately. Driver convenience is "
               "supported by charging-behaviour literature; host upside beyond the revenue share is "
               "assumed; operator defensibility is hypothesised and directly challenged by "
               "incumbent scale (Chapter 6)."))

story.append(P("3.4 Customer Journey", H2))
story.append(journey())
story.append(P("Source: author\u2019s conceptual framework. Friction at any step \u2014 occupied bays, "
               "app failures, opaque pricing \u2014 converts directly into lost sessions.", CAPTION))
story.append(P("Journey reliability is the product. With a national non-functional rate of 18% "
               "(MMCM, 2026), a new operator\u2019s credible promise is not more chargers but "
               "dependable ones: live bay availability, single-tap payment, enforced EV-only bays "
               "and published uptime. Chapter 7 sets the uptime hypothesis (H6) at \u226590%."))

story.append(P("3.5 Revenue Model", H2))
story.append(P("{} The operator charges drivers per kWh. Observed public AC rates cluster around "
               "Rs.8\u201315/kWh (Pulse Energy, 2025), while full public-network tariffs span "
               "Rs.15\u201330/kWh (EVBlogs, 2025). The operator pays electricity at the commercial "
               "tariff (Rs.6\u201315/kWh depending on state and load) plus the host\u2019s share. The "
               "spread between consumer price and total delivered cost determines contribution per "
               "session \u2014 modelled rigorously in Chapter 5." .format(badge("FACT"))))
story.append(P("Three commercial structures are available; the choice trades host income certainty "
               "against operator risk:"))
cs = [[P("<b>STRUCTURE</b>", CELL_H), P("<b>MECHANICS</b>", CELL_H), P("<b>WHEN IT FITS</b>", CELL_H)],
      [P("<b>Revenue share</b>", CELL), P("Host receives 15\u201325% of session revenue", CELL), P("Operator confident in utilisation; host accepts variability", CELL)],
      [P("<b>Fixed access fee</b>", CELL), P("Host receives fixed monthly rent per bay", CELL), P("Host demands certainty; operator carries utilisation risk", CELL)],
      [P("<b>Hybrid</b>", CELL), P("Base fee + reduced variable share", CELL), P("Early sites: de-risks host while preserving upside alignment", CELL)]]
story.append(styled_table(cs, [34 * mm, 62 * mm, W - 96 * mm]))
story.append(P("{} The hybrid structure is the recommended default for pilot sites: it secures host "
               "commitment during the unproven ramp-up period while keeping both parties exposed to "
               "session volume." .format(badge("ASSUMPTION"))))
story.append(NextPageTemplate("Ch4"))
story.append(PageBreak())

# ============================================================ CHAPTER 4
story.append(P("CHAPTER 04", CHAP_LABEL))
story.append(P("04 \u2014 Market &amp; Customer Analysis", H1))

story.append(P("4.1 Target Customer Segments", H2))
seg = [[P("<b>SEGMENT</b>", CELL_H), P("<b>CHARACTERISTICS</b>", CELL_H), P("<b>RELEVANCE</b>", CELL_H), P("<b>STATUS</b>", CELL_H)],
       [P("<b>Apartment-dwelling owners</b>", CELL), P("No home charging; regular destination pattern", CELL), P("High \u2014 primary pool", CELL), P(badge("HYPOTHESIS"), CELL)],
       [P("<b>Villa / bungalow owners</b>", CELL), P("Reliable home charging", CELL), P("Low \u2014 supplementary only", CELL), P(badge("FACT"), CELL)],
       [P("<b>Ride-hailing / fleet drivers</b>", CELL), P("High daily km; no employer charging", CELL), P("Medium\u2013High \u2014 frequent users", CELL), P(badge("HYPOTHESIS"), CELL)],
       [P("<b>Long-trip urban drivers</b>", CELL), P("Opportunity charging mid-journey", CELL), P("Medium", CELL), P(badge("HYPOTHESIS"), CELL)],
       [P("<b>Corporate employees</b>", CELL), P("Office-adjacent; possible subsidy", CELL), P("Medium \u2014 model-dependent", CELL), P(badge("ASSUMPTION"), CELL)]]
story.append(styled_table(seg, [38 * mm, 58 * mm, 42 * mm, W - 138 * mm]))
story.append(P("Segmentation matters because willingness to pay a premium over home tariffs "
               "concentrates in the first and third rows. Marketing spend aimed at villa owners "
               "with home chargers would subsidise sessions that add no network value \u2014 a customer-"
               "acquisition discipline the pilot must enforce (Appendix D)."))

story.append(P("4.2 Destination Category Assessment", H2))
dest = [[P("<b>DESTINATION</b>", CELL_H), P("<b>TYPICAL DWELL</b>", CELL_H), P("<b>RELEVANCE</b>", CELL_H), P("<b>HOST CONSIDERATIONS</b>", CELL_H), P("<b>OPPORTUNITY</b>", CELL_H)],
        [P("<b>Mall</b>", CELL), P("2\u20134 hrs", CELL), P("High", CELL), P("Large inventory; footfall data", CELL), P("High", CELL)],
        [P("<b>Hotel (overnight)</b>", CELL), P("8\u201314 hrs", CELL), P("Very high", CELL), P("Ideal overnight AC; premium fit", CELL), P("High", CELL)],
        [P("<b>Office</b>", CELL), P("7\u20139 hrs", CELL), P("High", CELL), P("Captive daily users; subsidy potential", CELL), P("High", CELL)],
        [P("<b>University</b>", CELL), P("4\u20138 hrs", CELL), P("High", CELL), P("Growing faculty EV use; policy support", CELL), P("High", CELL)],
        [P("<b>Hospital</b>", CELL), P("1\u20136 hrs", CELL), P("Medium\u2013High", CELL), P("Variable visitor mix", CELL), P("Medium\u2013High", CELL)],
        [P("<b>Theatre</b>", CELL), P("2\u20133 hrs", CELL), P("Medium\u2013High", CELL), P("Peak windows; episodic footfall", CELL), P("Medium", CELL)],
        [P("<b>Supermarket</b>", CELL), P("30\u201390 min", CELL), P("Medium", CELL), P("Short dwell caps kWh; high turnover", CELL), P("Medium", CELL)],
        [P("<b>Restaurant</b>", CELL), P("45\u201390 min", CELL), P("Medium", CELL), P("Limited parking; high opportunity cost", CELL), P("Low\u2013Medium", CELL)]]
story.append(styled_table(dest, [30 * mm, 24 * mm, 28 * mm, 52 * mm, W - 134 * mm], font_size=8.2))
story.append(P("Table 4.1 \u2014 Destination Category Assessment. Source: author\u2019s analysis. Dwell "
               "times are estimates absent primary research; opportunity ratings are qualitative "
               "judgements, not scored metrics.", CAPTION))
story.append(P("The ranking logic is dwell \u00d7 parking headroom \u00d7 EV-owner affinity. Overnight and "
               "workday sites dominate because long dwell converts directly into delivered kWh per "
               "session \u2014 the revenue unit. Restaurants rank lowest despite high footfall because "
               "parking scarcity raises the host\u2019s opportunity cost above any plausible revenue share."))

story.append(P("4.3 Customer Pain Points", H2))
pp = [[P("<b>DISCOVERY &amp; ACCESS</b>", CELL_H), P("<b>SESSION EXPERIENCE</b>", CELL_H)],
      [P("\u2014 <b>Range anxiety:</b> depletion fear before reaching a charger<br/>\u2014 <b>Availability:</b> occupied or dead chargers on arrival<br/>\u2014 <b>Detour time:</b> diversion to dedicated stations<br/>\u2014 <b>Queues:</b> unpredictable waits at popular points", CELL),
       P("\u2014 <b>Reliability:</b> 18% national non-functional rate (MMCM, 2026)<br/>\u2014 <b>Payment friction:</b> fragmented apps and wallets<br/>\u2014 <b>ICE-blocking:</b> non-EVs occupying EV bays<br/>\u2014 <b>Price opacity:</b> tariffs vary by state, operator, hour", CELL)]]
story.append(styled_table(pp, [W / 2, W / 2]))
story.append(P("Every pain point is a product requirement: live availability, enforced bays, "
               "interoperable payment and published tariffs. Notably, reliability and ICE-blocking "
               "are operator-controllable \u2014 the two cheapest differentiators against incumbents."))

story.append(P("4.4 Addressable Market \u2014 Filtering Framework", H2))
story.append(P("{} The funnel below filters from total EV sales to the behaviourally relevant pool. "
               "All intermediate figures are directional estimates, not a market-sizing forecast."
               .format(badge("ESTIMATE"))))
story.append(funnel())
story.append(P("Source: author\u2019s analysis based on Autocar Professional (2026), IESA (2025) and "
               "Cornell University (2025). The 40\u201355% home-charging-gap assumption is the "
               "funnel\u2019s pivotal input and is currently unvalidated.", CAPTION))
story.append(finding_block(
    "The passenger-EV addressable pool is currently small but growing ~77% annually.",
    "At 176,538 new electric passenger vehicles in CY2025, the fleet compounds fast. An "
    "operator entering today builds ahead of mass adoption \u2014 timing opportunity paired with "
    "early-period utilisation risk."))
story.append(P("{} A widespread unstated assumption in charging business cases is that EV owners "
               "will use public charging regularly. Home-charging preference challenges this "
               "directly: the segment that <i>cannot</i> charge reliably at home is the primary "
               "market, and its size in urban India cannot be determined from public data."
               .format(badge("ASSUMPTION"))))
story.append(P("<b>Evidence currently unavailable / requires primary validation:</b> what share of "
               "India\u2019s electric passenger-vehicle owners lack reliable home-charging access? "
               "This single input dominates the demand model and is the highest-priority question "
               "for Phase-1 interviews (Appendix A)."))
story.append(NextPageTemplate("Ch5"))
story.append(PageBreak())

# ============================================================ CHAPTER 5
story.append(P("CHAPTER 05", CHAP_LABEL))
story.append(P("05 \u2014 Economic Feasibility", H1))
story.append(finding_block(
    "Utilisation is the central economic variable \u2014 but price, tariff and revenue share decide whether any utilisation level suffices.",
    "A bay with insufficient session volume fails regardless of EV growth. As shown below, "
    "under reference-case inputs the bay fails at <i>every</i> plausible utilisation level; "
    "viability requires a stricter parameter envelope defined in Section 5.3."))
story.append(P("This chapter models a single AC bay (7\u201322 kW), corrects the reference case "
               "arithmetically, derives the breakeven frontier across parameter combinations, and "
               "defines the viable-parameter set used for the three-year scenario. All inputs are "
               "sourced from industry data where available and otherwise labelled."))

story.append(P("5.1 Unit Economics \u2014 Single Charging Bay", H2))
capex = [[P("<b>CAPEX ITEM</b>", CELL_H), P("<b>RANGE (Rs.)</b>", CELL_H), P("<b>STATUS</b>", CELL_H)],
         [P("AC charger hardware (7\u201322 kW)", CELL), P("40,000 \u2013 1,20,000", CELL), P("{} Pulse Energy (2026); GlobalsBlog (2026)" .format(badge("FACT")), CELL)],
         [P("Electrical wiring, cabling, conduit", CELL), P("20,000 \u2013 80,000", CELL), P("{} Pulse Energy (2026)" .format(badge("FACT")), CELL)],
         [P("Electricity connection upgrade", CELL), P("50,000 \u2013 2,00,000", CELL), P("{} Pulse Energy (2026)" .format(badge("FACT")), CELL)],
         [P("Civil works (trenching, mounting)", CELL), P("50,000 \u2013 2,00,000", CELL), P("{} Pulse Energy (2026)" .format(badge("FACT")), CELL)],
         [P("Signage, bay marking, safety", CELL), P("10,000 \u2013 30,000", CELL), P(badge("ESTIMATE"), CELL)],
         [P("<b>Total per bay \u2014 low / mid / high</b>", CELL), P("<b>~1.7L / ~3.0L / ~6.0L</b>", CELL), P(badge("ESTIMATE"), CELL)]]
story.append(styled_table(capex, [62 * mm, 44 * mm, W - 106 * mm]))
story.append(P("Table 5.1 \u2014 CAPEX per Charging Bay. Sources as cited. Equipment is only 30\u201350% "
               "of total investment; civil and grid works dominate (GlobalsBlog, 2026).", CAPTION))
opex = [[P("<b>ANNUAL OPEX ITEM</b>", CELL_H), P("<b>COST (Rs.)</b>", CELL_H), P("<b>STATUS</b>", CELL_H)],
        [P("Electricity (Rs.6\u201315/kWh commercial tariff)", CELL), P("Variable per session", CELL), P("{} Pulse Energy (2025)" .format(badge("FACT")), CELL)],
        [P("Annual maintenance contract", CELL), P("15,000 \u2013 50,000", CELL), P("{} GlobalsBlog (2026)" .format(badge("FACT")), CELL)],
        [P("Network / OCPP software (mandated for public stations)", CELL), P("24,000 \u2013 1,20,000", CELL), P("{} GlobalsBlog (2026)" .format(badge("FACT")), CELL)],
        [P("Insurance", CELL), P("8,000 \u2013 25,000", CELL), P("{} GlobalsBlog (2026)" .format(badge("FACT")), CELL)],
        [P("<b>Fixed OpEx envelope per bay</b>", CELL), P("<b>~50,000 \u2013 1,95,000</b>", CELL), P(badge("ESTIMATE"), CELL)]]
story.append(styled_table(opex, [62 * mm, 44 * mm, W - 106 * mm]))
story.append(P("Table 5.2 \u2014 Operating Cost per Bay (excl. electricity). Sources as cited; the "
               "modelling in Sections 5.2\u20135.3 uses Rs.80,000 (reference) and Rs.70,000 (viable "
               "set) within this envelope.", CAPTION))

story.append(P("5.2 Reference-Case Scenarios \u2014 Corrected", H2))
story.append(P("{} Reference inputs: 7.4 kW AC charger; consumer price Rs.12/kWh; 2-hour sessions "
               "delivering ~12 kWh; electricity Rs.9/kWh; host share 20% of gross; fixed OpEx "
               "Rs.80,000/bay/year. The table below is arithmetically exact." .format(badge("ASSUMPTION"))))
ref = [[P("<b>METRIC</b>", CELL_H), P("<b>CONSERVATIVE</b>", CELL_H), P("<b>BASE</b>", CELL_H), P("<b>HIGH</b>", CELL_H)],
       [P("Sessions / bay / day", CELL), P("3", CELL_C), P("6", CELL_C), P("10", CELL_C)],
       [P("kWh delivered / year", CELL), P("13,140", CELL_C), P("26,280", CELL_C), P("43,800", CELL_C)],
       [P("Gross revenue / year", CELL), P("Rs.1,57,680", CELL_C), P("Rs.3,15,360", CELL_C), P("Rs.5,25,600", CELL_C)],
       [P("Electricity @ Rs.9/kWh", CELL), P("Rs.1,18,260", CELL_C), P("Rs.2,36,520", CELL_C), P("Rs.3,94,200", CELL_C)],
       [P("Host share (20%)", CELL), P("Rs.31,536", CELL_C), P("Rs.63,072", CELL_C), P("Rs.1,05,120", CELL_C)],
       [P("Fixed OpEx / year", CELL), P("Rs.80,000", CELL_C), P("Rs.80,000", CELL_C), P("Rs.80,000", CELL_C)],
       [P("<b>Net contribution / year</b>", CELL), P("<b>Rs.\u221272,116</b>", CELL_C), P("<b>Rs.\u221264,232</b>", CELL_C), P("<b>Rs.\u221253,720</b>", CELL_C)],
       [P("<b>Payback (Rs.3L bay)</b>", CELL), P("<b>Not achieved</b>", CELL_C), P("<b>Not achieved</b>", CELL_C), P("<b>Not achieved</b>", CELL_C)]]
story.append(styled_table(ref, [52 * mm, (W - 52 * mm) / 3, (W - 52 * mm) / 3, (W - 52 * mm) / 3]))
story.append(P("Table 5.3 \u2014 Reference-Case Scenario Model (corrected arithmetic). Source: "
               "author\u2019s analysis from Pulse Energy (2025, 2026) and GlobalsBlog (2026) inputs. "
               "Illustrative scenarios, not forecasts.", CAPTION))
story.append(P("The reference case fails structurally, not marginally. The operator retains "
               "Rs.12 \u2212 Rs.9 \u2212 Rs.2.40 = <b>Rs.0.60/kWh</b>, i.e. <b>Rs.7.20 per session</b>. "
               "Covering Rs.80,000 of fixed cost at Rs.7.20/session requires 11,111 sessions/year "
               "\u2014 <b>~30.4 sessions/bay/day</b>, roughly four times the physical maximum for "
               "2-hour AC sessions. Higher utilisation barely helps: each added daily session "
               "contributes only ~Rs.2,628/year."))
story.append(warn_block("Reference-case verdict: not viable at any plausible utilisation.",
                        "Under Rs.12 / Rs.9 / 20% inputs, losses persist from 3 to 10 sessions/day "
                        "and payback is never achieved. Any business plan using these inputs must be "
                        "rejected or restructured \u2014 the required fix is not more volume but a wider "
                        "per-kWh spread, derived next."))

story.append(P("5.3 Sensitivity Analysis &amp; the Viability Frontier", H2))
story.append(P("Because the reference case cannot break even, sensitivity is measured on the "
               "viable-parameter set (VPS) defined below \u2014 the envelope within which the model "
               "can work. Directional impacts on annual margin from the VPS base:"))
sens = [[P("<b>VARIABLE</b>", CELL_H), P("<b>CHANGE</b>", CELL_H), P("<b>IMPACT ON MARGIN</b>", CELL_H)],
        [P("Sessions / day", CELL), P("6 \u2192 4", CELL), P("Down ~Rs.42K", CELL)],
        [P("Sessions / day", CELL), P("6 \u2192 8", CELL), P("Up ~Rs.42K", CELL)],
        [P("Electricity tariff", CELL), P("Rs.8 \u2192 Rs.11/kWh", CELL), P("Down ~Rs.79K \u2014 erases base margin", CELL)],
        [P("Consumer price", CELL), P("Rs.15 \u2192 Rs.13/kWh", CELL), P("Down ~Rs.45K", CELL)],
        [P("Host share", CELL), P("15% \u2192 25%", CELL), P("Down ~Rs.39K", CELL)],
        [P("Charger CAPEX", CELL), P("Rs.3L \u2192 Rs.5L", CELL), P("Payback 5.5y \u2192 9.1y", CELL)],
        [P("Charger CAPEX", CELL), P("Rs.3L \u2192 Rs.1.5L", CELL), P("Payback 5.5y \u2192 2.7y", CELL)],
        [P("Charger uptime", CELL), P("90% \u2192 75%", CELL), P("Down ~Rs.19K plus trust damage", CELL)]]
story.append(styled_table(sens, [44 * mm, 44 * mm, W - 88 * mm]))
story.append(P("Table 5.4 \u2014 Sensitivity of VPS Base-Case Margin. Source: author\u2019s analysis. "
               "Electricity tariff is the dominant risk: a Rs.3/kWh rise alone destroys viability.", CAPTION))
story.append(P("The breakeven frontier below compares four price/tariff/share combinations. Only "
               "combinations holding breakeven below the physical ceiling (~8 sessions/day for AC "
               "destination bays) are investable:"))
story.append(breakeven())
story.append(P("Source: author\u2019s analysis; fixed OpEx Rs.70,000/bay/year, 12 kWh/session. "
               "Combination A (reference) requires an impossible 30.4 sessions/day.", CAPTION))
story.append(P("{} <b>Viable-parameter set (VPS).</b> Consumer price Rs.15/kWh (upper end of the "
               "observed Rs.8\u201315 AC range \u2014 a destination-convenience premium); electricity "
               "Rs.8/kWh (low-mid commercial tariff \u2014 a site-selection threshold); host share 15% "
               "of gross; fixed OpEx Rs.70,000/year (AMC Rs.25,000 + software Rs.30,000 + insurance "
               "Rs.15,000). Per-session margin: 12 kWh \u00d7 Rs.4.75 = Rs.57.00; breakeven = "
               "70,000 / (57 \u00d7 365) = <b>~3.4 sessions/bay/day</b>." .format(badge("ASSUMPTION"))))
vps = [[P("<b>METRIC</b>", CELL_H), P("<b>CONSERVATIVE (3/DAY)</b>", CELL_H), P("<b>BASE (6/DAY)</b>", CELL_H), P("<b>HIGH (10/DAY)</b>", CELL_H)],
       [P("kWh / year", CELL), P("13,140", CELL_C), P("26,280", CELL_C), P("43,800", CELL_C)],
       [P("Gross revenue / year", CELL), P("Rs.1,97,100", CELL_C), P("Rs.3,94,200", CELL_C), P("Rs.6,57,000", CELL_C)],
       [P("Electricity @ Rs.8/kWh", CELL), P("Rs.1,05,120", CELL_C), P("Rs.2,10,240", CELL_C), P("Rs.3,50,400", CELL_C)],
       [P("Host share (15%)", CELL), P("Rs.29,565", CELL_C), P("Rs.59,130", CELL_C), P("Rs.98,550", CELL_C)],
       [P("Fixed OpEx / year", CELL), P("Rs.70,000", CELL_C), P("Rs.70,000", CELL_C), P("Rs.70,000", CELL_C)],
       [P("<b>Net contribution / year</b>", CELL), P("<b>Rs.\u22127,585</b>", CELL_C), P("<b>+Rs.54,830</b>", CELL_C), P("<b>+Rs.1,38,050</b>", CELL_C)],
       [P("<b>Payback (Rs.3L bay)</b>", CELL), P("<b>Not achieved</b>", CELL_C), P("<b>~5.5 years</b>", CELL_C), P("<b>~2.2 years</b>", CELL_C)]]
story.append(styled_table(vps, [52 * mm, (W - 52 * mm) / 3, (W - 52 * mm) / 3, (W - 52 * mm) / 3]))
story.append(P("Table 5.5 \u2014 Viable-Parameter Scenario Model. Source: author\u2019s analysis. Do not "
               "treat the base case as a prediction; it is the threshold the pilot must clear.", CAPTION))
story.append(waterfall())
story.append(P("Electricity remains the largest outflow (~53% of gross even in the VPS); the host "
               "share and fixed OpEx consume most of the remainder, leaving a thin but positive "
               "base margin. Source: author\u2019s model.", CAPTION))
story.append(P("The VPS reframes the investment question precisely: the model is viable <i>if and "
               "only if</i> sites can be held inside the Rs.15/Rs.8/15% envelope while delivering "
               "\u22653.5 sessions/bay/day. Every element of that sentence is testable \u2014 tariff by "
               "site survey, price by driver interviews, sessions by pilot."))

story.append(P("5.4 Host Economics", H2))
story.append(P("The host weighs the revenue share against the bay\u2019s opportunity cost \u2014 a general "
               "parking space at a busy destination has real value:"))
he = [[P("<b>HOST RECEIVES \u2014 MEASURABLE</b>", CELL_H), P("<b>HOST RECEIVES \u2014 UNPROVEN</b>", CELL_H)],
      [P("\u2014 <b>Revenue share:</b> ~Rs.30K\u2013Rs.99K/bay/year across VPS scenarios (Rs.59,130 base) {}<br/>\u2014 <b>Zero CAPEX</b> and zero operational burden<br/>\u2014 <b>Contracted income</b> under hybrid base fee" .format(badge("ESTIMATE")), CELL),
       P("\u2014 <b>Incremental customer spend</b> while charging {} \u2014 requires POS-data experiment<br/>\u2014 <b>EV-owner acquisition</b> via green positioning {} \u2014 untested in India" .format(badge("HYPOTHESIS"), badge("HYPOTHESIS")), CELL)]]
story.append(styled_table(he, [W / 2, W / 2]))
story.append(warn_block("Critical assumption \u2014 host incentive.",
                        "At low utilisation the measurable share (~Rs.30K/year at 3 sessions/day) may "
                        "not beat the parking opportunity cost at capacity-constrained sites. Durable "
                        "host contracts therefore require either demonstrated volume or a hybrid base "
                        "fee \u2014 both untested. Host economics, not driver demand alone, can veto the model."))
story.append(P("The practical implication is contractual: pilot hosts should be offered the hybrid "
               "structure (base fee + reduced share) so the partnership survives the ramp-up "
               "period, with a contractual step-down to pure revenue share once the site clears 3.5 "
               "sessions/day for three consecutive months."))

story.append(P("5.5 Three-Year Scenario Model (VPS)", H2))
story.append(P('<font color="#A6564B"><b>SCENARIO MODEL \u2014 NOT A FORECAST.</b></font> Directional '
               "illustration of network expansion under VPS base assumptions. Location counts, "
               "revenues and costs are modelling inputs dependent on unvalidated assumptions."))
y3 = [[P("<b>METRIC</b>", CELL_H), P("<b>YEAR 1</b>", CELL_H), P("<b>YEAR 2</b>", CELL_H), P("<b>YEAR 3</b>", CELL_H)],
      [P("Active destination sites", CELL), P("5", CELL_C), P("15", CELL_C), P("35", CELL_C)],
      [P("Charging bays (avg 4/site)", CELL), P("20", CELL_C), P("60", CELL_C), P("140", CELL_C)],
      [P("Avg sessions/bay/day", CELL), P("3 (ramp-up)", CELL_C), P("5 (maturing)", CELL_C), P("6 (base)", CELL_C)],
      [P("Gross charging revenue", CELL), P("Rs.39L", CELL_C), P("Rs.1.97Cr", CELL_C), P("Rs.5.52Cr", CELL_C)],
      [P("Deployed CAPEX (cumulative)", CELL), P("Rs.60L", CELL_C), P("Rs.1.8Cr", CELL_C), P("Rs.4.2Cr", CELL_C)],
      [P("Annual contribution", CELL), P("Rs.\u22122L (est.)", CELL_C), P("+Rs.20L (est.)", CELL_C), P("+Rs.77L (est.)", CELL_C)],
      [P("Cumulative cash requirement", CELL), P("Rs.0.7Cr", CELL_C), P("Rs.2.2Cr", CELL_C), P("Rs.4.7Cr", CELL_C)]]
story.append(styled_table(y3, [52 * mm, (W - 52 * mm) / 3, (W - 52 * mm) / 3, (W - 52 * mm) / 3]))
story.append(P("Table 5.6 \u2014 Three-Year Directional Scenario (VPS). Source: author\u2019s model. "
               "L = lakh, Cr = crore. Cash requirement includes CAPEX, working capital and early "
               "losses; excludes corporate overhead, customer acquisition and platform development.", CAPTION))
story.append(P("<b>Key modelling observations.</b> (1) Year 1 is mildly loss-making: ramp-up "
               "sessions sit below the 3.4/day breakeven. (2) Year-2 surplus depends on all 15 sites "
               "individually holding 5 sessions/day \u2014 portfolio averaging must not mask weak "
               "sites. (3) ~Rs.4.7 crore cumulative cash by Year 3 requires external capital and is "
               "sensitive to CAPEX overrun and tariff drift. (4) Excluded overheads (team, CAC, "
               "platform) would deepen early losses materially and must be modelled before fundraising."))
story.append(NextPageTemplate("Ch6"))
story.append(PageBreak())

# ============================================================ CHAPTER 6
story.append(P("CHAPTER 06", CHAP_LABEL))
story.append(P("06 \u2014 Competitive &amp; Strategic Analysis", H1))

story.append(P("6.1 Competitive Landscape", H2))
story.append(P("{} India\u2019s charging market is multi-layered: integrated utility CPOs, oil-marketing "
               "companies converting forecourts, private fast-charging specialists, OEM-affiliated "
               "networks, distributed peer-to-peer platforms and hardware enablers (Marqstats, 2026). "
               "Scale leaders by reported network size include Tata Power EZ Charge (5,500\u20138,000+ "
               "public points plus 86,000+ home chargers), Jio-bp pulse (6,000\u20137,000+ points), "
               "Statiq (7,000\u20138,000+), ChargeZone (2,200+ fast points across 58+ cities, highway-"
               "led) and Bolt.Earth (100,000+ distributed sockets across 1,900+ cities), with Ather "
               "Grid concentrated in two-wheelers (Electric Vehicle Insights, 2026; Autonexa, 2026; "
               "EVBlogs, 2025)." .format(badge("FACT"))))
story.append(P("Two vectors threaten a destination entrant directly. First, large-balance-sheet "
               "players (Tata Power, Jio-bp) can outbid on host terms and lend brand credibility "
               "hosts trust. Second, asset-light partner models (Bolt.Earth, Statiq) already onboard "
               "hosts at scale through mechanics nearly identical to this study\u2019s proposition \u2014 "
               "with existing app users and recognition. The window for independent site acquisition "
               "is finite and shrinking."))

story.append(P("6.2 Competitive Comparison", H2))
comp = [[P("<b>OPERATOR</b>", CELL_H), P("<b>SCALE</b>", CELL_H), P("<b>FOCUS</b>", CELL_H), P("<b>HOST MODEL</b>", CELL_H), P("<b>RELEVANCE</b>", CELL_H)],
        [P("<b>Tata Power EZ Charge</b>", CELL), P("Large", CELL), P("Highway + urban", CELL), P("Partner programmes", CELL), P("High", CELL)],
        [P("<b>Jio-bp pulse</b>", CELL), P("Large, growing", CELL), P("Fuel-adjacent, DC", CELL), P("Retail network", CELL), P("Medium", CELL)],
        [P("<b>Statiq</b>", CELL), P("Medium\u2013Large", CELL), P("Urban, app-first", CELL), P("Active partner model", CELL), P("High", CELL)],
        [P("<b>Bolt.Earth</b>", CELL), P("Very large (P2P)", CELL), P("Residential, small commercial", CELL), P("Host model at scale", CELL), P("High", CELL)],
        [P("<b>ChargeZone</b>", CELL), P("Medium", CELL), P("Highway DC hubs", CELL), P("Limited destination", CELL), P("Medium", CELL)],
        [P("<b>Ather Grid</b>", CELL), P("Medium (2W)", CELL), P("Two-wheeler urban", CELL), P("2W host model", CELL), P("Low", CELL)],
        [P("<b>Dest. entrant (this study)</b>", CELL), P("Nascent", CELL), P("Destination-first AC", CELL), P("Core proposition", CELL), P("\u2014", CELL)]]
story.append(styled_table(comp, [38 * mm, 30 * mm, 36 * mm, 36 * mm, W - 140 * mm], font_size=8.2))
story.append(P("Table 6.1 \u2014 Competitive Landscape. Sources: Marqstats (2026), Electric Vehicle "
               "Insights (2026), Autonexa (2026), EVBlogs (2025), EVSelect (2026). Relevance ratings "
               "are qualitative judgements, not scored metrics.", CAPTION))
story.append(P("The table\u2019s uncomfortable message: no incumbent ignores destinations, and two "
               "(Statiq, Bolt.Earth) already execute host-partnership playbooks. Differentiation must "
               "therefore come from execution \u2014 site selection, uptime, host depth \u2014 not from "
               "the partnership concept itself, which is not proprietary."))

story.append(P("6.3 Strategic Positioning", H2))
story.append(P("Defensible differentiation is possible but must be earned site by site:"))
sp = [[P("<b>ACHIEVABLE DIFFERENTIATION</b>", CELL_H), P("<b>REQUIRES EVIDENCE</b>", CELL_H)],
      [P("\u2014 Underserved categories: mid-size offices, standalone hospitals, Tier-1 universities<br/>\u2014 Uptime leadership against the 18% national failure rate<br/>\u2014 Deep host integration: co-marketing, data sharing, branded experience<br/>\u2014 Fastest site onboarding via standardised install protocol", CELL),
       P("{} Destination focus creates loyalty vs general-network loyalty<br/>{} Enough underserved sites exist to reach sustainability before incumbents arrive<br/>{} Host relationships resist switching to larger networks" .format(badge("HYPOTHESIS"), badge("HYPOTHESIS"), badge("HYPOTHESIS")), CELL)]]
story.append(styled_table(sp, [W / 2, W / 2]))
story.append(P("The honest strategic summary: the entrant\u2019s edge is focus and speed against "
               "incumbents\u2019 scale and brand. That edge compounds only if early sites clear VPS "
               "thresholds quickly enough to fund the next wave before hosts sign with larger networks."))

story.append(P("6.4 Location Strategy", H2))
story.append(P("{} Site selection is the operating decision that sets utilisation and hence "
               "economics. The criteria below structure evaluation; indicative thresholds must be "
               "calibrated with pilot data." .format(badge("ASSUMPTION"))))
loc = [[P("<b>CRITERION</b>", CELL_H), P("<b>WHY IT MATTERS</b>", CELL_H), P("<b>INDICATIVE THRESHOLD</b>", CELL_H)],
       [P("<b>EV density in catchment</b>", CELL), P("Thin density caps session volume", CELL), P("Top-20% registration density in city", CELL)],
       [P("<b>Customer dwell time</b>", CELL), P("Under ~45 min, kWh/session is uneconomic", CELL), P(">60 min average dwell", CELL)],
       [P("<b>Parking headroom</b>", CELL), P("Shortage creates EV-vs-general conflict", CELL), P(">15% inventory allocable to EV", CELL)],
       [P("<b>Electricity infrastructure</b>", CELL), P("Weak supply forces costly upgrades", CELL), P("3-phase supply; upgrade &lt;Rs.1L/bay", CELL)],
       [P("<b>Commercial tariff</b>", CELL), P("Tariff above Rs.8 breaks the VPS", CELL), P("Effective tariff \u2264 Rs.8/kWh", CELL)],
       [P("<b>Competitor proximity</b>", CELL), P("Adjacent chargers split sessions", CELL), P("No rival charger within ~500 m", CELL)],
       [P("<b>Host commitment</b>", CELL), P("Weak hosts churn at first friction", CELL), P("Minimum 12-month contract", CELL)],
       [P("<b>Install accessibility</b>", CELL), P("Complex layouts inflate civil works", CELL), P("Civil estimate &lt;Rs.60K/bay", CELL)]]
story.append(styled_table(loc, [42 * mm, 62 * mm, W - 104 * mm]))
story.append(P("Table 6.2 \u2014 Site Selection Criteria. Source: author\u2019s analysis. Thresholds are "
               "indicative assumptions pending pilot calibration.", CAPTION))
story.append(positioning())
story.append(P("Source: author\u2019s qualitative positioning \u2014 illustrative, not metric-scored. The "
               "entrant occupies the partnership-led, destination-focused quadrant contested most "
               "directly by Statiq and Bolt.Earth.", CAPTION))
story.append(NextPageTemplate("Ch7"))
story.append(PageBreak())

# ============================================================ CHAPTER 7
story.append(P("CHAPTER 07", CHAP_LABEL))
story.append(P("07 \u2014 Validation &amp; Risk Analysis", H1))

story.append(P("7.1 Key Hypotheses Requiring Validation", H2))
story.append(P("Six hypotheses carry the model. None has been tested. Each maps to evidence, method "
               "and the consequence of failure:"))
hyp = [[P("<b>ID</b>", CELL_H), P("<b>HYPOTHESIS</b>", CELL_H), P("<b>EVIDENCE REQUIRED</b>", CELL_H), P("<b>METHOD</b>", CELL_H), P("<b>IF FALSE</b>", CELL_H)],
       [P("<b>H1</b>", CELL_C), P("Drivers regularly use destination charging on routine visits", CELL), P("Stated preference + session frequency", CELL), P("Driver interviews + pilot logs", CELL), P("Utilisation below breakeven", CELL)],
       [P("<b>H2</b>", CELL_C), P("Hosts allocate bays on 12-month terms", CELL), P("Surveys + signed agreements", CELL), P("Host interviews + negotiation", CELL), P("Network cannot form", CELL)],
       [P("<b>H3</b>", CELL_C), P("Charging lifts host customer spend measurably", CELL), P("EV vs non-EV transaction data", CELL), P("POS-data pilot experiment", CELL), P("Share alone must justify hosts", CELL)],
       [P("<b>H4</b>", CELL_C), P("Sites reach \u22653.5 sessions/bay/day in 6\u201312 months", CELL), P("Session logs per site", CELL), P("Pilot, \u22653 months data", CELL), P("Model stays loss-making", CELL)],
       [P("<b>H5</b>", CELL_C), P("15% host share secures and retains hosts", CELL), P("Outcomes across 5+ categories", CELL), P("Commercial negotiation data", CELL), P("Churn (too low) or margin loss (too high)", CELL)],
       [P("<b>H6</b>", CELL_C), P("\u226590% uptime is maintainable at destination sites", CELL), P("Uptime logs per site", CELL), P("Pilot monitoring, monthly", CELL), P("Distrust, session loss, host damage", CELL)]]
story.append(styled_table(hyp, [12 * mm, 52 * mm, 42 * mm, 42 * mm, W - 148 * mm], font_size=8.0))
story.append(P("Table 7.1 \u2014 Hypotheses and Validation Requirements. Source: author\u2019s analysis. "
               "H4\u2019s threshold follows the VPS breakeven (3.4/day); the reference case has no "
               "achievable threshold.", CAPTION))

story.append(P("7.2 Validation Plan", H2))
phases = [
    ("PHASE 1 \u2014 DISCOVERY (WEEKS 1\u20138)",
     "<b>Driver interviews (n=20\u201330)</b> across 2 cities: charging behaviour, home access, visit frequency, price response. Tests H1, informs H4.",
     "<b>Host interviews (n=15\u201320)</b> with mall, hotel, hospital, office managers: parking pressure, bay willingness, share expectations. Tests H2, H5."),
    ("PHASE 2 \u2014 COMMERCIAL (WEEKS 8\u201316)",
     "<b>Host intent signal:</b> operator landing page measuring enquiry-to-meeting conversion. Early H2 evidence without deployment.",
     "<b>Site economics:</b> per-site models for 8\u201310 prospects using local tariffs, registration density and 2\u20133 installation quotes each."),
    ("PHASE 3 \u2014 PILOT (MONTHS 4\u201310)",
     "<b>3\u20135 heterogeneous pilots</b> (mall, hotel, hospital/university, office), 3\u20134 bays each: sessions, kWh, demographics, uptime, host satisfaction. Tests H1, H4, H6.",
     "<b>H3 experiment (optional):</b> POS-data comparison of EV vs non-EV spend with host consent; privacy-reviewed."),
    ("PHASE 4 \u2014 DECISION (MONTHS 10\u201312)",
     "<b>Go / No-Go / Pivot</b> against pre-registered thresholds: \u22653 of 5 sites at \u22653.5 sessions/day by month 6, zero host churn, \u226590% uptime.",
     "<b>Locked metrics:</b> sessions/bay/day, uptime, renewal rate, CAC, revenue/site, pilot NPV \u2014 thresholds fixed before the pilot, never adjusted ex-post."),
]
for title, a, b in phases:
    ph = [[P("<b>" + title + "</b>", CELL_H), P("<b></b>", CELL_H)],
          [P(a, CELL), P(b, CELL)]]
    story.append(styled_table(ph, [W / 2, W / 2], zebra=False))
    story.append(Spacer(1, 2 * mm))
story.append(P("Figure 7.1 \u2014 Four-Phase Validation Plan. Source: author\u2019s framework. Total "
               "direct pilot cost is bounded by 12\u201320 bays of CAPEX plus operating losses \u2014 the "
               "cheapest reliable answer to the viability question.", CAPTION))

story.append(P("7.3 Risk Matrix", H2))
story.append(P("Risks are rated qualitatively on probability \u00d7 impact from industry evidence and "
               "the Chapter-5 model \u2014 not actuarially:"))
risk = [[P("<b>RISK</b>", CELL_H), P("<b>PROB.</b>", CELL_H), P("<b>IMPACT</b>", CELL_H), P("<b>RATING</b>", CELL_H), P("<b>MITIGATION</b>", CELL_H)],
        [P("<b>Persistent low utilisation</b> (&lt;3/day at maturity)", CELL), P("Med\u2013High", CELL_C), P("Critical", CELL_C), P("<b>HIGH</b>", CELL_C), P("Strict site criteria; exit clauses for weak sites", CELL)],
        [P("<b>Incumbent competition</b> for the same hosts", CELL), P("High", CELL_C), P("High", CELL_C), P("<b>HIGH</b>", CELL_C), P("First-mover contracts; exclusivity; faster onboarding", CELL)],
        [P("<b>Host churn</b> at renewal", CELL), P("Medium", CELL_C), P("High", CELL_C), P("<b>MED\u2013HIGH</b>", CELL_C), P("Long terms; hybrid fees; engagement programme", CELL)],
        [P("<b>Charger downtime</b> (&lt;85% uptime)", CELL), P("Medium", CELL_C), P("High", CELL_C), P("<b>MED\u2013HIGH</b>", CELL_C), P("Preventive maintenance; certified hardware; NOC monitoring", CELL)],
        [P("<b>Tariff volatility</b> (>20% rise)", CELL), P("Medium", CELL_C), P("High", CELL_C), P("<b>MED\u2013HIGH</b>", CELL_C), P("Tariff-indexed consumer pricing; site tariff caps", CELL)],
        [P("<b>ICE-blocking</b> of EV bays", CELL), P("High", CELL_C), P("Medium", CELL_C), P("<b>MEDIUM</b>", CELL_C), P("Bollards; enforcement protocol; bay monitoring", CELL)],
        [P("<b>CAPEX overrun</b>", CELL), P("Medium", CELL_C), P("Medium", CELL_C), P("<b>MEDIUM</b>", CELL_C), P("Standard installs; pre-surveyed capacity; contingency", CELL)],
        [P("<b>Grid / regulatory delay</b>", CELL), P("Medium", CELL_C), P("Low\u2013Med", CELL_C), P("LOW\u2013MED", CELL_C), P("Prioritise adequate-capacity sites; buffer lead times", CELL)],
        [P("<b>Customer acquisition cost</b>", CELL), P("Medium", CELL_C), P("Low\u2013Med", CELL_C), P("LOW\u2013MED", CELL_C), P("App interoperability (OCPI); host co-marketing", CELL)]]
story.append(styled_table(risk, [52 * mm, 20 * mm, 20 * mm, 24 * mm, W - 116 * mm], font_size=8.0))
story.append(P("Table 7.2 \u2014 Risk Register. Source: author\u2019s analysis. Tariff risk is rated "
               "up versus conventional assessments because Table 5.4 shows a Rs.3/kWh rise erases "
               "the entire VPS margin.", CAPTION))
mx = [[P("", CELL_C), P("<b>HIGH PROB.</b>", CELL_C), P("<b>MEDIUM PROB.</b>", CELL_C), P("<b>LOW PROB.</b>", CELL_C)],
      [P("<b>HIGH IMPACT</b>", CELL_C), P("Low utilisation<br/>Incumbent competition", CELL_C), P("Host churn<br/>Downtime<br/>Tariff volatility", CELL_C), P("", CELL_C)],
      [P("<b>MEDIUM IMPACT</b>", CELL_C), P("ICE-blocking", CELL_C), P("CAPEX overrun", CELL_C), P("CAC", CELL_C)],
      [P("<b>LOW IMPACT</b>", CELL_C), P("", CELL_C), P("Grid / regulatory", CELL_C), P("", CELL_C)]]
t = Table(mx, colWidths=[30 * mm, (W - 30 * mm) / 3, (W - 30 * mm) / 3, (W - 30 * mm) / 3])
t.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.4, LINES),
    ("BACKGROUND", (1, 1), (2, 1), HexColor("#F0D9D5")),
    ("BACKGROUND", (1, 2), (2, 2), HexColor("#ECE7DD")),
    ("BACKGROUND", (3, 2), (3, 2), HexColor("#E2E7E2")),
    ("BACKGROUND", (1, 3), (-1, 3), HexColor("#E2E7E2")),
    ("BACKGROUND", (3, 1), (3, 1), HexColor("#ECE7DD")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
]))
story.append(t)
story.append(P("Figure 7.2 \u2014 Risk Probability \u00d7 Impact Matrix. Source: author\u2019s analysis. "
               "The red zone \u2014 utilisation, competition, hosts, downtime, tariffs \u2014 is the "
               "pilot\u2019s measurement agenda.", CAPTION))
story.append(NextPageTemplate("Ch8"))
story.append(PageBreak())

# ============================================================ CHAPTER 8
story.append(P("CHAPTER 08", CHAP_LABEL))
story.append(P("08 \u2014 Findings &amp; Conclusion", H1))

story.append(P("What Is Supported by Evidence", H2))
sup = [[P("<b>EV MARKET GROWTH</b><br/>Passenger EVs +77% in CY2025; 2.27M total EVs. Demand for charging will rise. {}" .format(badge("FACT")), CELL),
        P("<b>INFRASTRUCTURE GAP</b><br/>1:235 charger-to-EV ratio; 1.32M stations needed by 2030. The gap is structural. {}" .format(badge("FACT")), CELL)],
       [P("<b>LAND-COST PROBLEM</b><br/>Urban leases absorb up to 40% of dedicated-project budgets. Host access avoids this. {}" .format(badge("FACT")), CELL),
        P("<b>POLICY ALIGNMENT</b><br/>De-licensed activity; Rs.2,000Cr PM E-DRIVE; designated host categories. {}" .format(badge("FACT")), CELL)]]
story.append(styled_table(sup, [W / 2, W / 2], header=False, zebra=False))

story.append(P("What Is Directionally Supported", H2))
story.append(finding_block(
    "Under viable parameters (Rs.15 / Rs.8 / 15%), base-case unit economics are positive: +Rs.54,830/bay/year at 6 sessions/day, ~5.5-year payback.",
    "Directionally viable \u2014 but conditional on holding every VPS input simultaneously. A "
    "single-parameter slip (tariff Rs.8\u2192Rs.11) erases the margin. The pilot must prove the "
    "envelope, not just the volume."))
story.append(finding_block(
    "The destination model structurally reduces site cost versus dedicated stations.",
    "Avoided land acquisition and shared electrical infrastructure lower CAPEX per bay \u2014 "
    "though the magnitude depends on site-specific upgrade needs, which vary 4\u00d7 in the data."))

story.append(P("What Remains Unproven", H2))
un = [[P("<b>UNPROVEN ELEMENT</b>", CELL_H), P("<b>WHY</b>", CELL_H), P("<b>IF WRONG</b>", CELL_H)],
      [P("Driver demand for destination charging", CELL), P("No interviews or session data", CELL), P("Sessions below breakeven; model fails", CELL)],
      [P("Host willingness to commit parking", CELL), P("No negotiations conducted", CELL), P("Network cannot form", CELL)],
      [P("Incremental host revenue from EV users", CELL), P("No transaction data", CELL), P("Share alone must justify hosts", CELL)],
      [P("Sustainable competitive position", CELL), P("Incumbents expanding into hosts", CELL), P("First-mover window closes early", CELL)],
      [P("VPS tariff/price envelope", CELL), P("Rs.15/Rs.8/15% jointly untested", CELL), P("Reverts to reference-case losses", CELL)]]
story.append(styled_table(un, [52 * mm, 52 * mm, W - 104 * mm]))
story.append(P("Table 8.1 \u2014 Unproven Elements. Source: author\u2019s analysis. Any single row "
               "failing is sufficient to reject or pivot the model.", CAPTION))

story.append(P("Conditions for Viability", H2))
cond = [[P("<b>01 \u2014 UTILISATION</b><br/>\u22653.5 sessions/bay/day within 6\u201312 months. Below this the VPS base does not contribute.", CELL),
         P("<b>02 \u2014 PRICE / TARIFF SPREAD</b><br/>Consumer price \u2265 Rs.15 with commercial tariff \u2264 Rs.8. The spread is the business.", CELL)],
        [P("<b>03 \u2014 HOST SHARE \u2264 15\u201320%</b><br/>Higher shares transfer the margin to the host. Hybrid fees only during ramp-up.", CELL),
         P("<b>04 \u2014 UPTIME \u2265 90%</b><br/>The 18% national failure rate must not be replicated; trust is the product.", CELL)],
        [P("<b>05 \u2014 COMPETITIVE ACCESS</b><br/>Secure hosts before larger networks do. The window is finite and shrinking.", CELL),
         P("<b>06 \u2014 SITE DISCIPLINE</b><br/>Reject sub-threshold sites; exit weak ones fast. Averages must not hide failures.", CELL)]]
story.append(styled_table(cond, [W / 2, W / 2], header=False, zebra=False))

story.append(P("Recommendation", H2))
rec = [[P("The destination-charging model is structurally coherent and addresses a documented infrastructure gap. Its economics are viable <b>only inside a narrow, testable parameter envelope</b> \u2014 and every parameter in that envelope is currently unvalidated. <b>No scaling decision should be made on the basis of this analysis alone.</b><br/><br/>The recommended next step is the structured, time-bounded validation programme in Chapter 7 (Phases 1\u20133), designed to force a Go / No-Go / Pivot decision within 10\u201312 months against pre-registered thresholds that are never adjusted after data collection.", BODY)]]
rt = Table(rec, colWidths=[W])
rt.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, SAGE),
                        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#EFF1EC")),
                        ("TOPPADDING", (0, 0), (-1, -1), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                        ("LEFTPADDING", (0, 0), (-1, -1), 12),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 12)]))
story.append(rt)
story.append(Spacer(1, 4 * mm))
story.append(evidence_maturity())
story.append(P("Source: author\u2019s assessment. Bar length reflects qualitative confidence, not a "
               "statistical measure. The drop from market evidence to site-level validation is the "
               "report\u2019s central message.", CAPTION))
story.append(P("<b>Research limitations.</b> This study relies entirely on secondary data, industry "
               "reports and analytical modelling. No primary interviews, negotiations or pilot data "
               "were collected. All models contain unvalidated assumptions. Use this report as the "
               "foundation for a primary-research programme \u2014 not as a basis for capital "
               "allocation.", BODY_S))
story.append(NextPageTemplate("Refs"))
story.append(PageBreak())

# ============================================================ REFERENCES
story.append(P("REFERENCES", CHAP_LABEL))
story.append(P("References", H1))
story.append(P("APA 7th edition. URLs given for directly consulted sources; remaining entries are "
               "industry and policy sources as compiled in the project research.", BODY_S))
refs = [
    "Autocar Professional. (2026, January 7). <i>EV sales in India hit record 2.27 million in CY2025, all 4 segments scale new highs.</i> https://www.autocarpro.in",
    "Autocar Professional. (2026, January 2). <i>Electric car and SUV sales hit highest level in CY2025: 176,538 units.</i> https://www.autocarpro.in",
    "Autocar Professional. (2026, January 1). <i>Record 1.28 million e-2Ws sold in CY2025.</i> https://www.autocarpro.in",
    "Autocar Professional. (2025, July 8). <i>EV sales in India race past a million units in first-half CY2025.</i> https://www.autocarpro.in",
    "Humans of EV. (2025, December). <i>India\u2019s EV sales cross 2 million in 2025, driven largely by two-wheelers.</i> https://humansofev.info",
    "Observer Research Foundation. (2025). <i>Charging infrastructure: The missing link in India\u2019s EVs transition.</i> https://www.orfonline.org",
    "MMCM. (2026, May). <i>EV charging infrastructure in India: Status, types &amp; 2030 targets.</i> https://mmcm.in",
    "Ministry of Power, Government of India. (2025). <i>Public charging station data, August 2025</i> [29,277 stations; cited in ORF, 2025].",
    "Ministry of Power, Government of India. (2026). <i>Parliament data, March 2026</i> [27,737 installed / 22,753 operational; cited in MMCM, 2026].",
    "The Economic Times. (2025, July 17). <i>India\u2019s EV charging infra grew 5 times in last 3 years, but still only 1 public station for every 235 EVs</i> [cited in ORF, 2025].",
    "Avaada. (2026, April). <i>How to set up EV charging infrastructure in India.</i> https://www.avaada.com",
    "Bolt.Earth. (2025, November). <i>India\u2019s EV charging infrastructure policy 2025: Impact on CPOs and OEMs.</i> https://bolt.earth",
    "International Council on Clean Transportation. (2025, January). <i>India synchronizes EV sales and charging infrastructure growth in 2024.</i> https://theicct.org",
    "India Energy Storage Alliance. (2025). <i>Annual report: India EV market 2025</i> [Vahan data; cited in India Last Week, Substack, 2025].",
    "Cornell SC Johnson College of Business. (2025, July). <i>India\u2019s emerging electric vehicle market.</i> https://business.cornell.edu",
    "India Data Map. (2025, November). <i>EV charging stations in India: State-wise breakdown 2025.</i> https://indiadatamap.com",
    "India Brand Equity Foundation. (2026, May). <i>EV charging infrastructure: The key to mass EV adoption in India.</i> https://www.ibef.org",
    "Marqstats. (2026, April). <i>India EV charging station market size, share and forecast 2026\u20132030.</i>",
    "Mordor Intelligence. (2025). <i>India EV charging infrastructure market analysis</i> [urban lease and budget-share data, as compiled in project research].",
    "Pulse Energy. (2025). <i>Public AC charging tariffs in India</i> [Rs.6\u201315/kWh range, as compiled in project research].",
    "Pulse Energy. (2026). <i>Charging hardware and installation cost benchmarks</i> [as compiled in project research].",
    "GlobalsBlog. (2026, June). <i>EV charging station cost in India 2026 \u2014 breakdown.</i> https://globalsblog.com",
    "EVtech.news. (2025). <i>AC charger cost benchmarks</i> [as compiled in project research].",
    "Anari Energy. (2025). <i>State EV policies and preferred hosting sites</i> [as compiled in project research].",
    "Expert Market Research. (2026). <i>India EV charging market size, share and forecast trends.</i>",
    "EVSelect.in. (2026, July). <i>Top EV charging companies in India (2026): The complete list.</i> https://www.evselect.in",
    "Electric Vehicle Insights. (2026, August). <i>EV charging network in India.</i> https://electricvehicleinsights.in",
    "Autonexa. (2026, April). <i>E-bike charging station in India 2026 complete guide.</i> https://autonexa.com",
    "EVBlogs. (2025, November). <i>Tata Power EZ Charge vs competitors in India EV charging 2025.</i> https://www.evblogs.in",
    "Clean Mobility Shift. (n.d.). <i>EV Vahan dashboard.</i> https://cleanmobilityshift.com",
]
for r in refs:
    story.append(P(r, REF))
story.append(NextPageTemplate("Appx"))
story.append(PageBreak())

# ============================================================ APPENDIX
story.append(P("APPENDIX", CHAP_LABEL))
story.append(P("Appendix", H1))

story.append(P("A \u2014 Customer Interview Questions", H2))
cust_q = [
    "Where do you currently charge your EV most often, and why that location?",
    "Do you have access to reliable home or workplace charging? If not, what blocks it?",
    "Which destinations (mall, office, hotel, hospital, other) do you visit weekly, and how long do you typically stay?",
    "Have you ever wanted to charge at a destination but could not? What happened?",
    "What would you pay per kWh for charging during shopping or dining, versus your home tariff?",
    "How do you find chargers today, and what frustrates you most about the experience?",
    "Have you encountered non-working public chargers? How did it affect your trust?",
    "Would guaranteed bay availability (enforced EV-only bays) change your charging habits?",
    "What payment method would you prefer \u2014 existing UPI apps, RFID, or a dedicated app?",
    "What would stop you from using destination charging even if it were available nearby?",
]
for i, q in enumerate(cust_q, 1):
    story.append(P("<b>%d.</b>  %s" % (i, q), BULLET))

story.append(P("B \u2014 Host Interview Questions", H2))
host_q = [
    "How many parking bays do you operate, and what is typical occupancy by day and hour?",
    "Have EV drivers ever asked for charging at your location? How often?",
    "Would you allocate 2\u20134 bays to EV charging under a 12-month agreement? What concerns you?",
    "What revenue share or monthly fee would make allocated bays worthwhile versus general parking?",
    "Would a guaranteed base fee change your willingness? At what level?",
    "Is 3-phase supply available near the parking area? Has load capacity ever constrained you?",
    "Who would enforce EV-only bay usage, and what enforcement tools exist today?",
    "Would you share anonymised footfall or transaction data for a charging-impact study?",
    "What would make you terminate a charging partnership at renewal?",
    "Which operator attributes matter most \u2014 brand, revenue, reliability, or marketing support?",
]
for i, q in enumerate(host_q, 1):
    story.append(P("<b>%d.</b>  %s" % (i, q), BULLET))

story.append(P("C \u2014 Unit-Economics Assumptions Log", H2))
story.append(P("Every modelling input in Chapter 5, with source and validation route:"))
ass = [[P("<b>#</b>", CELL_H), P("<b>INPUT</b>", CELL_H), P("<b>VALUE USED</b>", CELL_H), P("<b>SOURCE / STATUS</b>", CELL_H), P("<b>VALIDATED BY</b>", CELL_H)],
       [P("C1", CELL_C), P("Charger capacity", CELL), P("7.4 kW AC", CELL), P(badge("ASSUMPTION"), CELL), P("Procurement spec", CELL)],
       [P("C2", CELL_C), P("Energy per session", CELL), P("12 kWh (2 hrs)", CELL), P(badge("ASSUMPTION"), CELL), P("Pilot meter data", CELL)],
       [P("C3", CELL_C), P("Consumer price (ref / VPS)", CELL), P("Rs.12 / Rs.15 per kWh", CELL), P("Range {}; VPS {}" .format(badge("FACT"), badge("ASSUMPTION")), CELL), P("Driver interviews", CELL)],
       [P("C4", CELL_C), P("Electricity tariff (ref / VPS)", CELL), P("Rs.9 / Rs.8 per kWh", CELL), P("Range {}; VPS {}" .format(badge("FACT"), badge("ASSUMPTION")), CELL), P("Site survey", CELL)],
       [P("C5", CELL_C), P("Host share (ref / VPS)", CELL), P("20% / 15% of gross", CELL), P(badge("ASSUMPTION"), CELL), P("Host negotiation", CELL)],
       [P("C6", CELL_C), P("Fixed OpEx (ref / VPS)", CELL), P("Rs.80,000 / Rs.70,000 per year", CELL), P("Envelope {}" .format(badge("FACT")), CELL), P("Vendor quotes", CELL)],
       [P("C7", CELL_C), P("CAPEX per bay (mid)", CELL), P("Rs.3,00,000", CELL), P(badge("ESTIMATE"), CELL), P("Installation quotes", CELL)],
       [P("C8", CELL_C), P("Home-charging gap", CELL), P("40\u201355% of e-PV owners", CELL), P(badge("ASSUMPTION"), CELL), P("Driver interviews", CELL)],
       [P("C9", CELL_C), P("Dwell times by category", CELL), P("Table 4.1 values", CELL), P(badge("ESTIMATE"), CELL), P("Host footfall data", CELL)],
       [P("C10", CELL_C), P("Uptime target", CELL), P("\u226590%", CELL), P(badge("HYPOTHESIS"), CELL), P("Pilot logs", CELL)]]
story.append(styled_table(ass, [12 * mm, 40 * mm, 44 * mm, 40 * mm, W - 136 * mm], font_size=8.0))

story.append(P("D \u2014 Pilot Metrics &amp; Decision Thresholds", H2))
story.append(P("Measured monthly per site; Go / No-Go evaluated at month 6 against thresholds "
               "registered before launch:"))
met = [[P("<b>METRIC</b>", CELL_H), P("<b>DEFINITION</b>", CELL_H), P("<b>GO THRESHOLD</b>", CELL_H), P("<b>NO-GO</b>", CELL_H)],
       [P("Sessions / bay / day", CELL), P("Completed sessions \u00f7 bays \u00f7 days", CELL), P("\u22653.5 on \u22653 of 5 sites", CELL), P("&lt;2.5 on majority", CELL)],
       [P("kWh per session", CELL), P("Metered energy \u00f7 sessions", CELL), P("\u226510 kWh mean", CELL), P("&lt;7 kWh mean", CELL)],
       [P("Charger uptime", CELL), P("Available hours \u00f7 total hours", CELL), P("\u226590%", CELL), P("&lt;80%", CELL)],
       [P("Host renewal intent", CELL), P("Hosts renewing at month 6", CELL), P("100% renew", CELL), P("Any churn", CELL)],
       [P("Customer acquisition cost", CELL), P("Marketing \u00f7 active users", CELL), P("&lt;Rs.500", CELL), P(">Rs.1,500", CELL)],
       [P("Gross revenue per site", CELL), P("Monthly kWh \u00d7 realised price", CELL), P("Covers site opex + share", CELL), P("&lt;70% of opex", CELL)],
       [P("Net promoter (drivers)", CELL), P("Recommend-to-other-drivers score", CELL), P("\u2265 +30", CELL), P("Negative", CELL)],
       [P("ICE-blocking rate", CELL), P("Blocked bay-hours \u00f7 total", CELL), P("&lt;5%", CELL), P(">15%", CELL)]]
story.append(styled_table(met, [36 * mm, 52 * mm, 42 * mm, W - 130 * mm], font_size=8.2))
story.append(P("Pivot triggers: if utilisation clears thresholds only at offices/hotels, narrow the "
               "model to long-dwell categories; if tariff discipline fails, test fixed-fee host "
               "contracts; if price resistance appears at Rs.15, re-derive the frontier before "
               "continuing. Any threshold change after data collection invalidates the decision.", BODY_S))

# ============================================================ BUILD
doc = build_doc("Destination-EV-Charging-Report.pdf")
doc.multiBuild(story)
print("BUILD OK")
