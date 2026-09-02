import os

def append_to_file(path, text):
    if os.path.exists(path):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(text)

append_to_file("README.md", """
## Local Executive Briefing and Stakeholder Communication

Local briefing layer yatirim tavsiyesi uretmez.
Executive summary resmi karar belgesi degildir.
Non-technical briefing deck source PPTX/PDF zorunlu degildir; markdown/json source uretir.
Decision-context binder karar verdirmez; karar baglami saglar.
Safe communication guide overclaim riskini azaltmak icindir.
Stakeholder templates canli trading, broker execution veya production release iddiasi icermez.
Ciktilar data/lake/local_briefing ve reports/output/local_briefing altinda olusur.

python -m scripts.run_briefing_profile_registry
python -m scripts.run_executive_summary_pack
python -m scripts.run_briefing_deck_source
python -m scripts.run_decision_context_binder
python -m scripts.run_stakeholder_communication_kit
python -m scripts.run_briefing_quality_report
python -m scripts.run_briefing_status
""")

append_to_file("docs/ARCHITECTURE.md", """
Docs / Reports / DataLake / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR / Training
-> CommunicationProfileRegistry
-> StakeholderAudienceRegistry
-> ExecutiveSummaryPack
-> ProjectOnePager
-> NonTechnicalBriefingDeckSource
-> ProjectNarrativeReport
-> DecisionContextBinder
-> CapabilityMap
-> BoundaryNonUseSummary
-> RiskLimitationNarrative
-> MilestoneNarrative
-> PhaseEvolutionNarrative
-> ArchitectureNarrative
-> StakeholderFAQ
-> ExecutiveGlossary
-> SafeCommunicationGuide
-> CommunicationDoDont
-> StakeholderTemplates
-> CommunicationGaps
-> CommunicationRisks
-> BriefingValidation
-> BriefingQuality
-> Local Briefing Outputs
""")

append_to_file("docs/PHASE_LOG.md", """
## Phase 74
- Local briefing profile sistemi eklendi.
- Briefing label registry eklendi.
- StakeholderAudience, BriefingSection, DeckSlideSource, DecisionQuestion ve CommunicationFinding modelleri eklendi.
- Stakeholder audience registry eklendi.
- Executive summary pack eklendi.
- Project one-pager eklendi.
- Non-technical briefing deck source eklendi.
- Project narrative report eklendi.
- Decision-context binder eklendi.
- Capability map eklendi.
- Boundary/non-use summary eklendi.
- Risk/limitation narrative eklendi.
- Milestone ve phase evolution narrative eklendi.
- Local-only architecture narrative eklendi.
- Stakeholder FAQ ve executive glossary eklendi.
- Safe communication guide eklendi.
- Communication do/don't registry eklendi.
- Stakeholder update templates eklendi.
- Communication gap register ve risk summary eklendi.
- Briefing validation ve quality report eklendi.
- LocalBriefingPipeline eklendi.
- DataLake local briefing kayit destegi aldi.
- Local briefing scriptleri eklendi.
- Testler genisletildi.
""")

for doc in ["docs/OPERATOR_MANUAL.md", "docs/ANALYST_HANDBOOK.md", "docs/CODEX_AGENT_GUIDE.md", "docs/SAFE_USAGE_GUIDE.md", "docs/INSTALLATION.md", "docs/CONFIGURATION.md"]:
    append_to_file(doc, """
### Local Briefing
- Executive summary pack nasil okunur?
- Non-technical briefing deck source ne yapar/ne yapmaz?
- Decision-context binder nasil kullanilir?
- Safe communication guide neden onemlidir?
- Stakeholder templates nasil kullanilmali?
- Communication risks nasil yorumlanir?
- Yatirim tavsiyesi, canli emir, broker execution, deployment, production release ve resmi karar olmadigi acik yazilsin.
""")
