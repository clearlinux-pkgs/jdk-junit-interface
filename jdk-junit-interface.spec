Name     : jdk-junit-interface
Version  : 0.11
Release  : 2
URL      : http://repo2.maven.org/maven2/com/novocode/junit-interface/0.11/junit-interface-0.11.jar
Source0  : http://repo2.maven.org/maven2/com/novocode/junit-interface/0.11/junit-interface-0.11.jar
Source1  : http://repo2.maven.org/maven2/com/novocode/junit-interface/0.11/junit-interface-0.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-junit-interface-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-junit-interface package.
Group: Data

%description data
data components for the jdk-junit-interface package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/junit-interface.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/junit-interface.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/junit-interface.xml \
%{buildroot}/usr/share/maven-poms/junit-interface.pom \
%{buildroot}/usr/share/java/junit-interface.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/junit-interface.jar
/usr/share/maven-metadata/junit-interface.xml
/usr/share/maven-poms/junit-interface.pom
