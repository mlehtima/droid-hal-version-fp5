%define device fp5
%define vendor fairphone

# Manufacturer and device name to be shown in UI
%define vendor_pretty Fairphone
%define device_pretty Fairphone 5

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_binder 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

