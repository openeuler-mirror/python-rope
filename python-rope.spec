%global _empty_manifest_terminate_build 0
Name:		python-rope
Version:	0.17.0
Release:	2
Summary:	a python refactoring library...
License:	LGPL-3.0-or-later and LGPL-3.0-only and GPL-3.0-only
URL:		https://github.com/python-rope/rope
Source0:	https://files.pythonhosted.org/packages/ba/44/714486676aeb10de586f892348973d2e6b7c2be4eaff434caaaa45e19e14/rope-0.17.0.tar.gz
BuildArch:	noarch


%description
Rope is a python refactoring library.

%package -n python3-rope
Summary:	a python refactoring library...
Provides:	python-rope
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-rope
Rope is a python refactoring library.

%package help
Summary:	Development documents and examples for rope
Provides:	python3-rope-doc
%description help
Rope is a python refactoring library.

%prep
%autosetup -n rope-0.17.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-rope -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon May 9 2022 yaoxin <yaoxin30@h-partners.com> - 0.17.0-2
- License compliance rectification

* Thu Sep 03 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
