# Syntaris GRC Compliance & Security Maturity Audit Lab
## NIST CSF 2.0 & GDPR Co-Audit Framework for Fintech Platform

[![GRC Audit](https://img.shields.io/badge/GRC-Audit-blue.svg)](#)
[![NIST CSF 2.0](https://img.shields.io/badge/Framework-NIST%20CSF%202.0-green.svg)](#)
[![GDPR Compliant](https://img.shields.io/badge/Compliance-GDPR%20%2F%20RGPD-orange.svg)](#)
[![Python Automation](https://img.shields.io/badge/Automation-Python%203-blue.svg)](#)

This repository constitutes a professional security audit and compliance lab for **Syntaris Group**, a fast-growing fintech company processing payments and performing digital Identity Verification (KYC) across Europe and the United States. 

As an external Cyber Security Advisor, this lab demonstrates how to bridge corporate governance, regulatory constraints (GDPR, PCI-DSS), and international security frameworks (NIST CSF 2.0) into a unified, risk-driven technical roadmap.

---

## 📂 Repository Structure

*   `data/nist_csf_evaluation.csv` : Raw GRC audit database containing 22 core NIST CSF 2.0 subcategories evaluated with current scores, target scores, and justifications.
*   `scripts/scoring_nist_csf.py` : Python 3 automation script that calculates maturity scores, generates ASCII comparison dual-bar charts, and automatically outputs the detailed report.
*   `reports/nist_csf_report.md` : Automatically generated detailed NIST CSF 2.0 maturity report.
*   `reports/gdpr_compliance_analysis.md` : Regulatory analysis focused on GDPR Articles 5 (Principles), 25 (Privacy by Design/Default), 32 (Security of Processing), and 33 (Data Breach Notification).
*   `reports/roadmap_recommendations.md` : Prioritized strategic roadmap (Urgency High/Medium/Low) based on Risk vs. Effort optimization (Pareto principle).
*   `reports/presentation_slides.md` : Structure and trame of the 5-10 minute pitch presentation for CODIR or academic defense.

---

## ⚙️ Automated Scoring & Heatmap Generation

This lab utilizes code to prove compliance. To run the automated scoring and generate the visual comparison and audit report, execute:

```bash
python3 scripts/scoring_nist_csf.py
```

### Console Output Preview
```text
============================================================
      NIST CSF 2.0 MATURITY PROFILE: CURRENT VS TARGET
============================================================

GV - GOVERN:
  Current: [████████░░░░░░░░░░░░] 1.50 / 4.0
  Target:  [██████████████████░░] 3.67 / 4.0
  Gap:     +2.17

ID - IDENTIFY:
  Current: [████████░░░░░░░░░░░░] 1.50 / 4.0
  Target:  [███████████████████░] 3.75 / 4.0
  Gap:     +2.25

PR - PROTECT:
  Current: [█████████░░░░░░░░░░░] 1.83 / 4.0
  Target:  [████████████████████] 4.00 / 4.0
  Gap:     +2.17

DE - DETECT:
  Current: [████████░░░░░░░░░░░░] 1.50 / 4.0
  Target:  [████████████████████] 4.00 / 4.0
  Gap:     +2.50

RS - RESPOND:
  Current: [█████░░░░░░░░░░░░░░░] 1.00 / 4.0
  Target:  [████████████████████] 4.00 / 4.0
  Gap:     +3.00

RC - RECOVER:
  Current: [█████░░░░░░░░░░░░░░░] 1.00 / 4.0
  Target:  [████████████████████] 4.00 / 4.0
  Gap:     +3.00
============================================================
```

---

## 🎯 Strategic Key Takeaways & Core Gaps

1.  **Maturity Progression:** Global security maturity currently stands at a weak **1.50 / 4.0** (Tier 1 - Partial) with a target to achieve a robust **3.86 / 4.0** (Tier 3/4 - Repeatable/Adaptive).
2.  **Respond & Recover Gaps:** The most critical technical exposures reside in Respond (RS) and Recover (RC) with current scores of **1.00 / 4.0**. Syntaris has no formal Data Breach Playbook or validated Disaster Recovery Plan (PCA/PRA).
3.  **The Biometric Exposure:** Collecting and processing biometric face templates for customer KYC activates **GDPR Article 9 (Sensitive Data)**, making a formal Data Protection Officer (DPO) and a Data Protection Impact Assessment (DPIA/AIPD) strictly mandatory.

---

## 🛡️ Executive Roadmap (Pareto Principle)

*   **Priority 1 (0-30 Days - Quick Wins):** Register DPO + Author 72h Breach Notification Playbook (GDPR compliance safeguarding) + Enforce mandatory MFA on AWS/Azure and GitHub consoles.
*   **Priority 2 (30-90 Days - Tech Protections):** Implement API Tokenization for payment cards (PCI-DSS) + Deploy synthetic test databases to dev environments (Art. 25 Privacy by Default) + AES-256 Backup Encryption.
*   **Priority 3 (90-180 Days - Governance):** Draft Corporate Information Security Policy (PSSI) + Deploy SIEM and partner with a Managed SOC for 24/7 intrusion monitoring.

---

## 🤝 How to use this Lab
1.  Clone this repository.
2.  Explore the raw metrics in `data/nist_csf_evaluation.csv`.
3.  Modify scores or add justifications to fit other audit scopes.
4.  Run the Python script to auto-generate the updated reports.
