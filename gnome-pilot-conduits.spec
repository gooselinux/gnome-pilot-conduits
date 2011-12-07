%define gnome_pilot_version 2.0.17

### Abstract ###

Name: gnome-pilot-conduits
Version: 2.0.17
Release: 4%{?dist}
License: GPLv2+ and MPLv1.0
Group: Applications/Communications
Summary: Additional conduits for gnome-pilot
URL: http://live.gnome.org/GnomePilot
BuildRoot: %{_tmppath}/%{name}-%{version}
Source: http://download.gnome.org/source/%{name}/2.0/%{name}-%{version}.tar.bz2
ExcludeArch: s390 s390x

### Dependencies ###

Requires: gnome-pilot >= %{gnome_pilot_version}

### Build Dependencies ###

BuildRequires: gettext
BuildRequires: gnome-pilot-devel >= %{gnome_pilot_version}
BuildRequires: libtool

%description
gnome-pilot is a collection of programs and daemon for integrating
GNOME and the PalmPilot<tm>.

This is a collection of additional conduits for gnome-pilot, it
currently features
 - MAL conduit
 - Time synchronization conduit
 - Email conduit
 - Expense conduit
 - Memo file conduit

%prep
%setup -q

%build
%configure
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
%makeinstall LIBTOOL=/usr/bin/libtool

mv $RPM_BUILD_ROOT/%{_datadir}/gnome-pilot/conduits/*.conduit \
   $RPM_BUILD_ROOT/%{_libdir}/gnome-pilot/conduits

rm -f $RPM_BUILD_ROOT/%{_libdir}/gnome-pilot/conduits/*.{la,a}
rm -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/avantgo.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/gnome-pilot/conduits/*.conduit
%{_libdir}/gnome-pilot/conduits/*.so

%changelog
* Thu Jan 14 2010 Matthew Barnes <mbarnes@redhat.com> - 2.0.17-4
- Fix rpmlint warnings.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.17-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Matthew Barnes <mbarnes@redhat.com> - 2.0.17-1
- Update to 2.0.17
- Bump gnome_pilot_version to 2.0.17.

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.16-2
- fix license tag

* Tue Feb 26 2008 Matthew Barnes <mbarnes@redhat.com> - 2.0.16-1.fc9
- Update to 2.0.16

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-6.fc9
- Rebuild with GCC 4.3

* Fri Nov 23 2007 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-5.fc9
- Rebuild against newer libpisync.so.

* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-4.fc8
- Rebuild

* Sat Dec 30 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-3.fc7
- Remove Prereq: /sbin/install-info (RH bug #220520).

* Mon Nov 27 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-2.fc7
- Rebuild against pilot-link 0.12.

* Fri Nov 24 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.15-1.fc7
- Update to 2.0.15

* Mon Nov  6 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.14-2.fc7
- Move conduit files under $(libdir) (RH bug #189369).

* Sun Nov  5 2006 Matthew Barnes <mbarnes@redhat.com> - 2.0.14-1.fc7
- Update to 2.0.14
- Remove patches fixed upstream:
	gnome-pilot-conduits-2.0.10-lib64.patch
	gnome-pilot-conduits-2.0.13-port-to-pilot-link-0.12.patch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.13-6.1
- rebuild

* Thu Jun 08 2006 Jesse Keating <jkeating@redhat.com> 2.0.13-6
- Add missing BR gettext, libtool

* Wed Mar 29 2006 Than Ngo <than@redhat.com> 2.0.13-4 
- rebuilt against pilot-link-0.11.8
- don't apply gnome-pilot-conduits-2.0.13-port-to-pilot-link-0.12.patch

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.13-3.FC5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.13-3.FC5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 11 2006 David Malcolm <dmalcolm@redhat.com> - 2.0.13-3.FC5
- extend patch 2 to handle a missing fix in the email conduit, renaming it from
  gnome-pilot-conduits-2.0.12-port-to-pilot-link-0.12.patch to
  gnome-pilot-conduits-2.0.13-port-to-pilot-link-0.12.patch in the process 
  (#159165) 

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 24 2005 David Malcolm <dmalcolm@redhat.com> - 2.0.13-2.FC5
- fixed gnome_pilot_version macro so that it is correctly substituted at build
  time (#169276)

* Mon Apr 11 2005 David Malcolm <dmalcolm@redhat.com> - 2.0.13-1
- 2.0.13
- require gnome-pilot 2.0.13
- Removed warning-fix patch (now upstream)

* Tue Mar 15 2005 David Malcolm <dmalcolm@redhat.com> - 2.0.12-5
- added patch to get it to build against pilot-link-0.12 API

* Mon Mar 14 2005 David Malcolm <dmalcolm@redhat.com> - 2.0.12-4
- rebuilt against pilot-link-0.12

* Tue Sep 21 2004 David Malcolm <dmalcolm@redhat.com> - 2.0.12-3
- added fix for compile-time warnings (bugzilla 114282)

* Mon Sep 20 2004 David Malcolm <dmalcolm@redhat.com>
- rebuilt

* Wed Sep 15 2004 David Malcolm <dmalcolm@redhat.com> - 2.0.12-1
- update upstream tarball and dependency on gnome-pilot from 2.0.11 to 2.0.12 

* Fri Aug 27 2004 David Malcolm <dmalcolm@redhat.com> - 2.0.11-1
- update upstream tarball from 2.0.10 to 2.0.11
- added more detailed version requirements on gnome-pilot/gnome-pilot-devel as imposed by the configuration script, version 2.0.11 is now required, rather than just 2.0

* Thu Aug 19 2004 David Malcolm <dmalcolm@redhat.com> - 2.0.10-4
- Added patch by Justin M. Forbes <64bit_fedora@comcast.net> for proper libdir in .conduit files (#121268)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jul 17 2003 Jeremy Katz <katzj@redhat.com> 2.0.10-1
- 2.0.10

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Jeremy Katz <katzj@redhat.com> 2.0.9-1
- Initial build for Red Hat Linux, clean up the spec file

* Sun Mar 5 2000 Eskil Heyn Olsen <deity@eskil.dk>
- redid the package from mal-conduit to gnome-pilot-conduits

* Sun Dec 5 1999 Eskil Heyn Olsen <deity@eskil.dk>
- Created the .spec file
