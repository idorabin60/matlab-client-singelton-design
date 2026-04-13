import time
from pathlib import Path
import matlab.engine


class MatlabClient:
    def __init__(self, matlab_code_dir: str):
        start = time.perf_counter()

        print("Starting MATLAB engine...")
        self.engine = matlab.engine.start_matlab()

        matlab_path = str(Path(matlab_code_dir).resolve())
        self.engine.addpath(matlab_path, nargout=0)

        end = time.perf_counter()
        self.startup_time = end - start

        print("MATLAB engine started successfully.")
        print(f"MATLAB path added: {matlab_path}")
        print(f"MATLAB startup took {self.startup_time:.3f} seconds")

    def add_numbers(self, a: float, b: float):
        return self.engine.add_numbers(a, b)

    def close(self):
        if self.engine:
            self.engine.quit()
            print("MATLAB engine closed.")