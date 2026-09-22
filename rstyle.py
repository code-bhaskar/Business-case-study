"""Shared styles, palette, page templates and helpers for the thesis-style report."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer, NextPageTemplate)

# ---------------------------------------------------------------- palette
BG       = HexColor("#F3F1EC")
TEXT     = HexColor("#202321")
SECOND   = HexColor("#68706D")
SAGE     = HexColor("#687C70")
SAGE_LT  = HexColor("#B5C4BB")
GRAPHITE = HexColor("#8A8072")
LINES    = HexColor("#D8D4C9")
CARD     = HexColor("#EAE7DF")
WHITE    = HexColor("#FBFAF7")
RISK     = HexColor("#A6564B")
AMBER    = HexColor("#8A6E3C")

PAGE_W, PAGE_H = A4
ML = MR = 22 * mm
MT = 20 * mm
MB = 22 * mm
W = PAGE_W - ML - MR          # usable content width (~470pt)

# ---------------------------------------------------------------- fonts
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-O", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-BO", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-O", boldItalic="DV-BO")

# ---------------------------------------------------------------- styles
def _ps(name, **kw):
    base = dict(fontName="DV", fontSize=9.2, leading=13.2, textColor=TEXT,
                alignment=TA_JUSTIFY, spaceAfter=5)
    base.update(kw)
    return ParagraphStyle(name, **base)

TITLE      = _ps("TitleX", fontName="DV-B", fontSize=30, leading=33, alignment=TA_LEFT,
                 textColor=TEXT, spaceAfter=6)
SUBTITLE   = _ps("SubtitleX", fontSize=11, leading=15, textColor=SECOND, alignment=TA_LEFT)
CHAP_LABEL = _ps("ChapLabel", fontName="DV-B", fontSize=7.5, leading=10, textColor=SECOND,
                 alignment=TA_LEFT, spaceAfter=2)
H1    = _ps("H1", fontName="DV-B", fontSize=19, leading=22, alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=6, keepWithNext=True)
H2    = _ps("H2", fontName="DV-B", fontSize=12, leading=15, alignment=TA_LEFT,
            spaceBefore=7, spaceAfter=4, keepWithNext=True)
H2NT  = _ps("H2NT", fontName="DV-B", fontSize=12, leading=15, alignment=TA_LEFT,
            spaceBefore=7, spaceAfter=4, keepWithNext=True)   # not in TOC
H1NT  = _ps("H1NT", fontName="DV-B", fontSize=19, leading=22, alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=6, keepWithNext=True)    # not in TOC
H3    = _ps("H3", fontName="DV-B", fontSize=10, leading=13.5, alignment=TA_LEFT,
            spaceBefore=5, spaceAfter=3, keepWithNext=True)
BODY  = _ps("Body")
BODY_S = _ps("BodyS", fontSize=8.8, leading=12.4)
BULLET = _ps("Bullet", leftIndent=12, firstLineIndent=0, bulletIndent=4,
             spaceAfter=2.5, alignment=TA_LEFT)
CAPTION = _ps("Caption", fontSize=7.8, leading=10, textColor=SECOND,
              alignment=TA_LEFT, spaceBefore=2, spaceAfter=5)
CELL   = _ps("Cell", fontSize=8.6, leading=11, alignment=TA_LEFT, spaceAfter=0)
CELL_H = _ps("CellH", fontName="DV-B", fontSize=8.2, leading=10.5, alignment=TA_LEFT,
             spaceAfter=0, textTransform="uppercase")
CELL_C = _ps("CellC", fontSize=8.6, leading=11, alignment=TA_CENTER, spaceAfter=0)
REF    = _ps("Ref", fontSize=8.6, leading=11, leftIndent=10, firstLineIndent=-10,
             spaceAfter=4, alignment=TA_LEFT)
FOOTNOTE = _ps("Footnote", fontSize=7.8, leading=10.5, textColor=SECOND, alignment=TA_LEFT)

# ---------------------------------------------------------------- helpers
BADGE_COLORS = {"FACT": SAGE, "ESTIMATE": GRAPHITE, "ASSUMPTION": AMBER, "HYPOTHESIS": RISK}

def badge(kind):
    c = BADGE_COLORS[kind].hexval()[2:]
    return '<font color="#%s"><b>[%s]</b></font>' % (c, kind)

def P(text, style=BODY, **kw):
    return Paragraph(text, style, **kw)

def inr(n):
    """Indian-format rupee string, e.g. 315360 -> Rs.3,15,360 (uses Rs. prefix)."""
    s = "%d" % abs(n)
    if len(s) > 3:
        tail, head = s[-3:], s[:-3]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    sign = "-" if n < 0 else ""
    return "Rs.%s%s" % (sign, s)

def styled_table(data, col_widths, header=True, font_size=8.6, zebra=True):
    """data: list of rows of Paragraph/str. Returns styled Table."""
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    st = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, LINES),
        ("LINEABOVE", (0, 0), (-1, 0), 0.7, LINES),
        ("LINEBELOW", (0, -1), (-1, -1), 0.7, LINES),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, LINES),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
    ]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), CARD),
               ("FONTNAME", (0, 0), (-1, 0), "DV-B")]
    if zebra and len(data) > 1:
        for i in range(1, len(data)):
            if i % 2 == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F7F5F0")))
    t.setStyle(TableStyle(st))
    return t

def finding_block(title, sub):
    inner = [[P('<b>%s</b><br/><font color="#68706D">%s</font>' % (title, sub),
                _ps("FindTmp", fontSize=9.6, leading=13.4, alignment=TA_LEFT, spaceAfter=0))]]
    t = Table(inner, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("LINEBEFORE", (0, 0), (-1, -1), 3, SAGE),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t

def warn_block(title, body):
    inner = [[P('<b><font color="#A6564B">%s</font></b><br/>%s' % (title, body),
                _ps("WarnTmp", fontSize=8.8, leading=12.4, alignment=TA_LEFT, spaceAfter=0))]]
    t = Table(inner, colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#F7ECEA")),
        ("BOX", (0, 0), (-1, -1), 0.6, RISK),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t

def stat_row(stats):
    """stats: list of (big, unit, label). Returns 3-col card table."""
    cells = []
    for big, unit, label in stats:
        cells.append(P(
            '<font size="26"><b>%s</b></font><font size="12" color="#687C70"><b>%s</b></font>'
            '<br/><font size="8" color="#68706D">%s</font>' % (big, unit, label), CELL_C))
    t = Table([cells], colWidths=[W / 3.0] * 3, spaceBefore=4, spaceAfter=6)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("BOX", (0, 0), (-1, -1), 0.4, LINES),
        ("LINEAFTER", (0, 0), (-2, 0), 0.4, LINES),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t

# ---------------------------------------------------------------- page drawing
def _draw_motif(c):
    """Subtle parking-bay geometry confined to the footer strip."""
    c.saveState()
    c.setStrokeColor(HexColor("#E2DED4"))
    c.setLineWidth(0.5)
    x0, y0 = PAGE_W - 14 * mm, 17 * mm
    for i in range(6):
        x = x0 - i * 8 * mm
        c.line(x, y0, x, y0 + 7 * mm)
    c.restoreState()

def cover_page(c, doc):
    c.saveState()
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(SAGE)
    c.rect(ML, PAGE_H - 46 * mm, 18 * mm, 2.2, stroke=0, fill=1)
    c.restoreState()

def make_body_page(header_right):
    def fn(c, doc):
        c.saveState()
        c.setFillColor(BG)
        c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        _draw_motif(c)
        # header
        c.setStrokeColor(LINES)
        c.setLineWidth(0.4)
        c.line(ML, PAGE_H - 17 * mm, PAGE_W - MR, PAGE_H - 17 * mm)
        c.setFont("DV-B", 6.5)
        c.setFillColor(SECOND)
        c.drawString(ML, PAGE_H - 12.5 * mm, "DESTINATION EV CHARGING")
        c.setFont("DV", 6.5)
        c.drawString(ML, PAGE_H - 15.5 * mm, "Business Model & Feasibility Study")
        c.setFont("DV", 6.5)
        c.setFillColor(GRAPHITE)
        c.drawRightString(PAGE_W - MR, PAGE_H - 12.5 * mm, header_right)
        # footer
        c.line(ML, 15 * mm, PAGE_W - MR, 15 * mm)
        c.setFont("DV", 7)
        c.setFillColor(GRAPHITE)
        c.drawString(ML, 11.5 * mm, "Destination-Based EV Charging Infrastructure in India")
        c.setFont("DV-B", 8)
        c.setFillColor(SECOND)
        c.drawRightString(PAGE_W - MR, 11.5 * mm, str(c.getPageNumber()))
        c.restoreState()
    return fn

# ---------------------------------------------------------------- document
class ReportDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            if flowable.style.name == "H1":
                txt = re.sub(r"\s+", " ", flowable.getPlainText()).strip()
                self.notify("TOCEntry", (0, txt, self.page))

SECTIONS = [("FrontA", "ABSTRACT"), ("FrontC", "CONTENTS"),
            ("Ch1", "CHAPTER 01"), ("Ch2", "CHAPTER 02"),
            ("Ch3", "CHAPTER 03"), ("Ch4", "CHAPTER 04"),
            ("Ch5", "CHAPTER 05"), ("Ch6", "CHAPTER 06"),
            ("Ch7", "CHAPTER 07"), ("Ch8", "CHAPTER 08"),
            ("Refs", "REFERENCES"), ("Appx", "APPENDIX")]

def build_doc(filename):
    doc = ReportDoc(filename, pagesize=A4, leftMargin=ML, rightMargin=MR,
                    topMargin=MT, bottomMargin=MB,
                    title="Destination-Based EV Charging Infrastructure in India",
                    author="Business Model & Feasibility Study",
                    subject="Compact thesis-style business research report",
                    keywords="EV charging, India, destination charging, feasibility")
    templates = [PageTemplate(id="Cover",
                              frames=[Frame(ML, MB, W, PAGE_H - MT - MB, id="cover")],
                              onPage=cover_page)]
    for tid, hdr in SECTIONS:
        templates.append(PageTemplate(
            id=tid,
            frames=[Frame(ML, 24 * mm, W, PAGE_H - 24 * mm - 26 * mm, id="f_" + tid)],
            onPage=make_body_page(hdr)))
    doc.addPageTemplates(templates)
    return doc
