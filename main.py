import time
from matlab_client_manager import init_matlab_client, close_matlab_client
from worker import do_work


def main():
    init_matlab_client()

    try:
        while True:
            time.sleep(2)
            print("working")
            do_work()
            print("-" * 40)
    finally:
        close_matlab_client()


if __name__ == "__main__":
    main()