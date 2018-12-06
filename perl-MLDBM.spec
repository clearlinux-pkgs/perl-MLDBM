#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MLDBM
Version  : 2.05
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/MLDBM-2.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/MLDBM-2.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmldbm-perl/libmldbm-perl_2.05-2.debian.tar.xz
Summary  : store multi-level Perl hash structure in single level tied hash
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
be used to store multidimensional hash structures in tied hashes
(including DBM files).

%package dev
Summary: dev components for the perl-MLDBM package.
Group: Development
Provides: perl-MLDBM-devel = %{version}-%{release}

%description dev
dev components for the perl-MLDBM package.


%prep
%setup -q -n MLDBM-2.05
cd ..
%setup -q -T -D -n MLDBM-2.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/MLDBM-2.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.1/MLDBM.pm
/usr/lib/perl5/vendor_perl/5.28.1/MLDBM/Serializer/Data/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/MLDBM/Serializer/FreezeThaw.pm
/usr/lib/perl5/vendor_perl/5.28.1/MLDBM/Serializer/Storable.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MLDBM.3
