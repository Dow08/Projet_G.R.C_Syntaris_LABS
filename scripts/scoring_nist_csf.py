#!/usr/bin/env python3
import csv
import sys
from collections import defaultdict
from datetime import datetime

# Mapping codes to function names
FUNCTIONS = {
    "GV": "Govern",
    "ID": "Identify",
    "PR": "Protect",
    "DE": "Detect",
    "RS": "Respond",
    "RC": "Recover"
}

def load_evaluation(csv_path):
    data = []
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "fonction": row["fonction"].strip(),
                    "categorie": row["categorie"].strip(),
                    "sous_categorie": row["sous_categorie"].strip(),
                    "nom": row["nom"].strip(),
                    "score_actuel": float(row["score_actuel"]),
                    "score_cible": float(row["score_cible"]),
                    "justification": row["justification"].strip()
                })
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        sys.exit(1)
    return data

def calculate_metrics(data):
    by_fn = defaultdict(lambda: {"actuel_sum": 0.0, "cible_sum": 0.0, "count": 0, "items": []})
    for item in data:
        fn = item["fonction"]
        by_fn[fn]["actuel_sum"] += item["score_actuel"]
        by_fn[fn]["cible_sum"] += item["score_cible"]
        by_fn[fn]["count"] += 1
        by_fn[fn]["items"].append(item)
    return by_fn

def draw_ascii_chart(metrics):
    print("\n" + "="*60)
    print("      NIST CSF 2.0 MATURITY PROFILE: CURRENT VS TARGET")
    print("="*60)
    for fn, name in FUNCTIONS.items():
        m = metrics[fn]
        avg_actuel = m["actuel_sum"] / m["count"] if m["count"] else 0.0
        avg_cible = m["cible_sum"] / m["count"] if m["count"] else 0.0
        
        # Draw bars
        bar_actuel = "█" * int(round(avg_actuel * 5)) + "░" * (20 - int(round(avg_actuel * 5)))
        bar_cible = "█" * int(round(avg_cible * 5)) + "░" * (20 - int(round(avg_cible * 5)))
        
        print(f"\n{fn} - {name.upper()}:")
        print(f"  Current: [{bar_actuel}] {avg_actuel:.2f} / 4.0")
        print(f"  Target:  [{bar_cible}] {avg_cible:.2f} / 4.0")
        print(f"  Gap:     {avg_cible - avg_actuel:+.2f}")
    print("="*60 + "\n")

def generate_report(data, metrics, output_path):
    lines = []
    lines.append("# NIST Cybersecurity Framework 2.0 Evaluation Report")
    lines.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("**Organization:** Syntaris Group")
    lines.append("**Auditor:** Cyber Security Advisory Lab\n")
    
    lines.append("## Executive Summary")
    lines.append("This report presents the cybersecurity maturity posture of Syntaris Group evaluated against the NIST CSF 2.0 framework. Syntaris operations as a fintech handling payment processing and digital KYC require robust defensive and resilience controls. Currently, Syntaris shows traits of Tier 1 (Partial) / Tier 2 (Risk Informed) maturity, with an objective to achieve Tier 3 (Repeatable) / Tier 4 (Adaptive) to satisfy merchant clients and ensure transatlantic GDPR/PCI-DSS compliance.\n")
    
    lines.append("## Function-level Maturity Summary\n")
    lines.append("| Function | Code | Current Score | Target Score | Gap | Maturity Tier (Target) |")
    lines.append("|---|---|---|---|---|---|")
    
    total_actuel = 0.0
    total_cible = 0.0
    total_count = 0
    
    for fn, name in FUNCTIONS.items():
        m = metrics[fn]
        avg_actuel = m["actuel_sum"] / m["count"] if m["count"] else 0.0
        avg_cible = m["cible_sum"] / m["count"] if m["count"] else 0.0
        gap = avg_cible - avg_actuel
        
        total_actuel += m["actuel_sum"]
        total_cible += m["cible_sum"]
        total_count += m["count"]
        
        tier = "Tier 3 (Repeatable)" if avg_cible >= 3.0 else "Tier 4 (Adaptive)"
        if avg_cible >= 3.8:
            tier = "Tier 4 (Adaptive)"
            
        lines.append(f"| {name} | {fn} | {avg_actuel:.2f} / 4.0 | {avg_cible:.2f} / 4.0 | {gap:+.2f} | {tier} |")
        
    global_actuel = total_actuel / total_count if total_count else 0.0
    global_cible = total_cible / total_count if total_count else 0.0
    lines.append(f"| **OVERALL** | **ALL** | **{global_actuel:.2f} / 4.0** | **{global_cible:.2f} / 4.0** | **{global_cible - global_actuel:+.2f}** | **Tier 3 (Repeatable)** |")
    lines.append("\n")
    
    lines.append("## Identified Gaps & Details\n")
    lines.append("| Code | Subcategory Name | Current | Target | Justification |")
    lines.append("|---|---|---|---|---|")
    for item in data:
        lines.append(f"| {item['sous_categorie']} | {item['nom']} | {item['score_actuel']:.0f} | {item['score_cible']:.0f} | {item['justification']} |")
        
    lines.append("\n## Core Recommendations")
    lines.append("1. **Formalize Security Governance (Govern - GV):** Draft and authorize a formal Information Security Policy (PSSI) and officially designate a Data Protection Officer (DPO).")
    lines.append("2. **Implement Data Lifecycle Mapping (Identify - ID):** Conduct data mapping flows for transactions and biometric KYC data.")
    lines.append("3. **Strengthen Platform Protections (Protect - PR):** Enforce strict multi-factor authentication (MFA) across all administrative and developer endpoints, and integrate automated static code analysis (SAST) in CI/CD pipeline.")
    lines.append("4. **Establish Real-Time Monitoring & Detection (Detect - DE):** Partner with a Managed SOC or centralize logs into a SIEM for 24/7 security event correlation.")
    lines.append("5. **Develop Incident & Recovery Plans (Respond & Recover - RS/RC):** Create incident response plans tailored to data breach notification (GDPR Art. 33) and business continuity plans (PCA/PRA).\n")
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Detailed Markdown Report successfully generated: {output_path}")
    except Exception as e:
        print(f"Error writing markdown report: {e}")

if __name__ == "__main__":
    csv_file = "/root/syntaris-grc/data/nist_csf_evaluation.csv"
    report_file = "/root/syntaris-grc/reports/nist_csf_report.md"
    
    data = load_evaluation(csv_file)
    metrics = calculate_metrics(data)
    draw_ascii_chart(metrics)
    generate_report(data, metrics, report_file)
