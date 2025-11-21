import os
import yaml
import mysql.connector


def _load_db_config():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    config_path = os.path.join(root_dir, "config", "app.yml")

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    return cfg["db"]


def get_connection():
    db_cfg = _load_db_config()
    return mysql.connector.connect(
        host=db_cfg["host"],
        port=db_cfg.get("port", 3306),
        user=db_cfg["user"],
        password=db_cfg["password"],
        database=db_cfg["database"],
    )