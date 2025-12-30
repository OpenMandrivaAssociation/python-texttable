%global upstream_name texttable

Name:		python-%{upstream_name}
Version:	1.6.4
Release:	5
Summary:	Python module to generate a formatted text table, using ASCII characters
Group:		Development/Python
License:	LGPLv3
URL:		https://github.com/foutaise/texttable
Source0:	https://files.pythonhosted.org/packages/d5/78/dbc2a5eab57a01fedaf975f2c16f04e76f09336dbeadb9994258aa0a2b1a/texttable-1.6.4.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{upstream_name}}

%description
Python module to generate a formatted text table, using ASCII characters.


%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{upstream_name}
%doc PKG-INFO README.md
%{python_sitelib}/texttable*
