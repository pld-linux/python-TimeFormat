
%define 	module	TimeFormat

Summary:	An alternative to using time.strftime()
Summary(pl.UTF-8):   Moduł konkurencyjny dla time.strftime()
Name:		python-%{module}
Version:	1.1.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.owlfish.com/software/TimeFormat/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	e228ba722218da492ae541f7571e1412
URL:		http://www.owlfish.com/software/TimeFormat/index.html
BuildRequires:	python-devel >= 1:2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeFormat implements new Python time and date formatting codes that
provide more flexibility to time.strftime(). The implementation avoids
using the C library time.strftime() where possible, so ensuring the
same operation across most platforms.

%description -l pl.UTF-8
TimeFormat implementuje od nowa funkcje formatujące datę i czas w
Pythonie, odznaczające się większą elastycznością od time.strftime().
Implementacja stara się uniknąć używania pochodzącej z biblioteki C
funkcji time.strftime() tam, gdzie to tylko możliwe, dzięki czemu
czemu moduł powinien tak samo działać na większości platform
sprzętowych.

%package doc
Summary:	Documentation for TimeFormat module
Summary(pl.UTF-8):   Dokumentacja do modułu TimeFormat
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for TimeFormat Python module.

%description doc -l pl.UTF-8
Moduł zawierający dokumentację dla modułu Pythona TimeFormat.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py_sitescriptdir}/timeformat.py[oc]

%files doc
%defattr(644,root,root,755)
%doc documentation/*
