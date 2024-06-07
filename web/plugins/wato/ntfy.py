#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.valuespec import (
    Age,
    CascadingDropdown,
    Dictionary,
    DropdownChoice,
    EmailAddress,
    FixedValue,
    HTTPUrl,
    IPv4Address,
    ListChoice,
    ListOfStrings,
    Password,
    TextAscii,
    TextUnicode,
    Transform,
    Tuple,
)

from cmk.gui.plugins.wato import (
    notification_parameter_registry,
    NotificationParameter,
)

@notification_parameter_registry.register
class NotificationParameterntfy(NotificationParameter):
    @property
    def ident(self):
        return "ntfy"

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            elements=[
                ("ntfy_server",
                 TextUnicode(
                     title=_("ntfy.sh Server"),
                     help=_("Configure the ntfy.sh server to use. "
                            "e.g. ntfy.sh or https://ntfy.sh."),
                     default_value="ntfy.sh",
                     size=64,
                     allow_empty=False,
                )),
                ("ntfy_topic",
                 TextUnicode(
                     title=_("ntfy.sh topic name"),
                     help=_("ntfy.sh topic name to use."),
                     default_value="checkmk-alerts",
                     size=64,
                     allow_empty=False,
                 )),
                ("ntfy_cmk_url",
                 TextUnicode(
                     title=_("Checkmk URL"),
                     default_value="https://cmk.example.com",
                     help=_("Host URL of your CheckMK monitoring site, without site name. "
                            "Required for the actions to work. "
                            "Example: https://cmk.example.com"),
                     size=64,
                     allow_empty=False,
                 )),
                ("ntfy_username",
                 TextUnicode(
                     title=_("ntfy Username (optional)"),
                     help=_("If the ntfy topic requires authentication, provide a username here."),
                     size=64,
                     default_value="",
                     allow_empty=True,
                 )),
                ("ntfy_password",
                 Password(
                     title=_("ntfy password (optional)"),
                     help=_("If the ntfy topic requires authentication, provide a password here."),
                     size=64,
                     default_value="",
                     allow_empty=True,
                 )),
                ("ntfy_cmk_username",
                 TextUnicode(
                     title=_("CheckMK username (optional)"),
                     help=_("The CheckMK user to use for the acknowledgment, e.g. automation."),
                     size=64,
                     default_value="",
                     allow_empty=True,
                 )),
                ("ntfy_cmk_password",
                 Password(
                     title=_("CheckMK password (optional)"),
                     help=_("The CheckMK user or secret to use for the acknowledgment, e.g. from automation user."),
                     size=64,
                     default_value="",
                     allow_empty=True,
                 )),
                ("ntfy_statetype",
                 TextUnicode(
                     title=_("Notify on Statetype (optional)"),
                     help=_("Allowed values: HARD / SOFT. Notifies on Hard- or Softstate. Defaults to HARD."),
                     size=64,
                     default_value="HARD",
                     allow_empty=True,
                 )),
            ],
        )

