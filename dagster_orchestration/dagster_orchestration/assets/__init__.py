import os
from dagster_dbt import DbtCliClientResource
from dagster_dbt import load_assets_from_dbt_project

resources = {
    "dbt": DbtCliClientResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR"),
    ),
}

dbt_assets = load_assets_from_dbt_project(
    project_dir=os.getenv("DBT_PROJECT_DIR"), profiles_dir=os.getenv("DBT_PROFILES_DIR"), key_prefix=["transformed_data"]
)

# dagster_orchestration/dagster_orchestration/__init__.py

from dagster import Definitions, load_assets_from_modules

from .assets import resources

defs = Definitions(assets=load_assets_from_modules(
    [assets]), resources=resources)