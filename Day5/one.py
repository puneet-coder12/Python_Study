class MyResource:

    def __enter__(self):
        print("Opening resource...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing resource...")


with MyResource() as resource:
    print("Resource is being used...")