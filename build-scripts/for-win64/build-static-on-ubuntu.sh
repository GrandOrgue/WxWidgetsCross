#!/bin/bash

set -e

SRC_DIR=`dirname $0`/../..
PARALLEL_PRMS="-j$(nproc)"
DEBIAN_PKG_NAME=wxwidgets3-mingw-w64-static
VERSION=${1:-3.2.3}
BUILD_VERSION=${2:-0.go}
MINGW64_PREFIX=/usr/x86_64-w64-mingw32
PKG_DIR=`pwd`/build/win64/${DEBIAN_PKG_NAME}_${VERSION}-${BUILD_VERSION}_all


mkdir -p build/win64
rm -rf build/win64/*
cp -Rv $SRC_DIR/submodules/WxWidgets build/win64/src

pushd build/win64/src

./configure --host=x86_64-w64-mingw32 --prefix=$MINGW64_PREFIX --enable-unicode --disable-shared

make $PARALLEL_PRMS

# install
MINGW_DIR=${PKG_DIR}${MINGW64_PREFIX}
mkdir -p $MINGW_DIR/bin # otherwise make install works incorrectly
make $PARALLEL_PRMS DESTDIR=${PKG_DIR} install

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
