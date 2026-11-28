"""Build both CVs as ATS-friendly PDFs in the existing design.

- Fonts: Inter converted to TrueType outlines, so Chrome embeds standard
  CID TrueType fonts with a full Unicode map (no lost "+", "(", "–").
- One column, plain document order: header, profile, skills, projects,
  experience (each job followed by its own bullets), education,
  certifications, languages.
"""
import html, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CONTACT = {
    "loc": "Vienna, Austria",
    "phone": "+43 670 603 8378",
    "email": "evanpapanast@gmail.com",
    "linkedin": "linkedin.com/in/evangelos-papanastasis-b7036920",
}

EDU = [
    ("MBA (Business Administration), Digital Management", "German University of Digital Science", "Oct 2026 – exp. Sep 2027"),
    ("MSc Financial Economics", "Erasmus University Rotterdam", ""),
    ("BSc Accounting & Finance", "University of Macedonia", ""),
]
CERTS = "Google GenAI Leader · Cornell Digital Transformation · Power BI · IBM Data Science · Tableau Analyst"
LANGS = "Greek (native) · English (fluent) · German (A2, learning)"

EMARSYS = ("Group Financial Controller", "Emarsys, Vienna", "Sep 2016 – Feb 2017", [
    "Managed group <b>budgeting</b>, intercompany and daily cash-flow updates across the group entities.",
    "Owned the financial system updates feeding <b>Qlik Sense</b> analytics.",
])
IBM = ("Reporting & Consolidation Analyst", "IBM, Bratislava", "Dec 2014 – Sep 2016", [
    "Delivered business-unit performance and <b>revenue-driver reporting to VP level</b>.",
    "Managed <b>intercompany</b> transactions for 3 regions: APAC, EMEA and the Caribbean.",
])

CVS = {
 "finance": dict(
  file="cv-finance-commercial-insights",
  title="Finance &amp; Commercial Insights · Business Partnering · Finance Controls",
  portfolio="evanpapanast.github.io/portfolio/#finance",
  profile=("Finance and commercial insights professional with 10+ years at IBM, Emarsys, WWF and MSD, "
           "turning financial, sales and marketing data into decisions leaders act on. Partnered with "
           "internal clients in Commercial, Marketing and FP&amp;A at MSD, linking campaign activity to sales and financial results. "
           "Now also builds AI-assisted month-end close pipelines where every figure reconciles before anyone sees it."),
  skills=[
   ("Finance", ["<b>Financial reporting</b>", "<b>Budget vs actual</b>", "Budgeting", "Grants reporting", "Consolidation", "Intercompany", "Month-end close"]),
   ("Business Partnering", ["<b>KPIs &amp; KPI design</b>", "<b>Stakeholder alignment</b>", "Requirements gathering", "Training &amp; self-service"]),
   ("Commercial Analytics", ["Sales performance", "Campaign performance", "Price/volume analysis", "Multi-channel marketing", "CRM data", "IQVIA market data"]),
   ("Data &amp; Controls", ["<b>Power BI dashboards</b>", "Power Query", "Excel &amp; Microsoft Office", "SQL", "Tableau", "<b>Data governance</b>", "Reconciliation &amp; audit trails", "AWS Redshift", "SAP", "Oracle", "Veeva CRM"]),
   ("AI &amp; Automation", ["<b>Claude (agents, connectors)</b>", "Google BigQuery (AI.FORECAST)", "GitHub Actions", "Power Automate", "GenAI adoption"]),
  ],
  project_bullets=[
   "Built an AI-assisted <b>month-end close</b> on public data with Claude, BigQuery and GitHub: compares actuals with budget (volume, mix, price), re-forecasts and drafts commentary; <b>17 automated checks</b> stop the run if any figure fails to reconcile, and a person approves every change.",
   "Validated the controls: a check <b>caught a wrong figure</b> in draft commentary (41%, not \"about a third\") before it reached management.",
   "Delivered <b>budget vs actual</b>, price/volume and outlook reporting on <b>34M order lines</b>, plus a channel profitability model (revenue vs cost by channel).",
  ],
  jobs=[
   ("Senior Business Intelligence Analyst", "MSD, Vienna", "Oct 2022 – Jul 2026", [
    "Developed <b>KPIs</b>, data models and Power BI dashboards for <b>50+ users</b> in Commercial, Marketing and FP&amp;A.",
    "Measured <b>campaign performance</b> against sales and financial data to guide commercial priorities and spend.",
    "Delivered an <b>Oncology 360</b> view (SAP, IQVIA, CRM; <b>2+ weeks</b> saved); automated the daily sales report (<b>4+ days</b> saved).",
    "Owned the BI platform end-to-end: requirements, design, <b>data governance</b>, rollout and training.",
    "Led a <b>global content-tagging standard</b> with documentation for 50+ countries.",
   ]),
   ("Senior Business Reporting Specialist", "WWF, Vienna", "May 2017 – Sep 2022", [
    "Built daily <b>budget-vs-actual reporting</b> for all HQ business units, replacing a manual Excel process (<b>3+ days saved</b>).",
    "Coordinated financial reporting for 2 regions (<b>Africa and APAC</b>) and supported regional and global consolidation.",
    "Led business-side UAT for Oracle Grants and Noetix; automated booking corrections with IT (<b>1+ day</b> saved per closing).",
   ]),
   EMARSYS, IBM,
  ]),
 "data": dict(
  file="cv-data-ai-transformation",
  title="Finance Data &amp; AI Governance · BI · GenAI Adoption",
  portfolio="evanpapanast.github.io/portfolio/#data",
  profile=("Finance and data professional with 10+ years at IBM, Emarsys, WWF and MSD. Makes finance and commercial "
           "data reliable enough for people and AI to act on: sets the standards, builds the governed data models and "
           "Power BI dashboards, and designs the checks that catch errors before they reach decision-makers, now "
           "including AI-assisted pipelines where a person approves every change."),
  skills=[
   ("Data &amp; AI Governance", ["<b>Data governance</b>", "<b>Data quality</b>", "Review of AI outputs", "Reconciliation &amp; audit trails"]),
   ("Transformation", ["<b>Requirements gathering</b>", "Stakeholder alignment", "Training &amp; adoption", "Agency &amp; IT collaboration", "UAT &amp; system migrations"]),
   ("AI &amp; Automation", ["<b>Claude (agents, connectors)</b>", "GenAI &amp; Copilot adoption", "Google BigQuery (AI.FORECAST)", "GitHub Actions", "Power Automate"]),
   ("BI &amp; Systems", ["<b>Power BI dashboards</b>", "DAX", "Power Query", "<b>SQL</b>", "Data modelling", "KPIs", "Excel &amp; Microsoft Office", "AWS Redshift", "Tableau", "SAP", "Oracle", "Veeva CRM", "IQVIA"]),
   ("Finance", ["Financial reporting", "Budgeting", "Budget vs actual", "Grants reporting", "Consolidation", "Intercompany"]),
  ],
  project_bullets=[
   "Built an AI-assisted <b>month-end close</b> on public data with Claude, BigQuery and GitHub: compares actuals with budget, re-forecasts and drafts commentary; <b>17 automated checks</b> stop the run if any figure fails to reconcile, and a person approves every change.",
   "Validated the controls: a check <b>caught a wrong figure</b> in draft commentary (41%, not \"about a third\") before it reached the report.",
   "Delivered budget vs actual, price/volume and outlook reporting on <b>34M order lines</b>, plus a customer and channel profitability model.",
  ],
  jobs=[
   ("Senior Business Intelligence Analyst", "MSD, Vienna", "Oct 2022 – Jul 2026", [
    "Built MSD Austria's first <b>Power BI platform</b> for the Commercial, Marketing and FP&amp;A teams.",
    "Owned it end-to-end: requirements, design, <b>data governance</b>, rollout to <b>50+ users</b>, training and support.",
    "Led a <b>global content-tagging standard</b> for 50+ countries, interviewing 25+ stakeholders across teams.",
    "Designed a global-regional-country matrix, user guide and documentation website; launched with an agency in <b>4 months</b>.",
    "Delivered an <b>Oncology 360</b> view (SAP, IQVIA, CRM; <b>2+ weeks</b> saved); automated the daily sales report (<b>4+ days</b> saved).",
    "Designed a 4-week employee <b>GenAI upskilling plan</b> as GenAI Ambassador, and gathered and prioritised AI use cases.",
   ]),
   ("Senior Business Reporting Specialist", "WWF, Vienna", "May 2017 – Sep 2022", [
    "Built daily <b>budget-vs-actual reporting</b> in Tableau for all HQ business units, replacing a manual Excel process (<b>3+ days saved</b>).",
    "Coordinated financial reporting for 2 regions (<b>Africa and APAC</b>) and supported regional and global consolidation.",
    "Led business-side UAT for Oracle Grants and Noetix; automated booking corrections with IT (<b>1+ day</b> saved per closing).",
   ]),
   EMARSYS, IBM,
  ]),
}

CSS = """
@font-face{font-family:InterT;src:url(fonts/Inter-Regular.ttf);font-weight:400}
@font-face{font-family:InterT;src:url(fonts/Inter-Medium.ttf);font-weight:500}
@font-face{font-family:InterT;src:url(fonts/Inter-SemiBold.ttf);font-weight:600}
@font-face{font-family:InterT;src:url(fonts/Inter-Bold.ttf);font-weight:700}
@font-face{font-family:InterT;src:url(fonts/Inter-Italic.ttf);font-style:italic}
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:InterT,sans-serif;font-feature-settings:"calt" 0,"case" 0;font-variant-ligatures:none;color:#1f2933;font-size:8.9pt;line-height:1.35}
.page{position:relative;width:210mm;padding:7mm 10mm 5mm}
.header{padding:12px 110px 12px 20px;color:#fff;height:110px;padding-top:13px}
.hbg{position:absolute;z-index:-1;left:10mm;top:7mm;right:10mm;height:110px;background:#0f4c5c;background:linear-gradient(135deg,#0d4553 0%,#17606f 100%);border-radius:10px}

.photo{position:absolute;right:calc(10mm + 18px);top:calc(7mm + 16px);width:78px;height:78px;border-radius:50%;border:3px solid rgba(255,255,255,.85);object-fit:cover}
h1{font-size:22pt;font-weight:700;letter-spacing:1.5px;margin:0;line-height:1.15}
.tag{color:#8fdede;font-weight:600;font-size:9.6pt;margin:3px 0 4px}
.contact{font-size:8.4pt;line-height:1.55;margin:0}
.contact a{color:#fff;font-weight:600}
h2{display:flex;align-items:center;gap:8px;margin:8px 0 3px;color:#0f4c5c;font-weight:700;letter-spacing:1px;font-size:9.6pt}
h2::before{content:"";width:3px;height:11px;background:#1b9aaa}
h2::after{content:"";flex:1;height:1px;background:#d0d7de}
p{margin:0}
.skills p{margin:0 0 2px}
.skills .k{color:#0f4c5c;font-weight:700}
b{font-weight:600;color:#0f4c5c}
.job{margin:0 0 4px}
.jh{display:flex;justify-content:space-between;align-items:baseline;font-weight:700;font-size:9.2pt}
.jh .org{color:#17808f;font-weight:600}
.jh .dt{font-weight:400;font-size:8.6pt;color:#3e4c59;white-space:nowrap}
ul{margin:1px 0 0;padding-left:0;list-style:none}
li{margin:0 0 1px;padding-left:11px;text-indent:-11px}
.bl{color:#1b9aaa;display:inline-block;width:11px;text-indent:0}
.edu p{margin:0 0 1px}
"""

def esc_link(t):
    return html.escape(t)

def build(key):
    c = CVS[key]
    o = []
    o.append(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Evangelos Papanastasis – CV</title><style>{CSS}</style></head><body><div class="page">')
    o.append('<div class="header"><div class="hbg"></div><img class="photo" src="../photo.jpg" alt=""><div class="htxt">')
    o.append('<h1>EVANGELOS PAPANASTASIS</h1>')
    o.append(f'<p class="tag">{c["title"]}</p>')
    o.append(f'<p class="contact">{CONTACT["loc"]} | {CONTACT["phone"]} | <a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a><br>'
             f'<a href="https://{c["portfolio"]}">{c["portfolio"].split("/#")[0]}</a> | '
             f'<a href="https://www.{CONTACT["linkedin"]}">{CONTACT["linkedin"]}</a></p>')
    o.append('</div></div>')
    o.append('<h2>PROFILE</h2>')
    o.append(f'<p>{c["profile"]}</p>')
    o.append('<h2>SKILLS</h2><div class="skills">')
    for k, items in c["skills"]:
        o.append(f'<p><span class="k">{k}:</span> {" · ".join(items)}</p>')
    o.append('</div>')
    o.append('<h2>PROJECTS</h2>')
    o.append('<div class="job"><div class="jh"><span>Finance Data &amp; AI Projects (independent, alongside MBA) · '
             '<span class="org">evanpapanast.github.io/experiments</span></span><span class="dt">2026 – Present</span></div><ul>')
    o += [f'<li><span class="bl">•</span>{b}</li>' for b in c["project_bullets"]]
    o.append('</ul></div>')
    o.append('<h2>PROFESSIONAL EXPERIENCE</h2>')
    for t, org, dt, bl in c["jobs"]:
        o.append(f'<div class="job"><div class="jh"><span>{t} · <span class="org">{org}</span></span><span class="dt">{dt}</span></div><ul>')
        o += [f'<li><span class="bl">•</span>{b}</li>' for b in bl]
        o.append('</ul></div>')
    o.append('<h2>EDUCATION</h2><div class="edu">')
    for deg, school, dt in EDU:
        o.append(f'<p><b>{deg}</b> · {school}{" · " + dt if dt else ""}</p>')
    o.append('</div>')
    o.append('<h2>CERTIFICATIONS</h2>')
    o.append(f'<p>{CERTS}</p>')
    o.append('<h2>LANGUAGES</h2>')
    o.append(f'<p>{LANGS}</p>')
    o.append('</div></body></html>')
    # Render from cv-source/ (fonts/ and ../photo.jpg resolve there); PDF goes to the repo root.
    html_path = os.path.join(HERE, f'{c["file"]}.html')
    pdf_path = os.path.join(ROOT, f'{c["file"]}.pdf')
    with open(html_path, "w") as fh:
        fh.write("\n".join(o))
    try:
        subprocess.run(["google-chrome", "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf_path}", html_path], stderr=subprocess.DEVNULL, check=True)
    finally:
        os.remove(html_path)
    return pdf_path

if __name__ == "__main__":
    for k in (sys.argv[1:] or CVS):
        print(build(k))
