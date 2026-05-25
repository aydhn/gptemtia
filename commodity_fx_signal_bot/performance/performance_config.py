from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class PerformanceProfile:
    name: str
    description: str
    profile_scripts: bool = True
    profile_memory: bool = True
    profile_cpu: bool = True
    detect_gpu: bool = True
    allow_gpu_optional: bool = True
    max_runtime_seconds_per_script: int = 300
    max_memory_mb_per_script: int = 2048
    max_batch_symbols: int = 50
    max_parallel_workers: int = 1
    enable_cache: bool = True
    cache_format: str = "parquet_or_csv"
    cache_ttl_hours: int = 24
    cache_max_size_mb: int = 2048
    enable_checkpointing: bool = True
    checkpoint_every_items: int = 25
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def _build_default_profiles() -> dict[str, PerformanceProfile]:
    return {
        "balanced_local_performance": PerformanceProfile(
            name="balanced_local_performance",
            description="Balanced profile for average local computer",
            max_runtime_seconds_per_script=300,
            max_memory_mb_per_script=2048,
            max_batch_symbols=50,
            max_parallel_workers=1,
            enable_cache=True,
            cache_ttl_hours=24,
            checkpoint_every_items=25,
            notes="Ortalama yerel bilgisayar için güvenli offline performans profili."
        ),
        "low_resource_performance": PerformanceProfile(
            name="low_resource_performance",
            description="Profile for low RAM/CPU systems",
            max_runtime_seconds_per_script=180,
            max_memory_mb_per_script=1024,
            max_batch_symbols=20,
            max_parallel_workers=1,
            cache_max_size_mb=1024,
            checkpoint_every_items=10,
            notes="Daha düşük RAM/CPU için kontrollü çalışma profili."
        ),
        "gpu_aware_local_performance": PerformanceProfile(
            name="gpu_aware_local_performance",
            description="Profile aware of GPU but not requiring it",
            detect_gpu=True,
            allow_gpu_optional=True,
            max_runtime_seconds_per_script=600,
            max_memory_mb_per_script=4096,
            max_batch_symbols=100,
            max_parallel_workers=1,
            notes="Nvidia GPU mevcutsa farkındalık raporu üretir; GPU zorunlu değildir."
        ),
        "large_research_run_performance": PerformanceProfile(
            name="large_research_run_performance",
            description="Profile for large offline research runs",
            max_runtime_seconds_per_script=900,
            max_memory_mb_per_script=4096,
            max_batch_symbols=200,
            max_parallel_workers=1,
            cache_max_size_mb=4096,
            checkpoint_every_items=25,
            notes="Büyük offline araştırma koşuları için batch, checkpoint ve cache odaklı profil."
        ),
    }

_PROFILES = _build_default_profiles()

def get_performance_profile(name: str) -> PerformanceProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown performance profile: {name}")
    return _PROFILES[name]

def list_performance_profiles(enabled_only: bool = True) -> List[PerformanceProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_performance_profiles() -> None:
    for profile in _PROFILES.values():
        if profile.max_runtime_seconds_per_script <= 0:
            raise ValueError(f"Profile {profile.name} max_runtime_seconds_per_script must be positive.")
        if profile.max_memory_mb_per_script <= 0:
            raise ValueError(f"Profile {profile.name} max_memory_mb_per_script must be positive.")
        if profile.max_batch_symbols <= 0:
            raise ValueError(f"Profile {profile.name} max_batch_symbols must be positive.")
        if profile.max_parallel_workers < 1:
            raise ValueError(f"Profile {profile.name} max_parallel_workers must be >= 1.")
        if profile.cache_ttl_hours <= 0:
            raise ValueError(f"Profile {profile.name} cache_ttl_hours must be positive.")
        if profile.cache_max_size_mb <= 0:
            raise ValueError(f"Profile {profile.name} cache_max_size_mb must be positive.")
        if profile.checkpoint_every_items <= 0:
            raise ValueError(f"Profile {profile.name} checkpoint_every_items must be positive.")
        if not 0.0 <= profile.min_quality_score <= 1.0:
            raise ValueError(f"Profile {profile.name} min_quality_score must be between 0.0 and 1.0.")

def get_default_performance_profile() -> PerformanceProfile:
    return get_performance_profile("balanced_local_performance")
