#!/bin/sh
# SPDX-License-Identifier: GPL-2.0-only
# check_cc.sh - Helper to test userspace compilation support
# Copyright (c) 2015 Andrew Lutomirski

CC="$1"
TESTPROG="$2"
shift 2

if [ -n "$CC" ] && $CC -o /dev/null "$TESTPROG" -O0 "$@"; then
    echo 1
else
    echo 0
fi

exit 0
