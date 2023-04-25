"# ReconhecimentoDeFacesObjetos" 
Preparation
First thing first, there are two things required (really need it indeed!).

CMake: This is because dlib was developed in C based programming language, so it needs this program to use it. It can be found in the link https://cmake.org/download/. To make sure matching with your operation system, in our case is Windows 10 64-bit version.

Visual studio: As I mentioned before, dlib is C based programming language. Another thing that really need is compiler. The Visual studio can be downloaded in the link https://visualstudio.microsoft.com/visual-cpp-build-tools/. After finishing the installation, you need to install additional packages for C, C++ programming, which is Packages CMake tools for Windows

Note
Sometimes we need manage the Windows PATH environment for CMake. (If you already added during installation, you can skip this section).

For checking whether the PATH already added or not, you can go to Environment Variables on Windows by go to This PC > Properties > Advance system settings. Then, go to Tab Advanced and click on Environment Variables.

Another windows will pop-up and click Edit…

If you are unable to find CMake path, you should add the CMake installed directory like image below.