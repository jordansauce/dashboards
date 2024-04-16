import fire
import glob
from pathlib import Path
import json
from natsort import natsorted
from sparsify.data import DatasetConfig
from sparsify.scripts.generate_dashboards import DashboardsConfig
from sparsify.scripts.generate_dashboards import main as generate_dashboards
from sparsify.utils import load_config

def main(json_filename: str | Path):
    """Read in a json file containing a list of interesing features for some interesting SAEs, and make dashboards for them"""
    with open(json_filename, "r") as read_file:
        region_data = json.load(read_file)

    dataset_config = DatasetConfig(
        dataset_name = 'apollo-research/Skylion007-openwebtext-tokenizer-gpt2',
        is_tokenized = True,
        tokenizer_name = 'gpt2',
        split = "train",
        n_ctx = 1024
    )

    for run in region_data["run_labels"]:
        run_type, run_id = run.split("-")
        # Get the .pt file of the SAE from the run_id
        run_sae_path = Path((natsorted(glob.glob(f"../*{run_id}/*.pt"))[-1])).resolve()
        print(f'run_sae_path = {run_sae_path}')
        # Get the relevant feature indices
        feature_inds = region_data[run_type]
        save_dir = Path(__file__).parent.resolve() / Path(json_filename.replace('.json','') + '_' + run + '_' + region_data["description"].replace(' ','_'))
        save_dir.mkdir(parents=True, exist_ok=True)

        dashbaords_config = DashboardsConfig(
            pretrained_sae_paths = run_sae_path,
            sae_config_path = run_sae_path.parent / Path("config.yaml"),
            n_samples = 5000,
            batch_size = 16, 
            minibatch_size_features = 50,
            data = dataset_config,
            save_dir = save_dir,
            save_json_data = False,
            feature_indices = feature_inds,
            prompt_centric = None,
            seed = 0
        )
        # Generate the dashboards for the relevant features
        generate_dashboards(dashbaords_config, run_sae_path)

if __name__ == "__main__":
    fire.Fire(main)