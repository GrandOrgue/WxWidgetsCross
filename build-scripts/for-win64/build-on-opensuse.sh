#!/bin/sh

set -e

mkdir -p /home/runner/wx/build/win64
rm -rf /home/runner/wx/build/win64/*
cp -Rv /mnt/host/home/oleg/my-projects/wx/WxWidgetsCross/wxWidgets-3.0.2 /home/runner/wx/build/win64/

 RPM_SOURCE_DIR="/home/runner/rpmbuild/SOURCES"
  RPM_BUILD_DIR="/home/runner/rpmbuild/BUILD"
  RPM_OPT_FLAGS="-O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables"
  RPM_ARCH="x86_64"
  RPM_OS="linux"
  RPM_BUILD_NCPUS="4"
  export RPM_SOURCE_DIR RPM_BUILD_DIR RPM_OPT_FLAGS RPM_ARCH RPM_OS RPM_BUILD_NCPUS
  RPM_DOC_DIR="/usr/share/doc/packages"
  export RPM_DOC_DIR
  RPM_PACKAGE_NAME="mingw64-wxWidgets-3_0"
  RPM_PACKAGE_VERSION="3.0.2"
  RPM_PACKAGE_RELEASE="12.996"
  export RPM_PACKAGE_NAME RPM_PACKAGE_VERSION RPM_PACKAGE_RELEASE
  LANG=C
  export LANG
  unset CDPATH DISPLAY ||:
  RPM_BUILD_ROOT="/home/runner/rpmbuild/BUILDROOT/mingw64-wxWidgets-3_0-3.0.2-12.996.x86_64"
  export RPM_BUILD_ROOT
  
  PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/usr/lib64/pkgconfig:/usr/share/pkgconfig"
  export PKG_CONFIG_PATH
  
  set -x
  umask 022
  cd "/home/runner/wx/build/win64/wxWidgets-3.0.2"
  /usr/bin/rm -rf "$RPM_BUILD_ROOT"
  /usr/bin/mkdir -p `dirname "$RPM_BUILD_ROOT"`
  /usr/bin/mkdir "$RPM_BUILD_ROOT"

HOST_CC=gcc; export HOST_CC; 
  PKG_CONFIG_PATH="/usr/x86_64-w64-mingw32/sys-root/mingw/lib/pkgconfig:/usr/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig"; export PKG_CONFIG_PATH; 
  CLASSPATH="$CLASSPATH:${MINGW64_CLASSPATH:-/usr/x86_64-w64-mingw32/sys-root/mingw/share/java/libgcj.jar:/usr/x86_64-w64-mingw32/sys-root/mingw/share/java/libgcj-tools.jar}"; export CLASSPATH; 
  _PREFIX="/usr/bin/x86_64-w64-mingw32-"; 
  for i in `ls -1 ${_PREFIX}* | grep -v 'gcc-'`; do 
    x=`echo $i|sed "s,${_PREFIX},,"|sed "s,\.awk*,,"|tr [:lower:] [:upper:] | tr "+-" "X_" | sed "s,\.,,g"`; 
    declare -x $x="$i" ; export $x; 
  done; 
  unset _PREFIX; 
  CC="${MINGW64_CC:-x86_64-w64-mingw32-gcc}"; export CC; 
  CFLAGS="${MINGW64_CFLAGS:--O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields}"; export CFLAGS; 
  LDFLAGS="${MINGW64_LDFLAGS:--Wl,--exclude-libs=libintl.a -Wl,--exclude-libs=libiconv.a -Wl,--no-keep-memory -fstack-protector}"; export LDFLAGS; 
  if [ -x "/usr/bin/x86_64-w64-mingw32-g++" ]; then 
    CXX="${MINGW64_CXX:-x86_64-w64-mingw32-g++}"; export CXX; 
    CXXFLAGS="${MINGW64_CXXFLAGS:--O2 -g -pipe -Wall -fexceptions --param=ssp-buffer-size=4 -mms-bitfields}"; export CXXFLAGS; 
  else 
    CXX=; export CXX; 
    ac_cv_prog_CXX=no; export ac_cv_prog_CXX; 
    CXXFLAGS=; export CXXFLAGS; 
  fi; 
  for i in `ls /usr/x86_64-w64-mingw32/sys-root/mingw/bin/*|grep -- "-config$"` ; do 
    x=`basename $i|tr [:lower:] [:upper:] | tr "+-" "X_" | sed "s,\.,,g"`; 
    declare -x $x="$i" ; export $x; 
  done; 
  unset x i ; 
  __mingw64_topdir=.; if ! test -x configure; then __mingw64_topdir=..; fi; \
  $__mingw64_topdir/configure --cache-file=mingw64-config.cache \
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
