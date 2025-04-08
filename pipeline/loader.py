import yaml

def load_pipeline_config(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data.get("pipeline", [])