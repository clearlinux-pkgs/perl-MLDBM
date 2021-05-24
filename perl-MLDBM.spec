#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MLDBM
Version  : 2.05
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/MLDBM-2.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/MLDBM-2.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmldbm-perl/libmldbm-perl_2.05-2.debian.tar.xz
Summary  : store multi-level Perl hash structure in single level tied hash
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MLDBM-license = %{version}-%{release}
Requires: perl-MLDBM-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
be used to store multidimensional hash structures in tied hashes
(including DBM files).

%package dev
Summary: dev components for the perl-MLDBM package.
Group: Development
Provides: perl-MLDBM-devel = %{version}-%{release}
Requires: perl-MLDBM = %{version}-%{release}

%description dev
dev components for the perl-MLDBM package.


%package license
Summary: license components for the perl-MLDBM package.
Group: Default

%description license
license components for the perl-MLDBM package.


%package perl
Summary: perl components for the perl-MLDBM package.
Group: Default
Requires: perl-MLDBM = %{version}-%{release}

%description perl
perl components for the perl-MLDBM package.


%prep
%setup -q -n MLDBM-2.05
cd %{_builddir}
tar xf %{_sourcedir}/libmldbm-perl_2.05-2.debian.tar.xz
cd %{_builddir}/MLDBM-2.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/MLDBM-2.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MLDBM
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-MLDBM/0818edd921e5984915ebffd633848e732071f2e7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MLDBM.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MLDBM/0818edd921e5984915ebffd633848e732071f2e7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/MLDBM.pm
/usr/lib/perl5/vendor_perl/5.34.0/MLDBM/Serializer/Data/Dumper.pm
/usr/lib/perl5/vendor_perl/5.34.0/MLDBM/Serializer/FreezeThaw.pm
/usr/lib/perl5/vendor_perl/5.34.0/MLDBM/Serializer/Storable.pm
