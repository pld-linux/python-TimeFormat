
%include	/usr/lib/rpm/macros.python
%define 	module TimeFormat

Summary:	An alternative to using time.strftime()
Summary(pl):	Modu³ konkurencyjny dla time.strftime()
Name:		python-%{module}
Version:	1.0.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.owlfish.com/software/%{module}/downloads/%{module}-%{version}.tar.gz
# Source0-md5:	04f42919421c65a6f1c404dd522fabef
URL:		http://www.owlfish.com/software/%{module}/index.html
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeFormat implements new Python time and date formatting codes that
provide more flexibility to time.strftime(). The implementation avoids
using the C library time.strftime() where possible, so ensuring the
same operation across most platforms.

%description -l pl
TimeFormat implementuje od nowa funkcje formatuj±ce datê i czas w
Pythonie, odznaczaj±ce siê wiêksz± elastyczno¶ci± od time.strftime().
Implementacja stara siê unikn±æ u¿ywania pochodz±cej z biblioteki C
funkcji time.strftime() tam, gdzie to tylko mo¿liwe, dziêki czemu
czemu modu³ powinien tak samo dzia³aæ na wiêkszo¶ci platform
sprzêtowych.

%package doc
Summary:	Documentation for TimeFormat module
Summary(pl):	Dokumentacja do modu³u TimeFormat
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for TimeFormat Python module.

%description doc -l pl
Modu³ zawieraj±cy dokumentacjê dla modu³u Pythona TimeFormat.

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
