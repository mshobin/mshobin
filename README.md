<!--
  Profile README for github.com/mshobin
  Repository: mshobin/mshobin (public, README.md at the root)
  Rule for this file: every number and claim must be something Shobin can defend in an interview.
-->

<p align="center">
  <img src="assets/hero-banner.svg" alt="Shobin Mathews — Enterprise IT Operations Architect. BMC Helix AIOps, Observability, Event Correlation, Discovery & CMDB, Automation." width="100%">
</p>

<p align="center">
  <a href="mailto:mshobin@outlook.com"><img src="https://img.shields.io/badge/Email-mshobin%40outlook.com-0E2236?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Email"></a>
  <a href="https://www.linkedin.com/in/mshobin/"><img src="https://img.shields.io/badge/LinkedIn-mshobin-0E2236?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/Based_in-Kuwait-0E2236?style=for-the-badge&logo=googlemaps&logoColor=2DD4BF" alt="Based in Kuwait">
  <img src="https://img.shields.io/badge/Delivery-GCC_%2B_Asia-0E2236?style=for-the-badge&logo=globe&logoColor=2DD4BF" alt="Delivery across GCC and Asia">
</p>

---

### I make enterprise IT operations quieter, clearer and more predictable.

I'm a **Team Leader for BMC Helix ITOM & AIOps** at Diyar United Company in Kuwait, with **20+ years** of enterprise
IT delivery behind me — from field engineering and SCCM/SCOM on an oil & gas estate, through **14 years as a Senior
Solutions Architect**, to leading a team that designs and runs **BMC Helix Operations Management, event correlation,
Discovery, CMDB and AIOps** for organizations across the Middle East and Asia.

Outside client work I build software products end to end — architecture, code, security model, tests, installers and
documentation. That's where most of this GitHub lives.

<table>
<tr>
<td width="50%" valign="top">

#### 🎯 Recruiter quick view

| | |
|---|---|
| **Role** | Team Leader · Solutions Architect |
| **Focus** | BMC Helix ITOM · AIOps · Observability |
| **Experience** | 20+ years enterprise IT (since 2005) |
| **Delivery** | 35+ key projects · 6 countries |
| **Industries** | Oil & gas · Banking · Telecom · Healthcare · Government · Energy · Education |
| **Strengths** | Solution architecture · Presales & PoCs · Delivery leadership · C-level advisory |
| **Location** | Kuwait (GCC travel) |

</td>
<td width="50%" valign="top">

#### 🧩 Problems I solve

- **Alert storms** → policies that deduplicate, suppress and correlate events into actionable situations
- **"What is this server for?"** → Discovery and a reconciled CMDB that service models can trust
- **Monitoring silos** → integrations that bring tools into one operational view
- **Reactive operations** → predictive, service-centric AIOps
- **Manual toil** → Python / PowerShell / REST automation
- **Tech that doesn't land** → presales, workshops and PoCs that tie platforms to business outcomes

</td>
</tr>
</table>

---

## 📊 Impact at a glance

<table>
<tr>
<td align="center" width="16%"><h2>20+</h2><sub>years in<br>enterprise IT</sub></td>
<td align="center" width="16%"><h2>35+</h2><sub>key projects<br>delivered</sub></td>
<td align="center" width="16%"><h2>6</h2><sub>countries:<br>KW · QA · SA · AE · BH · MM</sub></td>
<td align="center" width="16%"><h2>7</h2><sub>industries<br>served</sub></td>
<td align="center" width="16%"><h2>14</h2><sub>years as Senior<br>Solutions Architect</sub></td>
<td align="center" width="16%"><h2>2</h2><sub>products built<br>end to end</sub></td>
</tr>
</table>

---

## 🏗️ Architecture portfolio

Reference architectures for the problems I work on. They are **generic patterns** — no client names, data or
configurations — drawn to show how I think about the design.

<details open>
<summary><b>1 · Event management & correlation pipeline (BMC Helix Operations Management)</b></summary>
<br>

```mermaid
flowchart LR
  subgraph SRC[Event sources]
    A1[Infrastructure<br>monitoring]
    A2[Application &<br>APM]
    A3[Logs & metrics]
    A4[Third-party tools<br>REST · webhooks]
  end
  subgraph ING[Ingest & enrich]
    B1[Connectors /<br>Event REST API]
    B2[Normalize<br>common event model]
    B3[Enrich from CMDB<br>CI · owner · service]
  end
  subgraph POL[Event policies]
    C1[Deduplicate]
    C2[Suppress &<br>blackout]
    C3[Correlate<br>topology + time]
  end
  subgraph OUT[Act]
    D1[Situation +<br>service impact]
    D2[Incident in<br>Helix ITSM]
    D3[Automated<br>remediation]
  end
  A1 & A2 & A3 & A4 --> B1 --> B2 --> B3 --> C1 --> C2 --> C3 --> D1
  D1 --> D2
  D1 --> D3
```

**Design decisions:** enrich *before* correlating (correlation is only as good as the CI and service context on
each event) · suppress maintenance windows at policy level, not at the source · one incident per situation, not
per event · automation only for runbooks with a known, safe rollback.

→ [Full pattern, ADRs and go-live checklist](https://github.com/mshobin/itom-reference-architectures/blob/main/patterns/event-management-and-correlation.md)

</details>

<details>
<summary><b>2 · Discovery → CMDB → service model</b></summary>
<br>

```mermaid
flowchart LR
  S[Scan scopes &<br>credential vault] --> DI[Discovery<br>scans & patterns]
  DI --> NR[Normalize &<br>reconcile]
  NR --> CM[(CMDB<br>golden record)]
  CM --> SM[Service models<br>business → technical]
  SM --> OP[Operations:<br>impact & correlation]
  SM --> CH[ITSM:<br>change & incident]
  CM -. data-quality KPIs .-> GV[Governance<br>owners · completeness · staleness]
  GV -. remediation .-> S
```

**Design decisions:** reconciliation rules decide which source wins per attribute · service models are built from
the business service down, not the infrastructure up · CMDB quality is measured and owned, or it decays.

→ [Full pattern and data-quality KPIs](https://github.com/mshobin/itom-reference-architectures/blob/main/patterns/discovery-cmdb-service-model.md)

</details>

<details>
<summary><b>3 · Product architecture — A.R.Q. (local-first, security-first desktop platform)</b></summary>
<br>

```mermaid
flowchart TB
  UI[React + TypeScript UI<br>in Tauri / WebView2] -->|IPC allowlist| CP{Authorization<br>chokepoint}
  CP --> IDX[Indexing<br>read-only walker]
  CP --> SR[Search<br>FTS + operators]
  CP --> ASK[Ask<br>local evidence-only RAG]
  CP --> FIN[Finance<br>integer-money ledger]
  CP --> BK[Backup & restore<br>signed, two-phase]
  IDX --> EX[Extraction worker<br>isolated, memory-capped]
  EX --> OCR[Optional OCR<br>Tesseract, isolated]
  IDX & SR & ASK & FIN & BK --> DB[(SQLCipher database<br>DPAPI-protected key)]
  CP --> AU[Tamper-evident<br>audit log]
```

</details>

---

## 🚀 Featured work

<table>
<tr>
<td width="50%" valign="top">

### 🗂️ A.R.Q. — Access. Retrieve. Quantify.
A private, **local-first document and household finance intelligence platform** for Windows. Search and question
your own files, keep an exact ledger and share selected documents with family — with no cloud, no accounts and no
telemetry.

**Engineering:** 22-crate Rust workspace · Tauri + React/TypeScript · SQLCipher encryption at rest ·
isolated extraction workers · 13 ADRs · threat model · 20-gate production-readiness checklist · CycloneDX SBOM ·
benchmarks to 100k files (search p95 under 100 ms at 10k).

`Rust` `Tauri` `TypeScript` `React` `SQLite/SQLCipher` `GitHub Actions` `Playwright`

**[Read the case study →](case-studies/arq.md)** <sub>· source private</sub>

</td>
<td width="50%" valign="top">

### ⛪ Kingdom Connect — Connect. Present. Worship.
A **service presentation platform for churches**: plan a service as Frames, then present to the room, to
Zoom / Teams / Meet through its own virtual camera, and to a stream — run from a PC, phone or iPad. Built for
volunteers, offline by default.

**Engineering:** Python backend + vanilla JS front end · virtual camera with background segmentation ·
PIN-protected phone remote · CI-built Windows installer with checksums · role-based guides for church teams ·
20+ versions shipped, v4.0 → v6.6.

`Python` `JavaScript` `MediaPipe` `Inno Setup` `GitHub Actions`

**[Read the case study →](case-studies/kingdom-connect.md)** <sub>· source private</sub>

</td>
</tr>
</table>

### 🧭 Open source · ITOM

<table>
<tr>
<td valign="top">

**[itom-reference-architectures](https://github.com/mshobin/itom-reference-architectures)** — reference designs for
event management & correlation and Discovery → CMDB → service model, each with architecture diagrams, ADRs, sizing
questions, anti-patterns, KPIs and a go-live checklist. Written for BMC Helix practitioners, vendor-neutral at heart.

`Event correlation` `CMDB` `Discovery` `Service modeling` `ADRs` `MIT`

</td>
</tr>
</table>

<!--
  More ITOM showcase repos — uncomment each card only once the public repo exists.

<table><tr>
<td width="50%" valign="top"><b><a href="https://github.com/mshobin/helix-ops-toolkit">helix-ops-toolkit</a></b><br>Python client and CLI for sending, querying and testing events against BMC Helix Operations Management.</td>
<td width="50%" valign="top"><b><a href="https://github.com/mshobin/event-correlation-lab">event-correlation-lab</a></b><br>A small, runnable simulator that shows dedup, suppression and topology correlation on synthetic events.</td>
</tr></table>
-->

---

## 🧰 Technology wall

**Operations & observability**<br>
<img src="https://img.shields.io/badge/BMC_Helix_Operations_Management-0E2236?style=flat-square&logo=bmcsoftware&logoColor=white" alt="BMC Helix Operations Management">
<img src="https://img.shields.io/badge/BMC_Helix_AIOps-0E2236?style=flat-square&logo=bmcsoftware&logoColor=white" alt="BMC Helix AIOps">
<img src="https://img.shields.io/badge/BMC_Helix_Discovery-0E2236?style=flat-square&logo=bmcsoftware&logoColor=white" alt="BMC Helix Discovery">
<img src="https://img.shields.io/badge/BMC_Helix_CMDB-0E2236?style=flat-square&logo=bmcsoftware&logoColor=white" alt="BMC Helix CMDB">
<img src="https://img.shields.io/badge/BMC_Client_Management-0E2236?style=flat-square&logo=bmcsoftware&logoColor=white" alt="BMC Client Management">
<img src="https://img.shields.io/badge/Microsoft_SCOM-0E2236?style=flat-square&logo=microsoft&logoColor=white" alt="Microsoft SCOM">
<img src="https://img.shields.io/badge/Microsoft_SCCM-0E2236?style=flat-square&logo=microsoft&logoColor=white" alt="Microsoft SCCM">

**Practices**<br>
<img src="https://img.shields.io/badge/Event_Correlation-134E4A?style=flat-square" alt="Event correlation">
<img src="https://img.shields.io/badge/Service_Modeling-134E4A?style=flat-square" alt="Service modeling">
<img src="https://img.shields.io/badge/ITIL-134E4A?style=flat-square" alt="ITIL">
<img src="https://img.shields.io/badge/Solution_Architecture-134E4A?style=flat-square" alt="Solution architecture">
<img src="https://img.shields.io/badge/Presales_%26_PoCs-134E4A?style=flat-square" alt="Presales and PoCs">
<img src="https://img.shields.io/badge/Threat_Modeling-134E4A?style=flat-square" alt="Threat modeling">

**Automation & engineering**<br>
<img src="https://img.shields.io/badge/Python-0E2236?style=flat-square&logo=python&logoColor=FFD43B" alt="Python">
<img src="https://img.shields.io/badge/PowerShell-0E2236?style=flat-square&logo=powershell&logoColor=white" alt="PowerShell">
<img src="https://img.shields.io/badge/REST_APIs-0E2236?style=flat-square&logo=openapiinitiative&logoColor=white" alt="REST APIs">
<img src="https://img.shields.io/badge/Rust-0E2236?style=flat-square&logo=rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/TypeScript-0E2236?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript">
<img src="https://img.shields.io/badge/React-0E2236?style=flat-square&logo=react&logoColor=61DAFB" alt="React">
<img src="https://img.shields.io/badge/Tauri-0E2236?style=flat-square&logo=tauri&logoColor=FFC131" alt="Tauri">
<img src="https://img.shields.io/badge/JavaScript-0E2236?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript">
<img src="https://img.shields.io/badge/SQLite-0E2236?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/GitHub_Actions-0E2236?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
<img src="https://img.shields.io/badge/Playwright-0E2236?style=flat-square&logo=playwright&logoColor=white" alt="Playwright">

**Infrastructure**<br>
<img src="https://img.shields.io/badge/Microsoft_Azure-0E2236?style=flat-square&logo=microsoftazure&logoColor=white" alt="Microsoft Azure">
<img src="https://img.shields.io/badge/Windows_Server-0E2236?style=flat-square&logo=windows&logoColor=white" alt="Windows Server">
<img src="https://img.shields.io/badge/Linux-0E2236?style=flat-square&logo=linux&logoColor=white" alt="Linux">
<img src="https://img.shields.io/badge/Active_Directory_%26_GPO-0E2236?style=flat-square&logo=microsoft&logoColor=white" alt="Active Directory and Group Policy">
<img src="https://img.shields.io/badge/Hyper--V-0E2236?style=flat-square&logo=microsoft&logoColor=white" alt="Hyper-V">

---

## 🧭 Enterprise skills matrix

| Capability | Level | Evidence |
|---|---|---|
| BMC Helix ITOM & AIOps (Operations Management, event management, AIOps) | ●●●●● Expert | Team Leader for Helix ITOM & AIOps; regional delivery |
| Solution architecture & presales | ●●●●● Expert | 14 years Senior Solutions Architect; demos, PoCs, workshops |
| Delivery & team leadership | ●●●●○ Advanced | Leads ITOM team; supervised field engineers under SLAs |
| Discovery, CMDB & service modeling | ●●●●○ Advanced | Helix ITOM implementations |
| Microsoft systems management (SCCM, SCOM, AD/GPO) | ●●●●○ Advanced | Oil & gas estate: deployment, patching, monitoring |
| Automation (Python, PowerShell, REST) | ●●●●○ Advanced | Integrations; product build and release tooling |
| Product engineering (Rust, TypeScript, Python) | ●●●●○ Advanced | A.R.Q. and Kingdom Connect |
| Security engineering (threat models, encryption, supply chain) | ●●●○○ Proficient | A.R.Q. threat model, SBOM, cargo-deny, SQLCipher |

---

## 🗓️ Career timeline

| Years | Role | Highlights |
|---|---|---|
| **2025 – now** | **Team Leader, BMC Helix ITOM & AIOps** · Diyar United | Leads strategy, delivery and operations of Helix ITOM; predictive operations, event management, workflow automation across the Middle East |
| **2011 – 2025** | **Senior Solutions Architect** · Diyar United | BMC & Microsoft solutions for major organizations; presales, PoCs, C-level advisory, end-to-end delivery |
| **2009 – 2011** | **Microsoft IT Consultant** · oil & gas project | SCCM software deployment and remote control; SUS → SCCM patching; SCOM monitoring for clustered databases |
| **2007 – 2008** | **Business Desktops Deployment Lead** · oil & gas project | Enterprise Windows 7 rollout under policy; MED-V virtualization of drilling applications |
| **2005 – 2007** | **Technical Workshop Supervisor** · oil & gas project | Hyper-V automated builds; ITIL incident, problem and configuration management on BMC Helpdesk |
| **2004 – 2005** | **IT Trainer / Administrator** · St. Joseph's Convent, Cyprus | Systems administration and IT training |
| **2000 – 2004** | **B.S. Computer Science** · Cyprus College | |

---

## 🎓 Certifications

<p>
<img src="https://img.shields.io/badge/BMC_Certified_Associate-Client_Management-134E4A?style=for-the-badge&logo=bmcsoftware&logoColor=white" alt="BMC Certified Associate: Client Management">
<img src="https://img.shields.io/badge/Microsoft_Office_Specialist-Expert_(Microsoft_365_Apps)-134E4A?style=for-the-badge&logo=microsoft&logoColor=white" alt="Microsoft Office Specialist: Expert (Microsoft 365 Apps)">
<img src="https://img.shields.io/badge/IBM_Lenovo-Mobile_Systems_(RTC05)-134E4A?style=for-the-badge&logo=lenovo&logoColor=white" alt="IBM Lenovo Mobile Systems (RTC05)">
</p>

---

## 🔭 Current focus

- Predictive, service-centric operations on **BMC Helix AIOps**
- Event correlation patterns that cut noise without hiding real failures
- Publishing reusable ITOM patterns — [itom-reference-architectures](https://github.com/mshobin/itom-reference-architectures) — and tooling here on GitHub
- Taking **A.R.Q.** through its open production gates: code signing, clean-VM installer tests, external security review

---

## 📈 GitHub activity

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=mshobin&show_icons=true&hide_border=true&bg_color=0E2236&title_color=2DD4BF&icon_color=F59E0B&text_color=CBD5E1&count_private=true" alt="GitHub stats" height="165">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=mshobin&layout=compact&hide_border=true&bg_color=0E2236&title_color=2DD4BF&text_color=CBD5E1" alt="Top languages" height="165">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mshobin/mshobin/output/github-snake-dark.svg">
    <img src="https://raw.githubusercontent.com/mshobin/mshobin/output/github-snake.svg" alt="Contribution graph animation">
  </picture>
</p>

---

## 🧭 How I work

> **Evidence over marketing.** If a feature isn't done or a result isn't verified, the documentation says so.
> **Reliability over features.** Operations software earns trust by never being the thing that fails.
> **Design from the service down.** Infrastructure exists to serve a business outcome; models and alerts should say which one.

---

<p align="center">
  <b>Looking for BMC Helix ITOM / AIOps architecture, delivery leadership or a solutions architect for the GCC?</b><br>
  <a href="mailto:mshobin@outlook.com">mshobin@outlook.com</a> · <a href="https://www.linkedin.com/in/mshobin/">linkedin.com/in/mshobin</a>
</p>

<p align="center"><sub>BMC, BMC Helix and other product names are trademarks of their respective owners. Architecture diagrams here are generic patterns and contain no client information.</sub></p>
