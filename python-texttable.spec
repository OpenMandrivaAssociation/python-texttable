%global upstream_name texttable

Name:		python-%{upstream_name}
Version:	1.7.1
Release:	1
Summary:	Python module to generate a formatted text table, using ASCII characters
Group:		Development/Python
License:	LGPLv3
URL:		https://github.com/foutaise/texttable
Source0:	https://files.pythonhosted.org/packages/source/t/texttable/texttable-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
%{?python_provide:%python_provide python3-%{upstream_name}}

%description
Python module to generate a formatted text table, using ASCII characters.


%prep
%autosetup -p1 -n texttable-%{version}

%build
%py_build

%install
%py_install

%files -n python-%{upstream_name}
%doc PKG-INFO README.md
%{python_sitelib}/texttable*
