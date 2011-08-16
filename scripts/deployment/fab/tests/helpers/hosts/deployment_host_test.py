#!/usr/bin/env python

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


import mox

from testing.helpers.execution import TestSuiteLoader, TestRunner

from fab.helpers.feedback import ExecutionFeedback
from fab.helpers.filesystem import FileSystem
from fab.helpers.hosts import DeploymentHost
from fab.helpers.hosts import RemoteHost
from fab.helpers.internet import Internet
from fab.helpers.permissions import AkvoPermissions
from fab.helpers.virtualenv import VirtualEnv


class DeploymentHostTest(mox.MoxTestBase):

    def setUp(self):
        super(DeploymentHostTest, self).setUp()
        self.mock_remote_host = self.mox.CreateMock(RemoteHost)
        self.mock_file_system = self.mox.CreateMock(FileSystem)
        self.mock_permissions = self.mox.CreateMock(AkvoPermissions)
        self.mock_internet = self.mox.CreateMock(Internet)
        self.mock_virtualenv = self.mox.CreateMock(VirtualEnv)
        self.mock_feedback = self.mox.CreateMock(ExecutionFeedback)

        self.mock_remote_host.feedback = self.mock_feedback
        self.deployment_host = DeploymentHost(self.mock_remote_host, self.mock_file_system, self.mock_permissions,
                                              self.mock_internet, self.mock_virtualenv)

    def test_can_create_a_deploymenthost_instance(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can create a DeploymentHost instance"""

        self.assertTrue(isinstance(DeploymentHost.create_instance("/some/virtualenv/path"), DeploymentHost))

    def test_can_create_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can create a directory"""

        new_dir = "/var/new/dir"

        self.mock_file_system.create_directory(new_dir)
        self.mox.ReplayAll()

        self.deployment_host.create_directory(new_dir)

    def test_can_create_directory_with_sudo(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can create a directory with sudo"""

        new_dir = "/var/new/dir"

        self.mock_file_system.create_directory_with_sudo(new_dir)
        self.mox.ReplayAll()

        self.deployment_host.create_directory_with_sudo(new_dir)

    def test_can_ensure_directory_exists(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can ensure a directory exists"""

        new_dir = "/var/new/dir"

        self.mock_file_system.ensure_directory_exists(new_dir)
        self.mox.ReplayAll()

        self.deployment_host.ensure_directory_exists(new_dir)

    def test_can_ensure_directory_exists_with_sudo(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can ensure a directory exists with sudo"""

        new_dir = "/var/new/dir"

        self.mock_file_system.ensure_directory_exists_with_sudo(new_dir)
        self.mox.ReplayAll()

        self.deployment_host.ensure_directory_exists_with_sudo(new_dir)

    def test_can_rename_file(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can rename a file"""

        original_file = "/var/tmp/original/file.txt"
        new_file = "/var/tmp/something/else.txt"

        self.mock_file_system.rename_file(original_file, new_file)
        self.mox.ReplayAll()

        self.deployment_host.rename_file(original_file, new_file)

    def test_can_rename_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can rename a directory"""

        original_dir = "/var/tmp/original"
        new_dir = "/var/tmp/something/else"

        self.mock_file_system.rename_directory(original_dir, new_dir)
        self.mox.ReplayAll()

        self.deployment_host.rename_directory(original_dir, new_dir)

    def test_can_delete_file(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can delete a file"""

        expected_file_path = "/some/dir/file_to_delete.txt"

        self.mock_file_system.delete_file(expected_file_path)
        self.mox.ReplayAll()

        self.deployment_host.delete_file(expected_file_path)

    def test_can_delete_file_with_sudo(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can delete a file with sudo"""

        expected_file_path = "/some/dir/file_to_delete.txt"

        self.mock_file_system.delete_file_with_sudo(expected_file_path)
        self.mox.ReplayAll()

        self.deployment_host.delete_file_with_sudo(expected_file_path)

    def test_can_delete_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can delete a directory"""

        expected_dir_to_delete = "/some/dir/to/delete"

        self.mock_file_system.delete_directory(expected_dir_to_delete)
        self.mox.ReplayAll()

        self.deployment_host.delete_directory(expected_dir_to_delete)

    def test_can_delete_directory_with_sudo(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can delete a directory with sudo"""

        expected_dir_to_delete = "/some/dir/to/delete"

        self.mock_file_system.delete_directory_with_sudo(expected_dir_to_delete)
        self.mox.ReplayAll()

        self.deployment_host.delete_directory_with_sudo(expected_dir_to_delete)

    def test_can_compress_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can compress a directory"""

        expected_dir_to_compress = "/some/dir/to/compress"

        self.mock_file_system.compress_directory(expected_dir_to_compress)
        self.mox.ReplayAll()

        self.deployment_host.compress_directory(expected_dir_to_compress)

    def test_can_decompress_code_archive(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can decompress a code archive"""

        code_archive_file = "rsr_v1.0.10.zip"
        destination_dir = "/some/destination/dir"

        self.mock_file_system.decompress_code_archive(code_archive_file, destination_dir)
        self.mox.ReplayAll()

        self.deployment_host.decompress_code_archive(code_archive_file, destination_dir)

    def test_will_exit_if_user_is_not_member_of_web_group(self):
        """fab.tests.helpers.hosts.deployment_host_test  Will exit if user is not a member of the web user group"""

        self.mock_permissions.exit_if_user_is_not_member_of_web_group("joesoap")
        self.mox.ReplayAll()

        self.deployment_host.exit_if_user_is_not_member_of_web_group("joesoap")

    def test_can_set_web_group_permissions_on_specified_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can set web user group permissions on a specified directory"""

        self.mock_permissions.set_web_group_permissions_on_directory("/some/web/dir")
        self.mox.ReplayAll()

        self.deployment_host.set_web_group_permissions_on_directory("/some/web/dir")

    def test_can_set_web_group_ownership_on_specified_directory(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can set web user group ownership on a specified directory"""

        self.mock_permissions.set_web_group_ownership_on_directory("/some/web/dir")
        self.mox.ReplayAll()

        self.deployment_host.set_web_group_ownership_on_directory("/some/web/dir")

    def test_can_ensure_directory_exists_with_web_group_permissions(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can ensure directory exists with web user group permissions"""

        web_dir = "/some/web/dir"
        self.mock_file_system.directory_exists(web_dir).AndReturn(False)
        self.mock_file_system.ensure_directory_exists_with_sudo(web_dir)
        self.mock_permissions.set_web_group_permissions_on_directory(web_dir)
        self.mox.ReplayAll()

        self.deployment_host.ensure_directory_exists_with_web_group_permissions(web_dir)

    def test_will_confirm_existing_directory_when_ensuring_directory_exists_with_web_group_permissions(self):
        """fab.tests.helpers.hosts.deployment_host_test  Will confirm existing directory when ensuring directory exists with web user group permissions"""

        web_dir = "/some/web/dir"
        self.mock_file_system.directory_exists(web_dir).AndReturn(True)
        self.mock_feedback.comment("Found expected directory: %s" % web_dir)
        self.mox.ReplayAll()

        self.deployment_host.ensure_directory_exists_with_web_group_permissions(web_dir)

    def test_can_get_file_name_at_specified_url(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can get the file name at a specified URL"""

        archives_url = "http://some.server.org/archives/dev"
        self.mock_internet.file_name_at_url(archives_url).AndReturn("code_archive.zip")
        self.mox.ReplayAll()

        self.assertEqual("code_archive.zip", self.deployment_host.file_name_at_url(archives_url))

    def test_can_get_file_name_from_url_headers(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can get a file name from the URL headers"""

        file_url = "http://some.server.org/archives/latest"
        expected_file_name = "rsr_1.0.10.zip"
        self.mock_internet.file_name_from_url_headers(file_url).AndReturn(expected_file_name)
        self.mox.ReplayAll()

        self.assertEqual(expected_file_name, self.deployment_host.file_name_from_url_headers(file_url))

    def test_can_download_file_at_url_and_save_it_at_specified_file_path(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can download the file at a URL and save it at the specified file path"""

        file_url = "http://some.server.org/archives/latest"
        downloaded_file_path = "/var/tmp/code/archives/rsr_1.0.10.zip"
        self.mock_internet.download_file_at_url_as(downloaded_file_path, file_url)
        self.mox.ReplayAll()

        self.deployment_host.download_file_at_url_as(downloaded_file_path, file_url)

    def test_can_create_empty_virtualenv(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can create empty virtualenv"""

        expected_pip_log_file = "/some/log/dir/pip_log.txt"

        self.mock_virtualenv.create_empty_virtualenv(expected_pip_log_file)
        self.mox.ReplayAll()

        self.deployment_host.create_empty_virtualenv(expected_pip_log_file)

    def test_can_install_virtualenv_packages(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can install virtualenv packages"""

        expected_pip_requirements_file = "/some/pip/requirements.txt"
        expected_pip_log_file = "/some/log/dir/pip_log.txt"

        self.mock_virtualenv.install_packages(expected_pip_requirements_file, expected_pip_log_file)
        self.mox.ReplayAll()

        self.deployment_host.install_virtualenv_packages(expected_pip_requirements_file, expected_pip_log_file)

    def test_can_list_installed_virtualenv_packages(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can create empty virtualenv"""

        self.mock_virtualenv.list_installed_virtualenv_packages()
        self.mox.ReplayAll()

        self.deployment_host.list_installed_virtualenv_packages()

    def test_can_run_command_within_virtualenv(self):
        """fab.tests.helpers.hosts.deployment_host_test  Can run command within virtualenv"""

        self.mock_virtualenv.run_within_virtualenv("some command")
        self.mox.ReplayAll()

        self.deployment_host.run_within_virtualenv("some command")


def suite():
    return TestSuiteLoader().load_tests_from(DeploymentHostTest)

if __name__ == "__main__":
    from fab.tests.test_settings import TEST_MODE
    TestRunner(TEST_MODE).run_test_suite(suite())
