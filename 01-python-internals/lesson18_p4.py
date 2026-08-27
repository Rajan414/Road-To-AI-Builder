# context manager
class Demo:
    def __enter__(self):
        print("Rajan Dai")

    def __exit__(self, exc_type, exc_value, tb):
        print("Completed")


with Demo():
    print("Jai Rajan")