from pathlib import Path
import yaml
import pandas as pd

def load_config(config_path: str = "config.yml") -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    cfg = load_config()
    repo_root = Path(__file__).resolve().parent

    data_dir = repo_root / cfg["data_dir"]
    out_dir = repo_root / cfg["output_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)

    input_path = data_dir / cfg["input_file"]
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    print("Loaded:", input_path)
    print("Shape:", df.shape)
    print(df.head())

if __name__ == "__main__":
    main()
  
