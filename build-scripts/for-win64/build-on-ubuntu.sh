#!/bin/bash

set -e

SRC_DIR=`dirname $0`/../..
PARALLEL_PRMS="-j$(nproc)"
DEBIAN_PKG_NAME=wxwidgets3.0-mingw-w64
VERSION=${1:-3.0.2}
BUILD_VERSION=${2:-0.go}
MINGW64_PREFIX=/usr/x86_64-w64-mingw32
PKG_DIR=`pwd`/build/win64/${DEBIAN_PKG_NAME}_${VERSION}-${BUILD_VERSION}_all


mkdir -p build/win64
rm -rf build/win64/*
cp -Rv $SRC_DIR/submodules/WxWidgets build/win64/src

pushd build/win64/src

patch -p1 <$SRC_DIR/patches/soversion.diff
patch -p1 <$SRC_DIR/patches/16849.diff
patch -p1 <$SRC_DIR/patches/16984-2.patch
patch -p0 <$SRC_DIR/patches/fix-msw-ConvertToImage-alpha.patch

export LIBPNG16_CONFIG=/usr/x86_64-w64-mingw32/bin/libpng16-config
export HOST_CC=gcc
export CC=x86_64-w64-mingw32-gcc
export CFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export CXX=x86_64-w64-mingw32-g++
export CXXFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export PKG_CONFIG_PATH="$MINGW64_PREFIX/lib/pkgconfig:$MINGW64_PREFIX/share/pkgconfig"
export LDFLAGS="-Wl,--exclude-libs=libintl.a -Wl,--exclude-libs=libiconv.a -Wl,--no-keep-memory -fstack-protector"

./configure --cache-file=mingw64-config.cache \
	--host=x86_64-w64-mingw32 \
	--build=x86_64-suse-linux-gnu \
	--target=x86_64-w64-mingw32 \
	--prefix=$MINGW64_PREFIX \
	--exec-prefix=$MINGW64_PREFIX \
	--bindir=$MINGW64_PREFIX/bin \
	--sbindir=$MINGW64_PREFIX/sbin \
	--sysconfdir=$MINGW64_PREFIX/etc \
	--datadir=$MINGW64_PREFIX/share \
	--includedir=$MINGW64_PREFIX/include \
	--libdir=$MINGW64_PREFIX/lib \
	--libexecdir=$MINGW64_PREFIX/libexec \
	--localstatedir=$MINGW64_PREFIX/var \
	--sharedstatedir=$MINGW64_PREFIX/com \
	--mandir=$MINGW64_PREFIX/share/man \
	--infodir=$MINGW64_PREFIX/share/info --enable-stl --enable-release --enable-debug --enable-accessibility \
	--enable-vendor=ubuntu

make $PARALLEL_PRMS

# install
MINGW_DIR=${PKG_DIR}${MINGW64_PREFIX}

make $PARALLEL_PRMS DESTDIR=${PKG_DIR} install
mkdir -p $MINGW_DIR/bin
mv -v $MINGW_DIR/lib/*.dll $MINGW_DIR/bin/
/usr/x86_64-w64-mingw32/bin/strip $MINGW_DIR/bin/*.dll

cd ..

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
