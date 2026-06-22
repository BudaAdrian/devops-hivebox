MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH_VERSION = 2

def get_version():
    return f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"

if __name__ == "__main__":
    print("Starting Hivebox v " + get_version())