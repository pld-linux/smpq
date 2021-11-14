Summary:	StormLib MPQ archiving utility
Name:		smpq
Version:	1.6
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://launchpad.net/smpq/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c7124d2dfdbaaf428413513856f446ce
URL:		https://launchpad.net/smpq
BuildRequires:	StormLib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPQ is StormLib MPQ archiving utility. This utility is designed for
full manipulating with Blizzard MPQ archives. It supports extracting,
appending, renaming and deleting files in MPQ archives. It also can
create MPQ archive. SMPQ can access to different type of MPQ archives
and version. It support encrypted, compressed, partial and patched MPQ
archives with version 1-4.

%prep
%setup -q

%build
%{__cxx} %{rpmcxxflags} %{rpmcppflags} \
	-DVERSION='"%{version}"' \
	append.c \
	extract.c \
	info.c \
	listfiles.c \
	main.c \
	print.c \
	remove.c \
	rename.c \
	%{rpmldflags} -o smpq -lstorm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p smpq $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/smpq
