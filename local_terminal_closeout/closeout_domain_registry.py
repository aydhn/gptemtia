import pandas as pd
from .closeout_models import TerminalCloseoutDomain
from .__init__ import get_warning

def create_domain_registry() -> pd.DataFrame:
    df = pd.DataFrame(columns=["domain_id", "domain_label", "domain_name", "description", "required_outputs", "warnings"])
    return df
