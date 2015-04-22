# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Test implementation of collections

"""

import os
import platform

from nose.tools import assert_raises, assert_is_instance, assert_true, assert_equal, assert_false, assert_in

from datalad.support.dataset import Dataset
from datalad.support.collection import Collection
from datalad.tests.utils import with_tempfile, with_testrepos, assert_cwd_unchanged, ignore_nose_capturing_stdout, \
    on_windows, ok_clean_git_annex_proxy, swallow_logs, swallow_outputs, in_, with_tree,\
    get_most_obscure_supported_name, ok_clean_git


# ###########
# Test the handling of base classes before
# implementing it into the actual commands
# ############

def get_local_collection():
    # May be this location my change.
    # So, we need a ~/.datalad or sth.

    # TODO: local collection needs a name too!

    return Collection(os.path.expanduser(
        os.path.join('~', 'datalad', 'localcollection')))


def register_collection(url, name):
    # Is there a default name of a collection?
    # derived from url?

    # add as remote to the local one:
    localCollection = get_local_collection()
    localCollection.git_remote_add(name, url)



def install_collection(name, dst):
    # cloning the remote 'name' of local collection to dst.
    localCollection = get_local_collection()
    url = localCollection.git_get_remote_url(name)
    return Collection(dst, url)



def install_handle(?):
    # TODO: get a handle (identified what way? => collectionName/handleName?)


def new_collection(handles):
    # create a new collection

#----------------------------------------------
    # add a handle to collection
    # remove a handle from a collection
    # publish a collection
    # update metadata cache?




# ##########
# Now the actual tests for collection class
# ##########