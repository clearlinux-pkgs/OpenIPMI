#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : OpenIPMI
Version  : 2.0.32
Release  : 41
URL      : https://sourceforge.net/projects/openipmi/files/OpenIPMI%202.0%20Library/OpenIPMI-2.0.32.tar.gz
Source0  : https://sourceforge.net/projects/openipmi/files/OpenIPMI%202.0%20Library/OpenIPMI-2.0.32.tar.gz
Summary  : %{name} - Library interface to IPMI
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: OpenIPMI-bin = %{version}-%{release}
Requires: OpenIPMI-lib = %{version}-%{release}
Requires: OpenIPMI-license = %{version}-%{release}
Requires: OpenIPMI-man = %{version}-%{release}
Requires: OpenIPMI-python = %{version}-%{release}
Requires: OpenIPMI-python3 = %{version}-%{release}
BuildRequires : gdbm-dev
BuildRequires : pkgconfig(libedit)
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : swig
BuildRequires : tcl
BuildRequires : texlive
Patch1: 0001-Update-for-python-3.10.patch

%description
This is the OpenIPMI library, a library that makes simplifies building
complex IPMI management software.

%package bin
Summary: bin components for the OpenIPMI package.
Group: Binaries
Requires: OpenIPMI-license = %{version}-%{release}

%description bin
bin components for the OpenIPMI package.


%package dev
Summary: dev components for the OpenIPMI package.
Group: Development
Requires: OpenIPMI-lib = %{version}-%{release}
Requires: OpenIPMI-bin = %{version}-%{release}
Provides: OpenIPMI-devel = %{version}-%{release}
Requires: OpenIPMI = %{version}-%{release}

%description dev
dev components for the OpenIPMI package.


%package lib
Summary: lib components for the OpenIPMI package.
Group: Libraries
Requires: OpenIPMI-license = %{version}-%{release}

%description lib
lib components for the OpenIPMI package.


%package license
Summary: license components for the OpenIPMI package.
Group: Default

%description license
license components for the OpenIPMI package.


%package man
Summary: man components for the OpenIPMI package.
Group: Default

%description man
man components for the OpenIPMI package.


%package python
Summary: python components for the OpenIPMI package.
Group: Default
Requires: OpenIPMI-python3 = %{version}-%{release}
Provides: openipmi-python

%description python
python components for the OpenIPMI package.


%package python3
Summary: python3 components for the OpenIPMI package.
Group: Default
Requires: python3-core

%description python3
python3 components for the OpenIPMI package.


%prep
%setup -q -n OpenIPMI-2.0.32
cd %{_builddir}/OpenIPMI-2.0.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666821051
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static --with-perl=no
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1666821051
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/OpenIPMI
cp %{_builddir}/OpenIPMI-%{version}/COPYING %{buildroot}/usr/share/package-licenses/OpenIPMI/dfac199a7539a404407098a2541b9482279f690d || :
cp %{_builddir}/OpenIPMI-%{version}/COPYING.BSD %{buildroot}/usr/share/package-licenses/OpenIPMI/6041dfa4b268e7399d2c7e18c644cb291982028a || :
cp %{_builddir}/OpenIPMI-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/OpenIPMI/cf756914ec51f52f9c121be247bfda232dc6afd2 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipmi_sim
/usr/bin/ipmi_ui
/usr/bin/ipmicmd
/usr/bin/ipmilan
/usr/bin/ipmish
/usr/bin/openipmi_eventd
/usr/bin/openipmicmd
/usr/bin/openipmish
/usr/bin/rmcp_ping
/usr/bin/sdrcomp
/usr/bin/solterm

%files dev
%defattr(-,root,root,-)
/usr/include/OpenIPMI/deprecator.h
/usr/include/OpenIPMI/dllvisibility.h
/usr/include/OpenIPMI/extcmd.h
/usr/include/OpenIPMI/internal/ilist.h
/usr/include/OpenIPMI/internal/ipmi_control.h
/usr/include/OpenIPMI/internal/ipmi_domain.h
/usr/include/OpenIPMI/internal/ipmi_entity.h
/usr/include/OpenIPMI/internal/ipmi_event.h
/usr/include/OpenIPMI/internal/ipmi_fru.h
/usr/include/OpenIPMI/internal/ipmi_int.h
/usr/include/OpenIPMI/internal/ipmi_locks.h
/usr/include/OpenIPMI/internal/ipmi_malloc.h
/usr/include/OpenIPMI/internal/ipmi_mc.h
/usr/include/OpenIPMI/internal/ipmi_oem.h
/usr/include/OpenIPMI/internal/ipmi_sel.h
/usr/include/OpenIPMI/internal/ipmi_sensor.h
/usr/include/OpenIPMI/internal/ipmi_utils.h
/usr/include/OpenIPMI/internal/locked_list.h
/usr/include/OpenIPMI/internal/md2.h
/usr/include/OpenIPMI/internal/md5.h
/usr/include/OpenIPMI/internal/opq.h
/usr/include/OpenIPMI/internal/winsock_compat.h
/usr/include/OpenIPMI/ipmbserv.h
/usr/include/OpenIPMI/ipmi_addr.h
/usr/include/OpenIPMI/ipmi_auth.h
/usr/include/OpenIPMI/ipmi_bits.h
/usr/include/OpenIPMI/ipmi_cmdlang.h
/usr/include/OpenIPMI/ipmi_conn.h
/usr/include/OpenIPMI/ipmi_debug.h
/usr/include/OpenIPMI/ipmi_err.h
/usr/include/OpenIPMI/ipmi_fru.h
/usr/include/OpenIPMI/ipmi_glib.h
/usr/include/OpenIPMI/ipmi_lan.h
/usr/include/OpenIPMI/ipmi_lanparm.h
/usr/include/OpenIPMI/ipmi_log.h
/usr/include/OpenIPMI/ipmi_mc.h
/usr/include/OpenIPMI/ipmi_msgbits.h
/usr/include/OpenIPMI/ipmi_pef.h
/usr/include/OpenIPMI/ipmi_pet.h
/usr/include/OpenIPMI/ipmi_picmg.h
/usr/include/OpenIPMI/ipmi_posix.h
/usr/include/OpenIPMI/ipmi_sdr.h
/usr/include/OpenIPMI/ipmi_smi.h
/usr/include/OpenIPMI/ipmi_sol.h
/usr/include/OpenIPMI/ipmi_solparm.h
/usr/include/OpenIPMI/ipmi_string.h
/usr/include/OpenIPMI/ipmi_tcl.h
/usr/include/OpenIPMI/ipmi_types.h
/usr/include/OpenIPMI/ipmi_ui.h
/usr/include/OpenIPMI/ipmi_user.h
/usr/include/OpenIPMI/ipmiif.h
/usr/include/OpenIPMI/lanserv.h
/usr/include/OpenIPMI/lanserv_dllvisibility.h
/usr/include/OpenIPMI/mcserv.h
/usr/include/OpenIPMI/msg.h
/usr/include/OpenIPMI/mxp.h
/usr/include/OpenIPMI/os_handler.h
/usr/include/OpenIPMI/persist.h
/usr/include/OpenIPMI/selector.h
/usr/include/OpenIPMI/serserv.h
/usr/include/OpenIPMI/serv.h
/usr/lib64/libIPMIlanserv.so
/usr/lib64/libOpenIPMI.so
/usr/lib64/libOpenIPMIcmdlang.so
/usr/lib64/libOpenIPMIposix.so
/usr/lib64/libOpenIPMIpthread.so
/usr/lib64/libOpenIPMIui.so
/usr/lib64/libOpenIPMIutils.so
/usr/lib64/pkgconfig/OpenIPMI.pc
/usr/lib64/pkgconfig/OpenIPMIcmdlang.pc
/usr/lib64/pkgconfig/OpenIPMIposix.pc
/usr/lib64/pkgconfig/OpenIPMIpthread.pc
/usr/lib64/pkgconfig/OpenIPMIui.pc
/usr/lib64/pkgconfig/OpenIPMIutils.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libIPMIlanserv.so.0
/usr/lib64/libIPMIlanserv.so.0.0.1
/usr/lib64/libOpenIPMI.so.0
/usr/lib64/libOpenIPMI.so.0.0.5
/usr/lib64/libOpenIPMIcmdlang.so.0
/usr/lib64/libOpenIPMIcmdlang.so.0.0.5
/usr/lib64/libOpenIPMIposix.so.0
/usr/lib64/libOpenIPMIposix.so.0.0.1
/usr/lib64/libOpenIPMIpthread.so.0
/usr/lib64/libOpenIPMIpthread.so.0.0.1
/usr/lib64/libOpenIPMIui.so.1
/usr/lib64/libOpenIPMIui.so.1.0.1
/usr/lib64/libOpenIPMIutils.so.0
/usr/lib64/libOpenIPMIutils.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/OpenIPMI/6041dfa4b268e7399d2c7e18c644cb291982028a
/usr/share/package-licenses/OpenIPMI/cf756914ec51f52f9c121be247bfda232dc6afd2
/usr/share/package-licenses/OpenIPMI/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipmi_sim.1
/usr/share/man/man1/ipmi_ui.1
/usr/share/man/man1/openipmi_eventd.1
/usr/share/man/man1/openipmicmd.1
/usr/share/man/man1/openipmigui.1
/usr/share/man/man1/openipmish.1
/usr/share/man/man1/rmcp_ping.1
/usr/share/man/man1/solterm.1
/usr/share/man/man5/ipmi_lan.5
/usr/share/man/man5/ipmi_sim_cmd.5
/usr/share/man/man7/ipmi_cmdlang.7
/usr/share/man/man7/openipmi_conparms.7
/usr/share/man/man8/ipmilan.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
