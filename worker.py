import time
from matlab_client_manager import get_matlab_client


def do_work():
    client = get_matlab_client()

    print(f"[worker] Using MATLAB client object id = {id(client)}")

    start = time.perf_counter()
    result = client.add_numbers(5, 7)
    end = time.perf_counter()

    print(f"[worker] result = {result}")
    print(f"[worker] call took = {(end - start):.6f} seconds")
    return result