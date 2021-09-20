#!/bin/sh

set -e

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  g++-mingw-w64-x86-64 gcc-mingw-w64-x86-64 pkg-config-mingw-w64-x86-64 file binutils \
  autoconf automake libtool binutils-mingw-w64-x86-64 make


sudo zypper install -y mingw64-filesystem mingw64-libexpat-devel mingw64-libjpeg-devel mingw64-libpng-devel mingw64-libtiff-devel

