# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

from katello.client.api.base import KatelloAPI

class UserAPI(KatelloAPI):
    """
    Connection class to access User Data
    """
    def create(self, name, pw, disabled):
        userdata = {"username": name,
                "password": pw,
                "disabled": disabled}
        path = "/api/users/"
        return self.server.POST(path, userdata)[1]

    def delete(self, user_id):
        path = "/api/users/%s" % str(user_id)
        return self.server.DELETE(path)[1]

    def update(self, user_id, pw, disabled):
        userdata = {}
        userdata = self.update_dict(userdata, "password", pw)
        userdata = self.update_dict(userdata, "disabled", disabled)
        path = "/api/users/%s" % str(user_id)
        return self.server.PUT(path, {"user": userdata})[1]

    def users(self, query={}):
        path = "/api/users/"
        orgs = self.server.GET(path, query)[1]
        return orgs

    def user(self, user_id):
        path = "/api/users/%s" % str(user_id)
        org = self.server.GET(path)[1]
        return org

    def report(self, format):
        to_return = self.server.GET("/api/users/report", customHeaders={"Accept": format})
        return (to_return[1], to_return[2])
