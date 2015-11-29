#!/usr/local/bin/python3
"""This test the fileTypecounter.py
"""

import unittest
import fileTypeCounter
import os
import tempfile
import shutil

class test_FileTypeCounter(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.current_directory = tempfile.mkdtemp("testdir")
        os.chdir(self.current_directory)  
        os.mkdir("isDirectory")    
        count = 1
        self.file_types_expected = {".bs":5,"":5,".py":5,".doc":5}
        for count in range(0,5):
            fn = "file"+ str(count)
            for tp in self.file_types_expected.keys():
                f = open(fn + tp, "w")
                print()
                f.close()
                
    def test_verify_files(self):
        # I like this observed need to get in the habit of using it
        observed= fileTypeCounter.fileTypeCounter(".")
        self.assertEqual(observed,self.file_types_expected,"Observed does not match expected")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.current_directory)
                        
if __name__ == "__main__":
    unittest.main()             
