#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-automat
Version  : 20.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/80/c5/82c63bad570f4ef745cc5c2f0713c8eddcd07153b4bee7f72a8dc9f9384b/Automat-20.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/c5/82c63bad570f4ef745cc5c2f0713c8eddcd07153b4bee7f72a8dc9f9384b/Automat-20.2.0.tar.gz
Summary  : Self-service finite-state machines for the programmer on the go.
Group    : Development/Tools
License  : MIT
Requires: pypi-automat-bin = %{version}-%{release}
Requires: pypi-automat-license = %{version}-%{release}
Requires: pypi-automat-python = %{version}-%{release}
Requires: pypi-automat-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)
BuildRequires : pypi(m2r)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Automat
        =======

%package bin
Summary: bin components for the pypi-automat package.
Group: Binaries
Requires: pypi-automat-license = %{version}-%{release}

%description bin
bin components for the pypi-automat package.


%package license
Summary: license components for the pypi-automat package.
Group: Default

%description license
license components for the pypi-automat package.


%package python
Summary: python components for the pypi-automat package.
Group: Default
Requires: pypi-automat-python3 = %{version}-%{release}

%description python
python components for the pypi-automat package.


%package python3
Summary: python3 components for the pypi-automat package.
Group: Default
Requires: python3-core
Provides: pypi(automat)
Requires: pypi(attrs)
Requires: pypi(six)

%description python3
python3 components for the pypi-automat package.


%prep
%setup -q -n Automat-20.2.0
cd %{_builddir}/Automat-20.2.0
pushd ..
cp -a Automat-20.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657154034
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-automat
cp %{_builddir}/Automat-20.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-automat/944ce938a25e9f1da81b24a90769159306d08ba5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/automat-visualize

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-automat/944ce938a25e9f1da81b24a90769159306d08ba5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*