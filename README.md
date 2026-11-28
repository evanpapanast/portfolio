# Evangelos Papanastasis – Portfolio

**Live site: [evanpapanast.github.io/portfolio](https://evanpapanast.github.io/portfolio/)**

Portfolio and CV page of Evangelos (Evan) Papanastasis, Senior BI and FP&A analyst in Vienna, Austria. 10+ years in finance reporting and analytics at IBM, Emarsys, WWF and MSD (Merck & Co.).

Open to remote roles across the EU and hybrid roles in Vienna.

## CVs

| CV | Best for | Download |
| --- | --- | --- |
| Finance & Commercial Insights | FP&A, business controlling, finance business partnering, commercial analytics | [PDF](cv-finance-commercial-insights.pdf) |
| Data & AI Transformation | BI lead, analytics, data governance, digital transformation | [PDF](cv-data-ai-transformation.pdf) |

## Selected work

- **Oncology 360 dashboard (MSD):** combined SAP, IQVIA and CRM data in Power BI, saving analysts at least two weeks of manual reporting.
- **Global content-tagging hub (MSD):** one source of truth for all MSD entities, launched in 4 months.
- **Budget vs actual for every HQ business unit (WWF):** daily-refreshed Tableau reporting on Oracle actuals and budget data, saving at least 3 days of work.
- **Sales reporting automation (MSD):** replaced a manual Excel file with a daily Power BI report, then rolled the platform out to 50+ users with training and ongoing support.

## Experiments

Side projects that show how I pick up new tools and use them end to end: Claude as an AI pair connected to Google BigQuery and GitHub, a data model and forecasts in BigQuery, automatic quality checks, and every change through a Git branch and pull request ([all experiments](https://evanpapanast.github.io/experiments/)). I define the question and select the data, ensure data governance and compliance (licensing, privacy and reuse terms), validate the results and approve each change; Claude writes the code and prepares the pull requests.

- **[Customer 360](https://evanpapanast.github.io/experiments/customer-360/dashboard/):** which customer groups and channels drive profitable revenue; modelled in dbt on BigQuery with 43 tests, GDPR-minimised data and only groups of 50+ customers shown.
- **[Iowa spirits market](https://evanpapanast.github.io/experiments/liquor-market/dashboard/):** price vs volume, budget vs actual, BigQuery forecast and a 2027 budget builder.
- **[What the ECB says, and what it does](https://evanpapanast.github.io/experiments/ecb-speeches/dashboard/):** do ECB speeches predict interest rate decisions?
- **[AI adoption in EU enterprises](https://evanpapanast.github.io/experiments/ai-adoption-eu/dashboard/):** who uses AI in Europe, for what, and what holds the rest back.

## Contact

- Email: [evanpapanast@gmail.com](mailto:evanpapanast@gmail.com)
- LinkedIn: [evangelos-papanastasis](https://www.linkedin.com/in/evangelos-papanastasis-b7036920/)

## Repository contents

- `index.html` – the whole site in one file (no build step; fonts load from Google Fonts)
- `cv-finance-commercial-insights.pdf`, `cv-data-ai-transformation.pdf` – the two CVs
- `.nojekyll` – tells GitHub Pages to serve the files as they are

- `cv-source/build.py` – the source of both CVs: their text and design, and the script that turns them into the two PDFs
- `cv-source/fonts/` – Inter converted to TrueType, so the PDFs keep every character (+, brackets, dashes) when applicant tracking systems read them

To update a CV, edit its text in `cv-source/build.py` and run `python3 cv-source/build.py` (needs Google Chrome). It writes both PDFs to the repository root with the same file names, and the site picks them up automatically. The layout is one column in reading order (header, profile, skills, projects, each job with its own bullets, education, certifications, languages), so applicant tracking systems read it top to bottom.
