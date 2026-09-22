"""Vector charts (ReportLab Drawings) for the report."""
from reportlab.graphics.shapes import Drawing, String, Rect, Line, Polygon
from reportlab.lib.colors import HexColor
from rstyle import W, SAGE, SAGE_LT, GRAPHITE, LINES, CARD, TEXT, SECOND, RISK, WHITE

def _lbl(d, x, y, text, size=7.5, color=SECOND, anchor="start", bold=False):
    d.add(String(x, y, text, fontName="DV-B" if bold else "DV",
                 fontSize=size, fillColor=color, textAnchor=anchor))

# ------------------------------------------------------- generic h-bar chart
def hbar_chart(rows, value_labels=None, colors=None, maxv=None,
               label_w=118, track_w=240, height_per=16, title=None):
    """rows: [(label, value)]. Returns Drawing."""
    n = len(rows)
    top = 18 if title else 6
    h = top + n * height_per + 10
    d = Drawing(W, h)
    if title:
        _lbl(d, 0, h - 12, title, size=8.5, color=TEXT, bold=True)
    mv = maxv or max(v for _, v in rows)
    y = h - top - 12
    for i, (lab, val) in enumerate(rows):
        c = (colors[i % len(colors)] if colors else SAGE)
        _lbl(d, label_w - 4, y + 1, lab, anchor="end")
        d.add(Rect(label_w, y - 2, track_w, 10, strokeColor=LINES,
                   strokeWidth=0.4, fillColor=CARD))
        bw = track_w * (val / mv) if mv else 0
        if bw > 0.5:
            d.add(Rect(label_w, y - 2, bw, 10, strokeColor=c, strokeWidth=0, fillColor=c))
        vl = value_labels[i] if value_labels else ("%.1f" % val)
        _lbl(d, label_w + track_w + 6, y + 1, vl, color=TEXT, bold=True)
        y -= height_per
    return d

def ev_composition():
    return hbar_chart(
        [("Two-wheelers", 56), ("Three-wheelers", 35),
         ("Passenger cars", 7.8), ("Others", 1.2)],
        value_labels=["56%", "35%", "7.8%", "~1%"],
        colors=[SAGE, GRAPHITE, SAGE_LT, LINES],
        title="Figure 2.1 \u2014 India EV Sales Composition by Vehicle Type, CY2025")

def evidence_maturity():
    return hbar_chart(
        [("EV market growth", 95), ("Infrastructure gap", 90),
         ("Land-cost problem", 85), ("Unit economics (modelled)", 55),
         ("Driver demand", 20), ("Host willingness", 15),
         ("Site utilisation rate", 10), ("Incremental host spend", 5)],
        value_labels=["Strong evidence", "Strong evidence", "Strong evidence",
                      "Directional \u2014 modelled", "Hypothesis \u2014 unvalidated",
                      "Hypothesis \u2014 unvalidated", "Unvalidated \u2014 critical",
                      "Unvalidated \u2014 speculative"],
        colors=[SAGE, SAGE, SAGE, GRAPHITE, HexColor("#B08D57"),
                HexColor("#B08D57"), RISK, RISK],
        title="Figure 8.1 \u2014 Evidence Maturity by Business Model Element",
        label_w=150, track_w=150, height_per=17.5)

# ------------------------------------------------------- vertical bar: PCS growth
def pcs_growth():
    d = Drawing(W, 168)
    _lbl(d, 0, 156, "Figure 2.2 \u2014 Public Charging Stations in India, Dec 2022 \u2013 Aug 2025",
         size=8.5, color=TEXT, bold=True)
    data = [("Dec 2022", 5151), ("Dec 2024", 25202), ("Aug 2025", 29277)]
    base, top, left, slot = 34, 140, 90, 110
    mv = 32000
    for i, (lab, v) in enumerate(data):
        x = left + i * slot
        bh = (top - base) * v / mv
        d.add(Rect(x, base, 64, bh, strokeColor=SAGE, strokeWidth=0, fillColor=SAGE if i == 2 else SAGE_LT if i == 0 else GRAPHITE))
        _lbl(d, x + 32, base + bh + 5, "%s" % f"{v:,}", color=TEXT, bold=True, anchor="middle")
        _lbl(d, x + 32, 18, lab, anchor="middle")
    d.add(Line(left - 20, base, left + 3 * slot, base, strokeColor=LINES, strokeWidth=0.6))
    _lbl(d, left + 3 * slot - 130, top + 2,
         "2030 requirement: ~1.32M stations (ORF) \u2014 45\u00d7 current base",
         size=7.5, color=RISK, bold=True)
    return d

# ------------------------------------------------------- framework flow (5 boxes)
def framework_flow():
    titles = ["EV DEMAND", "DESTINATION", "SESSION", "HOST VALUE", "OPERATOR ECONOMICS"]
    subs = [["Fleet growth", "Urban density", "Range anxiety"],
            ["Dwell time", "Parking", "Electricity"],
            ["kWh delivered", "Duration", "Frequency"],
            ["Revenue share", "Footfall", "Differentiation"],
            ["Margin", "Payback", "Scale"]]
    bw, bh, gap, n = 82, 62, 12.75, 5
    d = Drawing(W, bh + 26)
    _lbl(d, 0, bh + 14, "Figure 2.3 \u2014 Destination Charging Analytical Framework",
         size=8.5, color=TEXT, bold=True)
    x = 0
    for i in range(n):
        d.add(Rect(x, 0, bw, bh, strokeColor=LINES, strokeWidth=0.5, fillColor=WHITE))
        _lbl(d, x + bw / 2, bh - 13, titles[i], size=6.5, color=SAGE, bold=True, anchor="middle")
        yy = bh - 26
        for s in subs[i]:
            _lbl(d, x + bw / 2, yy, s, size=7, anchor="middle")
            yy -= 11
        if i < n - 1:
            ax = x + bw + 2
            d.add(String(ax, bh / 2 - 4, "\u2192", fontName="DV-B", fontSize=11, fillColor=SAGE))
        x += bw + gap
    return d

# ------------------------------------------------------- stakeholders
def stakeholder():
    d = Drawing(W, 118)
    _lbl(d, 0, 106, "Figure 3.1 \u2014 Three-Party Commercial Structure",
         size=8.5, color=TEXT, bold=True)
    cards = [("EV DRIVER", ["Pays per session /", "kWh consumed"], 118),
             ("CHARGING OPERATOR", ["Owns hardware \u00b7 Collects", "revenue \u00b7 Manages network"], 150),
             ("HOST BUSINESS", ["Provides parking +", "electricity \u00b7 Gets share"], 118)]
    widths = [118, 150, 118]
    total = sum(widths) + 2 * 34
    x = (W - total) / 2
    for i, (t, lines, cw) in enumerate(cards):
        box_c = SAGE if i == 1 else LINES
        lw = 1.6 if i == 1 else 0.5
        d.add(Rect(x, 0, cw, 88, strokeColor=box_c, strokeWidth=lw, fillColor=WHITE))
        _lbl(d, x + cw / 2, 72, t, size=7, color=SAGE, bold=True, anchor="middle")
        yy = 54
        for s in lines:
            _lbl(d, x + cw / 2, yy, s, size=7.5, anchor="middle")
            yy -= 12
        x += cw
        if i < 2:
            d.add(String(x + 8, 40, "\u21c4", fontName="DV-B", fontSize=13, fillColor=SAGE))
            x += 34
    return d

# ------------------------------------------------------- customer journey
def journey():
    steps = ["Arrive at\ndestination", "Park &\nlocate bay", "Plug in via\napp / card",
             "Charge during\ndestination use", "Unplug &\ndepart"]
    bw, bh, gap = 80, 46, 13.75
    d = Drawing(W, bh + 26)
    _lbl(d, 0, bh + 14, "Figure 3.2 \u2014 Destination Charging Customer Journey",
         size=8.5, color=TEXT, bold=True)
    x = 0
    for i, s in enumerate(steps):
        d.add(Rect(x, 0, bw, bh, strokeColor=LINES, strokeWidth=0.5, fillColor=CARD))
        l1, l2 = s.split("\n")
        _lbl(d, x + bw / 2, 26, l1, size=7.5, color=TEXT, bold=True, anchor="middle")
        _lbl(d, x + bw / 2, 14, l2, size=7.5, color=TEXT, anchor="middle")
        if i < len(steps) - 1:
            d.add(String(x + bw + 2, bh / 2 - 4, "\u2192", fontName="DV-B", fontSize=10, fillColor=SAGE))
        x += bw + gap
    return d

# ------------------------------------------------------- funnel
def funnel():
    rows = [("~2.27M", 300, "Total EV sales in India, CY2025 \u2014 all vehicle types"),
            ("~176K", 255, "Passenger electric 4-wheelers sold, CY2025"),
            ("~600K", 210, "Cumulative e-PV fleet, 2015\u20132025 (estimate)"),
            ("~240\u2013330K", 150, "Urban owners without reliable home charging (ASSUMPTION)"),
            ("~100\u2013150K", 100, "Behaviourally aligned to destination charging (HYPOTHESIS)")]
    filters = ["Passenger four-wheelers only (~7.8% of total)",
               "Cumulative addressable fleet (past years\u2019 sales)",
               "ASSUMPTION: ~40\u201355% lack reliable home charging",
               "Urban Tier-1, within range of destination sites"]
    rh, fh = 20, 15
    h = 24 + len(rows) * rh + len(filters) * fh + 6
    d = Drawing(W, h)
    _lbl(d, 0, h - 12, "Figure 4.1 \u2014 Addressable Market Funnel (directional, not a forecast)",
         size=8.5, color=TEXT, bold=True)
    y = h - 24 - rh
    for i, (num, bw, lab) in enumerate(rows):
        c = SAGE if i < 3 else (GRAPHITE if i == 3 else HexColor("#A79C8C"))
        d.add(Rect(0, y, bw, rh - 3, strokeColor=c, strokeWidth=0, fillColor=c))
        d.add(String(8, y + 5, num, fontName="DV-B", fontSize=8, fillColor=WHITE))
        _lbl(d, bw + 8, y + 5, lab, size=7.8)
        y -= rh
        if i < len(filters):
            _lbl(d, 10, y + 3, "\u25bc  " + filters[i], size=7, color=SECOND)
            y -= fh
    return d

# ------------------------------------------------------- waterfall (VPS base case)
def waterfall():
    d = Drawing(W, 190)
    _lbl(d, 0, 178, "Figure 5.1 \u2014 Annual Contribution Waterfall per Bay, Viable-Parameter Base Case (6 sessions/day)",
         size=8.5, color=TEXT, bold=True)
    items = [("Revenue\nRs.3,94,200", 394200, SAGE), ("Electricity\nRs.2,10,240", -210240, RISK),
             ("Host share\nRs.59,130", -59130, GRAPHITE), ("Fixed OpEx\nRs.70,000", -70000, GRAPHITE),
             ("Net\n+Rs.54,830", None, SAGE)]
    base, top, left, slot, bw = 40, 162, 30, 86, 56
    mv = 400000
    run = 0
    prev_top = None
    for i, (lab, v, c) in enumerate(items):
        x = left + i * slot
        if v is None:
            y0 = base
            y1 = base + (top - base) * run / mv
            fill = SAGE
        else:
            y0 = base + (top - base) * run / mv
            y1 = base + (top - base) * (run + v) / mv
            lo, hi = (y1, y0) if v < 0 else (y0, y1)
            d.add(Rect(x, lo, bw, max(hi - lo, 2), strokeColor=c, strokeWidth=0, fillColor=c))
            run += v
            prev_top = y1
            if i > 0:
                d.add(Line(x - (slot - bw), base + (top - base) * (run - v) / mv, x,
                           base + (top - base) * (run - v) / mv, strokeColor=LINES,
                           strokeWidth=0.5))
            l1, l2 = lab.split("\n")
            _lbl(d, x + bw / 2, 24, l1, size=7, anchor="middle")
            _lbl(d, x + bw / 2, 13, l2, size=7, color=TEXT, bold=True, anchor="middle")
            continue
        d.add(Rect(x, y0, bw, max(y1 - y0, 2), strokeColor=SAGE, strokeWidth=0, fillColor=SAGE))
        l1, l2 = lab.split("\n")
        _lbl(d, x + bw / 2, 24, l1, size=7, anchor="middle")
        _lbl(d, x + bw / 2, 13, l2, size=7, color=SAGE, bold=True, anchor="middle")
    d.add(Line(left - 14, base, left + 5 * slot, base, strokeColor=LINES, strokeWidth=0.6))
    return d

# ------------------------------------------------------- breakeven frontier
def breakeven():
    rows = [("A \u00b7 Reference (Rs.12 / Rs.9 / 20%)", 30.4),
            ("B \u00b7 Rs.15 / Rs.9 / 20%", 4.4),
            ("C \u00b7 VPS: Rs.15 / Rs.8 / 15%", 3.4),
            ("D \u00b7 Rs.18 / Rs.8 / 15%", 2.2)]
    d = Drawing(W, 148)
    _lbl(d, 0, 136, "Figure 5.2 \u2014 Breakeven Threshold (sessions/bay/day) Under Alternative Price / Tariff / Share Combinations",
         size=8.5, color=TEXT, bold=True)
    label_w, track_w, mv = 190, 220, 32
    y = 108
    cols = [RISK, GRAPHITE, SAGE, SAGE]
    for i, (lab, v) in enumerate(rows):
        _lbl(d, label_w - 4, y + 1, lab, anchor="end", size=7.5,
             bold=(i == 2), color=TEXT if i == 2 else SECOND)
        d.add(Rect(label_w, y - 2, track_w, 10, strokeColor=LINES, strokeWidth=0.4, fillColor=CARD))
        d.add(Rect(label_w, y - 2, track_w * v / mv, 10, strokeColor=cols[i], strokeWidth=0, fillColor=cols[i]))
        _lbl(d, label_w + track_w + 6, y + 1, "%.1f/day" % v, color=TEXT, bold=True, size=7.5)
        y -= 22
    lx = label_w + track_w * 8 / mv
    d.add(Line(lx, 30, lx, 116, strokeColor=RISK, strokeWidth=0.7))
    for yy in range(30, 116, 6):
        d.add(Line(lx, yy, lx, yy + 3, strokeColor=WHITE, strokeWidth=0.8))
    _lbl(d, lx + 4, 118, "plausible max ~8/day", size=7, color=RISK)
    return d

# ------------------------------------------------------- positioning map
def positioning():
    mw, mh, ox, oy = 430, 150, 20, 26
    d = Drawing(W, mh + 52)
    _lbl(d, 0, mh + 40, "Figure 6.1 \u2014 Destination-Charging Operator Positioning Map (indicative, qualitative)",
         size=8.5, color=TEXT, bold=True)
    d.add(Rect(ox, oy, mw, mh, strokeColor=LINES, strokeWidth=0.5, fillColor=WHITE))
    d.add(Line(ox, oy + mh / 2, ox + mw, oy + mh / 2, strokeColor=LINES, strokeWidth=0.5))
    d.add(Line(ox + mw / 2, oy, ox + mw / 2, oy + mh, strokeColor=LINES, strokeWidth=0.5))
    _lbl(d, ox + 6, oy + 6, "Dedicated site model", size=7)
    _lbl(d, ox + mw - 6, oy + 6, "Partnership / host model", size=7, anchor="end")
    _lbl(d, ox + 6, oy + mh - 12, "Highway focus", size=7)
    _lbl(d, ox + 6, oy + 18, "Destination focus", size=7)
    pts = [("ChargeZone", 0.22, 0.74, GRAPHITE, False),
           ("Jio-bp", 0.34, 0.60, GRAPHITE, False),
           ("Tata Power", 0.72, 0.72, GRAPHITE, False),
           ("Statiq", 0.78, 0.46, GRAPHITE, False),
           ("Bolt.Earth", 0.82, 0.22, GRAPHITE, False),
           ("\u25cf Dest. Operator (this study)", 0.58, 0.32, SAGE, True)]
    for t, fx, fy, c, b in pts:
        d.add(String(ox + mw * fx, oy + mh * fy, t, fontName="DV-B" if b else "DV",
                     fontSize=8 if b else 7.5, fillColor=c))
    return d
