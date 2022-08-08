import unittest

class TestInstallPackages(unittest.TestCase):
    
    def test_pandas_install(self):
        """
        Test pandas installation
        """

        try:
            import pandas
            HAS_PANDAS = True
        except:
            HAS_PANDAS = False
        
        self.assertTrue(HAS_PANDAS)

    def test_pandas_version(self):
        """
        Test pandas version
        """

        import pandas
        version = pandas.__version__
        self.assertEqual(version, '1.4.3')
    
    def test_ipykernel_install(self):
        """
        Test ipykernel installation
        """

        try:
            import ipykernel
            HAS_ipykernel = True
        except:
            HAS_ipykernel = False
        
        self.assertTrue(HAS_ipykernel)

    def test_ipykernel_version(self):
        """
        Test ipykernel version
        """

        import ipykernel
        version = ipykernel.__version__
        self.assertEqual(version, '6.9.1')

    def test_mypy_install(self):
        """
        Test mypy installation
        """

        try:
            import mypy
            HAS_mypy = True
        except:
            HAS_mypy = False
        
        self.assertTrue(HAS_mypy)

    def test_python_version(self):
        """
        Test python version
        """

        import sys
         
        version = str(sys.version_info.major) + '.' + \
            str(sys.version_info.minor) + '.' + \
                str(sys.version_info.micro)
        self.assertEqual(version, '3.9.12')    


if __name__ == '__main__':
    unittest.main()

