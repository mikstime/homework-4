# -*- coding: utf-8 -*-

import unittest

from tests.contacts.delete_contact_test import DeleteContactsTest
from tests.contacts.add_contact_test import AddContactTest
from tests.contacts.edit_contact import EditContactTest
from tests.signatures.creation_test import CreationTest
from tests.signatures.editing_test import EditingTest
from tests.signatures.deletion_test import DeletionTest
from tests.other.groups_test import GroupsTest
from tests.other.features_test import FeaturesTest
from tests.other.import_export_test import ImportExportTest
import sys


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(CreationTest),
        # unittest.makeSuite(EditingTest),
        # unittest.makeSuite(DeletionTest),
        # unittest.makeSuite(GroupsTest),
        # unittest.makeSuite(FeaturesTest),
        # unittest.makeSuite(ImportExportTest),
        # unittest.makeSuite(AddContactTest),
        unittest.makeSuite(EditContactTest),
        # unittest.makeSuite(DeleteContactsTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
