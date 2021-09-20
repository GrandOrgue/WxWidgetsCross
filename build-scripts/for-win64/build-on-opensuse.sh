#!/bin/sh

set -e

mkdir -p /home/runner/wx/build/win64
rm -rf /home/runner/wx/build/win64/*
cp -Rv /mnt/host/home/oleg/my-projects/wx/WxWidgetsCross/wxWidgets-3.0.2 /home/runner/wx/build/win64/

cd /home/runner/wx/build/win64/wxWidgets-3.0.2

export LIBPNG16_CONFIG=/usr/x86_64-w64-mingw32/sys-root/mingw/bin/libpng16-config
export HOST_CC=gcc
export CC=x86_64-w64-mingw32-gcc
export CFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export CXX=x86_64-w64-mingw32-g++
export CXXFLAGS="-O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields"
export PKG_CONFIG_PATH="/usr/x86_64-w64-mingw32/sys-root/mingw/lib/pkgconfig:/usr/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig"
export LDFLAGS="-Wl,--exclude-libs=libintl.a -Wl,--exclude-libs=libiconv.a -Wl,--no-keep-memory -fstack-protector"

  ./configure --cache-file=mingw64-config.cache \
	--host=x86_64-w64-mingw32 \
	--build=x86_64-suse-linux-gnu \
	--target=x86_64-w64-mingw32 \
	--prefix=/usr/x86_64-w64-mingw32/sys-root/mingw \
	--exec-prefix=/usr/x86_64-w64-mingw32/sys-root/mingw \
	--bindir=/usr/x86_64-w64-mingw32/sys-root/mingw/bin \
	--sbindir=/usr/x86_64-w64-mingw32/sys-root/mingw/sbin \
	--sysconfdir=/usr/x86_64-w64-mingw32/sys-root/mingw/etc \
	--datadir=/usr/x86_64-w64-mingw32/sys-root/mingw/share \
	--includedir=/usr/x86_64-w64-mingw32/sys-root/mingw/include \
	--libdir=/usr/x86_64-w64-mingw32/sys-root/mingw/lib \
	--libexecdir=/usr/x86_64-w64-mingw32/sys-root/mingw/libexec \
	--localstatedir=/usr/x86_64-w64-mingw32/sys-root/mingw/var \
	--sharedstatedir=/usr/x86_64-w64-mingw32/sys-root/mingw/com \
	--mandir=/usr/x86_64-w64-mingw32/sys-root/mingw/share/man \
	--infodir=/usr/x86_64-w64-mingw32/sys-root/mingw/share/info --enable-stl --enable-release --enable-debug --enable-accessibility \
	--enable-vendor=suse
make -j4
