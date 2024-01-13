# Data Ingestion Entity
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE: Path
    required_files: list
    data_path: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    preprocessor_path: Path
    data_path: Path
    train_path: Path
    test_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    train_path: Path 