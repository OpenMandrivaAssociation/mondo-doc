#
# $Id: mondo-doc.spec 755 2006-08-06 23:15:58Z bruno $
#

Summary:	Documentation for Mondo Rescue

Name:		mondo-doc
Version:	2.29.3
%define upstreamv       2.2.9.3
Release:	3
License:	GPL
Group:		Archiving/Backup
Url:		https://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{upstreamv}.tar.gz
BuildRequires:	man,docbook-utils,groff,imagemagick,docbook-dtd41-sgml,docbook-utils-pdf,lynx,groff-for-man
BuildRequires:	ghostscript-common
BuildArch: noarch

%description
Documentation for Mondo Rescue

%prep
%setup -q -n %{name}-%{upstreamv}

%build
%{__make} -f Makefile.man VERSION=%{version}
%{__make} -f Makefile.howto VERSION=%{version}

%install
%{__make} -f Makefile.man install INSTALLDIR=%{buildroot}/%{_defaultdocdir}/%{name}-%{version}
%{__make} -f Makefile.howto install INSTALLDIR=%{buildroot}/%{_defaultdocdir}/%{name}-%{version}

%clean

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}-%{version}



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.29.3-2mdv2011.0
+ Revision: 612921
- the mass rebuild of 2010.1 packages

* Fri May 21 2010 Bruno Cornec <bcornec@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 545669
- Update build dependencies after chroot mdv2010.0 test
- mondo-doc needs also groff to be built
- Adds the Buildrequire on the man package needed for man2html command
- Update mondo-doc to upstream 2.2.9.3
- Update mondo-doc to upstream 2.2.8 (here 2.28)

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.24-3mdv2009.0
+ Revision: 241030
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 01 2007 Bruno Cornec <bcornec@mandriva.org> 2.24-1mdv2008.0
+ Revision: 77257
- Updated to 2.2.4
- Size of DVD is 4482 (or more surely 4480 to avoid problems - used everywhere) (Bruno Cornec)
- New Hardware migration guide with P2V (Eric Montaut/Gallig/Renaud/Bruno Cornec)
- Fix a memory allocation bug where strings were freed to early (Nick Hajek)
- yum support added to ftp server (Mark Nienberg/Bruno Cornec)
- Also computes number of media for NFS backups (Patrick Albert/Bruno Cornec)
- Improve message around ISO directory (Patrick Albert/Bryan Gartner)
- Improved Ubuntu support (Fix #159) (Bruno Cornec)
- Improved VMWare ESX supoprt (Amaury Tanquerel/Bruno Cornec)
- Fix a bug (hang #136) when no floppy available (Bruno Cornec)
- Adds OCFS support in -N (Bruno Cornec)
- Reduce log file verbosity in sort phase (Bruno Cornec)
- Fix a spelling error (James Cameron/Bruno Cornec)
- mondo rpm pkg depends on buffer and cdrecord (Vincen Danen/Bruno Cornec)
- Adds -p option support to mondorestore (Fix #114) (Bruno Cornec)
- Adds support for Boot loader in partitions (Fix #117) (Bruno Cornec)
- Fix a bug where Unallocated space was considered as an error (Bruno Cornec)
- MINDI_CACHE set to /var/cache/mindi new location of mindi images instead of /root/images/mindi (Andree Leidenfrost)
- Fix bug #158 (cummings)
- Do not use mindi-boot.2880.img (which may not exist) anymore in mondorestore (Bruno Cornec)
- get_architecture now returns correctly the built arch used (Bruno Cornec)
- Fix a bug in mondoarchive for UUID support of /boot (Bruno Cornec)
- Fix a bug for mountlist creation (UUID wasn't printed)
- Build process now creates yum and urpmi repositories for the respective rpm based distros (Bruno Cornec)
- Updated to 2.2.3
- Fix a critical bug where bzip2 files where not considered during restore (Dale Tronrud/Scott Cummings)

* Wed Apr 25 2007 Bruno Cornec <bcornec@mandriva.org> 2.22-1mdv2008.0
+ Revision: 18030
- Updated to 2.2.2
- Log files are now consistent: mondoarchive.log for mondoarchive (containing also mindi.log) and mondorestore.log for mondorestore (copied from /tmp (ram) to /var/log (disk) at the end of the restore) (Bruno Cornec)
- Script label-partitions-as-necessary now works correctly for LABEL and UUID (Bruno Cornec)
- Remove useless script compare-me (Bruno Cornec)
- Some FreeBSD fixes (Bruno Cornec)
- Fix a bug where losetup is called with only one parameter (#140) (Bruno Cornec)
- Fix a core dumped when a Big file doesn't exist an can't be created (Nic
  Watson/Bruno Cornec)
- support UUID in mondorestore (Fix #103) (Bruno Cornec)
- Fix a bug in size computation for cciss and similar devices needing a p before their partition name (Bruno Cornec)
- Fix 2 references to grep -x (Fix for #96) (Bruno Cornec)
- Add build support for Mandriva 2007.1, RREL 5 and Debian 4.0 (Bruno Cornec)
- Fix a bug on is_this_raid_personality_registered (John Pearson/Bruno Cornec)
- Fix a bug with raid5 arrays synchronization (R?\195?\169mi Bondoin)
- Tape support improvements (Benoit Donnette/Michel Loiseleur)
- Handle no compression + verify correctly (Scott Cummings)
- various HOWTO fixes (Mike Kinney)
- Fix temporarily a bug when a biggiefile > 32MB was compressed below the size
  of a slice (16MB) (Michel Loiseleur/Bruno Cornec)
- Better module loading in insmod_crucial_modules (Andree Leidenfrost)
- Improve Gentoo packaging (Linos)
- Small typo fix for mondorestore man page (petes-bugs)
- Small memory management improvements (Michel Loiseleur/Bruno Cornec)
- Store NFS config only once (Bruno Cornec)
- Fix a flaw in libmondo-mountlist.c (there since rev [1] !!) (Bruno Cornec)
- Increased MAX_STR_LEN to 384 to make it divisible without remainder by eight
  for 64 bits platforms (Andree Leidenfrost)
- Fix a bug where no bzip2 format file would be found when supporting gzip (Andy Wright)
- CentOS fixes (Andy Wright)


* Thu Jan 04 2007 bcornec <bcornec> 2.21-1mdv2007.0
+ Revision: 103983
- Updated to 2.2.1
- Fix a memory allocation bug in gen_aux_list (Klaus Ade Johnstad/Andree Leidenfrost)
- fedora core 6 and suse 10.2 support added in build process (Bruno Cornec)
- Fix a bug where grub.conf was a symlink (Bruno Cornec)
- mondo now supports gzip compression  (-G option) (#113) (Bruno Cornec)
- ACL and XATTR are now NOT backed up anymore by default. Should increase mondoarchive speed. To handle them as before, please use the -z option. Fix Bug #63 (Bruno Cornec)
- Fix a bug in libmondo-fifo.c where potentially no buffer content could let mondo runni ng forever in case of an exception (Bruno Cornec)
- Fix a bug where ps (busybox) and ps (system) do not give PID in the same column (Bruno Cornec)
- TAG is now per package (Bruno Cornec)
- Add CentOS build support (Andy Wright/Bruno Cornec)
- Fix bug #89 (env var were queried too early, and not ncessarily in PXE mode) (Bruno Cornec)
- fix #66 (setfacl not existing => no error) (Bruno Cornec)
- Removal of grep -w|-x during restore as not supported by busybox fixes bug #101 (Alfred Chua/Bruno Cornec)
- Fix a bug with DVD+RW , when mondo asks for retry without success indifinitely (Mariano Aliaga)
- Fix Bug #90 mondoarchive fails when using space in the prefix (Bruno Cornec)
- Fix Bug #87 LABEL= swap does not come online after mondorestore (Bruno Cornec)
- Source directory for mondo is now src (compatibility with trunk) (Bruno Cornec)
- Updated to 2.2.1
- Fix a memory allocation bug in gen_aux_list (Klaus Ade Johnstad/Andree Leidenfrost)
- fedora core 6 and suse 10.2 support added in build process (Bruno Cornec)
- Fix a bug where grub.conf was a symlink (Bruno Cornec)
- mondo now supports gzip compression  (-G option) (#113) (Bruno Cornec)
- ACL and XATTR are now NOT backed up anymore by default. Should increase mondoarchive speed. To handle them as before, please use the -z option. Fix Bug #63 (Bruno Cornec)
- Fix a bug in libmondo-fifo.c where potentially no buffer content could let mondo runni ng forever in case of an exception (Bruno Cornec)
- Fix a bug where ps (busybox) and ps (system) do not give PID in the same column (Bruno Cornec)
- TAG is now per package (Bruno Cornec)
- Add CentOS build support (Andy Wright/Bruno Cornec)
- Fix bug #89 (env var were queried too early, and not ncessarily in PXE mode) (Bruno Cornec)
- fix #66 (setfacl not existing => no error) (Bruno Cornec)
- Removal of grep -w|-x during restore as not supported by busybox fixes bug #101 (Alfred Chua/Bruno Cornec)
- Fix a bug with DVD+RW , when mondo asks for retry without success indifinitely (Mariano Aliaga)
- Fix Bug #90 mondoarchive fails when using space in the prefix (Bruno Cornec)
- Fix Bug #87 LABEL= swap does not come online after mondorestore (Bruno Cornec)
- Source directory for mondo is now src (compatibility with trunk) (Bruno Cornec)
- Addition of spec file again
- Try to update .spec which seems blocked
- update to 2.2.0

* Thu Aug 10 2006 bcornec <bcornec> 2.0.9-1mdv2007.0
+ Revision: 54841
- Use of %%mkrel
- import mondo-doc-2.0.9

* Sat Aug 05 2006 Bruno Cornec <bcornec@mandriva.org> 2.0.9-2.20060mdk
- Updated to 2.0.9
- Preliminary build process working for Debian and Gentoo (Bruno Cornec)
- New NFS/PXE support. start-nfs is now a fixed script. Allow more possibilities at restore time (Bruno Cornec)
- Fix some compiler warnings for 64bits mode (Andree Leidenfrost)
- Fix various screen corruption for 'Configure LVM'/RAID sync (Andree Leidenfrost)
- SuSE RPMS now use bzip2 (Lars Rupp/Bruno Cornec)
- Exclude ClearCase mvfs type of filesystem from mondo backup (rzonum_at_gmail.com/Bruno Cornec)
- Improved .spec Requires (Fedora/SuSE feedbacks) (Bruno Cornec)
- Indication for users of IDE burners and 2.6 kernels (Christopher Moriarity/Bruno Cornec)
- remove df -P during restore as busybox doesn't support it (Bruno Cornec)
- nfsmount option added to allow redeployment from another NFS server (Bruno Cornec)
- This version should work a bit better with files having special char bug #7421 - but more to come (Bruno Cornec)
- Fix Debian Bug #369321 by increasing MAX_TAPECATALOG_ENTRIES to 8192 and bkpinfo->optimal_set_size to 16MB (Andree Leidenfrost)
- Fix problem with BurnProof+DVD (Andree Leidenfrost)
- Fix bug #7820: mondo should now support files > 2GB (taps23_at_yahoo.com/Bruno Cornec)
- Replaced all occurrences of egrep with 'grep -E' and of fgrep with 'grep -F' (Andree Leidenfrost)
- Optimize grep usage - fixes Debian bug #222052 (Andree Leidenfrost)
- Avoid false alerts about growisofs not running under sudo (Andree Leidenfrost)
- Increase PPCFG_RAMDISK_SIZE to 350 MB (Thomas Börkel/Bruno Cornec)
- Removed useless mondo-makefilelist (Andree Leidenfrost)
- Fix a segmentation fault in parse_mdstat() (Andree Leidenfrost)
- Fix gcc 4.1.2 warnings (Andree Leidenfrost)

* Thu Jun 08 2006 Bruno Cornec <bcornec@mandriva.org> 2.0.8-3.20060mdk
- Updated to 2.0.8-3
- Fix a bug in -I and -E handling !!  (Paolo Bernardoni <bernardoni_at_sysnet.it>/Bruno Cornec)
- Fix permissions for autorun (Bruno Cornec)
- Fox delivery problems for tar files with too restrictive umask (Bruno Cornec)
- Fix parsing of DHCP information in start-nfs script (Andree Leidenfrost)

* Sat Jun 03 2006 Bruno Cornec <bcornec@mandriva.org> 2.0.8-2.20060mdk
- Updated to 2.0.8-2
- PXE mode now supports change of NIC for redeployment (Bruno Cornec)

* Fri May 26 2006 Bruno Cornec <bcornec@mandriva.org> 2.0.8-1.20060mdk
- Updated to 2.0.8-1
- new build process (Bruno Cornec)
- Fix a bug in .spec for RPM build (%%attr now unused) (Bruno Cornec)
- Support of dm and LVM v2 (Andree Leidenfrost)
- New mr_strtok functionn added and used for dm support (Andree Leidenfrost)
- Complete doc is now a separate package. mondo still contains the man pages and howto in minimal useful formats (Bruno Cornec)
- HOWTO now contains a new chapter on unattended support for mondo
- Increase size (4 times) of include|exclude variables
- Fix a bug on -I and -E not working with multiple parameters
- Fix a bug in verify for NFS by swapping nfs_remote_dir and isodir when assembling name for image file to verify (Andree Leidenfrost)
- Fix mondo when restoring filenames containing blanks (still a problem for filenames with ') (Bruno Cornec)
- Fix a RPM generation bug for rh7.3 (i386-redhat-linux prefix for binaries) (Bruno Cornec)

* Fri Mar 10 2006 Bruno Cornec <bcornec@mandriva.org> 2.0.7-1.20060mdk
- Updated to 2.0.7
- useless cat, sort|uniq commands removed (Bruno Cornec/Sébastien Aperghis-Tramoni)
- Doc cleanup (Andree Leidenfrost)
- Add the actual  to messages after calls to function is_this_a_valid_disk_format() about unsupported formats.  (Andree Leidenfrost)
- Abort|Warn when one of the include|exclude dirs (-I|-E) does not exist (Bruno Cornec/Jeffs)
- Replaced partimagehack with ntfsclone from ntfsprogs package. (Andree Leidenfrost)
- use df -P everywhere (Bruno Cornec)
- Paypal incitations removed (Andree Leidenfrost)
- mondo now uses /usr/share for the restore-scripts (Bruno Cornec)
- rpmlint cleanups (Bruno Cornec)
- no shared librairies and no X11 anymore (were useless) (Bruno Cornec)
- files > 2GB are now really supported (Andree Leidenfrost)
- new SGML based Mondo Rescue documentation + new Web site (Bruno Cornec/Andree Leidenfrost)
- mondoarchive aborts when 'mindi --findkernel' gives a fatal error (See also Debian bug #352323.) (Andree Leidenfrost)
- /tmp not excluded anymore from backup (Bruno Cornec)
- New RPM Build environement (Bruno Cornec)

* Fri Dec 23 2005 Bruno Cornec <bcornec@mandriva.org> 2.06-1.20060mdk
- Updated to 2.06
- better error handling of failed commands/mindi (Andree Leidenfrost)
- fix compiler warnings (Andree Leidenfrost)
- -p improvements for NFS/PXE/ISO modes (Bruno Cornec)
- support of default route and netmask for PXE/NFS (Bruno Cornec)
- fix for restoring mondo backups on md-raid systems (Philippe De Muyter)
- remove excessive 'cat' commands (Philippe De Muyter)
- fix to force growisofs to use speed=1 for DVD burning (Philippe De Muyter)
- now handles cifs correctly (Bruno Cornec)
- fix issue where mondoarchive ejects CD/DVD despite writing iso images (Andree Leidenfrost)
- Add -P option to df calls (Andree Leidenfrost/Chuan-kai Lin)
- fix usage of joint -B and -m options (Andree Leidenfrost/Efraim Feinstein)
- Quadrupled ARBITRARY_MAXIMUM from 500 to 2000 for mondorestore's filebrowser (Andree Leidenfrost)
- remove the renice of mondoarchive (Hugo Rabson)
- relocate what was under /usr/share to /usr/lib (FHS compliance) (Bruno Cornec/Andree Leidenfrost)
- manage non ambiguous delivery under /usr (packages) or /usr/local (tar ball) (Bruno Cornec)
- disable x11 build by default (Bruno Cornec)
- remove sbminst (Bruno Cornec/Andree Leidenfrost)
- use parted2fdisk everywhere (Bruno Cornec)
- exports MONDO_LIB (Bruno Cornec)
- RPM build for fedora core 4, sles9, redhat 7.3, rhel 3/4, mandriva 2006.0, mandrake 10.2/10.1 (Bruno Cornec/Gary Granger)
- interactive mode now asks for image size and prefix in NFS mode (Gallig Renaud/Bruno Cornec)
- iso-prefix should be read in iso mode even when -H not given (Stan Benoit)
- VERSION/RELEASE Tag added (Bruno Cornec)
- many code cleanup, small fixes, PXE/NFS code improvements (Sébastien Aperghis-Tramoni/Bruno Cornec)

* Sat Nov 19 2005 Bruno Cornec <bcornec@mandriva.org> 2.05-1.20060mdk
- Updated to 2.05
- -p options works better for NFS cases  (Bruno Cornec)
- ia64 is now working for rhel3  (Bruno Cornec)
- delivery process to BerliOS improved (Bruno Cornec)
- now handles cifs correctly (Bruno Cornec)

* Sun Oct 30 2005 Bruno Cornec <bcornec@mandriva.org> 2.04_berlios-1.20060mdk
- Updated to 2.04_berlios
- Add -p option to generate ISO images file names with prefix. The new default name for ISO images is mondorescue-1.iso, ... For PXE environment, you have to use the prefix option on the command line (read README.pxe) (Bruno Cornec)
- Mandrake 2005 support (Bruno Cornec)
- NFS patches (Yann Aubert <technique@alixen.fr>)
- mondorestore shouldn't now ask final questions with -H (this is an unattended mode) (Bruno Cornec)

* Wed May 04 2005 Bruno Cornec <bcornec@mandriva.org> 2.04-1.20060mdk
- Updated to 2.04
- made mondo more clever about finding its home. Avoids mondo considering directories like '/usr/share/doc/momdo' as its home.

* Thu Sep 30 2004 Bruno Cornec <bcornec@mandriva.org> 2.03-1.20060mdk
- Updated to 2.03
- better SLES8 support
- test user-specified temp dir's sanity

* Thu Jul 22 2004 Bruno Cornec <bcornec@mandriva.org> 2.02-1.20060mdk
- Updated to 2.02
- instead of using 'dd' to erase partition table, delete existing partitions w/ the same call to fdisk that is used to create the new partitions; this should avoids locking up the partition table
- set bootable partition in the above same call to fdisk, for the same reason (avoids locking up the partition table)
- better software RAID support
- mount ext3 partitions as ext2 when restoring - better for Debian
- better star, ACL support
- added ACL, xattr support for afio users

* Tue Jun 22 2004 Bruno Cornec <bcornec@mandriva.org> 2.01-1.20060mdk
- Updated to 2.01
- fixed cvs for SuSE systems
- fixed NTFS backup/restore bug relating to partimagehack log file overflow and NTFS v non-NTFS differentiation
- more reliable extraction of config info from CDs, floppies
- better support of ISO dirs at restore-time (Conor Daly)

* Sat Jun 19 2004 Bruno Cornec <bcornec@mandriva.org> 2.00-1.20060mdk
- Updated to 2.00
- first 2.0 release
- updated grub-install.patched to support SuSE and Red Hat
- added kdelibs as xmondo dependency (Joshua Oreman)
- better find_cdrom_device(), to cope w/ multiple CD writers
- added xmondo pixmap installation
- fixed -m and -Vc flags
- fixed NTFS support!
- bootable CD uses native, not El Torito, support now
- added -devel package
- made xmondo a second package
- added ability to specify --without xmondo at build time
- Clean up, added spanish translation
- Set prefix to be /usr
- added/fixed Requires
- remove CVS directories prior to building
- added 2.6 kernel support
- if 2.6 kernel, insist that the user specify CD device
- drop Embleer; insist on ms-sys and parted if Windows partition
- added support for boot/root multi floppies
- call 'mt' to set block size to 32K before opening in/out tape
- updated mondo-prep.c to create each disk's partitions all at once (one call per drive) instead of one call to fdisk per partition
- when extracting cfg file and mountlist from all.tar.gz (tape copy), use block size of INTERNAL_TAPE_BLK_SIZE, not TAPE_BLOCK_SIZE
- added star and rudimentary SELinux support
- fixed lots of bugs
- all logging now goes to /var/log/mondo-archive.log, with symlink to /tmp/mondo-restore.log for restore-time log-tracking
- added grub-install.patched
- removed embleer & other binaries
- added '-b' to specify block size
- added '-R' for star support

* Tue Mar 30 2004 Bruno Cornec <bcornec@mandriva.org> 1.75-1.20060mdk
- Updated to 1.75
- fixed chmod/chown bug (Jens Richter)
- ask user to confirm NFS mountpoint in Interactive Mode
- rewritten format_everything() to make sure LVMs, RAIDs and regular partitions are prepped in the correct order
- better magicdev support
- rewritten external binary caller subroutine
- DVD support added
- better backup-time control gui; offer to exclude nfs if appl.
- fixed multi-tape support
- re-implemented -D and -J
- fixed bug in extract_config_file_from_ramdisk() which affected tape+floppy users
- updated is_incoming_block_valid() to make it return end-of-tape if >300 flotsam blocks
- unmount CD-ROM before burning (necessary for RH8/9)
- fixed some stray assert()'s
- fixed bug in grub-MR (Christian)
- make user remove floppy/CD before restoring interactively from tape
- fixed bug in am_I_in_disaster_recovery_mode()
- added code to nuke_mode() to make sure NFS (backup) share is mounted in Nuke Mode
- improved tape device detection code
- better GRUB support
- better logging of changed bigfiles at compare-time
- better NTFS support, thanks to partimagehack-static
- better logging
- rewrote tape-handling code, breaking compatibility w/ previous versions
- fixed ISO/CD biggiefile verification bug in mondoarchive
- fixed bug which stopped boot/compare-time changelist from popping up
- replaced mondo-makefilelist with C code - faster, cleaner
- tweaked GUI - better feedback
	
1.74 (2003-09-24)
- fixed biggiefile atime/ctime restoration bug 73
- fixed 'default boot loader' detection bug (Joshua Oreman)
- use single-threaded make_afioballs_and_images() if FreeBSD
- fixed mondoarchive -Vi multi-CD verify bug (Tom Mortell)
- superior get_phys_size_of_drive() (Joshua Oreman)
- fixed RAID-related bug in where_is_root_mounted()
- ISO tweaks
- fixed silly bug in load_filelist() which stopped funny German filenames from being handled properly
- misc fixes (Michael Hanscho's friend)
- added rudimentary support for SME
- added better label support
- fixed various calls to popup_and_get_string()
- fixed spec file
- reject -E /
- added partimagehack to the mix
	
1.73 (2003-05-04)
- mark relevant partitions as bootable _after_ unmounting them
- resolve boot device (-f) if softlink
- post_param_configuration() --- store iso-dev and isodir
- added post-nuke-sample.tgz to package
- Nuke Mode now checks mountlist against hardware; offer user opportunity to edit mountlist if insane; if user declines, abort
- added lots of assert()'s and other checks
- ran code thru Valgrind to catch & fix some memory leaks
- made mondo-restore.c smaller by moving some subroutines to common/libmondo-raid.c and mondorestore/mondo-rstr-compare.c
- added '-Q' flag, to let user test mondoarchive's ability to find their boot loader and type
- improved which_boot_loader()
- when burning or comparing to a CD, defeat autorun if it is running, to avoid confusing mondoarchive and the user
- if original backup media no longer available at boot-time then offer user chance to choose another media source
- when booting, type 'nuke noresize' to nuke w/o resizing mountlist to fill your drives
- add 'textonly' when booting, to avoid using Newt gui
- run nice(20) to prioritize mondoarchive at start
- don't pause and wait for next blank CD at backup-time unless necessary (e.g. previous CD has not been removed)
- get_phys_size_of_drive() --- better support of older drives
- don't eject if "donteject" is in kernel's command line
- cleaned up segfault-handling
- added Conor's strip_path() to improve file list display
- added Herman Kuster's multi-level bkp patch
- added Joshua Oreman's FreeBSD patches x3
- fixed interactive/textonly support
- fixed support for subdir-within-NFS-mount
- fixed "Can't backup if ramdisk not mounted" bug
- try to work around eccentricities of multi-CD drive PCs
- misc clean-ups (Steve Hindle)

