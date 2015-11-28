'''
Created on Nov 3, 2012
Test for pyArchive
@author: rduvalwa2
'''
import unittest
import pyArchive
import os
import tempfile
import shutil

class test_pyArchive(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.current_directory = (tempfile.mkdtemp("testdir") )
        os.chdir(self.current_directory)  
        os.mkdir("testDirectory")
        global fileNames
        fileNames = ['testA','testB','testc']    
        for fn in fileNames:
                f = open(fn, "w")
                f.close()
                    
    def test_ArchiveContainsFilesWithSlash(self):
        test_dir = os.path.split(self.current_directory)[1]
        observed = pyArchive.pyArchive(self.current_directory + "/")
        for fn in fileNames:
                self.assertTrue(os.path.join(test_dir + "/", fn) in observed)


    def test_ArchiveContainsFilesWithoutSlash(self):
        test_dir = os.path.split(self.current_directory)[1]
        observed = pyArchive.pyArchive(self.current_directory)
        for fn in fileNames:
                self.assertTrue(os.path.join(test_dir + "/", fn) in observed)

    def test_ArchiveDoesNotContainDirectory(self):
        test_dir = os.path.split(self.current_directory)[1]
        observed = pyArchive.pyArchive(self.current_directory)
        self.assertFalse(os.path.join(test_dir + "/","testDirectory") in observed, "Failed a directory is in the archive")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.current_directory)
                        
if __name__ == "__main__":
    unittest.main()             
