#!/bin/sh
rpm -ivh /mnt/host/home/oleg/my-projects/wx/WxWidgetsCross/mingw64-wxWidgets-3_0-3.0.2-12.996.src.rpm

sudo zypper addrepo http://download.opensuse.org/repositories/windows:mingw:win32/openSUSE_Tumbleweed/windows:mingw:win32.repo
sudo zypper addrepo http://download.opensuse.org/repositories/windows:mingw:win64/openSUSE_Tumbleweed/windows:mingw:win64.repo

sudo zypper install rpm-build

sudo zypper install autoconf automake libtool mingw64-cross-binutils mingw64-cross-gcc mingw64-cross-gcc-c++ mingw64-cross-pkg-config mingw64-filesystem mingw64-libexpat-devel mingw64-libjpeg-devel mingw64-libpng-devel mingw64-libtiff-devel


rpmbuild -bb /mnt/host/home/oleg/rpmbuild/SPECS/mingw64-wxWidgets-3_0.spec
