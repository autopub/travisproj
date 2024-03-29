CHANGELOG
=========

0.1.13 - 2019-08-23
-------------------

Test with default subprocess encoding switched from ASCII to UTF-8.

0.1.12 - 2019-07-28
-------------------

Test corrected PyPI URL

0.1.11 - 2019-07-25
-------------------

* Move `travis_terminate` from AutoPub to `.travis.yml`
* Revert Travis v0 conditions opt-in

0.1.10 - 2019-07-25
-------------------

Use Travis v0 conditions, where `travis_terminate` command is allegedly available.

0.1.9 - 2019-07-25
------------------

Install Twine during before_deploy phase.

0.1.8 - 2019-07-20
------------------

Try pushing via GITHUB_TOKEN instead of SSH key.

0.1.7 - 2019-07-20
------------------

Trigger new release to see if Twine’s output is UTF-8-encoded.

0.1.6 - 2019-07-20
------------------

Use global `TWINE_USERNAME` and `TWINE_PASSWORD` environment variables.

0.1.5 - 2019-07-20
------------------

* Add `TWINE_USERNAME` and `TWINE_PASSWORD` environment variables
* Add missing PyPI metadata to `setup.py`

0.1.4 - 2019-07-20
------------------

Install AutoPub from test PyPI.

0.1.3 - 2019-07-19
------------------

Set `skip_cleanup: true` to stop Travis from auto-stashing

0.1.2 - 2019-07-19
------------------

Yet more tweaks and Travis workarounds.

0.1.0 - 2019-07-15
------------------

Initial project release.
