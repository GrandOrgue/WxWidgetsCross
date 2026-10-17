#!/bin/sh

set -e

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
  patch file binutils autoconf automake libtool make pkg-config wget gettext

# the same posix mingw toolchain that GrandOrgue is built with
`dirname $0`/prepare-mingw.sh
