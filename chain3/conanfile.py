from conan import ConanFile


class ChainConan(ConanFile):
    name = "nothing"
    version = "1.0.0"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    options = { "with_vulkan": [True, False] }
    default_options = { "with_vulkan": False }

    def configure(self):
        self.options["qt/*"].with_vulkan = self.options.with_vulkan
        self.options["qt/*"].shared = True

    def requirements(self):
        self.requires("qt/[>=5.15 <6]")  # Conflicts with libpng
        self.requires("libpng/1.6.40", override=True)
