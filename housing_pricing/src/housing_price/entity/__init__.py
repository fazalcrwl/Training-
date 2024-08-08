from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_path:Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    


from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataPretrainingConfig:
        root_dir: Path
        unzip_dir: Path
        pretrainn_data: Path


from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DatatrainingConfig:
        root_dir: Path
        pretrainn_data: Path
        model_save:Path


from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class PredictConfig:
        root_dir: Path
        model_save:Path