# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


# python 2.5 compatibilty
from __future__ import with_statement

import fabric.context_managers


class DataRetriever(object):

    def __init__(self, data_retriever_config, database_host):
        self.config = data_retriever_config
        self.database_host = database_host
        self.feedback = database_host.feedback

    def fetch_data_from_database(self):
        self.ensure_required_paths_exist()
        rsr_data_dump_path = self.config.rsr_data_dump_path
        self.feedback.comment("Fetching data from database at %s" % self.config.akvo_rsr_app_path)
        self.database_host.run_within_virtualenv("python %s -d %s dump" % (self.config.db_dump_script_path, rsr_data_dump_path))
        self.database_host.compress_directory(rsr_data_dump_path)
        self.database_host.delete_directory(rsr_data_dump_path)

    def ensure_required_paths_exist(self):
        self.database_host.ensure_directory_exists_with_sudo(self.config.data_dumps_home)
        self.database_host.exit_if_directory_does_not_exist(self.config.rsr_virtualenv_path)
        self.database_host.exit_if_file_does_not_exist(self.config.db_dump_script_path)