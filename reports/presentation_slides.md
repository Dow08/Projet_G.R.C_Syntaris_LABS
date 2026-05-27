# Slide Deck: Syntaris Group GRC Audit
## NIST CSF 2.0 & GDPR Strategic Security Plan
**Presenter:** Dorian Poncelet — Cyber Security Advisor

---

## Slide 1: Executive Context
### Who is Syntaris Group?
*   **Business:** Fintech provider handling online payment processing and digital Identity Verification (KYC).
*   **Scale:** Rapid transatlantic expansion (Europe and United States).
*   **Infrastructure:** Hybrid Cloud Architecture (AWS/Azure for transaction processing, secure on-premises office for corporate administration).
*   **Compliance Drivers:** GDPR (Europe), PCI-DSS (Payment Industry), and client demands for mature cybersecurity.

---

## Slide 2: Critical Asset & Data Mapping
*   **Personal Financial Data (GDPR / PCI-DSS):**
    *   Credit card numbers (PAN), transaction records, bank accounts.
*   **Biometric & Identity Data (GDPR Art. 9 / KYC):**
    *   Passeport/ID card scans, facial biometric templates.
    *   *Note:* Biometric data is classified as sensitive, requiring a mandatory DPIA (AIPD) and DPO appointment.
*   **Corporate Data:**
    *   Internal source code, API keys, customer database metadata.

---

## Slide 3: Top 3 Business Risks
1.  **Breach of KYC & Biometric Databases:**
    *   *Impact:* Up to 4% global turnover fine (GDPR Art. 83), complete loss of banking trust, CNIL audit.
2.  **Payment Platform Downtime (DDoS / Cloud Outage):**
    *   *Impact:* Immediate financial losses, contract SLA penalties with merchants, business disruption.
3.  **Software Supply Chain Attack (Magecart style):**
    *   *Impact:* Malicious code injected into transaction APIs, leading to real-time credit card theft.

---

## Slide 4: NIST CSF 2.0 Maturity Profile
*   **Global Current Score:** **1.50 / 4.0** (Tier 1 - Partial)
*   **Global Target Score:** **3.86 / 4.0** (Tier 3/4 - Repeatable/Adaptive)

### Function-level Results:
*   **Govern (GV):** Current 1.50 -> Target 3.67 *(Gap: +2.17)*
*   **Identify (ID):** Current 1.50 -> Target 3.75 *(Gap: +2.25)*
*   **Protect (PR):** Current 1.83 -> Target 4.00 *(Gap: +2.17)*
*   **Detect (DE):** Current 1.50 -> Target 4.00 *(Gap: +2.50)*
*   **Respond (RS):** Current 1.00 -> Target 4.00 *(Gap: +3.00)* - **CRITICAL GAP**
*   **Recover (RC):** Current 1.00 -> Target 4.00 *(Gap: +3.00)* - **CRITICAL GAP**

---

## Slide 5: GDPR Focus — Critical Gaps
*   **Article 5 (Minimization):** Unlimited retention of passport scans and raw biometric templates.
*   **Article 25 (Privacy by Design/Default):** Developpers using real client production data for local testing; raw PAN stored in logs.
*   **Article 32 (Security):** Inconsistent MFA on engineering accounts; lack of standard configurations and SAST code scanning.
*   **Article 33 (Breach Notification):** No formal 72h incident response plan, no designated DPO.

---

## Slide 6: Roadmap Priority 1: Quick Wins (0-30 Days)
### Core Focus: Legal Safeguarding & Access Control
*   **REC-01: Appoint a DPO & Author the 72H Breach Notification Playbook**
    *   *Objective:* Strict compliance with GDPR Art. 33 and 37. Define exact escalation and notification templates.
    *   *Owner:* General Counsel / CEO.
*   **REC-02: Enforce Mandatory MFA across Cloud and Code repositories**
    *   *Objective:* Stop 99% of bulk credential attacks.
    *   *Owner:* DevOps / IT Security.

---

## Slide 7: Roadmap Priority 2: Technical Protections (30-90 Days)
### Core Focus: Security Architecture & Resilience
*   **REC-03: Implement Payment Tokenization and Synthetic Test Data**
    *   *Objective:* Conform to PCI-DSS and GDPR Art. 25 (Privacy by Design). Avoid raw payment cards storage.
    *   *Owner:* Software Engineering / QA.
*   **REC-04: Secure Backup Strategy & AES-256 Encryption**
    *   *Objective:* Protect against ransomware and ensure offline immutable data persistence.
    *   *Owner:* IT Infrastructure.

---

## Slide 8: Roadmap Priority 3: Mature Operations (90-180 Days)
### Core Focus: Continuous Governance & Detection
*   **REC-05: Draft the Information Security Policy (PSSI) & User Charter**
    *   *Objective:* Formalize security expectations for employees and define acceptable use rules.
    *   *Owner:* CISO / HR.
*   **REC-06: Outsource to a Managed SOC (Security Operations Center)**
    *   *Objective:* Real-time, 24/7 security event monitoring and log correlation via SIEM.
    *   *Owner:* IT Security Director.

---

## Slide 9: Conclusion
### Key Takeaways for Syntaris Group
*   **Security is a Business Enabler:** Attaining a mature NIST CSF 2.0 posture is necessary to sign large banking partners.
*   **GDPR Compliance is Mandatory:** Transitioning from biometric data retention to tokenized KYC status protects Syntaris from catastrophic fines.
*   **Automation of GRC:** Using structured data (CSV) and automated compliance scripts ensures continuous verification and real-time reporting.

### Thank you! Questions?
