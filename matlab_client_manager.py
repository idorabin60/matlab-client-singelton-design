from pathlib import Path
from matlab_client import MatlabClient

_client = None


def init_matlab_client():
    global _client

    if _client is None:
        base_dir = Path(__file__).resolve().parent
        matlab_code_dir = base_dir / "matlab_code"

        print("[manager] Initializing MATLAB client...")
        _client = MatlabClient(str(matlab_code_dir))
        print(f"[manager] MATLAB client initialized. object id = {id(_client)}")
    else:
        print(f"[manager] MATLAB client already exists. object id = {id(_client)}")

    return _client


def get_matlab_client():
    if _client is None:
        raise RuntimeError("MATLAB client was not initialized. Call init_matlab_client() first.")
    return _client


def close_matlab_client():
    global _client

    if _client is not None:
        print(f"[manager] Closing MATLAB client. object id = {id(_client)}")
        _client.close()
        _client = None