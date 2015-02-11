%global cartridgedir %{_libexecdir}/openshift/cartridges/kdehaproxy

Name: 		openshift-origin-cartridge-kdehaproxy
Version:	1.4
Release:	1%{?dist}
Summary:	HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications.

Group:		Development/Languages
License:	GPLv2
URL:	 	http://haproxy.org	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64

Requires:	haproxy

%define _unpackaged_files_terminate_build 0


%description
HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications.

%prep
%setup -q


%build


%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{cartridgedir}
%__cp -r * %{buildroot}/%{cartridgedir}

%clean
rm -rf %{buildroot}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/versions
%{cartridgedir}/env
%{cartridgedir}/template
%{cartridgedir}/metadata
%{cartridgedir}


%changelog
