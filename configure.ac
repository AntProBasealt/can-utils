# -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
AC_PREREQ([2.59])

AC_INIT([can-utils],[trunk],[linux-can@vger.kernel.org])
AC_CONFIG_SRCDIR([lib.c])
AC_CONFIG_MACRO_DIR([config/m4])
AC_CONFIG_AUX_DIR([config/autoconf])
AC_CANONICAL_BUILD
AC_CANONICAL_HOST

# If possible, enable extensions to Posix
AC_USE_SYSTEM_EXTENSIONS

#AM_MAINTAINER_MODE

CFLAGS="${CFLAGS} -Wall"

#
# Checks for programs.
#
AC_PROG_CC
LT_INIT(win32-dll)

AM_INIT_AUTOMAKE([foreign no-exeext dist-bzip2 subdir-objects])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

#
# Checks for header files.
#
AC_CHECK_HEADERS([ \
	fcntl.h \
	limits.h \
	locale.h \
	stdint.h \
	stdlib.h \
	string.h \
	syslog.h \
	termios.h \
	unistd.h \
	\
	netinet/in.h \
	\
	sys/ioctl.h \
	sys/socket.h \
	sys/time.h \
])


#
# Checks for typedefs, structures, and compiler characteristics.
#
AC_C_INLINE
AC_SYS_LARGEFILE
AC_TYPE_OFF_T
AC_TYPE_PID_T
AC_TYPE_UINT64_T


#
# Checks for library functions.
#
AC_FUNC_FORK
AC_FUNC_MKTIME
AC_CHECK_FUNCS([ \
	alarm \
	gettimeofday \
	localtime_r \
	memset \
	select \
	setlocale \
	socket \
	strchr \
	strerror \
	strstr \
	strtoul \
])

AM_CONDITIONAL(HAVE_FORK, test "$ac_cv_func_fork_works" = "yes")

# glibc versions before 2.17 needs to link with -lrt for clock_nanosleep
AC_SEARCH_LIBS([clock_nanosleep], [rt])

AC_CHECK_DECL(SO_RXQ_OVFL,,
    [AC_DEFINE([SO_RXQ_OVFL], [40], [SO_RXQ_OVFL])],
    [[#include <linux/net.h>]]
)
AC_CHECK_DECL(PF_CAN,,
    [AC_DEFINE([PF_CAN], [29], [PF_CAN])],
    [[#include <net/if.h>]]
)
AC_CHECK_DECL(AF_CAN,,
    [AC_DEFINE([AF_CAN], [PF_CAN], [AF_CAN])],
    [[#include <net/if.h>]]
)
AC_CHECK_DECL(N_SLCAN,,
    [AC_DEFINE([N_SLCAN], [17], [N_SLCAN])],
    [[#include <linux/tty.h>]]
)
AC_CHECK_DECL(SCM_TIMESTAMPING_OPT_STATS,,
    [AC_DEFINE([SCM_TIMESTAMPING_OPT_STATS], [54], [SCM_TIMESTAMPING_OPT_STATS])],
    [[#include <linux/net.h>]]
)
AC_CHECK_DECL(CLOCK_TAI,,
    [AC_DEFINE([CLOCK_TAI], [11], [CLOCK_TAI])],
    [[#include <time.h>]]
)
AC_CHECK_DECL(SO_TXTIME,,
    [AC_DEFINE([SO_TXTIME], [61], [SO_TXTIME])],
    [[#include <sys/socket.h>]]
)
AC_CHECK_DECL(SCM_TXTIME,,
    [AC_DEFINE([SCM_TXTIME], [SO_TXTIME], [SCM_TXTIME])],
    [[#include <sys/socket.h>]]
)


#
# Debugging
#
AC_MSG_CHECKING([whether to enable debugging])
AC_ARG_ENABLE(debug,
    AS_HELP_STRING([--enable-debug], [enable debugging [[default=no]]]),
	[case "$enableval" in
	(y | yes) CONFIG_DEBUG=yes ;;
        (*) CONFIG_DEBUG=no ;;
    esac],
    [CONFIG_DEBUG=no])
AC_MSG_RESULT([${CONFIG_DEBUG}])
if test "${CONFIG_DEBUG}" = "yes"; then
    CFLAGS="${CFLAGS} -Wsign-compare -Wfloat-equal -Wformat-security -g -O1"
    AC_DEFINE(DEBUG, 1, [debugging])
else
    CFLAGS="${CFLAGS} -O2"
fi


AC_CONFIG_FILES([
	GNUmakefile
	])
AC_OUTPUT
