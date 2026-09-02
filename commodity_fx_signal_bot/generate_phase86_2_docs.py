import os
import re
from pathlib import Path

def append_to_file(filepath, content):
    if not Path(filepath).exists():
        print(f"Skip {filepath} - not found")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        existing = f.read()
    if "Local Red-Team Rehearsal and Safety Assurance" not in existing:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\\n\\n" + content + "\\n")
        print(f"Updated {filepath}")

def update_docs():
    readme_content = """## Local Red-Team Rehearsal and Safety Assurance
Phase 86 introduces a comprehensive Local Red-Team Rehearsal layer.

- **Final local red-team rehearsal packet** is NOT a real red-team test.
- **Misuse scenario library** does NOT contain real attack or exploit instructions.
- **Abuse-case simulation registry** is a dry-run documentation, not an active exploit generator.
- **Adversarial prompt safety checklist** is NOT a real jailbreak prompt collection.
- **Prompt-injection pattern registry** is NOT a payload database.
- **Safety assurance summary** is NOT a formal certification or production approval.
- Cloud upload, package publish, telemetry, dashboard, live trading, broker execution, and investment advice are explicitly disabled and out of scope.
- Outputs are saved under `data/lake/local_redteam` and `reports/output/local_redteam`.

**Commands to generate local red-team reports:**
```bash
python -m scripts.run_redteam_domain_registry
python -m scripts.run_final_local_redteam_rehearsal
python -m scripts.run_misuse_scenario_library
python -m scripts.run_adversarial_prompt_safety_checklist
python -m scripts.run_safety_assurance_summary
python -m scripts.run_redteam_quality_report
python -m scripts.run_redteam_status
```
"""
    append_to_file("README.md", readme_content)
    
    arch_content = """### Local Red-Team Rehearsal Flow
Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ RedTeamProfileRegistry
→ RedTeamDomainRegistry
→ FinalLocalRedTeamRehearsalPacket
→ MisuseScenarioLibrary
→ AbuseCaseSimulationRegistry
→ AdversarialPromptSafetyChecklist
→ PromptInjectionRiskPatterns
→ UnsafeOutputPatterns
→ ForbiddenCapabilityRequests
→ BoundaryViolationScenarios
→ SpecificMisuseRegistries
→ SafetyResponseExpectations
→ SafeRefusalTemplates
→ SafeRedirectPatterns
→ ManualEscalation
→ HumanReviewAbuseCases
→ RedTeamReadingOrder
→ SafetyAssuranceSummary
→ SafetyCoverageMatrix
→ SafetyBlindspots
→ SafetyNonGoals
→ RedTeamNoGoSafeGo
→ RedTeamExceptions
→ RedTeamGaps
→ RedTeamRisks
→ RedTeamReadinessScoring
→ RedTeamValidation
→ RedTeamQuality
→ Local Red-Team Outputs
"""
    arch_path = "docs/ARCHITECTURE.md"
    if Path(arch_path).exists():
        with open(arch_path, "r", encoding="utf-8") as f:
            existing = f.read()
        if "RedTeamProfileRegistry" not in existing:
            with open(arch_path, "a", encoding="utf-8") as f:
                f.write("\\n" + arch_content + "\\n")
            print("Updated ARCHITECTURE.md")

    phase_log_content = """
## Phase 86: Local Red-Team Rehearsal and Safety Assurance Layer
- Local red-team profile sistemi eklendi.
- Red-team label registry eklendi.
- RedTeamDomain, MisuseScenario, AbuseCaseSimulation, SafetyChecklistItem ve RedTeamFinding modelleri eklendi.
- Red-team domain registry eklendi.
- Final local red-team rehearsal packet eklendi.
- Misuse scenario library eklendi.
- Abuse-case simulation registry eklendi.
- Adversarial prompt safety checklist eklendi.
- Prompt-injection risk pattern registry eklendi.
- Unsafe output pattern registry eklendi.
- Forbidden capability request registry eklendi.
- Boundary-violation scenario registry eklendi.
- Specific misuse registries eklendi.
- Safety response expectation registry eklendi.
- Safe refusal template registry eklendi.
- Safe redirect pattern registry eklendi.
- Manual escalation checklist eklendi.
- Human review abuse-case checklist eklendi.
- Red-team reading order eklendi.
- Safety assurance summary ve evidence index eklendi.
- Safety coverage matrix eklendi.
- Safety blindspot register ve safety non-goals registry eklendi.
- Red-team no-go/safe-go summary eklendi.
- Red-team exception/gap/risk registerları eklendi.
- Red-team readiness score report eklendi.
- Red-team validation ve quality report eklendi.
- LocalRedTeamPipeline eklendi.
- DataLake local red-team kayıt desteği aldı.
- Local red-team scriptleri eklendi.
- Testler genişletildi.
"""
    append_to_file("docs/PHASE_LOG.md", phase_log_content)
    
    manuals = [
        "docs/OPERATOR_MANUAL.md", 
        "docs/ANALYST_HANDBOOK.md", 
        "docs/CODEX_AGENT_GUIDE.md", 
        "docs/SAFE_USAGE_GUIDE.md", 
        "docs/INSTALLATION.md", 
        "docs/CONFIGURATION.md"
    ]
    
    manual_content = """## Local Red-Team Rehearsal and Safety Assurance
- **How to read the red-team rehearsal packet?** It is a collection of dry-run safety boundary exercises to demonstrate the project's resilience to misuse.
- **How to interpret the misuse scenario library?** It catalogues theoretical abuse vectors in an abstract format. It does NOT contain real attack or exploit instructions.
- **Why is abuse-case simulation not a real attack?** It only records the expected refusal/boundary logic without actually executing malicious payloads against a live system.
- **Why is the adversarial prompt safety checklist not a jailbreak collection?** It is an abstract list of checks rather than operational payload inputs.
- **Why is the safety assurance summary not a certification?** It is an offline rehearsal report of system safety mechanisms, not an official compliance or production approval.
- **How to use the manual escalation checklist?** Use it to identify inputs that trigger a human review process for safety validation.
- **Disclaimer:** The outputs from this module DO NOT constitute real attacks, exploits, jailbreaks, credential exfiltration, telemetry, dashboard creation, live trading orders, broker execution, model deployment, or investment advice.
"""
    for m in manuals:
        append_to_file(m, manual_content)

if __name__ == "__main__":
    update_docs()
