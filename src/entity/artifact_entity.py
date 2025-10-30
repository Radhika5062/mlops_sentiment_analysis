from dataclasses import dataclass
import pandas as pd

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str