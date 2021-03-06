from conans import ConanFile, CMake
import os


class TestConanPackage(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  generators = "cmake"

  def configure(self):
    del self.settings.compiler.libcxx

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def imports(self):
    self.copy("*.dll", dst="bin", src="bin")
    self.copy("*.dylib*", dst="bin", src="lib")

  def test(self):
    os.chdir("bin")
    self.run(".%stest_package" % os.sep)
