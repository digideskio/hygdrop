#!/usr/bin/env python

import os
plugin_to_load = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "../plugins/github.hy")

from hy.importer import import_file_to_module

g = import_file_to_module("github", plugin_to_load)


def test_get_github_issue():
    expected = " ".join(
        ["Issue #" + "180", "on", "hylang/hy", "by",
         "khinsen:",
         "Macro expansion works differently from Lisp conventions",
         "(open)", "[bug]",
         "<https://github.com/hylang/hy/issues/180>"])
    actual = g.get_github_issue(None, None, "180", dry_run=True)
    assert expected == actual


def test_get_github_commit():
    expected = " ".join(
        ["Commit", "3e8941c", "on", "hylang/hy", "by",
         "Berker Peksag:",
         "Convert stdout and stderr to UTF-8 properly in the run_cmd helper.",
         "<https://github.com/hylang/hy" +
         "/commit/3e8941cdde01635890db524c4789f0640fe665c3>"])
    actual = g.get_github_commit(None, None, "3e8941c", dry_run=True)
    assert expected == actual


def test_get_core_members():
    expected = "Core Team consists of: " + \
               ", ".join(["Julien Danjou", "Nicolas Dandrimont",
                          "Gergely Nagy", "Berker Peksag",
                          "Christopher Allan Webber", "khinsen",
                          "J Kenneth King", "Paul Tagliamonte",
                          "Bob Tolbert", "Will Kahn-Greene",
                          "Morten Linderud", "Abhishek L"])
    actual = g.get_core_members(None, None, dry_run=True)
    assert actual == expected
