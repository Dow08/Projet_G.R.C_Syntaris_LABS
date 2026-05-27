# GDPR Compliance Assessment: Syntaris Group
**Date:** 2026-05-27
**Status:** Completed Draft (Phase 3)
**Auditor:** Cyber Security Advisory Lab

This report provides an in-depth analysis of Syntaris Group's compliance status against critical articles of the General Data Protection Regulation (GDPR), focusing on Articles 5, 25, 32, and 33.

---

## 1. Article 5: Principles Relating to Processing of Personal Data
Article 5 establishes the core principles of personal data processing. For Syntaris, two principles are currently at risk:

*   **Minimization (Art 5.1.c):** Syntaris collects financial data, identity documents, and biometric details. Currently, there is a risk of over-retention (keeping raw scans of passports indefinitely).
    *   *Remediation:* Enforce automatic deletion of biometric templates once identity verification is finalized. Store only verification tokens and status indicators.
*   **Storage Limitation (Art 5.1.e):** Personal data must not be kept longer than necessary.
    *   *Remediation:* Draft and implement a strict Data Retention Policy specifying precise retention limits (e.g., transaction data for 5 years under national fiscal laws; KYC raw documents deleted after 30 days).

---

## 2. Article 25: Data Protection by Design and by Default
As identified in the audit, Syntaris handles highly sensitive identity and payment flows but lacks formalized mapping or default privacy safeguards.

*   **Privacy by Design (API Tokenization):** The payment processing API should never propagate or store raw Primary Account Numbers (PAN / credit cards) in clear text within internal logs or secondary databases.
    *   *Remediation:* Implement payment tokenization at the entry gateway (conforming to PCI-DSS standards).
*   **Privacy by Default (Least Privilege & Testing):** Developers currently use production-like datasets containing real customer info for testing and debugging.
    *   *Remediation:* Implement systematic data masking and synthetic data generation for all non-production environments. Enforce strict RBAC (Role-Based Access Control) on production databases.

---

## 3. Article 32: Security of Processing
Article 32 mandates appropriate technical and organizational measures to ensure a level of security appropriate to the risk.

*   **Identified Gaps:**
    *   Lack of a formal Information Security Policy (PSSI).
    *   Absence of a Security Operations Center (SOC) or SIEM for real-time traffic monitoring.
    *   Inconsistent Multi-Factor Authentication (MFA) on developer workstations.
*   **Remediation:**
    *   Enforce mandatory MFA across all administrative and engineering accounts (NIST PR.AA-03).
    *   Adopt AES-256 encryption at rest with customer-managed keys (BYOK via AWS KMS) for sensitive KYC databases (NIST PR.DS-01).
    *   Deploy automated Static Application Security Testing (SAST) in the CI/CD pipeline to prevent vulnerability injections (NIST PR.PS-06).

---

## 4. Article 33: Notification of a Personal Data Breach to the Supervisory Authority
Article 33 requires the controller to notify the competent supervisory authority (e.g., CNIL in France) within **72 hours** after becoming aware of a breach, unless the breach is unlikely to result in a risk to rights and freedoms.

*   **Identified Gaps:**
    *   Syntaris has no formal Data Breach Response Plan.
    *   No incident escalation matrix or pre-drafted notification templates exist.
    *   No Data Protection Officer (DPO) has been designated to lead the response.
*   **Remediation:**
    *   Formally designate a DPO (Article 37) to oversee GDPR compliance and orchestrate regulatory reporting.
    *   Create a Data Breach Response Playbook detailing detection, escalation, containment, and notification steps within the 72-hour window.
    *   Maintain an internal Data Breach Log (even for non-notifiable events).
