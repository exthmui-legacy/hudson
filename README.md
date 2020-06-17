# Adding or updating a device

**Note:** Sort device listings in exthm-build-targets alphanumerically by codename.  
Steps:  
1. Edit exthm-build-targets with your device codename and branch.  
2. Update `updater/devices.json` according to the instructions below.  
3. Submit the change.

You can upload your change to gerrit with commands like these:

    git add exthm-build-targets updater/devices.json
    git commit
    git push

### devices.json
devices.json is an array of objects, each with several fields:

* `model`: should be the first thing on the line, and is the device's codename (`PRODUCT_DEVICE`) - e.g. `i9300`.
* `oem`: the manufacturer of the device. (`PRODUCT_BRAND`) - e.g. `Samsung`.
* `name`: the user-friendly name of the device - e.g. `Galaxy S III (International)`.
