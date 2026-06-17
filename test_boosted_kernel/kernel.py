from metakernel import MetaKernel


class TestKernel(MetaKernel):
    implementation = "test"
    implementation_version = "1.0"
    language = "no-op"
    help_suffix = "?"
    language_version = "0.1"
    language_info = {
        "name": "plop",
        "mimetype": "text/plain",
        "file_extension": ".plop",
    }
    banner = "Test Boosted Magics"
    app_name = "test"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
