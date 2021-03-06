from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")

class EasyLoggingTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "easyloggingpp/9.94.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.cc")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
