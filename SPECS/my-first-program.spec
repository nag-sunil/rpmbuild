Name:		my-first-program
Version:	1.0
Release:	1
Summary:	My first rpm

Group:		Application
License:	GPL
Source0:	my-first-program.sh
#BuildArch: 	noarch
BuildRequires:	httpd
Requires:	httpd

%description
A simple RPM package

#%%prep
#%%setup -q


%build



%install
install -m 0755 -d $RPM_BUILD_ROOT/tmp
install -m 0755 ../SOURCES/my-first-program.sh $RPM_BUILD_ROOT/tmp

%clean
echo I am in clean section now
rm -rf $RPM_BUILD_ROOT

%post
echo #############################

%files
/tmp/my-first-program.sh
%doc



%changelog

