%global upstream_name texttable

Name:           python-%{upstream_name}
Version:	1.6.2
Release:	1
Summary:        Python module to generate a formatted text table, using ASCII characters

Group:          Development/Python
License:        LGPLv3
URL:            https://github.com/foutaise/texttable
Source0:	https://files.pythonhosted.org/packages/82/a8/60df592e3a100a1f83928795aca210414d72cebdc6e4e0c95a6d8ac632fe/texttable-1.6.2.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{upstream_name}}

%description
Python module to generate a formatted text table, using ASCII characters.

#------------------------------------------------

%package -n     python2-%{upstream_name}
Summary:        Python 2 module to generate a formatted text table, using ASCII characters
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2dist(setuptools)
%{?python_provide:%python_provide python2-%{upstream_name}}

%description -n python2-%{upstream_name}
Python 2 module to generate a formatted text table, using ASCII characters.

#------------------------------------------------

%prep
%setup -q -n %{upstream_name}-%{version}

cp -a . %{py3dir}

%build
%py2_build
pushd %{py3dir}
%py3_build
popd

%install
%py2_install
pushd %{py3dir}
%py3_install
popd

%files -n python2-%{upstream_name}
%doc PKG-INFO README.md
%{python2_sitelib}/texttable*

%files -n python-%{upstream_name}
%doc PKG-INFO README.md
%{python3_sitelib}/texttable*
%{python3_sitelib}/__pycache__/texttable*
