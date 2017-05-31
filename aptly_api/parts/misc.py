# -* encoding: utf-8 *-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from aptly_api.base import AptlyAPIException


class MiscAPIClient:
    def __init__(self) -> None:
        pass

    def graph(self, ext: str, layout: str="horizontal"):
        raise NotImplementedError("The Graph API is not yet supported")

    def version(self) -> str:
        pass