from devtools.repo_hygiene import check_required_files, check_required_directories, check_gitignore_hygiene, check_large_files, check_empty_init_files
from devtools.dev_config import get_default_dev_experience_profile

def test_repo_hygiene_checks(tmp_path):
    profile = get_default_dev_experience_profile()
    c1, _ = check_required_files(tmp_path, profile)
    assert len(c1) > 0

    c2, _ = check_required_directories(tmp_path)
    assert len(c2) > 0

    c3, _ = check_gitignore_hygiene(tmp_path)
    assert len(c3) > 0
