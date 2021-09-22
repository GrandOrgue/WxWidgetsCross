#!/bin/bash

set -e

SRC_DIR=`dirname $0`/../..
PARALLEL_PRMS="-j$(nproc)"

mkdir -p build/win64
rm -rf build/win64/*
cp -Rv $SRC_DIR/wxWidgets-3.0.2 build/win64/src

DEBIAN_PKG_NAME=wxwidgets-mingw-w64
VERSION=${1:-3.0.2}
BUILD_VERSION=${2:-0.os}
MINGW64_PREFIX=/usr/x86_64-w64-mingw32
PKG_DIR=`readlink -f build/win64/${DEBIAN_PKG_NAME}_${VERSION}-${BUILD_VERSION}_all`

pushd build/win64/src

export LIBPNG16_CONFIG=/usr/x86_64-w64-mingw32/bin/libpng16-config
export HOST_CC=gcc
export CC=x86_64-w64-mingw32-gcc
export CFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export CXX=x86_64-w64-mingw32-g++
export CXXFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export PKG_CONFIG_PATH="/usr/x86_64-w64-mingw32/lib/pkgconfig:/usr/x86_64-w64-mingw32/share/pkgconfig"
export LDFLAGS="-Wl,--exclude-libs=libintl.a -Wl,--exclude-libs=libiconv.a -Wl,--no-keep-memory -fstack-protector"

./configure --cache-file=mingw64-config.cache \
	--host=x86_64-w64-mingw32 \
	--build=x86_64-suse-linux-gnu \
	--target=x86_64-w64-mingw32 \
	--prefix=/usr/x86_64-w64-mingw32 \
	--exec-prefix=/usr/x86_64-w64-mingw32 \
	--bindir=/usr/x86_64-w64-mingw32/bin \
	--sbindir=/usr/x86_64-w64-mingw32/sbin \
	--sysconfdir=/usr/x86_64-w64-mingw32/etc \
	--datadir=/usr/x86_64-w64-mingw32/share \
	--includedir=/usr/x86_64-w64-mingw32/include \
	--libdir=/usr/x86_64-w64-mingw32/lib \
	--libexecdir=/usr/x86_64-w64-mingw32/libexec \
	--localstatedir=/usr/x86_64-w64-mingw32/var \
	--sharedstatedir=/usr/x86_64-w64-mingw32/com \
	--mandir=/usr/x86_64-w64-mingw32/share/man \
	--infodir=/usr/x86_64-w64-mingw32/share/info --enable-stl --enable-release --enable-debug --enable-accessibility \
	--enable-vendor=ubuntu

make $PARALLEL_PRMS

# install
MINGW_DIR=${PKG_DIR}${MINGW64_PREFIX}

make $PARALLEL_PRMS DESTDIR=${PKG_DIR} install
mkdir -p $MINGW_DIR/bin
mv -v $MINGW_DIR/lib/*.dll $MINGW_DIR/bin/

mkdir $PKG_DIR/DEBIAN

cat >$PKG_DIR/DEBIAN/control <<EOF
Package: $DEBIAN_PKG_NAME
Version: $VERSION-$BUILD_VERSION
Architecture: all
Maintainer: Oleg Samarin <osamarin68@gmail.com>
Description: Everything needed for development with wxWidgets/wxMSW
EOF

dpkg-deb --build --root-owner-group $PKG_DIR

popd
