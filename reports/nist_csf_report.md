# NIST Cybersecurity Framework 2.0 Evaluation Report
**Date:** 2026-05-27
**Organization:** Syntaris Group
**Auditor:** Cyber Security Advisory Lab

## Executive Summary
This report presents the cybersecurity maturity posture of Syntaris Group evaluated against the NIST CSF 2.0 framework. Syntaris operations as a fintech handling payment processing and digital KYC require robust defensive and resilience controls. Currently, Syntaris shows traits of Tier 1 (Partial) / Tier 2 (Risk Informed) maturity, with an objective to achieve Tier 3 (Repeatable) / Tier 4 (Adaptive) to satisfy merchant clients and ensure transatlantic GDPR/PCI-DSS compliance.

## Function-level Maturity Summary

| Function | Code | Current Score | Target Score | Gap | Maturity Tier (Target) |
|---|---|---|---|---|---|
| Govern | GV | 1.50 / 4.0 | 3.67 / 4.0 | +2.17 | Tier 3 (Repeatable) |
| Identify | ID | 1.50 / 4.0 | 3.75 / 4.0 | +2.25 | Tier 3 (Repeatable) |
| Protect | PR | 1.83 / 4.0 | 4.00 / 4.0 | +2.17 | Tier 4 (Adaptive) |
| Detect | DE | 1.50 / 4.0 | 4.00 / 4.0 | +2.50 | Tier 4 (Adaptive) |
| Respond | RS | 1.00 / 4.0 | 4.00 / 4.0 | +3.00 | Tier 4 (Adaptive) |
| Recover | RC | 1.00 / 4.0 | 4.00 / 4.0 | +3.00 | Tier 4 (Adaptive) |
| **OVERALL** | **ALL** | **1.50 / 4.0** | **3.86 / 4.0** | **+2.36** | **Tier 3 (Repeatable)** |


## Identified Gaps & Details

| Code | Subcategory Name | Current | Target | Justification |
|---|---|---|---|---|
| GV.OC-01 | Mission organisationnelle comprise | 2 | 4 | La mission est comprise de facon informelle mais non formalisee dans une charte d entreprise. |
| GV.OC-03 | Exigences legales et reglementaires comprises | 2 | 4 | Le RGPD et PCI-DSS sont identifies mais pas completement integres dans les processus techniques. |
| GV.RM-01 | Objectifs de gestion des risques convenus | 1 | 3 | Pas de politique formelle de gestion des risques validée par la direction. |
| GV.RR-01 | Roles et responsabilites cyber etablis | 2 | 4 | Les roles existent au sein de la technique mais pas de responsabilisation transverse ni de DPO officiel. |
| GV.PO-01 | Politique cyber etablie | 1 | 4 | Pas de PSSI (Politique de Securite des Systemes d Information) globale et redigee. |
| GV.SC-01 | Programme de gestion des risques fournisseurs | 1 | 3 | Pas d audit systematique de la conformite des sous-traitants cloud et SaaS (Art 28 RGPD). |
| ID.AM-01 | Inventaire materiel maintenu | 2 | 3 | Inventaire automatique partiel des serveurs cloud mais pas des equipements locaux. |
| ID.AM-03 | Cartographie des flux de donnees | 1 | 4 | Aucune cartographie des flux de donnees personnelles et de paiement n est documentee. |
| ID.RA-01 | Vulnerabilites identifiees | 2 | 4 | Des scans de vulnerabilites ad-hoc sont faits mais pas de processus de gestion des correctifs formalise. |
| ID.RA-05 | Risques cyber prioritises | 1 | 4 | Pas de registre des risques formellement mis a jour et presente au CODIR. |
| PR.AA-03 | Authentification forte (MFA) | 2 | 4 | MFA actif sur les consoles cloud mais pas sur l ensemble des postes de developpement ni acces admin. |
| PR.AA-05 | Acces gere selon moindre privilege | 1 | 4 | Droits d acces trop permissifs accordes par defaut aux developpeurs et supports. |
| PR.DS-01 | Donnees protegees au repos | 2 | 4 | Bases de donnees cloud chiffrees par defaut mais cles de chiffrement gerees par le fournisseur (pas de KMS propre). |
| PR.DS-02 | Donnees protegees en transit | 3 | 4 | HTTPS systematique sur les APIs de paiement externes. |
| PR.DS-11 | Sauvegardes creees et testees | 2 | 4 | Sauvegardes automatiques dans le cloud mais pas de tests de restauration periodiques documentes. |
| PR.PS-06 | Pratiques securite du code | 1 | 4 | Pas d analyse statique de code (SAST) systematique ni de controle des dependances dans la CI/CD. |
| DE.CM-01 | Reseaux surveilles | 2 | 4 | Logs cloud collectes mais pas de SIEM ni de surveillance en temps reel centralisee. |
| DE.AE-02 | Activites suspectes analysees | 1 | 4 | Pas d equipe dediee (SOC interne ou externe) pour analyser et lever les alertes 24/7. |
| RS.MA-01 | Plan de reponse execute | 1 | 4 | Pas de plan de reponse aux incidents documente (PUI) ni de playbook de gestion des violations de donnees. |
| RS.CO-02 | Parties prenantes internes notifiees | 1 | 4 | Pas de procedure d escalade vers le juridique pour la notification CNIL sous 72h (Art 33). |
| RC.RP-01 | Plan de reprise execute | 1 | 4 | Pas de plan de continuite ni de reprise d activite (PCA/PRA) formalise et teste pour la fintech. |
| RC.RP-03 | Integrite sauvegardes verifiee | 1 | 4 | Aucun test formel de restauration des sauvegardes n est realise regulierement. |

## Core Recommendations
1. **Formalize Security Governance (Govern - GV):** Draft and authorize a formal Information Security Policy (PSSI) and officially designate a Data Protection Officer (DPO).
2. **Implement Data Lifecycle Mapping (Identify - ID):** Conduct data mapping flows for transactions and biometric KYC data.
3. **Strengthen Platform Protections (Protect - PR):** Enforce strict multi-factor authentication (MFA) across all administrative and developer endpoints, and integrate automated static code analysis (SAST) in CI/CD pipeline.
4. **Establish Real-Time Monitoring & Detection (Detect - DE):** Partner with a Managed SOC or centralize logs into a SIEM for 24/7 security event correlation.
5. **Develop Incident & Recovery Plans (Respond & Recover - RS/RC):** Create incident response plans tailored to data breach notification (GDPR Art. 33) and business continuity plans (PCA/PRA).
