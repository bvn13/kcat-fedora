Name: kcat
Version: 1.7.0
Release: 1%{?dist}
Summary: kcat is a generic non-JVM producer and consumer for Apache Kafka 0.8, think of it as a netcat for Kafka.

License:  BSD-2-Clause
URL:      https://github.com/edenhill/kcat

Source0:  %{version}.zip

Source:   https://github.com/edenhill/kcat/archive/refs/tags/1.7.0.zip

BuildRequires: zlib-devel
BuildRequires: gcc >= 4.1
BuildRequires: librdkafka-devel

%description
kcat is a generic non-JVM producer and consumer for Apache Kafka

%prep
%autosetup

%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/kcat

%doc README.md
%license LICENSE
%changelog CHANGELOG.md
