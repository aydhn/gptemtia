from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any, List, Optional
from portable_packaging.packaging_models import EnvironmentSnapshot
from portable_packaging.packaging_config import PortablePackagingProfile

def build_reproducible_setup_steps(profile: PortablePackagingProfile) -> List[Dict[str, str]]:
    return [
        {"step": "1", "desc": "Sanal ortamı oluşturun (python -m venv venv)."},
        {"step": "2", "desc": "Requirements minimal veya frozen dosyasından kurulum yapın (pip install -r requirements_minimal.txt)."},
        {"step": "3", "desc": "Config template üzerinden kendi yapılandırmanızı oluşturun (cp .env.example .env)."},
        {"step": "4", "desc": "Install verification scriptini çalıştırın (python -m scripts.run_install_verification)."}
    ]

def build_install_troubleshooting_section(install_df: pd.DataFrame, dependency_df: pd.DataFrame) -> str:
    return "Eğer kurulumda sorun yaşarsanız missing module veya versiyon çakışmalarını kontrol edin."

def build_reproducible_setup_guide(snapshot: Optional[EnvironmentSnapshot], dependency_df: pd.DataFrame, install_df: pd.DataFrame, profile: PortablePackagingProfile) -> Tuple[str, Dict[str, Any]]:
    steps = build_reproducible_setup_steps(profile)
    steps_md = "\n".join([f"{s['step']}. {s['desc']}" for s in steps])
    troubleshooting = build_install_troubleshooting_section(install_df, dependency_df)

    md = f"""# Reproducible Setup Guide

## Amaç ve Kapsam
Bu rehber, projenin taşınabilir offline kopyasını kurmanızı sağlar.

## Güvenlik Sınırları
- Canlı emir, broker entegrasyonu, model deploy işlemleri YOKTUR.

## Setup Steps
{steps_md}

## Troubleshooting
{troubleshooting}
"""
    return md, {"steps": len(steps)}

def save_reproducible_setup_guide(text: str, output_path: Path) -> Path:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
